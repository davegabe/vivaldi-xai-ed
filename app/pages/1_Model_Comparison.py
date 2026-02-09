"""
Model Comparison Dashboard - Compare multiple models across experiments.
Visualizes Zero-Shot vs Agentic performance across all metrics.
Refactored to use components/analytics.
"""

import streamlit as st
from pathlib import Path
import sys

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from auth import check_password
from components.translations import t, display_language_selector

# Import analytics components
from components.analytics.metrics import render_metrics_comparison
from components.analytics.expert import render_expert_scores
from components.analytics.fairness import render_fairness_analysis
from components.analytics.demographics import render_clinician_demographics

st.set_page_config(
    page_title="Model Comparison | XAI-Agent-Pulse",
    page_icon=":material/bar_chart:",
    layout="wide"
)

# Authentication check
check_password()

# Language Switcher
with st.sidebar:
    st.markdown("### Language / Lingua")
    display_language_selector(key="model_comp_lang_selector")

st.markdown(f"# {t('model_comparison_title')}")
st.markdown(t('model_comparison_subtitle'))


def main():
    """Main dashboard entry point."""
    tabs = st.tabs([t('metrics_tab'), t('fairness_tab'), t('expert_scores_tab'), t('clinician_stats_tab')])
    
    with tabs[0]:
        render_metrics_comparison()
    
    with tabs[1]:
        render_fairness_analysis()
    
    with tabs[2]:
        render_expert_scores()

    with tabs[3]:
        render_clinician_demographics()


if __name__ == "__main__":
    main()
