
import streamlit as st
import pandas as pd
import plotly.express as px
from components.translations import t
from .utils import load_all_model_results

def render_metrics_comparison():
    """Render metrics comparison between approaches using actual data."""
    st.markdown(f"## {t('metrics_header')}")
    
    # Load all model results
    model_results = load_all_model_results()
    
    if not model_results:
        st.info(t('no_results_warning'))
        return
    
    # Build comparison data
    comparison_data = []
    
    for model_name, data in model_results.items():
        if "metrics" not in data:
            continue
            
        metrics = data["metrics"]
        sample_size = data.get("sample_size", "N/A")
        
        # Zero-Shot metrics
        if "zero_shot" in metrics:
            zs = metrics["zero_shot"]
            comparison_data.append({
                "Model": model_name,
                "Approach": "Zero-Shot",
                "Sample Size": sample_size,
                "ESI F1 (W)": zs.get("esi_f1", 0),
                "qSOFA Accuracy (%)": zs.get("qsofa_accuracy", 0) * 100,
                "qSOFA MAE": zs.get("qsofa_mae", 0),
                "qSOFA RMSE": zs.get("qsofa_rmse", 0),
                "Pain MAE": zs.get("pain_mae", 0),
                "Pain RMSE": zs.get("pain_rmse", 0),
                "MAP MAE": zs.get("map_mae", 0),
                "MAP RMSE": zs.get("map_rmse", 0),
                "Shock Index MAE": zs.get("shock_index_mae", 0),
                "Length of Stay MAE (h)": zs.get("los_mae", 0),
                "Length of Stay RMSE (h)": zs.get("los_rmse", 0),
                "Avg Loops": None,
            })
        
        # Agentic metrics
        if "agentic" in metrics:
            ag = metrics["agentic"]
            comparison_data.append({
                "Model": model_name,
                "Approach": "Agentic",
                "Sample Size": sample_size,
                "ESI F1 (W)": ag.get("esi_f1", 0),
                "qSOFA Accuracy (%)": ag.get("qsofa_accuracy", 0) * 100,
                "qSOFA MAE": ag.get("qsofa_mae", 0),
                "qSOFA RMSE": ag.get("qsofa_rmse", 0),
                "Pain MAE": ag.get("pain_mae", 0),
                "Pain RMSE": ag.get("pain_rmse", 0),
                "MAP MAE": ag.get("map_mae", 0),
                "MAP RMSE": ag.get("map_rmse", 0),
                "Shock Index MAE": ag.get("shock_index_mae", 0),
                "Length of Stay MAE (h)": ag.get("los_mae", 0),
                "Length of Stay RMSE (h)": ag.get("los_rmse", 0),
                "Avg Loops": ag.get("average_loops", None),
            })
    
    if not comparison_data:
        st.info("No metrics data available in the loaded results.")
        return
    
    df = pd.DataFrame(comparison_data)
    
    # Display summary table
    st.markdown("### :material/table_chart: Metrics Overview")
    st.dataframe(df, width='stretch', hide_index=True)
    
    st.markdown("---")

    # Function to render a comparison block
    def render_model_comparison_block(block_key, title, help_text):
        st.markdown(f"### :material/group_work: {title}")
        st.markdown(help_text)
        
        col_grps = st.columns(2)
        all_models_metrics = sorted([m for m in model_results.keys() if "metrics" in model_results[m]])
        
        default_a = all_models_metrics[:2] if all_models_metrics else None
        default_b = all_models_metrics[2:] if len(all_models_metrics) > 2 else None
        
        # Unique keys for widgets
        key_a = f"metrics_group_a_{block_key}"
        key_b = f"metrics_group_b_{block_key}"
        key_scope = f"metrics_comp_scope_{block_key}"
        
        with col_grps[0]:
            group_a = st.multiselect("Group A Models", options=all_models_metrics, default=default_a, key=key_a)
        with col_grps[1]:
            group_b = st.multiselect("Group B Models", options=all_models_metrics, default=default_b, key=key_b)
            
        if group_a and group_b:
            # Prepare Comparison Data
            comp_scope_options = ["Combined", "Zero-Shot", "Agentic", "Agentic (A) vs Zero-Shot (B)", "Zero-Shot (A) vs Agentic (B)"]
            comp_approach = st.radio("Comparison Scope", comp_scope_options, horizontal=True, key=key_scope)
            
            comp_rows = []
            
            def add_rows(models, group_label, force_approach=None):
                for m_name in models:
                    if m_name not in model_results: continue
                    m_data = model_results[m_name]
                    if "metrics" not in m_data: continue
                    
                    metrics_data = m_data["metrics"]
                    
                    # Determine approaches to fetch
                    approaches = []
                    if force_approach:
                        if force_approach in metrics_data: approaches.append(force_approach)
                    else:
                        if comp_approach == "Combined":
                            if "zero_shot" in metrics_data: approaches.append("zero_shot")
                            if "agentic" in metrics_data: approaches.append("agentic")
                        elif comp_approach == "Zero-Shot":
                             if "zero_shot" in metrics_data: approaches.append("zero_shot")
                        elif comp_approach == "Agentic":
                             if "agentic" in metrics_data: approaches.append("agentic")
                    
                    for app_key in approaches:
                        app_label = "Agentic" if app_key == "agentic" else "Zero-Shot"
                        vals = metrics_data[app_key]
                        
                        # Extract essential metrics
                        # Updated list based on user preference
                        key_metrics = [
                            ("ESI F1", "esi_f1", 1.0),
                            ("qSOFA MAE", "qsofa_mae", 1.0),
                            ("qSOFA RMSE", "qsofa_rmse", 1.0),
                            ("Pain MAE", "pain_mae", 1.0),
                            ("Pain RMSE", "pain_rmse", 1.0),
                            ("MAP MAE", "map_mae", 1.0),
                            ("MAP RMSE", "map_rmse", 1.0),
                            ("Shock Index MAE", "shock_index_mae", 1.0),
                            ("LOS MAE", "los_mae", 1.0),
                            ("LOS RMSE", "los_rmse", 1.0),
                        ]
                        
                        for m_title, m_key, scale in key_metrics:
                           if m_key in vals and vals[m_key] is not None:
                               comp_rows.append({
                                   "Group": group_label,
                                   "Model": m_name,
                                   "Approach": app_label,
                                   "Metric": m_title,
                                   "Value": vals[m_key] * scale
                               })

            # Logic for mixed scopes
            if comp_approach == "Agentic (A) vs Zero-Shot (B)":
                add_rows(group_a, "Group A", "agentic")
                add_rows(group_b, "Group B", "zero_shot")
            elif comp_approach == "Zero-Shot (A) vs Agentic (B)":
                add_rows(group_a, "Group A", "zero_shot")
                add_rows(group_b, "Group B", "agentic")
            else:
                add_rows(group_a, "Group A")
                add_rows(group_b, "Group B")
                
            if comp_rows:
                df_comp = pd.DataFrame(comp_rows)
                
                # Allow drilling down? Just aggregated bar chart for now
                # Average of metrics per group
                df_agg = df_comp.groupby(["Group", "Metric"])["Value"].mean().reset_index()
                
                fig_comp = px.bar(
                    df_agg,
                    x="Value",
                    y="Metric",
                    color="Group",
                    barmode="group",
                    orientation='h',
                    title=f"Avg Metric Performance: Group A vs Group B ({comp_approach})",
                    text_auto='.2f'
                )
                fig_comp.update_layout(xaxis_title="Score", yaxis_title=None)
                st.plotly_chart(fig_comp, width='stretch', key=f"comp_chart_{block_key}")
                
                st.caption(f"**Group A:** {', '.join(group_a)}")
                st.caption(f"**Group B:** {', '.join(group_b)}")
            else:
                 st.info("No data available for the selected comparison.")

    # --- 1. Standard Comparison ---
    render_model_comparison_block(
        "primary",
        "Custom Model Group Comparison",
        "Select two groups of models to compare their aggregate performance."
    )
    
    st.markdown("---")
    

    
    # Create visualization for key metrics
    st.markdown("### :material/trending_up: Performance Comparison Charts")
    
    def render_section_charts(title, metrics_list):
        if not metrics_list: return
        st.markdown(f"#### {title}")
        cols = st.columns(2)
        for i, (metric_col, metric_name, is_higher_better) in enumerate(metrics_list):
            if metric_col not in df.columns: continue
            
            with cols[i % 2]:
                fig = px.bar(
                    df, x="Model", y=metric_col, color="Approach", barmode="group",
                    title=f"{metric_name} ({'↑' if is_higher_better else '↓'} Better)",
                    color_discrete_map={"Zero-Shot": "#ff6b6b", "Agentic": "#4ecdc4"}
                )
                fig.update_layout(height=280, margin=dict(t=40, b=20), showlegend=(i==0))
                st.plotly_chart(fig, width='stretch')

    # 1. TRIAGE (ESI)
    esi_metrics = [
        ("ESI F1 (W)", "ESI F1 Score", True),
    ]
    render_section_charts(":material/emergency: Triage (ESI)", esi_metrics)
    st.markdown("---")

    # 2. CLINICAL SCORING (Pain, qSOFA)
    score_metrics = [
        ("qSOFA Accuracy (%)", "qSOFA Accuracy", True),
        ("qSOFA MAE", "qSOFA MAE", False),
        ("qSOFA RMSE", "qSOFA RMSE", False),
        ("Pain MAE", "Pain MAE", False),
        ("Pain RMSE", "Pain RMSE", False),
    ]
    render_section_charts(":material/stethoscope: Clinical Scores", score_metrics)
    st.markdown("---")

    # 3. HEMODYNAMICS (MAP, Shock Index)
    hemo_metrics = [
        ("MAP MAE", "MAP MAE", False),
        ("MAP RMSE", "MAP RMSE", False),
        ("Shock Index MAE", "Shock Index MAE", False),
    ]
    render_section_charts(":material/vital_signs: Hemodynamics", hemo_metrics)
    st.markdown("---")

    # 4. OPERATIONS (LOS)
    ops_metrics = [
        ("Length of Stay MAE (h)", "LOS MAE", False),
        ("Length of Stay RMSE (h)", "LOS RMSE", False),
    ]
    render_section_charts(":material/schedule: Operations (LOS)", ops_metrics)
    
    # Efficiency metrics
    st.markdown("---")
    st.markdown("### :material/savings: Efficiency Metrics")
    
    efficiency_data = []
    for model_name, data in model_results.items():
        if "metrics" in data and "efficiency" in data["metrics"]:
            eff = data["metrics"]["efficiency"]
            efficiency_data.append({
                "Model": model_name,
                "Sample Size": data.get("sample_size", "N/A"),
                "Prompt Tokens": eff.get("total_prompt_tokens", 0),
                "Completion Tokens": eff.get("total_completion_tokens", 0),
                "Total Tokens": eff.get("total_prompt_tokens", 0) + eff.get("total_completion_tokens", 0),
                "Total Cost ($)": eff.get("total_cost_usd", 0),
            })
    
    if efficiency_data:
        eff_df = pd.DataFrame(efficiency_data)
        st.dataframe(eff_df, width='stretch', hide_index=True)
        
        # Cost comparison chart
        fig = px.bar(
            eff_df,
            x="Model",
            y="Total Cost ($)",
            title="Total Cost by Model",
            color="Model",
            text="Total Cost ($)"
        )
        fig.update_traces(texttemplate='$%{text:.2f}', textposition='outside')
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, width='stretch')
