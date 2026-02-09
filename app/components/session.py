
import streamlit as st
import certifi
import pymongo
from pymongo.server_api import ServerApi
import datetime

# =========================
# CONSTANTS
# =========================

SESSION_SCHEMA_VERSION = 1
SESSION_TTL_DAYS = 30
COOKIE_NAME = "reviewer_id"

PERSIST_KEYS = [
    "current_idx",
    "last_idx",
    "audio_key",
    "unlock_time",
    "trust",
    "factuality",
    "relevance",
    "justification",
    "chart_comprehensibility",
    "utility",
    "comments",
    "language",
    "tutorial_completed",
    # Note: 'audio_file' is handled dynamically
]

# =========================
# MONGODB CONNECTION
# =========================

@st.cache_resource
def init_connection():
    """Initialize MongoDB connection with caching."""
    try:
        # Check if secrets are available
        if "mongo" not in st.secrets:
            return None
        return pymongo.MongoClient(
            st.secrets["mongo"]["connection_string"],
            tls=True,
            tlsAllowInvalidCertificates=True,
            server_api=ServerApi('1')
        )
    except Exception as e:
        print(f"MongoDB Connection Error: {e}")
        return None

def get_collection(name: str):
    """Get collection with environment suffix."""
    client = init_connection()
    if not client:
        return None
        
    db = client["agent_pulse"]
    env = st.secrets.get("env", {}).get("type", "dev")
    return db[f"{name}_{env}"]

def get_session_collection():
    return get_collection("session_state")

# =========================
# STATE MANAGEMENT
# =========================

def init_session_state():
    """Initialize session state defaults."""
    if st.session_state.get("_initialized"):
        return

    st.session_state._initialized = True

    # Defaults
    st.session_state.setdefault('reviewer_id', "")
    st.session_state.setdefault('current_idx', 0)
    st.session_state.setdefault('audio_key', 0)
    st.session_state.setdefault('unlock_time', None)
    st.session_state.setdefault('last_idx', -1)
    st.session_state.setdefault('reviews', [])
    st.session_state.setdefault('review_forms', None)
    st.session_state.setdefault('clinician_profile', None)
    st.session_state.setdefault('cookies_loaded', False)
    st.session_state.setdefault('identity_locked', False)
    st.session_state.setdefault('_session_restored', False)
    st.session_state.setdefault('show_success_toast', False)
    st.session_state.setdefault('tutorial_completed', False)

    for k in PERSIST_KEYS:
        st.session_state.setdefault(k, None)

def load_persisted_session(reviewer_id: str):
    """Fetch the last known state from MongoDB for this user."""
    coll = get_session_collection()
    if coll is None:
        return None
    doc = coll.find_one({"_id": reviewer_id})
    if not doc:
        return None
    if doc.get("schema_version") != SESSION_SCHEMA_VERSION:
        return None
    return doc

def save_persisted_session(reviewer_id: str):
    """Push the current session state to MongoDB."""
    coll = get_session_collection()
    if coll is None:
        return

    snapshot = {k: st.session_state.get(k) for k in PERSIST_KEYS}

    coll.update_one(
        {"_id": reviewer_id},
        {
            "$set": {
                "schema_version": SESSION_SCHEMA_VERSION,
                "state": snapshot,
                "updated_at": datetime.datetime.now(datetime.UTC),
            }
        },
        upsert=True,
    )

def autosave():
    """Callback for widget on_change events. Saves immediately to DB."""
    if not st.session_state.reviewer_id:
        return
    save_persisted_session(st.session_state.reviewer_id)
