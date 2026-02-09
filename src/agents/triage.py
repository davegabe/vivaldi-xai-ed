"""
Triage Agent - Phase 0 Safety & Context.
Establish safety baselines and personalized interpretations before agentic reasoning.
"""

import time
from typing import Dict, Any, Optional, List, Tuple
from pathlib import Path
from langchain_core.messages import SystemMessage, HumanMessage

import numpy as np
from scipy.stats import linregress

from ..config import config
from ..logging import get_logger
from ..models import create_model
from ..data.schema import PatientVisit, VitalSignSeries
from ..utils.vitals_plots import generate_vitals_panel
from ..prompts import (
    TRIAGE_SYSTEM_PROMPT,
    TRIAGE_USER_TEMPLATE,
    TriageAssignmentResult,
    TriageArtifacts,
    TriageOutput,
    CalculationResult,
    get_shock_index_interpretation,
    get_map_interpretation,
    get_spo2_interpretation,
    get_hr_volatility_interpretation,
    get_pulse_pressure_interpretation,
    get_qsofa_interpretation,
    get_sirs_interpretation,
)

class TriageAgent:
    """
    The Triage Agent.
    
    Responsibilities:
    1. Deterministic Safety Calculations (via Coder) - Single Source of Truth for safety metrics.
    2. Context Synthesis (LLM) - Ingests PMH/Meds to generate clinical context summary and personalized thresholds.
    3. Artifact Generation (Vitals Panel) - Visualizes vitals with personalized threshold bands.
    """
    
    def __init__(self, model_key: Optional[str] = None):
        self.model_key = model_key or config.model.default_model
        # Use a faster/cheaper model if possible, but reliability is key
        self.llm = create_model(self.model_key, agent_name="triage")
        self.logger = get_logger()
        
    def run_assignment(
        self,
        patient: PatientVisit,
        vitals: VitalSignSeries,
        output_dir: Path,
        pmh: Optional[List[str]] = None,
        meds: Optional[List[str]] = None
    ) -> TriageAssignmentResult:
        """
        Execute the Triage assignment.
        Returns a structured TriageAssignmentResult.
        """
        start_time = time.time()
        visit_id = patient.visit_id
        
        try:
            # 1. Deterministic Safety Metrics (Migrated from Coder)
            # Calculated locally for consistency and speed
            safety_metrics = self._calculate_safety_metrics(vitals, visit_id)
            
            # 2. LLM Context Synthesis
            # Generate personalized thresholds and context summary
            context_output = self._synthesize_context(patient, pmh, meds, vitals)
            
            # 3. Generate Visualizations (using personalized thresholds)
            plot_path = self._generate_artifacts(
                vitals, 
                output_dir, 
                visit_id, 
                context_output.thresholds if context_output else None,
                context_output.warning_thresholds if context_output else None
            )
            
            duration_ms = (time.time() - start_time) * 1000
            
            # Log the step
            self.logger.log_agent_step(
                agent_name="triage",
                input_data={"visit_id": visit_id},
                output_data={
                    "safety_metrics": safety_metrics,
                    "context": context_output.model_dump() if context_output else None,
                    "success": True
                },
                duration_ms=duration_ms
            )
            
            # Combine into a unified result object
            return TriageAssignmentResult(
                metrics=safety_metrics,
                context=context_output,
                artifacts=TriageArtifacts(vitals_panel=str(plot_path) if plot_path else None)
            )

        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            self.logger.log_agent_step(
                agent_name="triage",
                input_data={"visit_id": visit_id},
                output_data={
                    "success": False,
                    "error": str(e)
                },
                duration_ms=duration_ms
            )
            raise e

    def _calculate_safety_metrics(
        self, 
        vitals: VitalSignSeries, 
        visit_id: str
    ) -> Dict[str, Any]:
        """Calculate deterministic safety scores locally."""
        metrics = {}
        
        # 1. Shock Index
        si_res = self._calculate_shock_index(vitals)
        if si_res.success:
            metrics["shock_index"] = si_res.value
            metrics["shock_index_interpretation"] = si_res.interpretation
            
        # 2. MAP
        map_res = self._calculate_map(vitals)
        if map_res.success:
            metrics["map_value"] = map_res.value
            metrics["map_interpretation"] = map_res.interpretation
            
        # 3. Pulse Pressure
        pp_res = self._calculate_pulse_pressure(vitals)
        if pp_res.success:
            metrics["pulse_pressure"] = pp_res.value
            
        # 4. qSOFA
        qsofa_res = self._calculate_qsofa(vitals)
        if qsofa_res.success:
            metrics["qsofa_score"] = qsofa_res.value
            metrics["qsofa_interpretation"] = qsofa_res.interpretation
            
        # 5. SIRS
        sirs_res = self._calculate_sirs(vitals)
        if sirs_res.success:
            metrics["sirs"] = sirs_res.value
            
        # 6. SpO2 Trend
        spo2_res = self._calculate_spo2_trend(vitals)
        if spo2_res.success:
            metrics["spo2_trend"] = spo2_res.value
            
        # 7. HR Volatility
        hrv_res = self._calculate_hr_volatility(vitals)
        if hrv_res.success:
            metrics["hr_volatility"] = hrv_res.value
                
        return metrics

    def _get_robust_arrival_value(self, values: List[float], n: int = 5) -> float:
        """
        Get a robust estimate of the 'arrival' value by taking the median of the FIRST n points.
        This focuses on the patient's presentation state for Triage, filtering initial artifacts.
        """
        if not values:
            return 0.0
        
        # Take first n values (or fewer if not enough data)
        initial = values[:n]
        # Return median to filter outliers
        return float(np.median(initial))

    def _calculate_shock_index(self, vitals: VitalSignSeries) -> CalculationResult:
        """Calculate Shock Index = HR / SBP."""
        if not vitals.heart_rate or not vitals.systolic_bp:
            return CalculationResult(
                success=False,
                metric_name="Shock Index",
                value=None,
                error_message="Missing heart rate or systolic BP data",
            )
        
        hr_values = [v.value for v in vitals.heart_rate]
        sbp_values = [v.value for v in vitals.systolic_bp]
        
        # Use robust arrival values (Median of first 5)
        hr_initial = self._get_robust_arrival_value(hr_values)
        sbp_initial = self._get_robust_arrival_value(sbp_values)
        
        if sbp_initial == 0:
            return CalculationResult(
                success=False,
                metric_name="Shock Index",
                value=None,
                error_message="Initial Systolic BP is zero (invalid)",
            )
        
        shock_index = hr_initial / sbp_initial
        interpretation = get_shock_index_interpretation(shock_index)
        
        return CalculationResult(
            success=True,
            metric_name="Shock Index",
            value=round(shock_index, 3),
            unit="ratio",
            interpretation=interpretation,
            code_executed=f"shock_index = robust_arrival(HR) {hr_initial:.1f} / robust_arrival(SBP) {sbp_initial:.1f} = {shock_index:.3f}",
        )
    
    def _calculate_map(self, vitals: VitalSignSeries) -> CalculationResult:
        """Calculate Mean Arterial Pressure = DBP + 1/3(SBP - DBP)."""
        if not vitals.systolic_bp or not vitals.diastolic_bp:
            return CalculationResult(
                success=False,
                metric_name="MAP",
                value=None,
                error_message="Missing blood pressure data",
            )
        
        sbp_values = [v.value for v in vitals.systolic_bp]
        dbp_values = [v.value for v in vitals.diastolic_bp]
        
        # Use robust arrival values
        sbp_initial = self._get_robust_arrival_value(sbp_values)
        dbp_initial = self._get_robust_arrival_value(dbp_values)
        
        map_value = dbp_initial + (sbp_initial - dbp_initial) / 3
        interpretation = get_map_interpretation(map_value)
        
        return CalculationResult(
            success=True,
            metric_name="MAP",
            value=round(map_value, 1),
            unit="mmHg",
            interpretation=interpretation,
            code_executed=f"MAP = {dbp_initial:.1f} + ({sbp_initial:.1f} - {dbp_initial:.1f}) / 3 = {map_value:.1f}",
        )
    
    def _calculate_spo2_trend(self, vitals: VitalSignSeries) -> CalculationResult:
        """
        Calculate SpO2 trend using linear regression for robustness.
        """        
        if not vitals.spo2 or len(vitals.spo2) < 3:
            return CalculationResult(
                success=False,
                metric_name="SpO2 Trend",
                value=None,
                error_message="Insufficient SpO2 data for trend analysis (need at least 3 points)",
            )
        
        # Extract values and create numeric time indices
        values = np.array([v.value for v in vitals.spo2])
        time_indices = np.arange(len(values))
        
        # Calculate statistics
        first_val = values[0]
        last_val = values[-1]
        min_val = float(np.min(values))
        mean_val = float(np.mean(values))
        
        # Linear regression for trend detection
        slope, intercept, r_value, p_value, std_err = linregress(time_indices, values)
        
        # Calculate percentage change from regression line
        n_samples = len(values)
        predicted_start = intercept
        predicted_end = intercept + slope * (n_samples - 1)
        trend_pct = ((predicted_end - predicted_start) / predicted_start) * 100 if predicted_start > 0 else 0
        
        interpretation = get_spo2_interpretation(min_val, slope, r_value**2)
        
        return CalculationResult(
            success=True,
            metric_name="SpO2 Trend",
            value={
                "first": round(first_val, 1),
                "last": round(last_val, 1),
                "min": round(min_val, 1),
                "mean": round(mean_val, 1),
                "slope": round(slope, 4),
                "r_squared": round(r_value**2, 3),
                "trend_pct": round(trend_pct, 2),
            },
            unit="%",
            interpretation=interpretation,
            code_executed=f"SpO2: {first_val:.0f}% -> {last_val:.0f}%, slope={slope:.4f}/sample, R²={r_value**2:.3f}",
        )
    
    def _calculate_hr_volatility(self, vitals: VitalSignSeries) -> CalculationResult:
        """
        Calculate Heart Rate Volatility (dispersion) from minute-averaged HR samples.
        """
        MIN_SAMPLES = 5
        
        if not vitals.heart_rate or len(vitals.heart_rate) < MIN_SAMPLES:
            return CalculationResult(
                success=False,
                metric_name="HR Volatility",
                value=None,
                error_message=f"Insufficient heart rate data for volatility analysis (need at least {MIN_SAMPLES} points)",
            )
        
        hr_values = np.array([v.value for v in vitals.heart_rate])
        n_samples = len(hr_values)
        
        # Estimate data density from timestamps
        try:
            timestamps = [v.timestamp for v in vitals.heart_rate]
            if hasattr(timestamps[0], 'timestamp'):
                first_ts = timestamps[0].timestamp()
                last_ts = timestamps[-1].timestamp()
                duration_seconds = last_ts - first_ts
            else:
                duration_seconds = (timestamps[-1] - timestamps[0]).total_seconds()
            
            samples_per_minute = n_samples / (duration_seconds / 60) if duration_seconds > 0 else 0
            
            if samples_per_minute < 1:
                data_density = "sparse"
            elif samples_per_minute < 10:
                data_density = "moderate"
            else:
                data_density = "dense"
        except Exception:
            data_density = "unknown"
        
        # Calculate dispersion (std dev of RR intervals derived from HR)
        rr_intervals = 60000 / hr_values  # Convert HR to RR in ms
        dispersion = float(np.std(rr_intervals))  # Analogous to SDNN
        
        # Calculate successive difference metric (analogous to RMSSD)
        successive_diffs = np.diff(rr_intervals)
        rmssd_analog = float(np.sqrt(np.mean(successive_diffs ** 2)))
        
        # Also calculate direct HR statistics
        hr_std = float(np.std(hr_values))
        hr_range = float(np.max(hr_values) - np.min(hr_values))
        
        interpretation = get_hr_volatility_interpretation(daily_cv=dispersion)
        
        return CalculationResult(
            success=True,
            metric_name="HR Volatility",
            value={
                "dispersion_ms": round(dispersion, 2),
                "rmssd_ms": round(rmssd_analog, 2),
                "hr_std_bpm": round(hr_std, 2),
                "hr_range_bpm": round(hr_range, 1),
                "n_samples": n_samples,
                "data_density": data_density,
            },
            unit="ms",
            interpretation=interpretation,
            code_executed=f"HR Volatility: std(HR)={hr_std:.1f}bpm, dispersion={dispersion:.1f}ms",
        )
    
    def _calculate_pulse_pressure(self, vitals: VitalSignSeries) -> CalculationResult:
        """Calculate Pulse Pressure = SBP - DBP."""
        if not vitals.systolic_bp or not vitals.diastolic_bp:
            return CalculationResult(
                success=False,
                metric_name="Pulse Pressure",
                value=None,
                error_message="Missing systolic or diastolic BP data",
            )
        
        sbp_values = [v.value for v in vitals.systolic_bp]
        dbp_values = [v.value for v in vitals.diastolic_bp]

        # Use robust arrival values
        sbp_initial = self._get_robust_arrival_value(sbp_values)
        dbp_initial = self._get_robust_arrival_value(dbp_values)
        
        if sbp_initial <= dbp_initial:
            return CalculationResult(
                success=False,
                metric_name="Pulse Pressure",
                value=None,
                error_message=f"Invalid BP values: SBP ({sbp_initial:.1f}) <= DBP ({dbp_initial:.1f})",
            )
        
        pp = sbp_initial - dbp_initial
        interpretation = get_pulse_pressure_interpretation(pp)
        
        return CalculationResult(
            success=True,
            metric_name="Pulse Pressure",
            value=round(pp, 1),
            unit="mmHg",
            interpretation=interpretation,
            code_executed=f"pulse_pressure = robust_arrival(SBP) {sbp_initial:.1f} - robust_arrival(DBP) {dbp_initial:.1f} = {pp:.1f} mmHg",
        )
    
    def _calculate_qsofa(
        self, 
        vitals: VitalSignSeries, 
        parameters: Optional[dict] = None
    ) -> CalculationResult:
        """
        Calculate qSOFA (Quick Sepsis-related Organ Failure Assessment) over time.
        """
        WINDOW_SECONDS = 3600  # 60 minutes alignment window
        
        if not vitals.systolic_bp or not vitals.respiratory_rate:
            return CalculationResult(
                success=False,
                metric_name="qSOFA",
                value=None,
                error_message="Missing SBP or RR data for qSOFA calculation",
            )
        
        # Build timestamp -> value dictionaries
        def to_timestamp(v):
            if hasattr(v.timestamp, 'timestamp'):
                return v.timestamp.timestamp()
            return float(v.timestamp)
        
        sbp_dict = {to_timestamp(v): v.value for v in vitals.systolic_bp}
        rr_dict = {to_timestamp(v): v.value for v in vitals.respiratory_rate}
        
        # Get aligned value within window
        def get_aligned_value(target_time: float, data_dict: dict) -> Optional[float]:
            best_val = None
            best_diff = WINDOW_SECONDS + 1
            for t, v in data_dict.items():
                diff = abs(t - target_time)
                if diff <= WINDOW_SECONDS and diff < best_diff:
                    best_val = v
                    best_diff = diff
            return best_val
        
        # Scan all timestamps
        all_times = sorted(set(sbp_dict.keys()) | set(rr_dict.keys()))
        
        max_score = 0
        total_aligned = 0
        max_criteria = []
        
        for t in all_times:
            sbp_val = get_aligned_value(t, sbp_dict)
            rr_val = get_aligned_value(t, rr_dict)
            
            if sbp_val is not None and rr_val is not None:
                score = 0
                criteria = []
                
                if sbp_val <= 100:
                    score += 1
                    criteria.append(f"SBP={sbp_val:.0f}")
                if rr_val >= 22:
                    score += 1
                    criteria.append(f"RR={rr_val:.0f}")
                
                if score > max_score:
                    max_score = score
                    max_criteria = criteria
                total_aligned += 1
        
        # Also check GCS from parameters (default 15 if not provided)
        gcs = parameters.get("gcs", 15) if parameters else 15
        if gcs < 15:
            max_score = min(max_score + 1, 3)
            max_criteria.append(f"GCS={gcs}")
        
        interpretation = get_qsofa_interpretation(max_score, max_criteria)
        
        return CalculationResult(
            success=True,
            metric_name="qSOFA",
            value=max_score,
            unit="points",
            interpretation=interpretation,
            code_executed=f"qSOFA (time-aligned, n={total_aligned}) = max({max_score})",
        )
    
    def _calculate_sirs(self, vitals: VitalSignSeries) -> CalculationResult:
        """
        Calculate SIRS (Systemic Inflammatory Response Syndrome) criteria.
        """
        score = 0
        criteria_met = []
        
        # Temperature
        if vitals.temperature:
            temp_c = vitals.temperature[-1].value
            if temp_c > 38 or temp_c < 36:
                score += 1
                criteria_met.append(f"Temp={temp_c:.1f}°C (abnormal)")
        
        # Heart Rate > 90
        if vitals.heart_rate:
            hr = vitals.heart_rate[-1].value
            if hr > 90:
                score += 1
                criteria_met.append(f"HR={hr:.0f} (>90)")
        
        # Respiratory Rate > 20
        if vitals.respiratory_rate:
            rr = vitals.respiratory_rate[-1].value
            if rr > 20:
                score += 1
                criteria_met.append(f"RR={rr:.0f} (>20)")
        
        interpretation = get_sirs_interpretation(score, criteria_met)
        
        return CalculationResult(
            success=True,
            metric_name="SIRS",
            value=score,
            unit="criteria",
            interpretation=interpretation,
            code_executed=f"SIRS = {' + '.join(criteria_met) if criteria_met else '0'}",
        )

    def _synthesize_context(
        self, 
        patient: PatientVisit, 
        pmh: List[str], 
        meds: List[str],
        vitals: Optional[VitalSignSeries] = None
    ) -> TriageOutput:
        """Run LLM to generate personalized context and thresholds."""
        
        vitals_summary = vitals.to_text_summary() if vitals else "No vltals available."

        prompt = TRIAGE_USER_TEMPLATE.format(
            age=patient.demographics.age,
            gender=patient.demographics.gender,
            ethnicity=patient.demographics.ethnicity,
            chief_complaint=patient.chief_complaint or "Not specified",
            vitals_summary=vitals_summary,
            pmh=", ".join(pmh) if pmh else "None",
            meds=", ".join(meds) if meds else "None"
        )
        
        messages = [
            SystemMessage(content=TRIAGE_SYSTEM_PROMPT),
            HumanMessage(content=prompt)
        ]
        
        # Structured output for type safety
        try:
            structured_llm = self.llm.with_structured_output(TriageOutput)
            return structured_llm.invoke(messages)
        except Exception as e:
            self.logger.log_error(f"Triage LLM Context generation failed: {e}")
            # No fallback - let error propagate for proper failure tracking
            raise

    def _generate_artifacts(
        self,
        vitals: VitalSignSeries,
        output_dir: Path,
        visit_id: str,
        thresholds: Optional[Dict[str, List[float]]],
        warning_thresholds: Optional[Dict[str, List[float]]] = None
    ) -> Optional[Path]:
        """Generate the standard vitals panel with personalized thresholds."""
        
        def _to_tuple_dict(d: Any) -> Optional[Dict[str, Tuple[float, float]]]:
            if not d:
                return None
            
            # Convert Pydantic model to dict if needed
            if hasattr(d, 'model_dump'):
                d = d.model_dump(exclude_none=True)
            elif hasattr(d, 'dict'):
                d = d.dict(exclude_none=True)
                
            res = {}
            for k, v in d.items():
                if not v: continue
                # v is a ThresholdRange object or a dict matching its structure
                if hasattr(v, 'low') and hasattr(v, 'high'):
                    res[k] = (v.low, v.high)
                elif isinstance(v, dict) and 'low' in v and 'high' in v:
                    res[k] = (v['low'], v['high'])
            return res if res else None
        
        plot_path, _ = generate_vitals_panel(
            vitals=vitals,
            output_dir=output_dir,
            visit_id=visit_id,
            thresholds=_to_tuple_dict(thresholds),
            warning_thresholds=_to_tuple_dict(warning_thresholds)
        )
        
        return plot_path
