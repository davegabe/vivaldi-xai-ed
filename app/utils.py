import streamlit as st
from pathlib import Path

def get_experiment_dir(key: str = "experiment_dir_selector") -> Path:
    """
    Render a sidebar widget to select the experiment output directory.
    Returns the selected Path object.
    """
    results_base = Path("results")
    if not results_base.exists():
        return results_base
    
    # Find subdirectories that look like experiment runs (contain full_results.json)
    subdirs = sorted([d for d in results_base.iterdir() if d.is_dir() and (d / "full_results.json").exists()])
    
    if not subdirs:
        # Fallback for flat structure or empty results
        return results_base
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### :material/folder: Experiment Data")
    
    # Add root "results" if it contains data too, or just list subdirs
    # If using strict subdirs, just list them.
    
    selected_dir = st.sidebar.selectbox(
        "Select Run / Model",
        subdirs,
        format_func=lambda x: x.name,
        key=key,
        help="Select which experiment run or model results to analyze."
    )
    
    return selected_dir
