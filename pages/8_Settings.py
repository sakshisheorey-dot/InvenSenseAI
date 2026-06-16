import streamlit as st
from utils.sidebar import render_sidebar

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

render_sidebar()

st.title("⚙️ Settings")

st.info(
"""
Settings Module

Coming Soon:

• Company Information
• Currency Settings
• Theme Selection
• Risk Threshold Configuration
• Notification Preferences
"""
)
