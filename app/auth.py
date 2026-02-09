import streamlit as st
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

def check_password():
    """
    Returns `True` if the user had the correct password.
    Stops execution with `st.stop()` if not authenticated.
    """
    
    # Simple check if already authenticated in session
    if st.session_state.get("password_correct", False):
        return True

    # Show login form
    st.markdown("## :material/lock: Admin Access Required")
    st.info("This section is restricted to administrators.")
    
    password = st.text_input("Enter Admin Password", type="password", key="admin_password_input")
    
    if st.button("Login"):
        # Check against env var or default
        # Default is 'admin' for simplicity in this context
        # Check against secrets, env var, or default
        # Priority: secrets.toml > .env > default
        correct_password = os.getenv("ADMIN_PASSWORD", "admin")

        if "security" in st.secrets and "ADMIN_PASSWORD" in st.secrets["security"]:
             correct_password = st.secrets["security"]["ADMIN_PASSWORD"]
        
        if password == correct_password:
            st.session_state.password_correct = True
            st.rerun()
        else:
            st.error("Incorrect password")
    
    # Stop execution of the rest of the page until logged in
    st.stop()
    return False
