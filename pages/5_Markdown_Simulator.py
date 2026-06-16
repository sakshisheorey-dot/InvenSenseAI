import streamlit as st
from utils.sidebar import render_sidebar

st.set_page_config(
    page_title="Markdown Simulator",
    page_icon="📉",
    layout="wide"
)

render_sidebar()

st.title("📉 Markdown Simulator")

st.info(
"""
Markdown Simulation Tool

Coming Soon:

• Discount Sliders
• Revenue Forecast
• Margin Forecast
• Inventory Recovery Projection
"""
)

