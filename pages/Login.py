import streamlit as st

st.set_page_config(
    page_title="InvenSense AI",
    page_icon="📦",
    layout="wide"
)

# -----------------------------
# SESSION STATE
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -----------------------------
# IF ALREADY LOGGED IN
# -----------------------------

if st.session_state.logged_in:
    st.switch_page("pages/dashboard.py")

# -----------------------------
# LOGIN PAGE
# -----------------------------

st.markdown(
"""
# InvenSense AI

### Fashion Retail Intelligence Platform
"""
)

left,right = st.columns([1,1])

with left:

    st.image(
        "https://images.unsplash.com/photo-1441986300917-64674bd600d8",
        use_container_width=True
    )

with right:

    st.markdown("## Sign In")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Login",
        use_container_width=True
    ):

        st.session_state.logged_in = True

        st.rerun()

    st.caption("Forgot Password?")

    if st.button("Demo Login"):
        st.session_state.logged_in = True
        st.rerun()
