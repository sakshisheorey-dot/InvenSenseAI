import streamlit as st
from utils.sidebar import render_sidebar

st.set_page_config(
    page_title="Inventory Management",
    page_icon="📦",
    layout="wide"
)

render_sidebar()

st.title("📦 Inventory Management")

st.info(
"""
Inventory Management Module

Coming Soon:

• Excel Upload
• CSV Upload
• Search
• Filters
• Interactive Table
• Export Functionality
"""
)

