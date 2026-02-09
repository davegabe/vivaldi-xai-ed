"""
Data schema definitions for MC-MED dataset.
Provides type-safe dataclasses for clinical data.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Literal
from enum import IntEnum
import numpy as np


class ESILevel(IntEnum):
    """Emergency Severity Index levels (1=most urgent, 5=least urgent)."""
    RESUSCITATION = 1
    EMERGENT = 2
    URGENT = 3
    LESS_URGENT = 4
    NON_URGENT = 5


class Disposition(IntEnum):
    """ED disposition outcomes."""
    DISCHARGE = 0
    ADMIT = 1


# Plausibility limits for outlier removal (User-defined)
PLAUSIBILITY_LIMITS = {
    "spo2": (70, 100),
    "temp": (32.0, 42.0),
    "hr": (30, 220),
    "rr": (4, 60),
    "sbp": (50, 250),
    "dbp": (30, 150),
}


@dataclass
class Demographics:
    """Patient demographic information."""
    
    age: int
    gender: Literal["M", "F", "Other"]
    ethnicity: str = "Unknown"  # Combined ethnicity field
    insurance_class: str = "Unknown"  # e.g., Medicare, Private, Medicaid

    def to_summary(self) -> str:
        """Return a string summary for prompt inclusion."""
        return f"{self.age}yo {self.gender} ({self.ethnicity})"


@dataclass
class PatientVisit:
    """
    Represents a single ED visit from visits.csv.
    Core unit of analysis for all experiments.
    """
    
    visit_id: str
    patient_id: str
    demographics: Demographics
    
    # Triage information
    chief_complaint: Optional[str] = None
    triage_acuity: Optional[ESILevel] = None  # Target
    triage_time: Optional[datetime] = None
    
    # Outcomes (Ground Truth)
    ed_disposition: Optional[Disposition] = None
    ed_los_hours: Optional[float] = None  # Target
    admit_time: Optional[datetime] = None
    
    # Additional context
    arrival_mode: Optional[str] = None  # Ambulance, Walk-in, etc.
    comorbidity_count: int = 0
    medication_count: int = 0


@dataclass
class VitalSign:
    """Single vital sign measurement."""
    
    timestamp: datetime
    value: float
    unit: str


@dataclass
class VitalSignSeries:
    """
    Time-series vital signs from numerics.csv.
    Used for trend analysis and derived metrics.
    """
    
    visit_id: str
    
    # Core vitals
    heart_rate: list[VitalSign] = field(default_factory=list)
    systolic_bp: list[VitalSign] = field(default_factory=list)
    diastolic_bp: list[VitalSign] = field(default_factory=list)
    spo2: list[VitalSign] = field(default_factory=list)
    respiratory_rate: list[VitalSign] = field(default_factory=list)
    temperature: list[VitalSign] = field(default_factory=list)
    # Target metrics
    pain_score: Optional[int] = None  # (0-10)
    
    def to_text_summary(self) -> str:
        """Return a formatted text summary of all available vital signs with range and average."""
        if not self.has_data():
            return "No vital signs available."
        
        summary_parts = []
        
        # Helper to format statistics
        def get_stats(vals: list[VitalSign]) -> Optional[str]:
            if not vals: 
                return None
            v = [x.value for x in vals]
            mean_val = sum(v)/len(v)
            if any(isinstance(x.value, float) and not x.value.is_integer() for x in vals):
                return f"{len(vals)} values, Range {min(v):.1f}-{max(v):.1f} (Mean: {mean_val:.2f})"
            return f"{len(vals)} values, Range {min(v):.0f}-{max(v):.0f} (Mean: {mean_val:.0f})"

        metrics = [
            ("Heart Rate (bpm)", self.heart_rate),
            ("Systolic BP (mmHg)", self.systolic_bp),
            ("Diastolic BP (mmHg)", self.diastolic_bp),
            ("SpO2 (%)", self.spo2),
            ("Respiratory Rate (brpm)", self.respiratory_rate),
            ("Temperature (°C)", self.temperature),
        ]

        for name, data in metrics:
            stats = get_stats(data)
            if stats:
                summary_parts.append(f"- {name}: {stats}")
        
        return "\n".join(summary_parts) if summary_parts else "No vital signs available."

    def to_text_raw(self, n: int = 30) -> str:
        """Return a comma-separated list of the last n values for each metric."""
        if not self.has_data():
            return "No vital signs available."
            
        raw_parts = []
        metrics = [
            ("Heart Rate (bpm)", self.heart_rate),
            ("Systolic BP (mmHg)", self.systolic_bp),
            ("Diastolic BP (mmHg)", self.diastolic_bp),
            ("SpO2 (%)", self.spo2),
            ("Respiratory Rate (brpm)", self.respiratory_rate),
            ("Temperature (°C)", self.temperature),
        ]
        
        for name, data in metrics:
            if data:
                last_n = data[-n:]
                if name == "Temperature (°C)":
                    vals_str = ", ".join(f"{v.value:.1f}" for v in last_n)
                else:
                    vals_str = ", ".join(f"{v.value:.0f}" for v in last_n)
                raw_parts.append(f"{name}: {vals_str}")
        
        return "\n".join(raw_parts) if raw_parts else "No vital signs available."

    def has_data(self) -> bool:
        """Check if any vital sign data is present."""
        return any([
            len(self.heart_rate) > 0,
            len(self.systolic_bp) > 0,
            len(self.diastolic_bp) > 0,
            len(self.spo2) > 0,
            len(self.respiratory_rate) > 0,
            len(self.temperature) > 0
        ])
    
    def filter_outliers(self) -> None:
        """
        Remove values outside the defined plausibility limits.
        Uses PLAUSIBILITY_LIMITS dictionary defined in this module.
        """
        # Map short keys to class attribute names
        mapping = {
            "hr": "heart_rate",
            "sbp": "systolic_bp",
            "dbp": "diastolic_bp",
            "rr": "respiratory_rate",
            "temp": "temperature",
            "spo2": "spo2"
        }
        
        for limit_key, (min_val, max_val) in PLAUSIBILITY_LIMITS.items():
            attr_name = mapping.get(limit_key)
            if attr_name and hasattr(self, attr_name):
                original_list = getattr(self, attr_name)
                # Filter list keeping only valid values
                filtered_list = [
                    v for v in original_list 
                    if min_val <= v.value <= max_val
                ]
                setattr(self, attr_name, filtered_list)



@dataclass
class MedicalHistory:
    """Past medical history from pmh.csv."""
    
    patient_id: str
    conditions: list[str] = field(default_factory=list)


@dataclass
class Medication:
    """Medication record from meds.csv."""
    
    patient_id: str
    name: str
    med_class: Optional[str] = None
    last_active: Optional[datetime] = None
