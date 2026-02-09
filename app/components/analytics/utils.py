
import json
import streamlit as st
from pathlib import Path

def load_all_model_results(results_base_dir: Path = None) -> dict:
    """
    Load all model results from results directories.
    Note: Always reads numeric metrics from the main results directory 
    as they are language-independent.
    """
    if results_base_dir is None:
        # Assuming this is called from app/ directory structure, but we used __file__ relative path before.
        # Original: Path(__file__).parent.parent.parent / "results" (from pages/1_Model_Comparison.py)
        # Now: Path(__file__).parent.parent.parent.parent / "results" (from components/analytics/utils.py)
        results_base_dir = Path(__file__).parent.parent.parent.parent / "results"
    
    model_results = {}
    
    # Scan for directories containing full_results.json
    if results_base_dir.exists():
        for item in results_base_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                # Skip translated_results folder itself if scanning root results
                if item.name == "translated_results":
                    continue
                    
                results_file = item / "full_results.json"
                if results_file.exists():
                    try:
                        with open(results_file) as f:
                            data = json.load(f)
                        model_results[item.name] = data
                    except (json.JSONDecodeError, IOError) as e:
                        st.warning(f"Could not load results for {item.name}: {e}")
    
    return model_results


def calculate_visit_metric(gt: dict, ag: dict, metric_name: str):
    """
    Calculate a specific metric for a single visit.
    Returns the score (float/int) or None if data is missing.
    """
    try:
        # --- ESI TRIAGE ---
        if metric_name in ["ESI Accuracy", "ESI F1"]:
            if gt.get("esi") and ag.get("esi_level"):
                return 1 if str(gt["esi"]) == str(ag["esi_level"]) else 0
        elif metric_name == "ESI MAE":
            if gt.get("esi") and ag.get("esi_level"):
                return abs(float(gt["esi"]) - float(ag["esi_level"]))

        # --- PAIN ASSESSMENT ---
        elif metric_name == "Pain MAE":
            if gt.get("pain") is not None and ag.get("pain_score") is not None:
                return abs(float(gt["pain"]) - float(ag["pain_score"]))

        # --- HEMODYNAMICS ---
        elif metric_name == "MAP MAE":
            if gt.get("map") is not None and ag.get("map_value") is not None:
                return abs(float(gt["map"]) - float(ag["map_value"]))
        elif metric_name == "Shock Index MAE":
            if gt.get("shock_index") is not None and ag.get("shock_index") is not None:
                return abs(float(gt["shock_index"]) - float(ag["shock_index"]))

        # --- SEPSIS SCORE ---
        elif metric_name == "qSOFA Accuracy":
            if gt.get("qsofa") is not None and ag.get("qsofa_score") is not None:
                return 1 if int(gt["qsofa"]) == int(ag["qsofa_score"]) else 0
        elif metric_name == "qSOFA MAE":
            if gt.get("qsofa") is not None and ag.get("qsofa_score") is not None:
                return abs(float(gt["qsofa"]) - float(ag["qsofa_score"]))

        # --- OPERATIONS ---
        elif metric_name == "Length of Stay MAE":
            if gt.get("los") is not None and ag.get("ed_los") is not None:
                return abs(float(gt["los"]) - float(ag["ed_los"]))
                
    except (ValueError, TypeError):
        return None
    
    return None

FAIRNESS_METRIC_GROUPS = {
    ":material/emergency: Triage (ESI)": ["ESI F1"],
    ":material/stethoscope: Clinical Scores": ["qSOFA Accuracy", "qSOFA MAE", "Pain MAE"],
    ":material/vital_signs: Hemodynamics": ["MAP MAE", "Shock Index MAE"],
    ":material/schedule: Operations (LOS)": ["Length of Stay MAE"]
}
