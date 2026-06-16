import streamlit as st
from utils.sidebar import render_sidebar

st.set_page_config(
    page_title="Inventory Health",
    page_icon="❤️",
    layout="wide"
)

render_sidebar()

st.title("❤️ Inventory Health Tracker")

st.info(
"""
Inventory Health Tracker

Coming Soon:

• Risk Scoring
• Health Classification
• Risk Distribution
• Category Heatmap
• Inventory Age Analysis
"""
)

