"""
Zero-Shot Baseline - Single LLM forward pass.
"""

import time
from typing import Optional
from langchain_core.messages import SystemMessage, HumanMessage

from ..config import config
from ..data.schema import PatientVisit, VitalSignSeries
from ..logging import get_logger
from ..models import create_model
from ..utils.vitals_plots import generate_vitals_panel
from ..prompts import (
    ZeroShotAssessment,
    ZeroShotAblatedAssessment,
    ZERO_SHOT_SYSTEM_PROMPT, 
    ZERO_SHOT_USER_PROMPT_TEMPLATE,
    ClinicalOutput,
)


class ZeroShotBaseline:
    """
    Single LLM forward pass baseline using MENTAL MATH.
    
    METHODOLOGY:
    This agent mimics standard LLM usage where the model is asked to "calculate"
    metrics directly in the prompt. This relies on the model's internal weights 
    and next-token prediction ("mental math"), which is prone to arithmetic hallucinations.
    
    Used as a baseline to measure the accuracy improvement of the Agentic 
    (code-execution) approach.
    """
    
    def __init__(self, model_key: Optional[str] = None, ablation: bool = False):
        self.model_key = model_key or config.model.default_model
        
        # Helper to differentiate agent name for logging
        agent_name = "zero_shot_ablated" if ablation else "zero_shot"
        self.ablation = ablation
        
        self.llm = create_model(self.model_key, agent_name=agent_name)
        self.logger = get_logger()
        # Output directory base (will be visits/visit_id/figures)
        self.output_base = self.logger.output_dir / "visits"
    
    def process_visit(
        self,
        patient: PatientVisit,
        vitals: Optional[VitalSignSeries] = None,
        pmh: Optional[list[str]] = None,
        meds: Optional[list[str]] = None,
    ) -> ClinicalOutput:
        """Single forward pass - all logged."""
        start_time = time.time()
        
        try:
            # Generate comprehensive vitals panel for embedding in output
            vitals_image = None
            if vitals and vitals.has_data():
                try:
                    # Standardize path: logs/visits/<visit_id>/figures
                    figures_dir = self.output_base / patient.visit_id / "figures"
                    figures_dir.mkdir(parents=True, exist_ok=True)
                    
                    plot_path, plot_b64 = generate_vitals_panel(
                        vitals, 
                        output_dir=figures_dir, 
                        visit_id=patient.visit_id
                    )
                    if plot_path and plot_b64:
                        vitals_image = {
                            "path": str(plot_path),
                            "caption": "Vital Signs Trend Analysis",
                            "base64": plot_b64,
                            "narrative": "Comprehensive overview of vital sign trends throughout the ED visit."
                        }
                except Exception as e:
                    self.logger.log_error(f"Failed to generate vitals panel: {e}")
            
            # Build comprehensive prompt with raw data
            prompt = self._build_prompt(patient, vitals, pmh, meds)
            sys_prompt = ZERO_SHOT_SYSTEM_PROMPT
            
            if self.ablation:
                schema = ZeroShotAblatedAssessment
            else:
                schema = ZeroShotAssessment
            
            messages = [
                SystemMessage(content=sys_prompt),
                HumanMessage(content=prompt),
            ]
            
            # Invoke with structured output
            structured_llm = self.llm.with_structured_output(schema, method="json_mode")
            
            try:
                assessment = structured_llm.invoke(messages)
            except Exception as e:
                self.logger.log_error(f"Zero-shot invocation failed: {e}")
                raise  # Re-raise to surface the error
            
            duration_ms = (time.time() - start_time) * 1000
            
            # Convert to standard ClinicalOutput with embedded vitals image
            output = ClinicalOutput.from_dict(
                assessment.model_dump(), 
                visit_id=patient.visit_id, 
                approach="zero_shot"
            )
            
            # Attach vitals panel if generated
            if vitals_image:
                output.embedded_images.append(vitals_image)
            
            # Log the agent step (manual log since we bypassed wrapper for structured output)
            self.logger.log_agent_step(
                agent_name="zero_shot_ablated" if self.ablation else "zero_shot",
                input_data={
                    "visit_id": patient.visit_id,
                    "chief_complaint": patient.chief_complaint,
                    "has_vitals": vitals is not None,
                    "prompt_length": len(prompt),
                },
                output_data={
                    "esi_level": output.esi_level,
                    "pain_score": output.pain_score,
                    "ed_los": output.ed_los,
                    "shock_index": output.metrics.shock_index,
                    "success": True
                },
                duration_ms=duration_ms,
            )
            
            return output

        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            self.logger.log_agent_step(
                agent_name="zero_shot",
                input_data={
                    "visit_id": patient.visit_id,
                    "chief_complaint": patient.chief_complaint,
                },
                output_data={
                    "success": False,
                    "error": str(e)
                },
                duration_ms=duration_ms,
            )
            raise e

    def _build_prompt(
        self,
        patient: PatientVisit,
        vitals: Optional[VitalSignSeries],
        pmh: Optional[list[str]],
        meds: Optional[list[str]],
    ) -> str:
        """Build comprehensive prompt using the unified template."""
        
        # Build vitals summary and raw data using standardized methods
        vitals_summary = vitals.to_text_summary() if vitals else "No vitals available"
        vitals_raw = vitals.to_text_raw(30) if vitals else "No vitals available"
        
        # Build PMH list
        pmh_list = "\n".join(f"- {c}" for c in pmh) if pmh else "None"
        
        # Build medications list
        meds_list = "\n".join(f"- {m}" for m in meds) if meds else "None"
        
        # Format the unified template
        return ZERO_SHOT_USER_PROMPT_TEMPLATE.format(
            visit_id=patient.visit_id,
            age=patient.demographics.age,
            gender=patient.demographics.gender,
            ethnicity=patient.demographics.ethnicity,
            chief_complaint=patient.chief_complaint or "Not specified",
            vitals_summary=vitals_summary,
            vitals_raw=vitals_raw,
            pmh_list=pmh_list,
            meds_list=meds_list,
        )
