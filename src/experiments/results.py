"""
Data models and conversion utilities for experiment results.
"""

from dataclasses import dataclass, field
from pathlib import Path
import re
from ..agents.triage import TriageAgent
from typing import Optional
from ..utils.vitals_plots import encode_image_to_base64
from ..data.schema import PatientVisit, VitalSignSeries
from ..prompts import AgentOutput, ClinicalOutput


def find_best_image_match(requested_name: str, available_paths: list[str]) -> Optional[str]:
    """
    Robustly match a requested image filename against available paths, 
    handling prefixes added by CoderAgent and slight naming variations.
    """
    if not available_paths:
        return None
        
    req_path = Path(requested_name)
    req_name = req_path.name.lower()
    req_stem = req_path.stem.lower()
    
    candidates = []
    
    # Prefix pattern: optional_visit_id + timestamp(digits) + uuid(hex) + underscore
    # We look for the part AFTER the standard prefix structure: _\d+_[0-9a-f]{8}_
    # If not found, we treat the whole name as the candidate.
    prefix_pattern = re.compile(r'.*?_\d+_[0-9a-f]{8}_(.*)')

    # Normalize for comparison (remove underscores/hyphens/spaces)
    def normalize(s):
        return re.sub(r'[_\-\s]', '', s).lower()
        
    req_norm = normalize(req_name)
    req_stem_norm = normalize(req_stem)

    for path_str in available_paths:
        p_obj = Path(path_str)
        p_name = p_obj.name.lower()
        
        # 1. Exact match (case-insensitive) of full filename
        if p_name == req_name:
            return path_str
            
        # 2. Extract "original" name by stripping prefix
        match = prefix_pattern.match(p_name)
        if match:
            clean_name = match.group(1)
        else:
            clean_name = p_name
            
        clean_norm = normalize(clean_name)
        clean_stem_norm = normalize(Path(clean_name).stem)
            
        # 3. Check for match with cleaned name
        if clean_name == req_name:
            return path_str
            
        # 4. Fuzzy containment checks (using normalized strings)
        # Check full normalized name (with extension)
        if clean_norm in req_norm:
            candidates.append((len(req_norm) - len(clean_norm), path_str))
        elif req_norm in clean_norm:
            candidates.append((len(clean_norm) - len(req_norm), path_str))
            
        # Check normalized stem (ignore extension)
        if clean_stem_norm in req_norm:
             candidates.append((len(req_norm) - len(clean_stem_norm), path_str))
        elif req_norm in clean_stem_norm:
             candidates.append((len(clean_stem_norm) - len(req_norm), path_str))
            
        # Stem matching (exact)
        if clean_stem_norm == req_stem_norm:
             candidates.append((0, path_str))

    if candidates:
        # Sort by length difference (prefer tightest match)
        candidates.sort(key=lambda x: x[0])
        return candidates[0][1]
        
    return None


@dataclass
class GroundTruth:
    """Structured ground truth data."""
    esi: Optional[int] = None
    los: Optional[float] = None
    pain: Optional[float] = None 
    shock_index: Optional[float] = None
    map_value: Optional[float] = None
    qsofa_score: Optional[int] = None
    
    @staticmethod
    def from_dict(data: Optional[dict]) -> "GroundTruth":
        if not data:
            return GroundTruth()
        return GroundTruth(
            esi=data.get("esi"),
            los=data.get("los"),
            pain=data.get("pain"),
            shock_index=data.get("shock_index"),
            map_value=data.get("map_value"),
            qsofa_score=data.get("qsofa_score"),
        )


@dataclass
class ComparisonResult:
    """Results from a single visit comparison."""
    visit_id: str
    ground_truth: GroundTruth
    demographics: dict = field(default_factory=dict)  # {age, gender, ethnicity} for fairness analysis
    zero_shot_output: ClinicalOutput = field(default_factory=lambda: ClinicalOutput(visit_id="MISSING", approach="zero_shot"))
    agentic_output: ClinicalOutput = field(default_factory=lambda: ClinicalOutput(visit_id="MISSING", approach="agentic"))
    
    esi_error_zs: Optional[int] = None
    esi_error_ag: Optional[int] = None
    shock_index_error_zs: Optional[float] = None
    shock_index_error_ag: Optional[float] = None

    @staticmethod
    def from_dict(data: dict) -> "ComparisonResult":
        """Create object from dictionary."""
        gt_data = data.get("ground_truth")
        if isinstance(gt_data, dict):
             gt = GroundTruth.from_dict(gt_data)
        elif isinstance(gt_data, GroundTruth):
             gt = gt_data
        else:
             gt = GroundTruth()

        # Handle mandatory outputs with fallbacks
        zs_data = data.get("zero_shot") # Original key used in data dict
        if zs_data:
            zs = ClinicalOutput.from_dict(zs_data)
        else:
            zs = ClinicalOutput(visit_id=data["visit_id"], approach="zero_shot")

        ag_data = data.get("agentic") # Original key used in data dict
        if ag_data:
            ag = ClinicalOutput.from_dict(ag_data)
        else:
            ag = ClinicalOutput(visit_id=data["visit_id"], approach="agentic")

        return ComparisonResult(
            visit_id=data["visit_id"],
            ground_truth=gt,
            demographics=data.get("demographics", {}),
            zero_shot_output=zs,
            agentic_output=ag,
        )


@dataclass
class ExperimentResults:
    """Aggregate results from comparison experiment."""
    experiment_name: str
    sample_size: int = 0
    total_duration_seconds: float = 0.0
    results: list[ComparisonResult] = field(default_factory=list)
    
    # Zero-Shot metrics
    zs_esi_accuracy: float = 0.0
    zs_esi_kappa: float = 0.0
    zs_esi_mae: float = 0.0
    zs_esi_rmse: float = 0.0
    zs_esi_precision: float = 0.0
    zs_esi_recall: float = 0.0
    zs_esi_f1: float = 0.0
    
    zs_pain_mae: float = 0.0
    zs_pain_rmse: float = 0.0
    zs_pain_acc_tol: float = 0.0
    
    zs_los_mae: float = 0.0
    zs_los_rmse: float = 0.0
    zs_los_acc_tol: float = 0.0
    
    zs_shock_index_mae: float = 0.0
    zs_shock_index_rmse: float = 0.0
    zs_shock_index_error_rate: float = 0.0
    
    # Agentic metrics
    ag_esi_accuracy: float = 0.0
    ag_esi_kappa: float = 0.0
    ag_esi_mae: float = 0.0
    ag_esi_rmse: float = 0.0
    ag_esi_precision: float = 0.0
    ag_esi_recall: float = 0.0
    ag_esi_f1: float = 0.0
    
    ag_pain_mae: float = 0.0
    ag_pain_rmse: float = 0.0
    ag_pain_acc_tol: float = 0.0
    
    ag_los_mae: float = 0.0
    ag_los_rmse: float = 0.0
    ag_los_acc_tol: float = 0.0
    
    ag_shock_index_mae: float = 0.0
    ag_shock_index_rmse: float = 0.0
    ag_shock_index_error_rate: float = 0.0
    ag_loss_rmse: float = 0.0
    ag_los_acc_tol: float = 0.0
    
    # qSOFA
    zs_qsofa_accuracy: float = 0.0
    zs_qsofa_kappa: float = 0.0
    zs_qsofa_mae: float = 0.0
    zs_qsofa_rmse: float = 0.0
    zs_qsofa_precision: float = 0.0
    zs_qsofa_recall: float = 0.0
    zs_qsofa_f1: float = 0.0

    ag_qsofa_accuracy: float = 0.0
    ag_qsofa_kappa: float = 0.0
    ag_qsofa_mae: float = 0.0
    ag_qsofa_rmse: float = 0.0
    ag_qsofa_precision: float = 0.0
    ag_qsofa_recall: float = 0.0
    ag_qsofa_f1: float = 0.0

    # MAP
    zs_map_mae: float = 0.0
    zs_map_rmse: float = 0.0
    zs_map_acc_tol: float = 0.0

    ag_map_mae: float = 0.0
    ag_map_rmse: float = 0.0
    ag_map_acc_tol: float = 0.0

    ag_shock_index_mae: float = 0.0
    ag_shock_index_rmse: float = 0.0
    ag_shock_index_error_rate: float = 0.0
    ag_verified_rate: float = 0.0
    ag_average_loops: float = 0.0
    
    # Cost & Efficiency
    total_prompt_tokens: int = 0
    total_completion_tokens: int = 0
    total_cost: float = 0.0
    
    # Failed Visits Tracking
    failed_visits: list[str] = field(default_factory=list)  # List of visit_ids that failed
    failed_errors: dict[str, str] = field(default_factory=dict)  # {visit_id: error_message}
    
    def to_summary_table(self) -> str:
        return f"""
## Experiment Results: {self.experiment_name}
**Sample Size:** {self.sample_size}

| Metric | Zero-Shot | Agentic | Improvement |
|--------|-----------|---------|-------------|
| ESI Accuracy | {self.zs_esi_accuracy:.1%} | {self.ag_esi_accuracy:.1%} | {(self.ag_esi_accuracy - self.zs_esi_accuracy):.1%} |
| ESI Kappa | {self.zs_esi_kappa:.3f} | {self.ag_esi_kappa:.3f} | {(self.ag_esi_kappa - self.zs_esi_kappa):.3f} |
| ESI MAE | {self.zs_esi_mae:.2f} | {self.ag_esi_mae:.2f} | {(self.zs_esi_mae - self.ag_esi_mae):.2f} |
| ESI RMSE | {self.zs_esi_rmse:.2f} | {self.ag_esi_rmse:.2f} | {(self.zs_esi_rmse - self.ag_esi_rmse):.2f} |
| ESI Precision (W) | {self.zs_esi_precision:.3f} | {self.ag_esi_precision:.3f} | {(self.ag_esi_precision - self.zs_esi_precision):.3f} |
| ESI Recall (W) | {self.zs_esi_recall:.3f} | {self.ag_esi_recall:.3f} | {(self.ag_esi_recall - self.zs_esi_recall):.3f} |
| ESI F1 (W) | {self.zs_esi_f1:.3f} | {self.ag_esi_f1:.3f} | {(self.ag_esi_f1 - self.zs_esi_f1):.3f} |
| Pain MAE | {self.zs_pain_mae:.2f} | {self.ag_pain_mae:.2f} | {(self.zs_pain_mae - self.ag_pain_mae):.2f} |
| Pain RMSE | {self.zs_pain_rmse:.2f} | {self.ag_pain_rmse:.2f} | {(self.zs_pain_rmse - self.ag_pain_rmse):.2f} |
| Pain Acc (+/-1) | {self.zs_pain_acc_tol:.1%} | {self.ag_pain_acc_tol:.1%} | {(self.ag_pain_acc_tol - self.zs_pain_acc_tol):.1%} |
| Length of Stay MAE (h) | {self.zs_los_mae:.2f} | {self.ag_los_mae:.2f} | {(self.zs_los_mae - self.ag_los_mae):.2f} |
| Length of Stay RMSE (h) | {self.zs_los_rmse:.2f} | {self.ag_los_rmse:.2f} | {(self.zs_los_rmse - self.ag_los_rmse):.2f} |
| Length of Stay Acc (+/-2h) | {self.zs_los_acc_tol:.1%} | {self.ag_los_acc_tol:.1%} | {(self.ag_los_acc_tol - self.zs_los_acc_tol):.1%} |
| qSOFA Accuracy | {self.zs_qsofa_accuracy:.1%} | {self.ag_qsofa_accuracy:.1%} | {(self.ag_qsofa_accuracy - self.zs_qsofa_accuracy):.1%} |
| qSOFA Kappa | {self.zs_qsofa_kappa:.3f} | {self.ag_qsofa_kappa:.3f} | {(self.ag_qsofa_kappa - self.zs_qsofa_kappa):.3f} |
| qSOFA F1 (W) | {self.zs_qsofa_f1:.3f} | {self.ag_qsofa_f1:.3f} | {(self.ag_qsofa_f1 - self.zs_qsofa_f1):.3f} |
| MAP MAE | {self.zs_map_mae:.2f} | {self.ag_map_mae:.2f} | {(self.zs_map_mae - self.ag_map_mae):.2f} |
| MAP RMSE | {self.zs_map_rmse:.2f} | {self.ag_map_rmse:.2f} | {(self.zs_map_rmse - self.ag_map_rmse):.2f} |
| MAP Acc (+/-10) | {self.zs_map_acc_tol:.1%} | {self.ag_map_acc_tol:.1%} | {(self.ag_map_acc_tol - self.zs_map_acc_tol):.1%} |
| Shock Index MAE | {self.zs_shock_index_mae:.3f} | {self.ag_shock_index_mae:.3f} | {(self.zs_shock_index_mae - self.ag_shock_index_mae):.3f} |
| Verified | N/A | {self.ag_verified_rate:.1%} | - |
| **Avg Loops** | N/A | {self.ag_average_loops:.1f} | - |

**Efficiency:**
- Total Prompt Tokens: {self.total_prompt_tokens:,}
- Total Completion Tokens: {self.total_completion_tokens:,}
- **Total Cost:** ${self.total_cost:.4f}
"""


def build_ground_truth(visit: PatientVisit, vitals: Optional[VitalSignSeries]) -> GroundTruth:
    """Build ground truth dictionary from visit data."""
    gt = GroundTruth(
        esi=visit.triage_acuity.value if visit.triage_acuity else None,
        los=visit.ed_los_hours,
    )
    
    if vitals:
        gt.pain = vitals.pain_score
        
        # Use TriageAgent methods for consistent safety metrics
        try:
            # Instantiate agent to access calculation logic
            triage = TriageAgent()
            
            metrics = triage._calculate_safety_metrics(vitals, visit.visit_id)
            
            if "shock_index" in metrics:
                gt.shock_index = metrics["shock_index"]
            
            if "map_value" in metrics:
                gt.map_value = metrics["map_value"]
                
            if "qsofa_score" in metrics:
                gt.qsofa_score = metrics["qsofa_score"]
                
        except Exception as e:
            # If agent calculation fails, log/print and proceed without these metrics
            print(f"Warning: Failed to calculate ground truth metrics for {visit.visit_id}: {e}")
    
    return gt


def convert_agentic_output(ag_result: AgentOutput, visit: PatientVisit) -> ClinicalOutput:
    """Convert raw agentic orchestrator output to structured ClinicalOutput."""
    # Use shared converter (Standardizes conversion across pipelines)
    if not ag_result.assessment:
        # Handle case where assessment is missing (e.g. fatal error)
        return ClinicalOutput(visit_id=visit.visit_id, approach="agentic")

    output = ClinicalOutput.from_dict(
        ag_result.assessment.model_dump(), 
        visit_id=visit.visit_id, 
        approach="agentic"
    )
    
    # Enrich with Agentic-specific metadata
    output.verified = ag_result.verified
    output.iterations_used = ag_result.iterations_used
    output.phase_durations = ag_result.phase_durations
    
    # Build map of image path -> script path from calculations
    path_to_script = {}
    if ag_result.calculations:
        for calc in ag_result.calculations:
            if calc.script_path and calc.image_paths:
                for img_path in calc.image_paths:
                    path_to_script[img_path] = calc.script_path

    # Embed images based on Image Reviews (Ranked)
    if ag_result.image_reviews:
        for review in ag_result.image_reviews:
            filename = review.filename
            description = review.description
            rationale = review.rationale
            relevance = review.relevance_score
            
            if not filename:
                continue

            # Try to find the best matching image path
            match_result = find_best_image_match(filename, ag_result.generated_images)
            
            if match_result:
                b64 = encode_image_to_base64(Path(match_result))
                
                # Retrieve script path if available
                script_path = path_to_script.get(match_result)
                
                output.embedded_images.append({
                    "path": match_result,
                    "caption": filename,
                    "base64": b64,
                    "narrative": description, # Short caption only (rationale integrated in text)
                    "relevance_score": relevance,
                    "script_path": script_path
                })
            else:
                 print(f"Warning: Could not find path for image filename '{filename}'")
                 print(f"Available images: {[Path(p).name for p in ag_result.generated_images]}")
    
    return output

