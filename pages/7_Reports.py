import streamlit as st
from utils.sidebar import render_sidebar

st.set_page_config(
    page_title="Reports",
    page_icon="📄",
    layout="wide"
)

render_sidebar()

st.title("📄 Reports")

st.info(
"""
Reports Module

Coming Soon:

• Inventory Summary Report
• AI Recommendation Report
• Profit Recovery Report
• PDF Export
• Excel Export
"""
)

