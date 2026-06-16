import streamlit as st
from utils.sidebar import render_sidebar

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

render_sidebar()

st.title("📊 Analytics Dashboard")

st.info(
"""
Analytics Module

Coming Soon:

• Sales Trends
• Demand Forecasting
• Category Performance
• Correlation Analysis
• Scatter Plots
"""
)

