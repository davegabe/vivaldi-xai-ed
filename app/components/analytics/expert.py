
import streamlit as st
import pandas as pd
import plotly.express as px
from collections import defaultdict
from components.translations import t
from components.session import init_connection

def render_expert_scores():
    """Render expert scores comparison with advanced statistics."""
    st.markdown(f"## {t('expert_scores_header')}")
    
    # Environment Selection (Dev Mode Only)
    current_env = st.secrets.get("env", {}).get("type", "dev")
    target_env = current_env
    
    if current_env == "dev":
        col_sel, _ = st.columns([1, 3])
        with col_sel:
            target_env = st.radio(
                "Data Source (Dev Mode)",
                options=["dev", "prod"],
                format_func=lambda x: "Development" if x == "dev" else "Production",
                horizontal=True
            )
            
    # Get reviews from selected environment
    reviews = []
    try:
        # We need to manually get the collection since get_collection uses current env
        client = init_connection()
        if client:
            db_name = "agent_pulse"
            coll_name = f"reviews_{target_env}"
            coll = client[db_name][coll_name]
            
            reviews = list(coll.find({}, {"_id": 0})) # Exclude _id
        else:
             st.error("Could not connect to MongoDB.")
             return
    except Exception as e:
        st.error(f"Error fetching reviews from MongoDB ({target_env}): {e}")
        return
    
    if not reviews:
        st.info(f"No reviews collected yet in **{target_env}** environment.")
        return
    
    # --- GLOBAL FILTERING ---
    # Identify reviewers with at least one complete review to enable filtering
    reviewer_valid_counts_global = defaultdict(int)
    required_fields = ['trust', 'factuality', 'relevance', 'justification', 'chart_comprehensibility', 'utility']
    
    for r in reviews:
        rid = r.get('reviewer_id', 'Unknown')
        is_complete = all(r.get(field) is not None for field in required_fields)
        if is_complete:
            reviewer_valid_counts_global[rid] += 1
            
    # Filter Controls
    col_filter, _ = st.columns([1, 1])
    with col_filter:
        min_reviews = st.number_input(
            "Minimum valid reviews per clinician", 
            min_value=0, 
            value=1, 
            step=1,
            help="Exclude clinicians who have submitted fewer than K valid (complete) reviews.",
            key="expert_min_reviews"
        )
        
        # Manual Exclusion Filter
        if "excluded_clinicians" not in st.session_state:
            st.session_state.excluded_clinicians = []
            
        # Get all reviewer IDs for the multiselect
        all_reviewers = sorted(list(reviewer_valid_counts_global.keys()))
        
        excluded_sel = st.multiselect(
            "Manually Excluded Clinicians",
            options=all_reviewers,
            default=st.session_state.excluded_clinicians,
            help="Select clinicians to exclude from the analysis. You can also click on the 'Votes by Clinician' chart below to exclude them.",
            key="manual_exclusion_multiselect"
        )
        
        # Sync state if changed via widget
        if excluded_sel != st.session_state.excluded_clinicians:
            st.session_state.excluded_clinicians = excluded_sel
            st.rerun()

    
    original_count = len(reviews)
    
    # Apply Filters (Min Reviews & Manual Exclusion)
    filtered_reviews = []
    for r in reviews:
        rid = r.get('reviewer_id', 'Unknown')
        
        # Check Min Reviews
        if reviewer_valid_counts_global[rid] < min_reviews:
            continue
            
        # Check Manual Exclusion
        if rid in st.session_state.excluded_clinicians:
            continue
            
        filtered_reviews.append(r)
        
    reviews = filtered_reviews
    
    if len(reviews) < original_count:
        st.caption(f"Showing {len(reviews)} reviews (filtered from {original_count})")
        
    if not reviews:
        st.info(f"No reviews match the filter criteria.")
        return

    # --- 0. EXPERT PARTICIPATION & DATA QUALITY ---
    st.markdown("### :material/group: Participation & Data Quality")
    
    # 1. Clinician Stats (Re-calculate on potentially filtered data)
    reviewer_counts = defaultdict(int)
    reviewer_valid_counts_local = defaultdict(int) 
    completed_count = 0
    total_reviews = len(reviews)
    
    for r in reviews:
        # Participation
        rid = r.get('reviewer_id', 'Unknown')
        reviewer_counts[rid] += 1
        
        # Completion
        is_complete = True
        for field in required_fields:
            if r.get(field) is None:
                is_complete = False
                break
        if is_complete:
            completed_count += 1
            reviewer_valid_counts_local[rid] += 1
            
    # Metrics
    num_clinicians = len(reviewer_counts)
    
    # Avg votes calculation
    avg_votes = (total_reviews / num_clinicians) if num_clinicians > 0 else 0
    completion_rate = (completed_count / total_reviews) if total_reviews > 0 else 0
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Active Clinicians", num_clinicians, help="Number of distinct reviewers present in current selection")
    with m2:
        st.metric("Avg Votes / Clinician", f"{avg_votes:.1f}", help="Average number of cases reviewed per clinician")
    with m3:
        st.metric("Global Completion Rate", f"{completion_rate:.1%}", help="Percentage of reviews with all fields filled")
        
    # Chart: Votes per Clinician
    st.markdown("#### Votes by Clinician")
    st.caption("Click on a bar to exclude that clinician.")
    
    # Use the local Valid Counts which correspond to the current subset
    voter_df = pd.DataFrame([{"Clinician ID": k, "Votes": v, "Valid Votes": reviewer_valid_counts_local[k]} for k, v in reviewer_counts.items()])
    
    if not voter_df.empty:
        voter_df = voter_df.sort_values("Votes", ascending=False)
        
        fig_voters = px.bar(
            voter_df, 
            x="Clinician ID", 
            y=["Votes", "Valid Votes"],
            barmode='overlay',
            text_auto=True,
            title="Total vs Valid Reviews per Clinician"
        )
        fig_voters.update_layout(xaxis_tickangle=-45)
        
        # Handle Selection
        event = st.plotly_chart(
            fig_voters, 
            width='stretch', 
            on_select="rerun", 
            selection_mode="points",
            key="voters_chart_selection"
        )
        
        if event and event["selection"]["points"]:
            for p in event["selection"]["points"]:
                selected_id = p["x"]
                if selected_id not in st.session_state.excluded_clinicians:
                    st.session_state.excluded_clinicians.append(selected_id)
                    st.rerun()
    else:
        st.info("No clinicians to display.")
    
    st.markdown("---")

    # --- 1. DETAILED TABLE (Raw Data) ---
    st.markdown("### :material/table_rows: Detailed Case Results")
    st.markdown("View individual scores for every case.")
    
    raw_data = []
    for r in reviews:
        raw_data.append({
            "Visit ID": r.get('visit_id', 'N/A'),
            "Model": r.get('model', 'Unknown'),
            "Approach": r.get('approach', 'Unknown'),
            "Trust": r.get('trust'),
            "Factuality": r.get('factuality'),
            "Relevance": r.get('relevance'),
            "Justification": r.get('justification'),
            "Chart Comp.": r.get('chart_comprehensibility'),
            "Utility": r.get('utility'),
            "Comments": r.get('comments')
        })
    
    df_raw = pd.DataFrame(raw_data)
    st.dataframe(df_raw, width="stretch", hide_index=True)
    st.markdown("---")

    st.markdown("---")

    # Prepare data for categorical plots
    cat_metrics = ['trust', 'factuality', 'relevance', 'justification']
    cat_data = []
    
    # Define order for categorical values
    cat_order = {"yes": 3, "partial": 2, "no": 1}
    
    for r in reviews:
        for metric in cat_metrics:
            val = r.get(metric)
            if val:
                cat_data.append({
                    "Model": r.get('model', 'Unknown'),
                    "Approach": r.get('approach', 'Unknown'),
                    "Metric": metric.capitalize(),
                    "Response": val,
                    "Order": cat_order.get(val, 0) # For sorting
                })
                
    if cat_data:
        df_cat = pd.DataFrame(cat_data)
        
        # Color map for responses
        color_map = {
            "yes": "#28a745",      # Green
            "partial": "#ffc107",  # Yellow/Gold
            "no": "#dc3545"        # Red
        }

        # --- 2. OVERALL APPROACH COMPARISON ---
        st.markdown("### :material/compare_arrows: Overall Approach Comparison")
        st.markdown("Aggregated performance of **Agentic vs Zero-Shot** across all models.")

        # Filter Models
        all_models = sorted(df_cat['Model'].unique())
        selected_models = st.multiselect(
            "Select Models to Include",
            options=all_models,
            default=all_models,
            key="model_filter_overall"
        )
        
        if selected_models:
            df_cat = df_cat[df_cat['Model'].isin(selected_models)]
        
        # Calculate percentages for Approach
        df_app_grouped = df_cat.groupby(['Approach', 'Metric', 'Response', 'Order'], observed=False).size().reset_index(name='Count')
        totals_app = df_app_grouped.groupby(['Approach', 'Metric'], observed=False)['Count'].transform('sum')
        df_app_grouped['Percentage'] = (df_app_grouped['Count'] / totals_app) * 100
        df_app_grouped = df_app_grouped.sort_values('Order', ascending=False)
        
        fig_approach = px.bar(
            df_app_grouped,
            x="Approach",
            y="Percentage",
            color="Response",
            facet_col="Metric",
            barmode="stack",
            text_auto='.1f',
            color_discrete_map=color_map,
            category_orders={"Response": ["yes", "partial", "no"]},
            title="Agentic vs Zero-Shot Distribution per Metric"
        )
        fig_approach.update_layout(yaxis_title="Percentage (%)")
        st.plotly_chart(fig_approach, width='stretch')
        
        st.markdown("---")

        # --- 3. DETAILED MODEL COMPARISON ---
        st.markdown("### :material/insert_chart: Detailed Model Comparison")
        st.markdown("Compare models on individual metrics.")
        
        # Toggle for filtering
        view_mode = st.radio(
            "Filter Approach",
            options=["Combined", "Zero-Shot", "Agentic"],
            horizontal=True,
            help="Switch between viewing all results, or focusing on a specific approach."
        )
        
        df_model_view = df_cat.copy()
        if view_mode != "Combined":
            df_model_view = df_model_view[df_model_view["Approach"] == view_mode]
            
        if not df_model_view.empty:
            # Calculate percentages for Model
            # If combined, we group by Model (mixed approaches) or facet by approach?
            # User wants "Compare other model better than another... splitting between agentic"
            # If Combined, let's Facet Row by Approach to separate them clearly.
            
            group_cols = ['Model', 'Metric', 'Response', 'Order']
            if view_mode == "Combined":
                group_cols.append('Approach')
                
            df_mod_grouped = df_model_view.groupby(group_cols, observed=False).size().reset_index(name='Count')
            
            # Totals for %
            # Denominator: Total count for that Model+Metric (+Approach if combined)
            norm_cols = ['Model', 'Metric']
            if view_mode == "Combined":
                norm_cols.append('Approach')
                
            totals_mod = df_mod_grouped.groupby(norm_cols, observed=False)['Count'].transform('sum')
            df_mod_grouped['Percentage'] = (df_mod_grouped['Count'] / totals_mod) * 100
            df_mod_grouped = df_mod_grouped.sort_values('Order', ascending=False)
            
            facet_row = "Approach" if view_mode == "Combined" else None
            height = 600 if view_mode == "Combined" else 400
            
            fig_models = px.bar(
                df_mod_grouped,
                x="Model",
                y="Percentage",
                color="Response",
                facet_col="Metric",
                facet_row=facet_row,
                barmode="stack",
                text_auto='.1f',
                color_discrete_map=color_map,
                category_orders={"Response": ["yes", "partial", "no"]},
                title=f"Model Performance ({view_mode})"
            )
            fig_models.update_layout(yaxis_title="Percentage (%)", height=height)
            st.plotly_chart(fig_models, width='stretch')
        else:
            st.info(f"No data available for {view_mode} approach.")


        st.markdown("---")

        # --- RQ3: VISUALIZATION QUALITY ANALYSIS ---
        st.markdown("### :material/image: Visualization Quality Analysis (RQ3)")
        st.markdown(
            "Focused comparison of **Chart Comprehensibility** and **Utility** scores to answer RQ3: "
            "*Which model provides the most comprehensible and clinically useful visualizations?*"
        )
        
        # Filter for relevant metrics
        viz_metrics = ['chart_comprehensibility', 'utility']
        viz_data = []
        
        for r in reviews:
            # Re-check completeness for viz metrics specifically (looser check allowed if needed, but sticking to valid)
            if not all(r.get(f) is not None for f in required_fields): continue
                
            for m_key in viz_metrics:
                val = r.get(m_key)
                if val:
                    viz_data.append({
                        "Model": r.get('model', 'Unknown'),
                        "Approach": r.get('approach', 'Unknown'),
                        "Metric": "Chart Comp." if m_key == 'chart_comprehensibility' else "Utility",
                        "Score": int(val)
                    })
                    
        if viz_data:
            df_viz = pd.DataFrame(viz_data)
            
            # 1. Comparative Bar Chart (Score Distribution per Approach)
            st.markdown("#### Score Distribution by Approach")
            
            # Group by Approach & Metric
            viz_agg = df_viz.groupby(['Approach', 'Metric'])['Score'].mean().reset_index()
            
            c1, c2 = st.columns(2)
            
            with c1:
                # Average Score Comparison
                fig_viz_bar = px.bar(
                    viz_agg, x="Metric", y="Score", color="Approach", barmode="group",
                    title="Average Score: Agentic vs Zero-Shot",
                    text_auto='.2f',
                    range_y=[0, 5.5]
                )
                st.plotly_chart(fig_viz_bar, width='stretch')
                
            with c2:
                # Win Rate / Preference (Simulated if paired, otherwise distribution)
                # Since reviews might not be strictly paired 1:1 in this view, we show Box Plot spread
                fig_viz_box = px.box(
                    df_viz, x="Metric", y="Score", color="Approach",
                    title="Score Spread: Agentic vs Zero-Shot",
                    points="all"
                )
                st.plotly_chart(fig_viz_box, width='stretch')
            
            # 2. Detailed Breakdown Table
            st.markdown("#### Detailed Stats by Model")
            viz_stats = df_viz.groupby(['Model', 'Approach', 'Metric'])['Score'].agg(['mean', 'std', 'count']).reset_index()
            viz_stats.columns = ['Model', 'Approach', 'Metric', 'Avg Score', 'Std Dev', 'Count']
            viz_stats = viz_stats.sort_values(by=['Metric', 'Avg Score'], ascending=[True, False])
            
            st.dataframe(viz_stats, width='stretch', hide_index=True)
            
        else:
            st.info("No visualization rating data available.")

        st.markdown("---")

        # --- 4. MODEL GROUP COMPARISON (Custom) ---
        st.markdown("### :material/group_work: Custom Model Group Comparison")
        st.markdown("Select two groups of models to compare their aggregate performance.")
        
        c_grp1, c_grp2 = st.columns(2)
        all_models_list = sorted(df_cat['Model'].unique())
        
        with c_grp1:
            group_a = st.multiselect("Group A Models", options=all_models_list, default=all_models_list[:2] if all_models_list else None, key="group_a_select")
        with c_grp2:
            group_b = st.multiselect("Group B Models", options=all_models_list, default=all_models_list[2:] if len(all_models_list) > 2 else None, key="group_b_select")
            
        if group_a and group_b:
            # Create subset for comparison
            df_a = df_cat[df_cat['Model'].isin(group_a)].copy()
            df_a['Group'] = "Group A"
            
            df_b = df_cat[df_cat['Model'].isin(group_b)].copy()
            df_b['Group'] = "Group B"
            
            df_comp = pd.concat([df_a, df_b])
            
            comp_scope_options = ["Combined", "Zero-Shot", "Agentic", "Agentic (A) vs Zero-Shot (B)", "Zero-Shot (A) vs Agentic (B)"]
            comp_approach = st.radio("Comparison Scope", comp_scope_options, horizontal=True, key="comp_scope_radio")
            
            if comp_approach == "Agentic (A) vs Zero-Shot (B)":
                 # Keep Agentic for Group A and Zero-Shot for Group B
                 df_comp = df_comp[
                     ((df_comp['Group'] == 'Group A') & (df_comp['Approach'] == 'Agentic')) |
                     ((df_comp['Group'] == 'Group B') & (df_comp['Approach'] == 'Zero-Shot'))
                 ]
            elif comp_approach == "Zero-Shot (A) vs Agentic (B)":
                 # Keep Zero-Shot for Group A and Agentic for Group B
                 df_comp = df_comp[
                     ((df_comp['Group'] == 'Group A') & (df_comp['Approach'] == 'Zero-Shot')) |
                     ((df_comp['Group'] == 'Group B') & (df_comp['Approach'] == 'Agentic'))
                 ]
            elif comp_approach != "Combined":
                df_comp = df_comp[df_comp['Approach'] == comp_approach]
            
            if not df_comp.empty:
                # Aggregate
                df_comp_grouped = df_comp.groupby(['Group', 'Metric', 'Response', 'Order'], observed=False).size().reset_index(name='Count')
                totals_comp = df_comp_grouped.groupby(['Group', 'Metric'], observed=False)['Count'].transform('sum')
                df_comp_grouped['Percentage'] = (df_comp_grouped['Count'] / totals_comp) * 100
                df_comp_grouped = df_comp_grouped.sort_values('Order', ascending=False)
                
                fig_comp = px.bar(
                    df_comp_grouped,
                    x="Group",
                    y="Percentage",
                    color="Response",
                    facet_col="Metric",
                    barmode="stack",
                    text_auto='.1f',
                    color_discrete_map=color_map,
                    category_orders={"Response": ["yes", "partial", "no"]},
                    title=f"Group A vs Group B Performance ({comp_approach})"
                )
                fig_comp.update_layout(yaxis_title="Percentage (%)")
                st.plotly_chart(fig_comp, width='stretch')
                
                # Show composition
                st.caption(f"**Group A:** {', '.join(group_a)}")
                st.caption(f"**Group B:** {', '.join(group_b)}")
            else:
                st.info("No data for selected scope.")
                
        st.markdown("---")

    # --- 3. NUMERIC METRICS (Distributions) ---
    st.markdown("### :material/analytics: Numeric Metrics Distribution")
    st.markdown("Distribution of scores (1-5) for Utility and Comprehensibility.")
    
    num_data = []
    num_metrics = ['chart_comprehensibility', 'utility']
    required_fields_strict = ['trust', 'factuality', 'relevance', 'justification', 'chart_comprehensibility', 'utility']
    
    for r in reviews:
        # Check completeness before processing numeric metrics
        is_complete = True
        for field in required_fields_strict:
            if r.get(field) is None:
                is_complete = False
                break
        
        if not is_complete:
            continue

        for metric in num_metrics:
            val = r.get(metric)
            if val is not None:
                 # Check if it's numeric
                 try:
                     val = int(val)
                     num_data.append({
                        "Model": r.get('model', 'Unknown'),
                        "Approach": r.get('approach', 'Unknown'),
                        "Metric": "Chart Comp." if metric == 'chart_comprehensibility' else "Utility",
                        "Score": val
                    })
                 except:
                     continue

    if num_data:
        df_num = pd.DataFrame(num_data)
        
        # 0. Approach Comparison Box Plot
        fig_box_app = px.box(
            df_num,
            x="Approach",
            y="Score",
            color="Approach",
            facet_col="Metric",
            points="all",
            title="Score Distribution by Approach (1-5 Scale)",
            range_y=[0.5, 5.5]
        )
        st.plotly_chart(fig_box_app, width='stretch')

        # Box Plot for comparison
        fig_box = px.box(
            df_num,
            x="Model",
            y="Score",
            color="Model",
            facet_col="Metric",
            points="all",
            title="Score Distribution (1-5 Scale)",
            range_y=[0.5, 5.5]
        )
        st.plotly_chart(fig_box, width='stretch')
        
        # Breakdown of counts (Histogram style) - Split by metric
        df_num_counts = df_num.groupby(['Model', 'Metric', 'Score'], observed=False).size().reset_index(name='Count')
        
        # 1. Utility Count Chart
        df_util = df_num_counts[df_num_counts['Metric'] == 'Utility']
        if not df_util.empty:
            fig_hist_util = px.bar(
                df_util,
                x="Score",
                y="Count",
                color="Model",
                barmode="group",
                title="Count of Scores by Value - Utility"
            )
            st.plotly_chart(fig_hist_util, width='stretch')
            
        # 2. Chart Comprehensibility Count Chart
        df_comp = df_num_counts[df_num_counts['Metric'] == 'Chart Comp.']
        if not df_comp.empty:
            fig_hist_comp = px.bar(
                df_comp,
                x="Score",
                y="Count",
                color="Model",
                barmode="group",
                title="Count of Scores by Value - Chart Comp."
            )
            st.plotly_chart(fig_hist_comp, width='stretch')
