"""
Sondaggio di Valutazione Esperta per Spiegazioni AI Cliniche
Valutazione basata su criteri per professionisti medici.

Design: Output individuali valutati con giudizi categorici.
Confronto statistico inferito da giudizi aggregati degli esperti.
"""

import streamlit as st
import uuid
import extra_streamlit_components as stx
import time
import streamlit.components.v1 as components
from datetime import datetime, timedelta
from pathlib import Path
import sys

# Add parent for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


# Import components
from components.session import (
    init_session_state,
    load_persisted_session,
    save_persisted_session,
    autosave,
    COOKIE_NAME,
    SESSION_TTL_DAYS
)
from components.data import load_blinded_outputs
from components.profiles import (
    save_user_profile,
    load_user_profile,
    get_completed_count
)
from components.ui import (
    render_output,
    inject_custom_css,
    tri_choice,
    info_container
)
from components.translations import t, display_language_selector, get_lang
from components.review import submit_review
from components.tutorial import render_tutorial

# Page configuration
st.set_page_config(
    page_title=t("page_title"),
    page_icon=":material/local_hospital:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject CSS
inject_custom_css()

# =========================
# MAIN APP
# =========================

def main():
    """Main application."""
    init_session_state()

    def go_back():
        """Navigate to previous case."""
        if st.session_state.current_idx > 0:
            st.session_state.current_idx -= 1

    
    # --- 1. COOKIE IDENTITY LAYER ---
    cookie_manager = stx.CookieManager(key="survey_cookie_manager")
    
    # Attempt to retrieve cookie if we don't have an ID yet
    if not st.session_state.identity_locked:
        # We need to wait for cookie manager to be ready in frontend
        # .get() return None on first run usually
        cookie_id = cookie_manager.get(cookie=COOKIE_NAME)
        
        if cookie_id:
            st.session_state.reviewer_id = cookie_id
            st.session_state.identity_locked = True
            st.rerun()

    # --- 2. HYDRATION LAYER ---
    # If we have an ID but haven't restored state (e.g. reload or new tab), fetch from DB
    if st.session_state.identity_locked and not st.session_state._session_restored:
        persisted = load_persisted_session(st.session_state.reviewer_id)
        if persisted:
            # Restore state to st.session_state *BEFORE* widgets are rendered
            # EXCLUDE form specific keys so reload/next page starts fresh (as requested)
            EXCLUDE_KEYS = ['trust', 'factuality', 'relevance', 'justification', 'chart_comprehensibility', 'utility', 'comments']
            
            for k, v in persisted["state"].items():
                if k in EXCLUDE_KEYS:
                    continue
                if v is not None:
                     st.session_state[k] = v
            st.session_state._session_restored = True
            
            # Restore profile if needed
            if not st.session_state.clinician_profile:
                st.session_state.clinician_profile = load_user_profile(st.session_state.reviewer_id)
            
            # Recalculate if completed count > restored index (edge case: review done on other device)
            completed = get_completed_count(st.session_state.reviewer_id) if 'get_completed_count' in globals() else 0
            if completed > st.session_state.current_idx:
                 st.session_state.current_idx = completed
                 
            st.toast(t("session_restored"), icon=":material/cloud_download:")

    # --- 3. ONBOARDING (If no ID or Profile) ---
    if not st.session_state.identity_locked or st.session_state.clinician_profile is None:
        col_title, col_lang = st.columns([3, 1])
        with col_title:
             st.markdown(f"## :material/medical_services: {t('clinical_profile')}")
        with col_lang:
            display_language_selector(key="onboarding_lang_selector")
        
        # Display ID (either generated or retrieved)
        display_id = st.session_state.reviewer_id if st.session_state.reviewer_id else f"User_{uuid.uuid4().hex[:6].upper()}"
        st.markdown(t("welcome_message", id=display_id))
        
        with st.form("clinician_profile_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                specialization = st.selectbox(
                    t("specialization_label"),
                    t("specializations")
                )

                experience = st.selectbox(
                    t("experience_label"),
                    t("experience_options")
                )

            with col2:
                setting = st.selectbox(
                    t("setting_label"),
                    t("settings")
                )

                ai_familiarity = st.select_slider(
                    t("ai_familiarity_label"),
                    options=[1, 2, 3, 4, 5],
                    value=3
                )
                
            submitted = st.form_submit_button(t("start_evaluation"), type="primary")
            
            if submitted:
                # 1. Lock Identity
                st.session_state.reviewer_id = display_id
                st.session_state.identity_locked = True
                
                # 2. Set Persistent Cookie
                expires = datetime.now() + timedelta(days=SESSION_TTL_DAYS)
                try:
                    cookie_manager.set(COOKIE_NAME, display_id, expires_at=expires)
                except Exception as e:
                    print(f"Cookie error: {e}")

                # 3. Save Profile
                profile = {
                    "specialization": specialization,
                    "experience": experience,
                    "setting": setting,
                    "ai_familiarity": ai_familiarity,
                    "ref_link": st.query_params.get("q")
                }
                st.session_state.clinician_profile = profile
                
                save_user_profile(display_id, profile)
                
                st.rerun()
        return

    # --- 4. TUTORIAL PAGE (After profile, before survey) ---
    if not st.session_state.tutorial_completed:
        render_tutorial()
        return

    # --- 5. SURVEY LOGIC ---
    if st.session_state.get('show_success_toast'):
        st.toast(t("response_saved"), icon=':material/check_circle:')
        st.session_state.show_success_toast = False

    # Load forms
    if st.session_state.review_forms is None:
        with st.spinner(t("loading_cases")):
            st.session_state.review_forms = load_blinded_outputs(st.session_state.reviewer_id, language=get_lang())
    
    forms = st.session_state.review_forms
    current_idx = st.session_state.current_idx

    # --- UX: Scroll to Top & Delay ---
    if st.session_state.current_idx != st.session_state.last_idx:
        st.session_state.last_idx = st.session_state.current_idx
        st.session_state.unlock_time = time.time() + 5.0 # 5 seconds delay
        # Save session to record the new index and unlock time
        save_persisted_session(st.session_state.reviewer_id)
        
        # Scroll to top
        js = """
        <script>
            setTimeout(function() {
                var top = window.parent.document.getElementById('top-anchor');
                if (top) { top.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
                else { window.parent.scrollTo(0,0); }
            }, 100);
        </script>
        """
        components.html(js, height=0)

    # Calculate Patient Sequence Number
    unique_visits = []
    seen = set()
    for f in forms:
        vid = f.get('visit_id')
        if vid and vid not in seen:
            unique_visits.append(vid)
            seen.add(vid)
            
    def get_patient_num(vid):
         try:
             return unique_visits.index(vid) + 1
         except ValueError:
             return 0

    # --- HEADER NAVIGATION ---
    
    # Pre-calculate patient map for navigation
    patient_map = {} # label -> idx
    patient_labels = []
    
    for idx, f in enumerate(forms):
        if f.get('type') == 'separator':
            vid = f.get('visit_id')
            p_num = get_patient_num(vid)
            label = f"Patient {p_num}"
            patient_map[label] = idx
            patient_labels.append(label)

    col1, col2, col3 = st.columns([1, 2, 1], vertical_alignment="center")
    with col1:
        st.markdown(f"### :material/local_hospital: {t('clinical_eval_header')}")
        st.caption(f"User: `{st.session_state.reviewer_id}`")
    with col2:
        if forms and current_idx < len(forms):
            current_form = forms[current_idx]
            
            # Determine current patient context
            c_vid = current_form.get('visit_id')
            c_p_num = get_patient_num(c_vid)
            current_label = f"Patient {c_p_num}"
            
            # Navigation & Status
            with info_container():
                # 1. Navigation Dropdown
                try:
                    p_idx = patient_labels.index(current_label)
                except ValueError:
                    p_idx = 0
                    
                selected_patient = st.selectbox(
                    "Navigate to Patient",
                    patient_labels,
                    index=p_idx,
                    key="header_patient_nav",
                    label_visibility="collapsed"
                )
                
                # Handle Navigation
                if selected_patient != current_label:
                    target = patient_map.get(selected_patient)
                    if target is not None:
                            st.session_state.current_idx = target
                            st.session_state.last_idx = target
                            st.rerun()

                # 2. Status Text
                if current_form.get('type') == 'separator':
                    pass
                else:
                    # Count reviews for this visit
                    count = sum(1 for f in forms[:current_idx+1] 
                                if f.get('visit_id') == c_vid and f.get('type') != 'separator')
                    
                    st.markdown(f":material/info: **Evaluation #{count}** for {current_label}")
                
            warning_note = t("patient_consistency_warning")

    with col3:
        display_language_selector(key="survey_lang_selector")
        
    # Render warning below header if present
    if warning_note:
        st.info(warning_note, icon=":material/info:")
            
    if not forms:
        st.warning(t("no_cases_found"))
        return
    
    if current_idx >= len(forms):
        st.success(t("all_reviews_complete"))
        return
    
    form = forms[current_idx]
    
    # --- HANDLE SEPARATOR ---
    if form.get('type') == 'separator':
        visit_id = form['visit_id']
        
        # Centered Layout
        _, center_col, _ = st.columns([1, 2.5, 1])
        with center_col:
            st.markdown(f"<div style='text-align: center; margin-top: 2rem;'></div>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='text-align: center;'><span class='material-icons' style='vertical-align: middle; font-size: 40px;'>medical_services</span> {t('new_visit')}</h1>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align: center; color: #555; margin-bottom: 2rem;'>{t('prepare_visit')} #{get_patient_num(visit_id)}</h3>", unsafe_allow_html=True)
            
            # Display Patient Context if available
            demo = form.get('demographics')
            overview = form.get('patient_overview')
            
            if demo or overview:
                age = demo.get('age', 'N/A') if demo else 'N/A'
                gender = demo.get('gender', 'N/A') if demo else 'N/A'
                
                st.info(f"**{t('patient')}**: {age} {gender}\n\n{overview}", icon="👤")

            st.markdown(f"<p style='text-align: center; margin-top: 1.5rem; margin-bottom: 2rem; font-style: italic; color: #666;'>{t('visit_instructions')}</p>", unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Nav buttons for separator
            b_col1, b_col2 = st.columns([1, 1], gap="medium")
            with b_col1:
                if current_idx > 0:
                    st.button(t("back_button"), on_click=go_back, width="stretch")
                else:
                    st.empty()
                    
            with b_col2:
                if st.button(t("start_evaluation_btn"), type="primary", width="stretch"):
                    st.session_state.current_idx += 1
                    st.rerun()
        return

    # --- HANDLE REVIEW FORM ---
    visit_id = form['visit_id']
    output = form['output']
    
    st.markdown("<div id='top-anchor'></div>", unsafe_allow_html=True)

    # Try to load patient data
    patient = None    
    # Fallback
    if 'patient_context' in output:
        ctx = output['patient_context']
        class DemographicsFallback:
            def __init__(self, data):
                    self.age = data.get('age', 'N/A')
                    self.gender = data.get('gender', 'N/A')
                    self.chief_complaint = data.get('chief_complaint', 'N/A')
            patient = DemographicsFallback(ctx)

    # Render Output (UI Component)
    # Note moved to header
    render_output(output, patient=patient)
    
    st.divider()
    
    # --- CRITERION-BASED EVALUATION ---
    st.markdown(f"### {t('your_evaluation')}")
    
    # ROW 1: Q1 (Trust) & Q2 (Factuality)
    r1_c1, r1_c2 = st.columns(2, gap="medium")
    with r1_c1:
        tri_choice(
            "trust",
            t("q1_label"),
            caption=t("q1_caption"),
            options=t("q1_options")
        )
    with r1_c2:
        tri_choice(
            "factuality",
            t("q2_label"),
            caption=t("q2_caption"),
            options=t("q2_options")
        )


    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)

    # ROW 2: Q3 (Relevance) & Q4 (Justification)
    r2_c1, r2_c2 = st.columns(2, gap="medium")
    with r2_c1:
        tri_choice(
            "relevance",
            t("q3_label"),
            caption=t("q3_caption"),
            options=t("q3_options")
        )
    with r2_c2:
        tri_choice(
            "justification",
            t("q4_label"),
            caption=t("q4_caption"),
            options=t("q4_options")
        )


    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)

    # ROW 3: Q5 (Clarity) & Q6 (Utility)
    r3_c1, r3_c2 = st.columns(2, gap="medium") 
    with r3_c1:
        st.markdown(f"**{t('q5_label')}**")
        st.caption(t("q5_caption"))

        # Ensure valid integer value for slider (handle legacy strings or None)
        if st.session_state.get('chart_comprehensibility') is None or not isinstance(st.session_state.chart_comprehensibility, int):
             st.session_state.chart_comprehensibility = 3

        st.select_slider(
            t("q5_label"),
            options=[1, 2, 3, 4, 5],
            value=st.session_state.chart_comprehensibility,
            key="chart_comprehensibility",
            label_visibility="collapsed",
            format_func=lambda x: t("q5_scale").get(x, str(x)),
            on_change=autosave
        )
    with r3_c2:
        st.markdown(f"**{t('q6_label')}**")
        st.caption(t("q6_caption"))
        
        # Ensure default value if None
        if st.session_state.utility is None:
             st.session_state.utility = 3

        st.select_slider(
            t("q6_label"),
            options=[1, 2, 3, 4, 5],
            value=3,
            key="utility",
            label_visibility="collapsed",
            format_func=lambda x: t("q6_scale").get(x, str(x)),
            on_change=autosave
        )

    
    st.divider()
    
    # Optional qualitative feedback
    st.markdown(f"**{t('optional_feedback')}**")
    st.caption(t("feedback_caption"))
    
    feedback_col1, feedback_col2 = st.columns([3, 2], gap="medium")
    with feedback_col1:
        st.caption(f":material/edit: {t('written_comments')}")
        st.text_area(
            t("written_feedback_label"),
            placeholder=t("comments_placeholder"),
            key="comments",
            height=80,
            label_visibility="collapsed",
            on_change=autosave
        )
    with feedback_col2:
        st.caption(f":material/mic: {t('audio_feedback')}")
        audio_col, clear_col = st.columns([5, 1], gap="small")
        with audio_col:
            st.audio_input(t("record_audio"), key=f"audio_feedback_{st.session_state.audio_key}", label_visibility="collapsed")
        with clear_col:
            st.button(":material/delete:", key="clear_audio", help=t("delete_recording"), on_click=lambda: setattr(st.session_state, 'audio_key', st.session_state.audio_key + 1))
    
    # Submit Footer
    
    # Calculate footer label (same as header)
    count = sum(1 for f in forms[:current_idx+1] 
              if f.get('visit_id') == visit_id and f.get('type') != 'separator')
    p_num = get_patient_num(visit_id)
    
    footer_label = t("patient_eval_header", visit_id=p_num, count=count)
    # Convert markdown bold to HTML bold for div
    footer_label = footer_label.replace("**", "<b>", 1).replace("**", "</b>", 1).replace("**", "<b>", 1).replace("**", "</b>", 1)

    st.markdown(
        f"<div style='text-align: center; color: #8A8F9C; font-size: 0.9rem; margin-top: 2rem; margin-bottom: 0.5rem;'>"
        f"{footer_label}"
        f"</div>", 
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 10, 1])
    with col2:
        # Check timer
        remaining = 0
        if st.session_state.unlock_time:
             remaining = st.session_state.unlock_time - time.time()
             
        if remaining > 0:
             st.button(f":material/timer: {t('wait_seconds')} {int(remaining)+1}s...", disabled=True, width="stretch", key="disabled_submit")
             time.sleep(remaining)
             st.rerun() 
        else:
            # Buttons row
            btn_col1, btn_col2 = st.columns([1, 1], gap="medium")
            with btn_col1:
                 if current_idx > 0:
                     st.button(t("back_button"), width="stretch", on_click=go_back)
            
            with btn_col2:
                st.button(
                    t("submit_continue"), 
                    type="primary", 
                    width="stretch",
                    on_click=submit_review,
                    args=(form, visit_id, f"audio_feedback_{st.session_state.audio_key}")
                )


if __name__ == "__main__":
    main()
