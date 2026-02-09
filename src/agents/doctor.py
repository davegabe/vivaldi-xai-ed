"""
Doctor Agent (Attending Physician) - Planning and Decision Making.
"""

import time
import base64
from typing import Optional
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, BaseMessage

from ..config import config
from ..logging import get_logger
from ..models import create_model
from ..data.schema import PatientVisit
from ..prompts import (
    DOCTOR_SYSTEM_PROMPT,
    DOCTOR_ANALYSIS_TEMPLATE,
    DOCTOR_TASK_SYSTEM_PROMPT,
    DOCTOR_RANKING_TEMPLATE,
    DOCTOR_RANKING_SYSTEM_PROMPT,
    CalculationResult,
    DoctorRankingOutput,
    DoctorTaskOutput,
    ImageReview
)

class DoctorAgent:
    """
    The Attending Physician Agent.
    
    Responsibilities:
    1. Analyze Situation (Hypothesis Generation)
    2. Prescribe Tasks (Task Generation based on Critique)
    3. Rank Images (Evidence Selection)
    """
    
    def __init__(self, model_key: Optional[str] = None):
        self.model_key = model_key or config.model.default_model
        # Primary LLM for logic
        self.llm = create_model(self.model_key, agent_name="doctor")
        self.logger = get_logger()
        self.messages: list[BaseMessage] = []
        # Retry logic
        self.max_retries = 2
        
    def reset(self):
        self.messages = []

    def analyze_situation(
        self,
        patient: PatientVisit,
        calculations: list[CalculationResult],
        vitals_summary: str,
        clinical_context: str = "",
        iteration: int = 1,
        image_reviews: Optional[list[ImageReview]] = None,
        available_image_paths: Optional[list[str]] = None
    ) -> str:
        """
        Step 1: Analyze the current state and generate working hypotheses.
        Does NOT generate tasks yet.
        """
        start_time = time.time()
        
        try:
            # Format summarized context
            calc_summary = "No calculations yet."
            if calculations:
                calc_summary = "\n".join([c.to_summary() for c in calculations])
            
            prompt = DOCTOR_ANALYSIS_TEMPLATE.format(
                iteration=iteration,
                clinical_context=clinical_context,
                vitals_summary=vitals_summary,
                calculation_results=calc_summary
            )
            
            # Simple stateless call for analysis (or could be stateful if we keep history)
            # Keeping history aids continuity across rounds.
            if not self.messages:
                self.messages = [SystemMessage(content=DOCTOR_SYSTEM_PROMPT)]
            
            # Construct Multimodal Message if images are provided
            # Standard order: [Images..., Text]
            image_parts = []
            
            if image_reviews and available_image_paths:
                # Create a map for fast lookup: filename -> full_path
                path_map = {p.split('/')[-1]: p for p in available_image_paths}
                
                # Load images for the Doctor to see
                # We only attach the reviewed images (Top N)
                max_images = self.llm.config.max_images
                attached_count = 0
                
                # Sort by relevance to prioritize best images if we must truncate
                sorted_reviews = sorted(image_reviews, key=lambda x: x.relevance_score, reverse=True)
                
                for rev in sorted_reviews:
                    if attached_count >= max_images:
                        break
                        
                    full_path = path_map.get(rev.filename)
                    if full_path:
                        try:
                            with open(full_path, "rb") as f:
                                b64 = base64.b64encode(f.read()).decode('utf-8')
                                image_parts.append({
                                    "type": "image_url",
                                    "image_url": {"url": f"data:image/png;base64,{b64}"}
                                })
                                attached_count += 1
                        except Exception as e:
                            self.logger.log_error(f"Failed to load image for analysis {full_path}: {e}")
                    else:
                        self.logger.log_warning(f"Image review references missing file: {rev.filename}")

            # Assemble content: Images first, then Text
            message_content = image_parts + [{"type": "text", "text": prompt}]
            
            # Prune images from PREVIOUS messages to avoid hitting total request limit
            # The model counts total images in the context, so we remove old ones and only keep the latest.
            for msg in self.messages:
                if isinstance(msg, HumanMessage) and isinstance(msg.content, list):
                    # Filter out images, keep text
                    msg.content = [
                        item for item in msg.content 
                        if isinstance(item, dict) and item.get("type") != "image_url"
                    ]

            self.messages.append(HumanMessage(content=message_content))
            
            response = self.llm.invoke(self.messages)
            analysis_text = response.content
            
            self.messages.append(AIMessage(content=analysis_text))
            
            self.logger.log_agent_step("doctor_analysis", {}, {"text": analysis_text[:100]}, (time.time() - start_time) * 1000)
            return analysis_text
            
        except Exception as e:
            self.logger.log_error(f"Doctor Analysis failed: {e}")
            raise e

    def prescribe_tasks(
        self,
        analysis_text: str,
        consultant_feedback: str,
        max_images: int = 10
    ) -> DoctorTaskOutput:
        """
        Step 3: Synthesize feedback and prescribe tasks.
        Returns structured tasks (parsed by Orchestrator).
        
        NOTE: This is a STATELESS call. The prompt already contains the Doctor's
        analysis and Consultant's critique, which synthesize all prior context.
        Full history is redundant and causes context bloat.
        We still append to self.messages for downstream steps (e.g., next round's analyze_situation).
        """
        start_time = time.time()
        try:
            prompt = DOCTOR_TASK_SYSTEM_PROMPT.format(
                doctor_analysis=analysis_text,
                consultant_feedback=consultant_feedback,
                max_images=max_images
            )
            
            # Stateless invocation with self-contained prompt
            structured_llm = self.llm.with_structured_output(DoctorTaskOutput)
            result = structured_llm.invoke([HumanMessage(content=prompt)])
            
            # We add to messages fixed human message and AI response to not increase too much history but still preserve knowledge for downstream steps
            # Convert list of tasks back to string representation for history
            task_text = "\n".join([f"- {t}" for t in result.tasks])
            
            self.messages.append(HumanMessage(content="Based on the doctor analysis and consultant feedback, generate the tasks for the Coder agent."))
            self.messages.append(AIMessage(content=task_text))
            
            self.logger.log_agent_step("doctor_tasks", {}, {"tasks": result.tasks}, (time.time() - start_time) * 1000)
            return result
            
        except Exception as e:
            self.logger.log_error(f"Doctor Task Prescription failed: {e}")
            # Fallback to empty list
            return DoctorTaskOutput(tasks=[])
            
    def _evaluate_image_batch(self, batch_images: list[dict], clinical_context: str, analysis_text: str) -> DoctorRankingOutput:
        try:
            # Prepare numbered text summary so LLM can reference by index
            results_text = "\n".join([f"Image {i+1}: {img['filename']} (Metric: {img['metric']})" for i, img in enumerate(batch_images)])
            
            # Create index -> filename mapping for post-processing
            index_to_filename = {i+1: img['filename'] for i, img in enumerate(batch_images)}
            
            # Prepare multimodal prompt: [Images..., Text]
            content = []
            
            # Attach images first (in order matching the numbered list)
            attached_count = 0
            for img in batch_images:
                try:
                    with open(img['path'], "rb") as f:
                        b64 = base64.b64encode(f.read()).decode('utf-8')
                        content.append({
                            "type": "image_url",
                            "image_url": {"url": f"data:image/png;base64,{b64}"}
                        })
                        attached_count += 1
                except Exception as e:
                    self.logger.log_error(f"Failed to load image {img['path']}: {e}")
            
            # Append text prompt after images
            content.append({
                "type": "text", 
                "text": DOCTOR_RANKING_TEMPLATE.format(
                    calculation_results=results_text,
                    clinical_context=clinical_context,
                    doctor_analysis=analysis_text,
                    num_images=len(batch_images)
                )
            })
            
            if attached_count == 0 and len(batch_images) > 0:
                self.logger.log_warning("Failed to attach any images to the prompt")
                return DoctorRankingOutput(selected_images=[], is_sufficient=False)

            structured_llm = self.llm.with_structured_output(DoctorRankingOutput)
            
            messages = [
                SystemMessage(content=DOCTOR_RANKING_SYSTEM_PROMPT),
                HumanMessage(content=content)
            ]
            
            # Retry loop to ensure we get a valid response
            for attempt in range(self.max_retries):
                result = structured_llm.invoke(messages)
                
                # VALIDATE: Check if we got a review for every image
                selected = result.selected_images if result else []
                
                if len(selected) == len(batch_images):
                    # POST-PROCESS: Map image_index back to actual filenames
                    if result and result.selected_images:
                        for review in result.selected_images:
                            actual_filename = index_to_filename.get(review.image_index, "")
                            if actual_filename:
                                review.filename = actual_filename
                            else:
                                self.logger.log_warning(f"Invalid image_index {review.image_index} returned by LLM (valid: 1-{len(batch_images)})")
                    
                    return result
                
                # Failure case
                if attempt < self.max_retries - 1:
                    self.logger.log_warning(f"Ranking mismatch (Attempt {attempt+1}): Expected {len(batch_images)}, got {len(selected)}. Retrying with feedback.")
                    
                    # Synthesize history to guide correction
                    previous_json = result.model_dump_json() if result else "{}"
                    messages.append(AIMessage(content=previous_json))
                    messages.append(HumanMessage(content=f"Error: You returned {len(selected)} reviews, but I provided {len(batch_images)} images. You must review ALL {len(batch_images)} images provided. Please fix and return a list of exactly {len(batch_images)} items."))
            
            # If all retries failed, return whatever we got (will be filtered later)
            return result
        except Exception as e:
            self.logger.log_error(f"Batch evaluation failed: {e}")
            return DoctorRankingOutput(selected_images=[], is_sufficient=False)

    def rank_images(
        self,
        new_results: list[CalculationResult],
        clinical_context: str,
        analysis_text: str,
        existing_reviews: Optional[list[ImageReview]] = None
    ) -> DoctorRankingOutput:
        """
        Step 5: Review new images and rank them.
        Optimized Strategy: Rank New -> Merge -> Prune.

        NOTE: This is a STATEFUL call. The prompt only contains the new images to rank.
        Full history is redundant and causes context bloat.
        We don't append to self.messages for downstream steps since this
        """
        start_time = time.time()
        existing = existing_reviews or []
        
        # 1. Collect NEW images
        new_images = []
        for res in new_results:
            if res.success and res.image_paths:
                for path in res.image_paths:
                    new_images.append({
                        "metric": res.metric_name,
                        "path": path,
                        "filename": path.split('/')[-1]
                    })
        
        if not new_images:
            return DoctorRankingOutput(selected_images=[], is_sufficient=False)
            
        # 2. Determine Strategy based on Model Limits
        max_images = self.llm.config.max_images

        # STRATEGY: Evaluate NEW images only
        new_reviews = []
        final_is_sufficient = False
        
        if new_images:
            # Batch process new images
            for i in range(0, len(new_images), max_images):
                batch = new_images[i : i + max_images]
                result = self._evaluate_image_batch(batch, clinical_context, analysis_text)
                if result:
                    # Filter out reviews with empty filenames (invalid indices)
                    # Use getattr since filename is added dynamically after mapping
                    valid_reviews = [rev for rev in result.selected_images if getattr(rev, 'filename', '')]
                    new_reviews.extend(valid_reviews)
                    
                    # Logic: If ANY batch says it's sufficient, we mark it as sufficient.
                    if result.is_sufficient:
                        final_is_sufficient = True
        
        # 2. Merge with Existing (Pre-ranked)
        # We trust the scores of existing reviews.
        # Deduplicate by filename (prefer NEW if collision, though unlikely)
        unique_reviews = {getattr(rev, 'filename', str(id(rev))): rev for rev in existing}
        for rev in new_reviews:
            unique_reviews[getattr(rev, 'filename', str(id(rev)))] = rev  # Overwrite/Add
            
        # 3. Prune (Keep Top N)
        all_reviews = list(unique_reviews.values())
        sorted_reviews = sorted(all_reviews, key=lambda x: x.relevance_score, reverse=True)
        top_reviews = sorted_reviews[:max_images]
        
        return DoctorRankingOutput(
            selected_images=top_reviews,
            is_sufficient=final_is_sufficient
        )
