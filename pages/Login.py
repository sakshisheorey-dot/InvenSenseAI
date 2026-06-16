import streamlit as st

if st.button("🚀 Start Free Analysis"):
    st.switch_page("pages/Login.py")

st.title("Login")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    st.switch_page(
        "pages/1_Dashboard.py"
    )
