"""
Centralized prompt management for the XAI-agent-pulse system.
This module exports all prompts, templates, schemas, and interpretation logic used across agents.
"""

from .agentic_structs import (
    TriageOutput,
    TriageAssignmentResult,
    TriageArtifacts,
    AgentOutput, 
    IterationHistory, 
    CalculationResult,
    ZeroShotAssessment,
    ZeroShotAblatedAssessment,
    ImageReview,
    DoctorRankingOutput,
    DoctorTaskOutput
)
from .agentic_prompts import (
    TRIAGE_SYSTEM_PROMPT,
    TRIAGE_USER_TEMPLATE,
    DOCTOR_SYSTEM_PROMPT,
    CONSULTANT_SYSTEM_PROMPT,
    CONSULTANT_USER_TEMPLATE,
    CODER_SYSTEM_PROMPT,
    CODER_USER_TEMPLATE,
    SYNTHESIZER_SYSTEM_PROMPT,
    SYNTHESIZER_USER_TEMPLATE,
    DOCTOR_ANALYSIS_TEMPLATE,
    DOCTOR_TASK_SYSTEM_PROMPT,
    DOCTOR_RANKING_TEMPLATE,
    DOCTOR_RANKING_SYSTEM_PROMPT,
)

from .coder_interpretations import (
    get_shock_index_interpretation,
    get_map_interpretation,
    get_spo2_interpretation,
    get_hr_volatility_interpretation,
    get_pulse_pressure_interpretation,
    get_qsofa_interpretation,
    get_sirs_interpretation,
)

from .output_template import (
    DerivedMetrics,
    ClinicalOutput,
)

from .zero_shot_prompts import (
    ZERO_SHOT_SYSTEM_PROMPT,
    ZERO_SHOT_USER_PROMPT_TEMPLATE,
)

__all__ = [
    # Agentic schemas
    "TriageOutput",
    "TriageAssignmentResult",
    "TriageArtifacts",
    "AgentOutput",
    "IterationHistory",
    "CalculationResult",
    "ZeroShotAssessment",
    "ZeroShotAblatedAssessment",
    "ImageReview",
    "DoctorRankingOutput",
    "DoctorTaskOutput",
    # Agentic prompts
    "TRIAGE_SYSTEM_PROMPT",
    "TRIAGE_USER_TEMPLATE",
    "DOCTOR_SYSTEM_PROMPT",
    "CONSULTANT_SYSTEM_PROMPT",
    "CONSULTANT_USER_TEMPLATE",
    "CODER_SYSTEM_PROMPT",
    "CODER_USER_TEMPLATE",
    "SYNTHESIZER_SYSTEM_PROMPT",
    "SYNTHESIZER_USER_TEMPLATE",
    "DOCTOR_ANALYSIS_TEMPLATE",
    "DOCTOR_TASK_SYSTEM_PROMPT",
    "DOCTOR_RANKING_TEMPLATE",
    "DOCTOR_RANKING_SYSTEM_PROMPT",
    "ZERO_SHOT_SYSTEM_PROMPT",
    "ZERO_SHOT_USER_PROMPT_TEMPLATE",
    # Coder interpretations
    "get_shock_index_interpretation",
    "get_map_interpretation",
    "get_spo2_interpretation",
    "get_hr_volatility_interpretation",
    "get_pulse_pressure_interpretation",
    "get_qsofa_interpretation",
    "get_sirs_interpretation",
    # Output templates
    "DerivedMetrics",
    "ClinicalOutput",
    "AgentOutput",
    "IterationHistory",
    "CalculationResult"
]
