"""
Tutorial page component for explaining the evaluation process to clinicians.
"""

import streamlit as st
from .translations import t, display_language_selector
from .ui import SECTION_COLORS


def render_tutorial():
    """
    Render the tutorial page explaining study objectives and evaluation process.
    """
    
    # Center-aligned container for tutorial
    col1, col_main, col2 = st.columns([0.5, 3, 0.5])
    
    with col_main:
        col_header, col_lang = st.columns([3, 1])
        with col_header:
            st.markdown(f"# :material/school: {t('tutorial_title')}")
        with col_lang:
            display_language_selector(key="tutorial_lang_selector")

        st.markdown("---")
        
        # 1. Study Objective
        st.markdown(f"### :material/target: {t('tutorial_objective_title_clean')}")
        st.markdown(t('tutorial_objective_desc'))
        
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        
        # 2. Your Task
        st.markdown(f"### :material/assignment: {t('tutorial_task_title_clean')}")
        st.markdown(t('tutorial_task_desc'))
        
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        
        # 3. Explanation Structure
        st.markdown(f"### :material/account_tree: {t('tutorial_structure_title_clean')}")
        st.markdown(t('tutorial_structure_intro'))
        
        st.markdown("")
        st.markdown("")
        
        # Structure Cards Template (Dashboard Mockup)
        
        with st.container(border=True):
             # Header-like title for the mockup
             st.markdown(f'<div style="font-weight: 600; margin-bottom: 16px; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.5px;">{t("tutorial_mockup_title")}</div>', unsafe_allow_html=True)
             
             # Main Dashboard Mockup (2-Column)
             st.markdown(f"""
<div style="display: flex; gap: 24px; flex-wrap: wrap;">
<div style="flex: 1.6; min-width: 300px;">
<div style="display: flex; align-items: center; gap: 8px; color: {SECTION_COLORS['identity']}; font-weight: bold; font-size: 0.9rem; margin-bottom: 6px;">
<span class="material-icons" style="font-size: 1.1rem;">person</span>
<span>{t('patient_summary')}</span>
</div>
<div style="font-size: 0.85rem; margin-bottom: 20px; padding-left: 28px;">
{t('tutorial_mockup_patient_desc')}
</div>
<div style="display: flex; align-items: center; gap: 8px; color: {SECTION_COLORS['metrics']}; font-weight: bold; font-size: 0.9rem; margin-bottom: 8px;">
<span class="material-icons" style="font-size: 1.1rem;">timeline</span>
<span>{t('vital_signs_profile')}</span>
</div>
<div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px; padding-left: 28px;">
<div style="background: rgba(128,128,128,0.08); border: 1px solid rgba(128,128,128,0.2); border-radius: 12px; padding: 2px 12px; font-size: 0.75rem;">
<span>ESI:</span> 2
</div>
<div style="background: rgba(128,128,128,0.08); border: 1px solid rgba(128,128,128,0.2); border-radius: 12px; padding: 2px 12px; font-size: 0.75rem;">
<span>STATUS:</span> <span>{t('tutorial_mockup_vitals_status')}</span>
</div>
<div style="background: rgba(128,128,128,0.08); border: 1px solid rgba(128,128,128,0.2); border-radius: 12px; padding: 2px 12px; font-size: 0.75rem;">
<span>MAP:</span> 52
</div>
<div style="background: rgba(128,128,128,0.08); border: 1px solid rgba(128,128,128,0.2); border-radius: 12px; padding: 2px 12px; font-size: 0.75rem;">
<span>Pain:</span> 3/10
</div>
</div>
<div style="display: flex; align-items: center; gap: 8px; color: {SECTION_COLORS['findings']}; font-weight: bold; font-size: 0.9rem; margin-bottom: 6px;">
<span class="material-icons" style="font-size: 1.1rem;">search</span>
<span>{t('key_abnormal_patterns')}</span>
</div>
<div style="font-size: 0.85rem; margin-bottom: 20px; padding-left: 28px;">
{t('tutorial_mockup_patterns_desc')}
</div>
<div style="display: flex; align-items: center; gap: 8px; color: {SECTION_COLORS['summary']}; font-weight: bold; font-size: 0.9rem; margin-bottom: 8px;">
<span class="material-icons" style="font-size: 1.1rem;">psychology</span>
<span>{t('clinical_interpretation')}</span>
</div>
<div style="background: rgba(95,143,157,0.08); border-left: 3px solid {SECTION_COLORS['summary']}; padding: 10px 14px; border-radius: 4px; margin-bottom: 20px; margin-left: 28px; font-size: 0.85rem; line-height: 1.4;">
{t('tutorial_mockup_interpretation_desc')}
</div>
<div style="display: flex; align-items: center; gap: 8px; color: {SECTION_COLORS['actions']}; font-weight: bold; font-size: 0.9rem; margin-bottom: 6px;">
<span class="material-icons" style="font-size: 1.1rem;">bolt</span>
<span>{t('clinical_actions')}</span>
</div>
<ul style="margin: 0 0 0 28px; padding-left: 14px; font-size: 0.85rem; line-height: 1.6;">
<li>{t('tutorial_mockup_action_1')}</li>
<li>{t('tutorial_mockup_action_2')}</li>
</ul>
</div>
<div style="flex: 1; min-width: 200px;">
<div style="display: flex; align-items: center; gap: 8px; font-weight: bold; font-size: 0.9rem; margin-bottom: 8px;">
<span class="material-icons" style="font-size: 1.1rem;">image</span>
<span>{t('visual_context')}</span>
</div>
<div style="background: rgba(128, 128, 128, 0.05); border: 1px dashed; padding: 20px; border-radius: 6px; height: 350px; display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 20px;">
<span class="material-icons" style="font-size: 3.5rem; color: rgba(128,128,128,0.4); margin-bottom: 16px;">show_chart</span>
<div style="font-size: 0.85rem; text-align: center; max-width: 80%; line-height: 1.4; color: rgba(255,255,255,0.7);">
{t('tutorial_mockup_visual_desc')}
</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)
        
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        
        # 4. Image full screen
        st.markdown(f"### :material/fullscreen: {t('tutorial_images_title_clean')}")
        st.markdown(t('tutorial_images_desc'))
        
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        
        # 5. Consecutive explanations
        st.markdown(f"### :material/repeat: {t('tutorial_consecutive_title_clean')}")
        st.markdown(t('tutorial_consecutive_desc'))
        
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        
        # 6. Questions
        st.markdown(f"### :material/quiz: {t('tutorial_questions_title_clean')}")
        st.markdown(t('tutorial_questions_desc'))
        
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        
        # 7. Session persistence
        st.markdown(f"### :material/save: {t('tutorial_session_title_clean')}")
        st.markdown(f"{t('tutorial_session_desc')}")
        
        st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
        
        # 8. Notes
        st.markdown(f"### :material/mic: {t('tutorial_notes_title_clean')}")
        st.markdown(t('tutorial_notes_desc'))
        
        st.markdown("---")
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        
        # Proceed button
        col_btn1, col_btn_center, col_btn2 = st.columns([1, 1, 1])
        with col_btn_center:
            if st.button(t('tutorial_proceed'), type="primary", width="stretch"):
                st.session_state.tutorial_completed = True
                st.rerun()
