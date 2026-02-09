
import streamlit as st
import base64
import io
from PIL import Image
from markdown_it import MarkdownIt

# --- STYLING ---
# We can keep the CSS injection here or in a function
from .session import autosave
from .translations import t

# --- STYLING ---
# We can keep the CSS injection here or in a function
from streamlit_extras.stylable_container import stylable_container

# --- STYLING ---
# We can keep the CSS injection here or in a function
def inject_custom_css():
    st.markdown("""
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
        .clinical-header {
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 600;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }
        .clinical-header .material-icons {
            font-size: 1.2rem;
        }
    
        .main { max-width: 1400px; margin: auto; }
        .stExpander { margin-bottom: 0.5rem; }
        .block-container { padding-top: 4rem; padding-bottom: 3rem; }
        h1 { font-size: 1.6rem !important; margin-bottom: 0.3rem !important; }
        h3 { font-size: 1.1rem !important; margin-top: 0.3rem !important; margin-bottom: 0.3rem !important; }
        h4 { font-size: 1rem !important; margin-top: 0.2rem !important; margin-bottom: 0.2rem !important; }
        .progress-text { font-size: 0.85rem; color: #888; }
        /* Compact expanders */
        .streamlit-expanderHeader { font-size: 0.9rem !important; padding: 0.3rem 0.5rem !important; }
        .streamlit-expanderContent { padding: 0.3rem 0.5rem !important; }
    </style>
    """, unsafe_allow_html=True)

def tri_choice(key, label, caption=None, options=None):
    """
    Render a 3-choice button group that behaves like a radio button.
    options: list of (value, label) tuples. 
             If None, defaults to [('yes', 'Sì'), ('partial', 'Parzialmente'), ('no', 'No')]
    """
    if options is None:
        options = [
            ("no", t("no")),
            ("partial", t("partial")),
            ("yes", t("yes"))
        ]
    
    # Ensure session state initialization
    if key not in st.session_state:
        st.session_state[key] = None

    if label:
        st.markdown(f"**{label}**")
        
    if caption:
        st.caption(caption)

    # Determine labels and types based on selection
    col1, col2, col3 = st.columns(3)
    
    def on_click_handler(v):
        st.session_state[key] = v
        autosave()

    # --- PALETTE DEFINITION ---
    # Top-level palette for cleaner maintenance
    PALETTE = {
        "green":  {
            "strong": "#137333", "light": "#e6f4ea", 
            "hover_strong": "#0f5a28", "hover_light": "#d4ebd9" 
        },
        "yellow": {
            "strong": "#6b5d08", "light": "#fff9db", 
            "hover_strong": "#4d4306", "hover_light": "#fff5c2"
        }, 
        "red":    {
            "strong": "#c5221f", "light": "#fce8e6", 
            "hover_strong": "#a51b19", "hover_light": "#fad2cf"
        },
    }
    
    COLOR_MAP = {
        "yes": "green",
        "partial": "yellow",
        "unsure": "yellow",
        "verbose": "yellow",
        "no": "red",
        "shallow": "red"
    }

    # Helper to generate CSS for Solid/Outline toggle
    def get_style(color_key, selected):
        p = PALETTE[color_key]
        if selected:
            # Solid Strong BG, White Text, Strong Border
            return f"""
            button {{
                background-color: {p['strong']} !important;
                border: 1px solid {p['strong']} !important;
                color: #ffffff !important;
            }}
            """
        else:
            # Light BG, Strong Text, 1px Strong Border (Outline)
            return f"""
            button {{
                background-color: {p['light']} !important;
                border: 1px solid {p['strong']} !important;
                color: {p['strong']} !important;
            }}
            """

    cols = st.columns(3)
    for i, (val, text) in enumerate(options):
        with cols[i]:
            is_selected = (st.session_state[key] == val)
            icon = ":material/check_box:" if is_selected else ":material/check_box_outline_blank:"
            color_key = COLOR_MAP.get(val, "green")
            
            with stylable_container(
                key=f"{key}_c{i}",
                css_styles=get_style(color_key, is_selected)
            ):
                st.button(f"{icon} {text}", key=f"{key}_btn_{val}", type="secondary", width="stretch", on_click=on_click_handler, args=(val,))


def colored_header(icon, text, color):
    st.markdown(f"""
        <div class="clinical-header" style="color: {color};">
            <span class="material-icons">{icon}</span>
            <span>{text}</span>
        </div>
    """, unsafe_allow_html=True)

SECTION_COLORS = {
    "identity": "#6C83B5",
    "metrics": "#455460",
    "findings": "#D1A35C",
    "summary": "#5F8F9D",
    "actions": "#B36B6B",
    "gaps": "#8A8F9C"
}

# Helper to clean and compare values
def check_match(criteria, val):
    if val is None: return False
    try:
        # Clean value (e.g. "8.0h" -> 8.0, "4/10" -> 4)
        s_val = str(val).lower().replace("h", "").split("/")[0].strip()
        # If value is numeric string like "1" or "1.0", convert to float
        f_val = float(s_val)
        
        # Clean criteria and handle unicode operators
        crit = str(criteria).lower().strip().replace("≥", ">=").replace("≤", "<=").replace("h", "").replace("mmhg", "").strip()
        
        # Range "0.5-0.7" or "60–64"
        if "-" in crit or "–" in crit:
            parts = crit.replace("–", "-").split("-")
            if len(parts) == 2:
                return float(parts[0]) <= f_val <= float(parts[1])
        
        # Inequality "< 60", ">= 2"
        if "<" in crit:
            limit = float(crit.replace("<", "").replace("=", ""))
            return f_val <= limit if "=" in crit else f_val < limit
        if ">" in crit:
            limit = float(crit.replace(">", "").replace("=", ""))
            return f_val >= limit if "=" in crit else f_val > limit
            
        # Exact Match (Numeric)
        return f_val == float(crit)
    except:
        # String match fallback
        return str(val).lower() in str(criteria).lower()

@st.dialog(" ")
def show_definition_modal(title, content, current_val=None):
    st.markdown(f"### {title}")
    


    if isinstance(content, dict):
        if "desc" in content:
            st.markdown(f"**{content['desc']}**")
            
        if "bullets" in content:
            for b in content['bullets']:
                st.markdown(f"- {b}")
                
        if "table" in content:
            headers = content["table"].get("headers", [])
            rows = content["table"].get("rows", [])
            
            # Build HTML Table
            html = "<table style='width:100%; border-collapse: collapse; margin-top: 10px;'>"
            
            # Header
            html += "<tr style='background-color: #2A3140; color: #fff;'>"
            for h in headers:
                html += f"<th style='padding: 8px; text-align: left; border: 1px solid #444;'>{h}</th>"
            html += "</tr>"
            
            # Rows
            for row in rows:
                cols = row.get("cols", [])
                match_rule = cols[0] # Use first col as rule by default
                
                # Check highlight
                is_selected = check_match(match_rule, current_val)
                bg_style = ""
                if is_selected:
                    # Map simple color names to hex with transparency for readability
                    c_map = {
                        "red": "rgba(179, 107, 107, 0.4)",
                        "orange": "rgba(209, 163, 92, 0.4)",
                        "yellow": "rgba(189, 189, 87, 0.4)",
                        "green": "rgba(97, 166, 107, 0.4)", 
                        "grey": "rgba(128, 128, 128, 0.3)"
                    }
                    raw_color = row.get("color", "grey")
                    bg_color = c_map.get(raw_color, "rgba(255,255,255,0.1)")
                    bg_style = f"background-color: {bg_color}; font-weight: bold;"
                
                html += f"<tr style='{bg_style}'>"
                for c in cols:
                     html += f"<td style='padding: 8px; border: 1px solid #444;'>{c}</td>"
                html += "</tr>"
                
            html += "</table>"
            st.markdown(html, unsafe_allow_html=True)
            
        if "note" in content:
            st.info(content["note"])
        
        if "extra_table" in content:
            headers = content["extra_table"].get("headers", [])
            rows = content["extra_table"].get("rows", [])
            html = "<table style='width:100%; border-collapse: collapse; margin-top: 10px;'>"
            html += "<tr style='background-color: #2A3140; color: #fff;'>"
            for h in headers:
                 html += f"<th style='padding: 8px; text-align: left; border: 1px solid #444;'>{h}</th>"
            html += "</tr>"
            for row in rows:
                cols = row.get("cols", [])
                html += "<tr>"
                for c in cols:
                     html += f"<td style='padding: 8px; border: 1px solid #444;'>{c}</td>"
                html += "</tr>"
            html += "</table>"
            st.markdown(html, unsafe_allow_html=True)
            
        # Fallback for string content
        st.markdown(content)

def info_container(key=None):
    """
    Creates a container styled like st.info but allows interactive widgets.
    """
    # Custom container to mimic st.info
    return stylable_container(
        key=key or "info_box",
        css_styles='''
            {
                background-color: rgba(28, 131, 225, 0.1) !important;
                border: 1px solid rgba(28, 131, 225, 0.4) !important;
                border-radius: 0.5rem !important;
                padding: 1rem !important;
                color: #BEE3F8 !important; /* Light blue text for dark mode */
            }
        '''
    )

def render_output(output: dict, patient=None):
    """
    Render a clinical output using the Modern Clinical Dashboard Layout.
    
    Layout:
    1. Header: Patient Snapshot + Visual Badges (Risk/ESI)
    2. Two-Column Dashboard:
       - LEFT (60%): Reasoning & Interpretation
       - RIGHT (40%): Visual Evidence Stack
    3. Footer: Metadata & Gaps (Open by default)
    """
    
    # --- 1. HEADER: Patient Snapshot & Risk Badges ---
    # Extract Metrics
    esi = output.get('esi_level', 'N/A')
    stress = output.get('physiological_stress', output.get('stress_status', 'Unknown'))
    
    # Extract Demographics string if patient object provided
    pt_str = ""
    if patient:
        pt_str = f"**{patient.age}** {patient.gender} | **{patient.chief_complaint}**"
    
    # Determine Risk Badge Color (Muted clinical palette)
    if str(esi) in ['1', '2']:
        badge_color = "#B36B6B" # High risk
        badge_bg = "rgba(179,107,107,0.15)"
    elif "stres" in str(stress).lower():
        badge_color = "#D1A35C" # Concerning
        badge_bg = "rgba(209,163,92,0.15)"
    else:
        badge_color = "#7FA998" # Stable
        badge_bg = "rgba(127,169,152,0.15)"
        
    risk_badge = f'<span style="color: {badge_color}; background-color: {badge_bg}; padding: 2px 8px; border-radius: 6px; font-weight: 600; font-size: 0.8rem;">{str(stress).upper()}</span>'
    
    # --- 2. MAIN DASHBOARD (2-Column) ---
    left_col, right_col = st.columns([1.6, 1], gap="medium")
    
    with left_col:
        # --- A. Context & Severity Grid ---
        
        # 1. Demographics & Overview
        colored_header("person", t("patient_summary"), SECTION_COLORS["identity"])
        if pt_str:
            st.markdown(f"**{t('patient')}**: {pt_str}")
            
        overview = output.get('patient_overview', '')
        if overview:
            st.markdown(overview)
        
        therapy = output.get('current_therapy', '')
        if therapy:
             st.markdown(f"**{t('current_therapy')}**: {therapy}")
        
        # Helper for converting potential string floats
        def safe_float(v):
            try:
                return float(v)
            except (ValueError, TypeError):
                return None

        # 2. Severity/Metrics Grid
        # Gather metrics
        st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
        derived = output.get('metrics', {})
        
        si_val = safe_float(derived.get('shock_index'))
        map_val = safe_float(derived.get('map_value'))

        # Metrics Mapping: Label -> (Value, Glossary Key, Raw Value)
        metrics_data = [
             {"label": "ESI", "value": f"{esi}", "raw": esi, "glossary": "glossary_esi"},
             {"label": "STATUS", "value": risk_badge, "is_html": True, "raw": str(stress), "glossary": "glossary_stress"},
             {"label": "qSOFA", "value": f"{derived.get('qsofa_score', '-')}", "raw": derived.get('qsofa_score'), "glossary": "glossary_qsofa"},
             {"label": "MAP", "value": f"{map_val:.0f}" if map_val is not None else "-", "raw": map_val, "glossary": "glossary_map"},
             {"label": "Shock Index", "value": f"{si_val:.2f}" if si_val is not None else "-", "raw": si_val, "glossary": "glossary_shock"},
             {"label": "Pain", "value": f"{output.get('pain_score', '-')}/10", "raw": output.get('pain_score'), "glossary": "glossary_pain"},
             {"label": "Length of Stay", "value": f"{output.get('ed_los', '-')}", "raw": output.get('ed_los'), "glossary": "glossary_los"},
        ]
        
        colored_header("timeline", t("vital_signs_profile"), SECTION_COLORS["metrics"])

        # Interactive Chips Layout (Adaptive Wrapping)
        # We calculate rows based on a heuristic "max character width" to ensure wrapping on small screens
        MAX_ROW_WIDTH = 55 
        
        current_row = []
        current_width = 0
        rows = []
        
        # 1. Pre-process and Group
        for item in metrics_data:
             # Determine Text
             if item.get("is_html"):
                 val_text = str(stress).upper()
                 label_text = f"{item['label']}: {val_text}"
             else:
                 label_text = f"{item['label']}: {item['value']}"
             
             # Calculate Weight (approx char length)
             weight = len(label_text) + 2
             
             # Check if we need to wrap
             if current_width + weight > MAX_ROW_WIDTH and current_row:
                 # Finish current row
                 rows.append(current_row)
                 current_row = []
                 current_width = 0
             
             # Add to current
             current_row.append({**item, "text": label_text, "weight": weight})
             current_width += weight
        
        # Add last row
        if current_row:
            rows.append(current_row)
            
        # 2. Render Rows
        for row_items in rows:
            # Create columns relative to the weights of items in this row
            row_weights = [item["weight"] for item in row_items]
            cols = st.columns(row_weights, gap="small")
            
            for i, (col, item) in enumerate(zip(cols, row_items)):
                with col:
                    # Determine Color Logic
                    bg_color = "#1B2233" # Default Dark
                    border_color = "#2A3140"
                    hover_bg = "#2A3140"
                    font_weight = "400"
                    
                    # Dynamic Color Logic based on Glossary
                    matched_color = None
                    glossary_content = t(item.get('glossary'))
                    
                    if isinstance(glossary_content, dict) and 'table' in glossary_content:
                        for row in glossary_content['table'].get('rows', []):
                            cols = row.get("cols", [])
                            # Use cols[0] as criteria, consistent with modal logic
                            if cols and check_match(cols[0], item.get('raw')):
                                matched_color = row.get("color")
                                break
                    
                    # Palette
                    CHIP_PALETTE = {
                        "red":    {"bg": "#5e2b2b", "border": "#d95555", "hover": "#753636"},
                        "orange": {"bg": "#664d2e", "border": "#e0aa60", "hover": "#7d5e38"},
                        "yellow": {"bg": "#5c5c3d", "border": "#b8b87a", "hover": "#6b6b47"},
                        "green":  {"bg": "#1e3a29", "border": "#4caf50", "hover": "#2a5239"},
                        "grey":   {"bg": "#2A3140", "border": "#4a5469", "hover": "#3b4459"},
                        "critical": {"bg": "#5e2b2b", "border": "#d95555", "hover": "#753636"} # Alias
                    }
                    
                    if matched_color and matched_color in CHIP_PALETTE:
                        p = CHIP_PALETTE[matched_color]
                        bg_color = p["bg"]
                        border_color = p["border"]
                        hover_bg = p["hover"]
                        font_weight = "600"
                    elif item['label'] == "ESI" and str(esi) in ['1', '2']:
                        # Fallback legacy logic
                        bg_color = "#5e2b2b" 
                        border_color = "#d95555" 
                        hover_bg = "#753636"
                        font_weight = "600"
                    elif item['label'] == "STATUS" and "stres" in str(stress).lower():
                        bg_color = "#664d2e" 
                        border_color = "#e0aa60"
                        hover_bg = "#7d5e38"
                        font_weight = "600"

                    # Styling
                    # Use a unique key based on label to avoid collision across rows
                    unique_key = f"chip_{item['label']}"
                    with stylable_container(
                        key=unique_key,
                        css_styles=f"""
                        button {{
                            background-color: {bg_color} !important;
                            border: 1px solid {border_color} !important;
                            border-radius: 8px !important;
                            color: #E6E9EF !important;
                            font-family: 'Source Sans Pro', sans-serif !important;
                            font-size: 11px !important;
                            padding: 0px 4px !important;
                            margin: 0px !important;
                            transition: all 0.2s ease;
                            height: 28px !important;
                            min-height: 0px !important;
                            line-height: 1 !important;
                            width: 100% !important;
                            display: flex !important;
                            align-items: center !important;
                            justify-content: center !important;
                            white-space: nowrap !important;
                            letter-spacing: -0.2px !important;
                        }}
                        button:hover, button:active, button:focus, button:focus:not(:active) {{
                            border-color: #FFFFFF !important;
                            background-color: {hover_bg} !important;
                            color: #FFFFFF !important;
                            cursor: pointer !important;
                            outline: none !important;
                            box-shadow: none !important;
                        }}
                        """
                    ):
                        if st.button(item["text"], icon=":material/info:", key=f"btn_metric_{item['label']}", width="stretch"):
                            show_definition_modal(t("description"), t(item['glossary']), current_val=item['raw'])
            
            # Spacer between rows
            st.markdown('<div style="margin-bottom: 6px;"></div>', unsafe_allow_html=True)
            
        st.markdown(f'<div style="margin-bottom: 0.5rem;"></div>', unsafe_allow_html=True)        
        st.markdown("---")

        # --- B. Clinical Reasoning ---
        
        # 3. Relevant Findings
        findings = output.get('relevant_abnormal_findings', '')
        if findings:
            st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
            colored_header("search", t("key_abnormal_patterns"), SECTION_COLORS["findings"])
            st.markdown(findings)
        
        # 4. Interpretation (The Core)
        interpretation = output.get('clinical_interpretation', '')
        if interpretation:
            st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
            colored_header("psychology", t("clinical_interpretation"), SECTION_COLORS["summary"])
            
            # Use markdown-it to render the text to HTML, ensuring bold/italics persist in the div
            md = MarkdownIt()
            interpretation_html = md.render(interpretation)
            
            st.markdown(f"""
<div style="background-color: rgba(95,143,157,0.12); border-left: 4px solid #5F8F9D; padding: 12px 14px; border-radius: 6px;">
    {interpretation_html}
</div>
""", unsafe_allow_html=True)
            
        # 5. Actions / Considerations
        considerations = output.get('clinical_considerations', [])
        if considerations:
            st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
            colored_header("bolt", t("clinical_actions"), SECTION_COLORS["actions"])
            if isinstance(considerations, list):
                for c in considerations:
                    st.markdown(f"- {c}")
            else:
                st.markdown(considerations)

    with right_col:
        # --- C. Visual Evidence Stack ---
        st.markdown(f"#### :material/image: {t('visual_context')}")
        
        images = output.get('images', [])
        if images:
            for idx, img in enumerate(images):
                if img.get('base64'):
                    # Native Streamlit Image for Click-to-Zoom
                    with st.container(border=True):
                        try:
                            # Decode base64 to PIL Image to ensure full interactivity
                            image_data = base64.b64decode(img['base64'])
                            image = Image.open(io.BytesIO(image_data))
                            
                            st.image(
                                image,
                                width="stretch",
                                caption=None # We use custom caption below
                            )
                        except Exception:
                            # Fallback if decoding fails
                            st.error(t("image_load_error"))

                        label = f"**{t('figure')} {idx+1}**"
                        if img.get('narrative'):
                             label += f": {img.get('narrative')}"
                        st.markdown(label)
        else:
            st.caption(t("no_visual_evidence"))
