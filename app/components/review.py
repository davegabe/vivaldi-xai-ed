
import streamlit as st
import json
import gridfs
from pathlib import Path
from datetime import datetime
from .session import get_collection, init_connection, save_persisted_session
from .translations import t

def save_audio_file(audio_bytes: bytes, filename: str, metadata: dict, output_dir: Path = Path("results")) -> str:
    """Save audio file to GridFS (fallback to file). Returns file ID or filename."""
    # 1. Try GridFS
    client = init_connection()
    if client:
        try:
            db = client["agent_pulse"]
            env = st.secrets.get("env", {}).get("type", "dev")
            bucket_name = f"audio_{env}"
            fs = gridfs.GridFS(db, collection=bucket_name)
            
            file_id = fs.put(
                audio_bytes,
                filename=filename,
                metadata=metadata
            )
            return str(file_id)
        except Exception as e:
            print(f"GridFS Save Error: {e}")

    # 2. Fallback to File
    audio_dir = output_dir / "audio_feedback"
    audio_dir.mkdir(parents=True, exist_ok=True)
    file_path = audio_dir / filename
    
    with open(file_path, "wb") as f:
        f.write(audio_bytes)
    return filename

def save_review(review: dict, output_dir: Path = Path("results")):
    """Save review to MongoDB (fallback to file if connection fails)."""
    # 1. Try MongoDB
    coll = get_collection("reviews")
    if coll is not None:
        try:
            coll.insert_one(review)
            return
        except Exception as e:
            print(f"MongoDB Save Error: {e}")
    
    # 2. Fallback to File
    output_dir.mkdir(parents=True, exist_ok=True)
    reviews_file = output_dir / "expert_reviews.json"
    
    existing = []
    if reviews_file.exists():
        with open(reviews_file) as f:
            existing = json.load(f)
    
    # Convert ObjectIds to str if any
    existing.append(review)
    
    with open(reviews_file, "w") as f:
        json.dump(existing, f, indent=2, default=str)

def submit_review(form, visit_id, audio_key_name):
    """Callback to handle review submission."""
    if not st.session_state.reviewer_id:
        st.error(t("reviewer_id_required"))
        return

    # 1. Handle Audio
    audio_data = st.session_state.get(audio_key_name)
    audio_reference = None
    if audio_data is not None:
        audio_filename = f"{st.session_state.reviewer_id}_{form['output_id']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
        metadata = {
            "reviewer_id": st.session_state.reviewer_id,
            "output_id": form['output_id'],
            "visit_id": visit_id,
            "model": form['model'],
            "timestamp": datetime.now().isoformat()
        }
        audio_reference = save_audio_file(audio_data.getvalue(), audio_filename, metadata)

    # 2. Construct review dict
    review = {
        "reviewer_id": st.session_state.reviewer_id,
        "clinician_profile": st.session_state.clinician_profile,
        "output_id": form['output_id'],
        "visit_id": visit_id,
        "model": form['model'],
        "approach": "Zero-Shot" if form['output_id'].endswith("_A") else "Agentic" if form['output_id'].endswith("_B") else "Unknown",
        "timestamp": datetime.now().isoformat(),
        # Use session state directly as the widgets update them
        "trust": st.session_state.trust,
        "factuality": st.session_state.factuality,
        "relevance": st.session_state.relevance,
        "justification": st.session_state.justification,
        "chart_comprehensibility": st.session_state.chart_comprehensibility,
        "utility": st.session_state.utility, # Added utility map
        "comments": st.session_state.comments if st.session_state.comments else None,
        "audio_file": audio_reference
    }
    
    # 3. Save & Advance
    st.session_state.reviews.append(review)
    save_review(review)
    st.session_state.current_idx += 1
    st.session_state.audio_key += 1
    
    # Reset form state for next case
    for k in ['trust', 'factuality', 'relevance', 'justification', 'chart_comprehensibility']:
        st.session_state[k] = None
    
    st.session_state.utility = 3 # Reset to neutral
    st.session_state.comments = "" # Reset comments

    # 4. Save Session
    save_persisted_session(st.session_state.reviewer_id)

    # Trigger success toast for next render
    st.session_state.show_success_toast = True
    st.session_state.unlock_time = None # Reset timer lock if used, though logic handles it via last_idx
