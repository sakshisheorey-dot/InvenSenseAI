import streamlit as st

def sidebar():

    with st.sidebar:

        st.markdown("# 📦 InvenSense AI")

        st.markdown("---")

        st.page_link(
            "pages/dashboard.py",
            label="🏠 Dashboard"
        )

        st.page_link(
            "pages/inventory.py",
            label="📦 Inventory"
        )

        st.page_link(
            "pages/health.py",
            label="❤️ Health Tracker"
        )

        st.page_link(
            "pages/recommendations.py",
            label="🤖 AI Recommendations"
        )

        st.page_link(
            "pages/markdown.py",
            label="📉 Markdown Simulator"
        )

        st.page_link(
            "pages/analytics.py",
            label="📊 Analytics"
        )

        st.page_link(
            "pages/reports.py",
            label="📄 Reports"
        )

        st.page_link(
            "pages/settings.py",
            label="⚙️ Settings"
        )

        st.markdown("---")

        if st.button("🚪 Logout"):

            st.session_state.logged_in = False

            st.switch_page("app.py")

