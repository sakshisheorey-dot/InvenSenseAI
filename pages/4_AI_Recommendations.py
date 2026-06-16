import streamlit as st
from utils.sidebar import render_sidebar

st.set_page_config(
    page_title="AI Recommendations",
    page_icon="🤖",
    layout="wide"
)

render_sidebar()

st.title("🤖 AI Discount Recommendation Engine")

st.info(
"""
AI Recommendation Engine

Coming Soon:

• AI Markdown Suggestions
• Revenue Recovery Estimates
• Margin Preservation Analysis
• AI Explanations
"""
)

