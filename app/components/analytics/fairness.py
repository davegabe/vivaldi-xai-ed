
import streamlit as st
import pandas as pd
import plotly.express as px
from components.translations import t
from .utils import load_all_model_results, calculate_visit_metric, FAIRNESS_METRIC_GROUPS
import numpy as np

def calculate_consistency_metrics(df, group_col, score_col):
    """Calculate disparity and variance metrics across groups."""
    if df.empty: return None
    
    # Calculate mean score per group
    group_means = df.groupby(group_col, observed=True)[score_col].mean()
    if group_means.empty: return None
    
    max_score = group_means.max()
    min_score = group_means.min()
    disparity = max_score - min_score
    std_dev = group_means.std()
    
    return {
        "Max Disparity": disparity,
        "Std Dev": std_dev,
        "Min Group": group_means.idxmin(),
        "Max Group": group_means.idxmax()
    }

def render_fairness_analysis():
    """Render fairness analysis using logged demographic data."""
    st.markdown(f"## {t('fairness_header')}")
    
    model_results = load_all_model_results()
    
    if not model_results:
        st.info("No experiment results found.")
        return

    # Check for demographic data in results
    models_with_demographics = {}
    
    for model_name, data in model_results.items():
        if "per_visit_results" in data:
            visits_with_demo = [v for v in data["per_visit_results"] if v.get("demographics")]
            if visits_with_demo:
                models_with_demographics[model_name] = visits_with_demo

    if not models_with_demographics:
        st.warning(
            "**No Demographic Data Found**\n\n"
            "Existing results do not contain demographic information. "
            "Please run new experiments with the latest codebase to capture demographic data for fairness analysis."
        )
        return

    # 1. Model Selection
    model_options = list(models_with_demographics.keys())
    selected_model_name = st.selectbox(t("model_select_label"), model_options, index=0)
    
    target_visits = models_with_demographics[selected_model_name]
    
    # 2. Render Groups
    for group_title, metrics_list in FAIRNESS_METRIC_GROUPS.items():
        st.markdown(f"### {group_title}")
        
        for metric_name in metrics_list:
            
            # Prepare Data for this metric
            rows = []
            for v in target_visits:
                demo = v["demographics"]
                gt = v["ground_truth"]
                ag = v.get("agentic")
                
                if not ag: continue
                
                score = calculate_visit_metric(gt, ag, metric_name)
                if score is not None:
                    rows.append({
                        "Age": demo.get("age"),
                        "Gender": demo.get("gender"),
                        "Ethnicity": demo.get("ethnicity"),
                        "Score": score
                    })

            if not rows:
                # st.caption(f"No data for {metric_name}")
                continue
                
            df = pd.DataFrame(rows)
            
            # --- Render 3 Sub-Charts in One Row ---
            st.markdown(f"**{metric_name}**")
            
            c1, c2, c3 = st.columns(3)
            
            # 1. Gender
            with c1:
                gender_group = df.groupby("Gender", observed=False)["Score"].agg(['mean', 'count']).reset_index()
                gender_group["Label"] = gender_group.apply(lambda x: f"{x['mean']:.2f}\n(n={int(x['count'])})", axis=1)
                
                fig_gen = px.bar(
                    gender_group, x="Gender", y="mean",
                    title=f"By Gender",
                    color="Gender", 
                    text="Label",
                    hover_data={"count": True}
                )
                fig_gen.update_layout(height=300, margin=dict(t=30, b=0, l=0, r=0), showlegend=False)
                fig_gen.update_yaxes(title=None)
                st.plotly_chart(fig_gen, width='stretch')
                
            # 2. Ethnicity
            with c2:
                eth_group = df.groupby("Ethnicity", observed=False)["Score"].agg(['mean', 'count']).reset_index()
                eth_group["Label"] = eth_group.apply(lambda x: f"{x['mean']:.2f}\n(n={int(x['count'])})", axis=1)
                
                fig_eth = px.bar(
                    eth_group, x="Ethnicity", y="mean",
                    title=f"By Ethnicity",
                    color="Ethnicity", 
                    text="Label",
                    hover_data={"count": True}
                )
                fig_eth.update_layout(height=300, margin=dict(t=30, b=0, l=0, r=0), showlegend=False)
                fig_eth.update_yaxes(title=None)
                st.plotly_chart(fig_eth, width='stretch')
                
            # 3. Age
            with c3:
                df["Age Group"] = pd.cut(df["Age"], bins=[0, 18, 35, 50, 65, 100], labels=["0-18", "19-35", "36-50", "51-65", "65+"])
                age_group = df.groupby("Age Group", observed=False)["Score"].agg(['mean', 'count']).reset_index()
                age_group["Label"] = age_group.apply(lambda x: f"{x['mean']:.2f}\n(n={int(x['count'])})", axis=1)
                
                fig_age = px.bar(
                    age_group, x="Age Group", y="mean",
                    title=f"By Age Group",
                    color="Age Group", 
                    text="Label",
                    hover_data={"count": True}
                )
                fig_age.update_layout(height=300, margin=dict(t=30, b=0, l=0, r=0), showlegend=False)
                fig_age.update_yaxes(title=None)
                st.plotly_chart(fig_age, width='stretch')

            st.markdown("---")
            
    st.markdown("---")

    # --- MODEL GROUP COMPARISON (Custom) ---
    st.markdown("### :material/group_work: Custom Model Group Comparison (Fairness)")
    st.markdown("Compare fairness metrics between two groups of models.")
    
    col_grps = st.columns(2)
    all_models_fairness = sorted(list(models_with_demographics.keys()))
    
    with col_grps[0]:
        group_a = st.multiselect("Group A Models", options=all_models_fairness, default=all_models_fairness[:2] if all_models_fairness else None, key="fair_group_a")
    with col_grps[1]:
        group_b = st.multiselect("Group B Models", options=all_models_fairness, default=all_models_fairness[2:] if len(all_models_fairness) > 2 else None, key="fair_group_b")
        
    if group_a and group_b:
        comp_scope_options = ["Combined", "Zero-Shot", "Agentic", "Agentic (A) vs Zero-Shot (B)", "Zero-Shot (A) vs Agentic (B)"]
        comp_approach = st.radio("Comparison Scope", comp_scope_options, horizontal=True, key="fair_comp_scope")
            
        # Select Metric to Compare
        # Flatten FAIRNESS_METRIC_GROUPS for selection
        all_metrics = []
        for v in FAIRNESS_METRIC_GROUPS.values():
            all_metrics.extend(v)
        
        target_metric = st.selectbox("Select Metric for Fairness Comparison", options=all_metrics, index=0)
        
        # Build Data
        comp_rows = []
        
        def process_group(models, group_label, force_approach=None):
            for m_name in models:
                visits = models_with_demographics.get(m_name, [])
                for v in visits:
                     demo = v.get("demographics")
                     if not demo: continue
                     
                     gt = v.get("ground_truth")
                     
                     # Determine approaches
                     approaches = []
                     if force_approach:
                         approaches.append(force_approach)
                     else:
                         if comp_approach == "Combined":
                             approaches = ["zero_shot", "agentic"]
                         elif comp_approach == "Zero-Shot":
                             approaches = ["zero_shot"]
                         elif comp_approach == "Agentic":
                             approaches = ["agentic"]
                     
                     for app_key in approaches:
                         output = v.get(app_key)
                         if not output: continue
                         
                         score = calculate_visit_metric(gt, output, target_metric)
                         if score is not None:
                             comp_rows.append({
                                 "Group": group_label,
                                 "Age": demo.get("age"),
                                 "Gender": demo.get("gender"),
                                 "Ethnicity": demo.get("ethnicity"),
                                 "Score": score
                             })

        if comp_approach == "Agentic (A) vs Zero-Shot (B)":
            process_group(group_a, "Group A", "agentic")
            process_group(group_b, "Group B", "zero_shot")
        elif comp_approach == "Zero-Shot (A) vs Agentic (B)":
            process_group(group_a, "Group A", "zero_shot")
            process_group(group_b, "Group B", "agentic")
        else:
            process_group(group_a, "Group A")
            process_group(group_b, "Group B")

        if comp_rows:
            df_comp = pd.DataFrame(comp_rows)
            
            # Render Charts per Demographic
            st.markdown(f"#### Fairness Analysis: {target_metric}")
            
            c1, c2, c3 = st.columns(3)
            
            # Helper for grouped bar comparison
            def render_fairness_chart(df_sub, group_col, chart_title):
                # Aggregate Mean Score AND Count
                agg = df_sub.groupby([group_col, "Group"], observed=False).agg(
                    Score=("Score", "mean"),
                    Count=("Score", "count")
                ).reset_index()
                
                # Format text to show Score and N
                agg["Label"] = agg.apply(lambda x: f"{x['Score']:.2f} (n={x['Count']})", axis=1)
                
                fig = px.bar(
                    agg, x=group_col, y="Score", color="Group", barmode="group",
                    title=chart_title, 
                    text="Label",
                    # Add Count to hover data
                    hover_data={"Count": True, "Score": ':.3f'}
                )
                fig.update_layout(height=300, margin=dict(t=30, b=0, l=0, r=0), showlegend=True)
                # Ensure text fits
                fig.update_traces(textposition='auto')
                return fig

            with c1:
                st.plotly_chart(render_fairness_chart(df_comp, "Gender", "By Gender"), width='stretch')
            with c2:
                st.plotly_chart(render_fairness_chart(df_comp, "Ethnicity", "By Ethnicity"), width='stretch')
            with c3:
                df_comp["Age Group"] = pd.cut(df_comp["Age"], bins=[0, 18, 35, 50, 65, 100], labels=["0-18", "19-35", "36-50", "51-65", "65+"])
                st.plotly_chart(render_fairness_chart(df_comp, "Age Group", "By Age Group"), width='stretch')

            st.caption(f"**Group A:** {', '.join(group_a)}")
            st.caption(f"**Group B:** {', '.join(group_b)}")
            st.caption(f"**Group A:** {', '.join(group_a)}")
            st.caption(f"**Group B:** {', '.join(group_b)}")
            
            st.markdown("---")
            
            # --- CONSISTENCY METRICS (RQ2) ---
            st.markdown("### :material/equal: Consistency Analysis (RQ2)")
            st.markdown(
                "Quantifying fairness through consistency. "
                "**Max Disparity** = Difference between highest and lowest performing demographic subgroups. "
                "**Lower is Better**."
            )
            
            # Use same calculated df_comp
            consistency_rows = []
            
            # Iterate over groups involved in comparison
            groups_in_view = df_comp["Group"].unique()
            demographic_factors = ["Gender", "Ethnicity", "Age Group"]
            
            for grp in groups_in_view:
                df_g = df_comp[df_comp["Group"] == grp]
                
                for demo_factor in demographic_factors:
                    c_metrics = calculate_consistency_metrics(df_g, demo_factor, "Score")
                    if c_metrics:
                        consistency_rows.append({
                            "Group": grp,
                            "Factor": demo_factor,
                            "Max Disparity": c_metrics["Max Disparity"],
                            "Std Dev": c_metrics["Std Dev"]
                        })
            
            if consistency_rows:
                df_cons = pd.DataFrame(consistency_rows)
                
                c1, c2 = st.columns(2)
                
                with c1:
                    fig_disp = px.bar(
                        df_cons, x="Factor", y="Max Disparity", color="Group", barmode="group",
                        title=f"Max Disparity (Lower is Better) - {target_metric}",
                        text_auto='.3f'
                    )
                    st.plotly_chart(fig_disp, width='stretch')
                    
                with c2:
                    fig_std = px.bar(
                        df_cons, x="Factor", y="Std Dev", color="Group", barmode="group",
                        title=f"Standard Deviation across Subgroups (Lower is Better)",
                        text_auto='.3f'
                    )
                    st.plotly_chart(fig_std, width='stretch')
            else:
                st.info("Insufficient data to calculate consistency metrics.")

        else:
            st.info("No data available for the selected comparison.")
