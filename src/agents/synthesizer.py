"""
Synthesizer Agent - Synthesizes a comprehensive clinical assessment.
"""

import time
from typing import Optional
from langchain_core.messages import SystemMessage, HumanMessage

from ..prompts import (
    SYNTHESIZER_SYSTEM_PROMPT, 
    SYNTHESIZER_USER_TEMPLATE,
    ZeroShotAssessment,
    AgentOutput
)
from ..config import config
from ..models import create_model
from ..logging import get_logger
from ..data.schema import PatientVisit, VitalSignSeries

class SynthesizerAgent:
    """
    Agent responsible for synthesizing comprehensive clinical assessments 
    from the outputs of the doctor agent.
    """
    def __init__(self, model_key: Optional[str] = None):
        self.model_key = model_key or config.model.default_model
        self.llm = create_model(self.model_key, agent_name="synthesizer")
        self.logger = get_logger()
        self.max_images = min(3, self.llm.config.max_images)

    def synthesize(
        self, 
        patient: PatientVisit, 
        vitals: Optional[VitalSignSeries],
        output: AgentOutput,
        clinical_context: str = "",
        iteration: int = 1,
        top_images: Optional[list] = None
    ) -> ZeroShotAssessment:
        """
        Synthesize a comprehensive clinical assessment using a dedicated LLM pass.
        Matches ZeroShotAssessment schema for consistent benchmarking.
        """
        start_time = time.time()
        top_images = top_images or []
        
        try:
            # Gather Calculations and Observations
            calc_summaries = [c.to_summary() for c in output.calculations if c.success]
            # Prepare Doctor's Evolution (History) - Interleaved with Consultant
            doctor_evolution = "No assessment available."
            if output.doctor_history:
                history_blocks = []
                for i, doctor_text in enumerate(output.doctor_history):
                    # Add doctor's analysis
                    history_blocks.append(f"### Iteration {i+1}\n\n**Doctor's Analysis:**\n{doctor_text}")
                    
                    # Add consultant's critique if available
                    if i < len(output.consultant_history):
                        consultant_text = output.consultant_history[i]
                        history_blocks.append(f"**Consultant's Critique:**\n{consultant_text}")
                
                doctor_evolution = "\n\n".join(history_blocks)

            # Prepare Image Reviews (Ranked) from Top-K Selection
            image_reviews_text = "No visualizations selected."
            if top_images:
                lines = []
                for i, rev in enumerate(top_images):
                    lines.append(f"Figure {i+1}: [{rev.filename}] - {rev.description} (Relevance: {rev.relevance_score})")
                image_reviews_text = "\n".join(lines)

            # Build synthesis prompt
            data_context = SYNTHESIZER_USER_TEMPLATE.format(
                clinical_context=clinical_context,
                vitals_summary=vitals.to_text_summary() if vitals else "No vital signs available.",
                calculation_results=chr(10).join(calc_summaries),
                doctor_evolution=doctor_evolution,
                image_reviews=image_reviews_text,
            )
            
            messages = [
                SystemMessage(content=SYNTHESIZER_SYSTEM_PROMPT),
                HumanMessage(content=data_context),
            ]
            
            # We want structured output to ensure consistency
            structured_syn = self.llm.with_structured_output(ZeroShotAssessment)
            assessment = structured_syn.invoke(messages)
            
            # Log the synthesis step
            duration_ms = (time.time() - start_time) * 1000
            self.logger.log_agent_step(
                agent_name="synthesizer",
                input_data={
                    "visit_id": patient.visit_id,
                    "iteration": iteration,
                    "num_calculations": len(calc_summaries),
                },
                output_data={
                    "assessment_length": len(assessment.patient_overview) if assessment else 0,
                    "esi_level": assessment.esi_level if assessment else None,
                    "success": True
                },
                duration_ms=duration_ms
            )
            
            return assessment

        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            self.logger.log_agent_step(
                agent_name="synthesizer",
                input_data={
                    "visit_id": patient.visit_id,
                    "iteration": iteration,
                },
                output_data={
                    "success": False,
                    "error": str(e)
                },
                duration_ms=duration_ms
            )
            raise e
