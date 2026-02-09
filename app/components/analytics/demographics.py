
import streamlit as st
import pandas as pd
import plotly.express as px
from components.session import init_connection

def render_clinician_demographics():
    """Render demographics statistics for valid clinicians."""
    st.markdown("## Clinician Demographics")
    st.markdown("Statistics for experts who have submitted at least one valid (complete) review.")

    # Environment Selection (Dev Mode Only)
    current_env = st.secrets.get("env", {}).get("type", "dev")
    target_env = current_env
    
    if current_env == "dev":
        target_env = st.radio(
            "Data Source",
            options=["dev", "prod"],
            format_func=lambda x: "Development" if x == "dev" else "Production",
            horizontal=True,
            key="demo_env_selector"
        )
            
    # Get reviews
    reviews = []
    try:
        client = init_connection()
        if client:
            db_name = "agent_pulse"
            coll_name = f"reviews_{target_env}"
            coll = client[db_name][coll_name]
            reviews = list(coll.find({}, {"_id": 0}))
        else:
             st.error("Could not connect to MongoDB.")
             return
    except Exception as e:
        st.error(f"Error: {e}")
        return
    
    if not reviews:
        st.info("No data found.")
        return

    # Filter Controls
    col_filter, _ = st.columns([1, 1])
    with col_filter:
        min_reviews = st.number_input(
            "Minimum valid reviews per clinician", 
            min_value=0, 
            value=1, 
            step=1,
            help="Exclude clinicians who have submitted fewer than K valid (complete) reviews.",
            key="demo_min_reviews"
        )

    # 1. Calculate Valid Review Counts per Clinician
    clinician_valid_counts = {}
    required_fields = ['trust', 'factuality', 'relevance', 'justification', 'chart_comprehensibility', 'utility']
    
    # Also collect accumulated valid reviews per clinician for later
    clinician_reviews_map = {} # rid -> list of valid reviews

    for r in reviews:
        rid = r.get('reviewer_id')
        if not rid: continue

        if all(r.get(f) is not None for f in required_fields):
            clinician_valid_counts[rid] = clinician_valid_counts.get(rid, 0) + 1
            if rid not in clinician_reviews_map:
                clinician_reviews_map[rid] = []
            clinician_reviews_map[rid].append(r)

    # 2. Filter Clinicians Based on K
    valid_clinicians_data = [] # List of dicts with profile + aggregated stats
    
    # We iterate through unique clinician IDs found in the reviews
    all_clinician_ids = set(r.get('reviewer_id') for r in reviews if r.get('reviewer_id'))
    
    for rid in all_clinician_ids:
        # Check if they meet the threshold
        count = clinician_valid_counts.get(rid, 0)
        
        if count >= min_reviews and count > 0:
            # Get profile from one of the reviews (assuming profile is consistent)
            # Find a review with profile
            # We can use the first valid review for profile
            associated_reviews = clinician_reviews_map.get(rid, [])
            if not associated_reviews: 
                continue # Should not happen if count > 0
                
            profile = associated_reviews[0].get('clinician_profile', {})
            
            # Normalize Ref Link (handle None)
            ref_link = profile.get("ref_link")
            if not ref_link:
                ref_link = "Direct / None"
                
            valid_clinicians_data.append({
                "ID": rid,
                "Specialization": profile.get("specialization", "Unknown"),
                "Experience": profile.get("experience", "Unknown"),
                "Setting": profile.get("setting", "Unknown"),
                "AI Familiarity": int(profile.get("ai_familiarity", 0)),
                "Ref Code": ref_link,
                "Valid Reviews": count
            })

    if not valid_clinicians_data:
        st.info(f"No clinicians found with >= {min_reviews} valid reviews.")
        return
        
    df_clinicians = pd.DataFrame(valid_clinicians_data)
    
    st.markdown(f"**Total Valid Clinicians:** {len(df_clinicians)}")
    st.markdown(f"**Total Valid Reviews (Filtered):** {df_clinicians['Valid Reviews'].sum()}")

    # --- NORMALIZATION ---
    from components.translations import TRANSLATIONS, get_lang
    
    def get_normalized_label(value, key):
        """
        Normalize a value (that could be in IT/EN/SQ) to the current language.
        Assumes TRANSLATIONS[key] allows looking up index.
        """
        if not value or value == "Unknown":
            return value
            
        current_lang = get_lang()
        category_map = TRANSLATIONS.get(key)
        
        if not category_map:
            return value
            
        # Search for the value in any language list to find its 'canonical' index
        found_index = -1
        for lang, options in category_map.items():
            if isinstance(options, list) and value in options:
                found_index = options.index(value)
                break
                
        if found_index != -1:
            # Get the label in the current language
            # Fallback to EN if current lang missing for some reason
            target_options = category_map.get(current_lang, category_map.get('en'))
            if target_options and found_index < len(target_options):
                return target_options[found_index]
                
        return value

    df_clinicians["Specialization"] = df_clinicians["Specialization"].apply(lambda x: get_normalized_label(x, "specializations"))
    df_clinicians["Experience"] = df_clinicians["Experience"].apply(lambda x: get_normalized_label(x, "experience_options"))
    df_clinicians["Setting"] = df_clinicians["Setting"].apply(lambda x: get_normalized_label(x, "settings"))
    
    st.markdown("---")

    # 0. Ref Code Usage
    st.markdown("### Referral Code Usage")
    
    # Group by Ref Code
    ref_stats = df_clinicians.groupby("Ref Code", observed=False).agg(
        Clinicians=('ID', 'count'),
        ValidReviews=('Valid Reviews', 'sum')
    ).reset_index()
    
    # Melt for stacked bar chart
    ref_melted = ref_stats.melt(id_vars="Ref Code", value_vars=["Clinicians", "ValidReviews"], var_name="Metric", value_name="Count")
    
    fig_ref = px.bar(
        ref_melted, 
        x="Ref Code", 
        y="Count", 
        color="Metric", 
        barmode="group",
        text_auto=True,
        title="Usage by Referral Code"
    )
    st.plotly_chart(fig_ref, width='stretch')
    
    st.markdown("---")

    # 1. Specialization
    st.markdown("### Specialization")
    c1, c2 = st.columns(2)
    with c1:
        spec_counts = df_clinicians["Specialization"].value_counts().reset_index()
        spec_counts.columns = ["Specialization", "Count"]
        fig_spec = px.bar(spec_counts, x="Specialization", y="Count", text_auto=True, title="Clinicians by Specialization")
        st.plotly_chart(fig_spec, width='stretch')
    with c2:
        spec_ai = df_clinicians.groupby("Specialization", observed=False)["AI Familiarity"].mean().reset_index()
        fig_spec_ai = px.bar(spec_ai, x="Specialization", y="AI Familiarity", text_auto='.1f', title="Avg AI Familiarity by Specialization", range_y=[0, 5])
        st.plotly_chart(fig_spec_ai, width='stretch')

    # 2. Experience
    st.markdown("### Experience")
    c3, c4 = st.columns(2)
    with c3:
        exp_counts = df_clinicians["Experience"].value_counts().reset_index()
        exp_counts.columns = ["Experience", "Count"]
        fig_exp = px.bar(exp_counts, x="Experience", y="Count", text_auto=True, title="Clinicians by Experience")
        st.plotly_chart(fig_exp, width='stretch')
    with c4:
        exp_ai = df_clinicians.groupby("Experience", observed=False)["AI Familiarity"].mean().reset_index()
        fig_exp_ai = px.bar(exp_ai, x="Experience", y="AI Familiarity", text_auto='.1f', title="Avg AI Familiarity by Experience", range_y=[0, 5])
        st.plotly_chart(fig_exp_ai, width='stretch')
        
    # 3. Setting
    st.markdown("### Work Setting")
    c5, c6 = st.columns(2)
    with c5:
        set_counts = df_clinicians["Setting"].value_counts().reset_index()
        set_counts.columns = ["Setting", "Count"]
        fig_set = px.bar(set_counts, x="Setting", y="Count", text_auto=True, title="Clinicians by Setting")
        st.plotly_chart(fig_set, width='stretch')
    with c6:
        set_ai = df_clinicians.groupby("Setting", observed=False)["AI Familiarity"].mean().reset_index()
        fig_set_ai = px.bar(set_ai, x="Setting", y="AI Familiarity", text_auto='.1f', title="Avg AI Familiarity by Setting", range_y=[0, 5])
        st.plotly_chart(fig_set_ai, width='stretch')
