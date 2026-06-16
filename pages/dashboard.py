import streamlit as st
from utils.sidebar import sidebar

st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

sidebar()

st.title("🏠 Executive Dashboard")

c1,c2,c3,c4,c5,c6 = st.columns(6)

c1.metric("Inventory Value", "$1.2M")
c2.metric("Healthy", "1,254")
c3.metric("Watch", "412")
c4.metric("At Risk", "87")
c5.metric("Recovery", "$220K")
c6.metric("Margin Saved", "18%")

st.markdown("---")

st.subheader("AI Insights")

st.info(
"""
Women's Winter Jackets show declining demand.
Suggested markdown: 25%
Potential recovery: $32,000
"""
)

st.info(
"""
Denim category performing above forecast.
Restocking recommended.
"""
)
