"""
Clinical interpretation logic for the Coder agent.
"""

def get_shock_index_interpretation(si: float) -> str:
    """Interpret Shock Index (HR / SBP)."""
    if si < 0.5:
        return f"Low ({si:.2f}), reference range 0.5-0.7. Consider hypertension or relative bradycardia."
    elif si <= 0.7:
        return f"Normal ({si:.2f}), within reference range 0.5-0.7. No hemodynamic instability indicated."
    elif si <= 1.0:
        return f"Elevated ({si:.2f}), above normal range (0.5-0.7). Early compensated shock possible, monitor closely."
    else:
        return f"HIGH ({si:.2f}), significantly above normal (0.5-0.7). Suggests decompensated shock, immediate intervention needed."

def get_map_interpretation(map_value: float) -> str:
    """Interpret Mean Arterial Pressure."""
    if map_value < 65:
        return f"LOW ({map_value:.0f} mmHg), below critical threshold of 65 mmHg. Indicates inadequate organ perfusion pressure."
    elif map_value <= 100:
        return f"Normal ({map_value:.0f} mmHg), within reference range 65-100 mmHg. Adequate perfusion pressure maintained."
    else:
        return f"Elevated ({map_value:.0f} mmHg), above reference range (65-100 mmHg). Consider hypertensive state."

def get_spo2_interpretation(min_val: float, slope: float, r_squared: float = 0.0) -> str:
    """Interpret SpO2 trend."""
    if min_val < 90:
        return f"CRITICAL: SpO2 dropped to {min_val:.0f}% - hypoxemia detected"
    elif min_val < 94:
        return f"Concerning: SpO2 reached {min_val:.0f}% during observation"
    elif slope < -0.05:
        return f"Declining trend (slope={slope:.3f}%/sample, R²={r_squared:.2f})"
    elif slope > 0.05:
        return f"Improving trend (slope={slope:.3f}%/sample)"
    else:
        return "Stable oxygen saturation"

def get_hr_volatility_interpretation(daily_cv: float) -> str:
    """Interpret Heart Rate Volatility."""
    if daily_cv < 10:
        return f"Low/Normal specific Heart Rate Volatility ({daily_cv:.1f}%), stable autonomic function"
    elif daily_cv < 20:
        return f"Moderate Heart Rate Volatility ({daily_cv:.1f}%), may indicate autonomic stress/response"
    else:
        return f"High Heart Rate Volatility ({daily_cv:.1f}%), indicative of significant autonomic instability or arrhythmia"

def get_pulse_pressure_interpretation(pp: float) -> str:
    """Interpret Pulse Pressure (SBP - DBP)."""
    if pp < 25: # Very narrow threshold
        return f"Narrow ({pp:.0f} mmHg), critical (<25). Possible tamponade, heart failure, or significant blood loss."
    elif pp < 40:
        return f"Narrow-Normal ({pp:.0f} mmHg), <40 mmHg. Monitor for declining stroke volume."
    elif pp <= 60:
        return f"Normal ({pp:.0f} mmHg), within reference range 40-60 mmHg."
    else:
        return f"Wide ({pp:.0f} mmHg), >60 mmHg. Consider stiffness, hyperthyroidism, or increased ICP (Cushing's)."

def get_qsofa_interpretation(score: int, criteria_met: list[str]) -> str:
    """Interpret qSOFA score."""
    if score >= 2:
        return f"High Risk (Score {score}/3). Criteria met: {', '.join(criteria_met)}. Associated with poor outcomes in sepsis."
    elif score == 1:
        return f"Moderate Risk (Score {score}/3). Criteria met: {', '.join(criteria_met)}. Monitor closely."
    else:
        return f"Low Risk (Score {score}/3). Sepsis screening negative."

def get_sirs_interpretation(score: int, criteria_met: list[str]) -> str:
    """Interpret SIRS score."""
    if score >= 2:
        return f"POSITIVE (Score {score}/4). Criteria met: {', '.join(criteria_met)}. Sepsis screening warranted if infection suspected."
    else:
        return f"Negative (Score {score}/4). Criteria met: {', '.join(criteria_met) if criteria_met else 'None'}."
