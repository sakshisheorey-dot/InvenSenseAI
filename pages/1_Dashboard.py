import streamlit as st
from utils.sidebar import render_sidebar

st.set_page_config(
    page_title="Dashboard",
    page_icon="🏠",
    layout="wide"
)

render_sidebar()

st.title("🏠 Executive Dashboard")

st.info(
"""
Dashboard UI will be built in Part 3.

This page will contain:

• KPI Cards
• Inventory Health Pie Chart
• Weekly Sales Trend
• Risk Analysis
• AI Insights Panel
"""
)


