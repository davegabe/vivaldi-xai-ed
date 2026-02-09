"""
Shared prompts and schemas for Zero-Shot baselines.

Used by:
- zero_shot.py (synchronous)
"""

# =============================================================================
# SHARED SYSTEM PROMPT
# =============================================================================

ZERO_SHOT_SYSTEM_PROMPT = """You are a Senior Emergency Physician providing clinical decision support.
Your role is to analyze a patient's chief complaint and clinical context to provide a comprehensive clinical assessment with ESI triage, risk stratification, and actionable recommendations.

## Clinical Guidelines
1. **Analyze Data**: Review all raw and aggregate clinical data to reach your conclusions.
2. **Clinical Justification**: Provide detailed pathophysiologic reasoning for your ESI, Pain, and LOS estimates within the relevant schema fields.
"""

ZERO_SHOT_USER_PROMPT_TEMPLATE = """## Patient Context
- Age: {age} years
- Gender: {gender}
- Ethnicity: {ethnicity}
- Chief Complaint: {chief_complaint}

## Clinical Data
{vitals_summary}

## Recent Vital Signs (Last 30 Samples)
{vitals_raw}

## Medical Background
{pmh_list}

## Medications
{meds_list}

## Objective
Analyze this patient and provide a clinical assessment.
Note: You must calculate all derived metrics (Shock Index, MAP, qSOFA, SIRS, Pulse Pressure, SpO2 Trend, HR Volatility) yourself directly from the raw vital signs provided.
"""
