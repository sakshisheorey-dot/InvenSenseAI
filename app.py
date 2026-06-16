import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="InvenSense AI",
    page_icon="📦",
    layout="wide"
)

# =====================================
# LOAD CSS
# =====================================

def load_css():
    with open("assets/styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# =====================================
# NAVBAR
# =====================================

st.markdown("""
<div class="navbar">
    <div class="logo">InvenSense AI</div>
    <div class="nav-links">
        <span>Features</span>
        <span>Pricing</span>
        <span>About</span>
        <span>Contact</span>
        <span>Sign In</span>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# HERO
# =====================================

st.markdown("""
<div class="hero">

<div class="hero-badge">
🚀 AI Powered Inventory Intelligence
</div>

<div class="hero-title">
Reduce Dead Stock.<br>
Recover Lost Profit.
</div>

<div class="hero-subtitle">
InvenSense AI helps fashion retailers identify
slow-moving inventory, predict stock risks,
and maximize profit recovery through intelligent
markdown recommendations.
</div>

</div>
""", unsafe_allow_html=True)

# =====================================
# CTA BUTTONS
# =====================================

c1,c2,c3 = st.columns([2,2,2])

with c2:
    st.button(
        "🚀 Start Free Analysis",
        use_container_width=True
    )

st.write("")

c1,c2,c3 = st.columns([2,2,2])

with c2:
    st.button(
        "📅 Book a Demo",
        use_container_width=True
    )

# =====================================
# FEATURES
# =====================================

st.markdown(
"""
<div class="section-title">
Powerful Features
</div>
""",
unsafe_allow_html=True
)

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📦</div>
        <div class="feature-title">
        Inventory Health Tracking
        </div>
        <div class="feature-text">
        Monitor inventory risk levels,
        identify overstock situations,
        and prevent dead stock.
        </div>
    </div>
    """,
    unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">
        AI Recommendations
        </div>
        <div class="feature-text">
        Receive intelligent markdown
        suggestions to maximize
        revenue recovery.
        </div>
    </div>
    """,
    unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">
        Advanced Analytics
        </div>
        <div class="feature-text">
        Explore trends, demand forecasts,
        and inventory performance
        with interactive dashboards.
        </div>
    </div>
    """,
    unsafe_allow_html=True)

# =====================================
# STATS SECTION
# =====================================

st.write("")
st.write("")

st.markdown("""
<div class="stats-section">

<center>

<h1>Trusted by Retailers Worldwide</h1>

</center>

</div>
""",
unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("Products Analyzed", "1.2M+")

with c2:
    st.metric("Profit Recovered", "$12M+")

with c3:
    st.metric("Inventory Optimized", "95%")

with c4:
    st.metric("Retail Partners", "500+")

# =====================================
# WHY INVENTSENSE
# =====================================

st.markdown(
"""
<div class="section-title">
Why InvenSense AI?
</div>
""",
unsafe_allow_html=True
)

left,right = st.columns([1,1])

with left:
    st.success("✔ Reduce inventory holding costs")
    st.success("✔ Improve inventory turnover")
    st.success("✔ Increase margin recovery")
    st.success("✔ Prevent dead stock accumulation")

with right:
    st.info("📈 Predict demand trends")
    st.info("📉 Simulate markdown strategies")
    st.info("📦 Track inventory health")
    st.info("🤖 AI-powered business insights")

# =====================================
# FOOTER
# =====================================

st.markdown("""
<div class="footer">

<h3>InvenSense AI</h3>

Helping retailers transform inventory
into profit using artificial intelligence.

support@invensense.ai

© 2026 InvenSense AI

</div>
""",
unsafe_allow_html=True)