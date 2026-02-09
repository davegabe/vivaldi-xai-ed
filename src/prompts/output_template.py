"""
Standardized Output Template for fair comparison between Zero-Shot and Agentic approaches.
Ensures both approaches produce outputs in identical formats for expert evaluation.
"""

from dataclasses import dataclass, field, asdict, fields
from typing import Optional, Literal, Any
from datetime import datetime
import hashlib


@dataclass
class DerivedMetrics:
    """Derived clinical metrics - calculated by Agentic, estimated by Zero-Shot."""
    shock_index: float = 0.0
    shock_index_interpretation: str = "N/A"
    
    map_value: float = 0.0  # Mean Arterial Pressure
    map_interpretation: str = "N/A"
    
    qsofa_score: int = 0
    qsofa_interpretation: str = "N/A"
    
    @staticmethod
    def from_dict(data: dict) -> "DerivedMetrics":
        """Create object from dictionary."""
        if not data:
            # Return with placeholders if no data (to satisfy mandatory fields)
            return DerivedMetrics(
                shock_index=0.0, shock_index_interpretation="N/A",
                map_value=0.0, map_interpretation="N/A",
                qsofa_score=0, qsofa_interpretation="N/A"
            )
            
        d = data.copy() # Copy to avoid mutating original
        
        # Filter to only valid fields for DerivedMetrics
        valid_fields = {f.name for f in fields(DerivedMetrics)}
        filtered_d = {k: v for k, v in d.items() if k in valid_fields}
        
        return DerivedMetrics(**filtered_d)

@dataclass
class ClinicalOutput:
    """
    Standardized clinical output for fair comparison.
    
    Both Zero-Shot and Agentic approaches must produce this exact structure.
    """
    
    visit_id: str
    approach: Literal["zero_shot", "agentic"]
    timestamp: datetime = field(default_factory=datetime.now)
    duration_seconds: float = 0.0
    phase_durations: dict[str, float] = field(default_factory=dict)
    
    # Primary predictions (ground truth available)
    esi_level: Optional[int] = None  # 1-5
    pain_score: Optional[int] = None  # 0-10
    ed_los: Optional[float] = None  # hours
    physiological_stress: Optional[Literal["normal", "stressed"]] = None
    
    # Derived metrics
    metrics: DerivedMetrics = field(default_factory=DerivedMetrics)
    
    # Clinical reasoning
    patient_overview: str = ""
    current_therapy: str = ""
    relevant_abnormal_findings: str = ""
    clinical_interpretation: str = ""
    clinical_considerations: list[str] = field(default_factory=list)
    
    # Raw response for debugging
    raw_response: str = ""
    
    # Verification (Agentic only)
    verified: bool = False
    iterations_used: int = 1
    
    # Embedded images for enriched output
    # Each dict: {"path": str, "caption": str, "base64": Optional[str], "narrative": Optional[str]}
    embedded_images: list[dict] = field(default_factory=list)

    @staticmethod
    def from_dict(data: dict, visit_id: Optional[str] = None, approach: Optional[str] = None) -> 'ClinicalOutput':
        """Create object from dictionary with robust schema mapping."""
        if not data:
            return ClinicalOutput(visit_id=visit_id or "unknown", approach=approach or "unknown")
            
        d = data.copy()
        if visit_id:
            d["visit_id"] = visit_id
        if approach:
            d["approach"] = approach
            
        # Ensure timestamp exists
        if "timestamp" not in d:
            if "metadata" in d and isinstance(d["metadata"], dict) and "timestamp" in d["metadata"]:
                d["timestamp"] = d["metadata"]["timestamp"]
            else:
                d["timestamp"] = datetime.now()
        
        # Handle datetime
        if isinstance(d.get("timestamp"), str):
            try:
                d["timestamp"] = datetime.fromisoformat(d["timestamp"])
            except ValueError:
                d["timestamp"] = datetime.now()
        
        # Handle Nested DerivedMetrics
        metrics_data = d.get("metrics", {})
        
        # Fallback: Check for flat fields (ZeroShotAssessment style) if not already in metrics
        if not metrics_data:
             metrics_data = {}
        
        if "shock_index" in d and "shock_index" not in metrics_data:
            metrics_data["shock_index"] = d["shock_index"]
            metrics_data["shock_index_interpretation"] = d.get("shock_index_interpretation", "N/A")
            
        if "map_value" in d and "map_value" not in metrics_data:
            metrics_data["map_value"] = d["map_value"]
            metrics_data["map_interpretation"] = d.get("map_interpretation", "N/A")
            
        if "qsofa_score" in d and "qsofa_score" not in metrics_data:
            metrics_data["qsofa_score"] = d["qsofa_score"]
            metrics_data["qsofa_interpretation"] = d.get("qsofa_interpretation", "N/A")
            
        d["metrics"] = DerivedMetrics.from_dict(metrics_data)
            
        # Filter to only valid fields for ClinicalOutput
        valid_fields = {f.name for f in fields(ClinicalOutput)}
        filtered_d = {k: v for k, v in d.items() if k in valid_fields}
        
        return ClinicalOutput(**filtered_d)
    
    def to_dict(self) -> dict:
        """Convert full object to dictionary."""
        return asdict(self)

    def to_blinded_format(self) -> dict:
        """
        Convert to blinded format for medical expert review.
        Removes approach identifier for unbiased evaluation.
        """        
        # Use visit_id + content hash for stable but unique IDs
        unique_str = f"{self.visit_id}_{self.raw_response}"
        stable_hash = hashlib.sha256(unique_str.encode('utf-8')).hexdigest()[:4]
        
        return {
            "review_id": f"{self.visit_id}_{stable_hash}",
            "esi_level": int(self.esi_level) if self.esi_level is not None else None,
            "pain_score": int(self.pain_score) if self.pain_score is not None else None,
            "ed_los": float(self.ed_los) if self.ed_los is not None else None,
            "stress_status": self.physiological_stress,
            "metrics": {
                "shock_index": float(self.metrics.shock_index) if self.metrics.shock_index is not None else None,
                "map_value": float(self.metrics.map_value) if self.metrics.map_value is not None else None,
                "qsofa_score": int(self.metrics.qsofa_score) if self.metrics.qsofa_score is not None else None,
            },
            # Structured reasoning fields
            "patient_overview": self.patient_overview,
            "current_therapy": self.current_therapy,
            "relevant_abnormal_findings": self.relevant_abnormal_findings,
            "clinical_interpretation": self.clinical_interpretation,
            "clinical_considerations": self.clinical_considerations,
            # Embedded images for rich display
            "images": [
                {
                    "caption": img.get("caption", ""),
                    "base64": img.get("base64"),
                    "narrative": img.get("narrative", ""),
                    "script_path": img.get("script_path"),
                }
                for img in self.embedded_images
            ],
        }
