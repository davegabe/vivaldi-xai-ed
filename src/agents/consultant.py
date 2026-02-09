"""
Consultant Agent (Specialist) - Curbside Consult for Differential Diagnosis.
"""

import time
from typing import Optional
from langchain_core.messages import SystemMessage, HumanMessage

from ..config import config
from ..logging import get_logger
from ..models import create_model
from ..prompts import (
    CONSULTANT_SYSTEM_PROMPT,
    CONSULTANT_USER_TEMPLATE,
    CalculationResult
)

class ConsultantAgent:
    """
    The Specialist Consultant.
    
    Responsibilities:
    1. Critique the Doctor's ANALYSIS (not plan yet).
    2. Suggest alternative diagnoses (Differential).
    """
    
    def __init__(self, model_key: Optional[str] = None):
        self.model_key = model_key or config.model.default_model
        self.llm = create_model(self.model_key, agent_name="consultant")
        self.logger = get_logger()
        
    def critique_analysis(
        self,
        doctor_analysis_text: str,
        vitals_summary: str,
        clinical_context: str,
        calculations: list[CalculationResult]
    ) -> str:
        """
        Review the Doctor's Analysis and provide feedback.
        """
        start_time = time.time()
        
        try:
            # Format calculations
            calc_summary = "No calculations yet."
            if calculations:
                calc_summary = "\n".join([c.to_summary() for c in calculations])
                
            # Format user prompt
            user_prompt = CONSULTANT_USER_TEMPLATE.format(
                vitals_summary=vitals_summary,
                clinical_context=clinical_context,
                calculation_results=calc_summary,
                doctor_analysis=doctor_analysis_text
            )
            
            messages = [
                SystemMessage(content=CONSULTANT_SYSTEM_PROMPT),
                HumanMessage(content=user_prompt)
            ]
            
            # Invoke LLM
            response = self.llm.invoke(messages)
            raw_text = response.content
            
            duration_ms = (time.time() - start_time) * 1000
            self.logger.log_agent_step(
                agent_name="consultant",
                input_data={"doctor_analysis_preview": doctor_analysis_text[:50]},
                output_data={
                    "text_preview": raw_text[:100],
                    "success": True
                },
                duration_ms=duration_ms
            )
            
            return raw_text

        except Exception as e:
            self.logger.log_error(f"Consultant Critique failed: {e}")
            raise e
