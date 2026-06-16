import streamlit as st

st.markdown("""
<style>

[data-testid="stSidebarNav"] {
    display: none;
}

</style>
""", unsafe_allow_html=True)

def render_sidebar():

    with st.sidebar:

        st.title("📦 InvenSense AI")

        st.markdown("---")

        st.page_link(
            "pages/1_Dashboard.py",
            label="🏠 Dashboard"
        )

        st.page_link(
            "pages/2_Inventory_Management.py",
            label="📦 Inventory"
        )

        st.page_link(
            "pages/3_Inventory_Health.py",
            label="❤️ Health Tracker"
        )

        st.page_link(
            "pages/4_AI_Recommendations.py",
            label="🤖 AI Recommendations"
        )

        st.page_link(
            "pages/5_Markdown_Simulator.py",
            label="📉 Markdown Simulator"
        )

        st.page_link(
            "pages/6_Analytics.py",
            label="📊 Analytics"
        )

        st.page_link(
            "pages/7_Reports.py",
            label="📄 Reports"
        )

        st.page_link(
            "pages/8_Settings.py",
            label="⚙️ Settings"
        )

