
import streamlit as st

st.set_page_config(
    page_title="InvenSense AI",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------
# LOAD CSS
# -------------------------

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# -------------------------
# NAVBAR
# -------------------------

st.markdown("""
<div class="navbar">
    <div class="logo">
        InvenSense AI
    </div>

    <div class="nav-links">
        <span>Features</span>
        <span>Pricing</span>
        <span>About</span>
        <span>Contact</span>
        <span>Sign In</span>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------
# HERO SECTION
# -------------------------

st.markdown("""
<div class="hero">

    <div class="hero-badge">
        AI-Powered Fashion Retail Intelligence
    </div>

    <div class="hero-title">
        Reduce Dead Stock.<br>
        <span class="gold-text">
            Recover Lost Profit.
        </span>
    </div>

    <div class="hero-subtitle">
        Transform excess inventory into opportunity using
        intelligent inventory analytics, AI-powered markdown
        recommendations, and real-time business insights.
    </div>

</div>
""", unsafe_allow_html=True)

# -------------------------
# CTA BUTTONS
# -------------------------

col1,col2,col3 = st.columns([1,2,1])

with col2:

    st.markdown("""
    <div class="cta-container">

        <button class="gold-btn">
            Start Free Analysis
        </button>

        <button class="outline-btn">
            Book Demo
        </button>

    </div>
    """, unsafe_allow_html=True)

# -------------------------
# FEATURES SECTION
# -------------------------

st.markdown("""
<div class="section-heading">
Powerful Features
</div>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)

with c1:

    st.markdown("""
    <div class="feature-card">

        <div class="feature-icon">
            📦
        </div>

        <div class="feature-title">
            Inventory Health Tracking
        </div>

        <div class="feature-text">
            Monitor inventory risk levels,
            identify slow-moving products,
            and prevent dead stock accumulation.
        </div>

    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class="feature-card">

        <div class="feature-icon">
            🤖
        </div>

        <div class="feature-title">
            AI Recommendations
        </div>

        <div class="feature-text">
            Receive intelligent markdown
            suggestions that maximize
            recovery while preserving margins.
        </div>

    </div>
    """, unsafe_allow_html=True)

with c3:

    st.markdown("""
    <div class="feature-card">

        <div class="feature-icon">
            📊
        </div>

        <div class="feature-title">
            Advanced Analytics
        </div>

        <div class="feature-text">
            Explore demand trends,
            inventory performance,
            and category risk analysis.
        </div>

    </div>
    """, unsafe_allow_html=True)

# -------------------------
# PLATFORM PREVIEW
# -------------------------

st.markdown("""
<div class="section-heading">
Platform Preview
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="preview-card">

<div class="preview-grid">

<div class="preview-box">
Inventory Health
</div>

<div class="preview-box">
AI Recommendations
</div>

<div class="preview-box">
Markdown Simulator
</div>

<div class="preview-box">
Analytics
</div>

</div>

</div>
""", unsafe_allow_html=True)

# -------------------------
# STATS
# -------------------------

st.markdown("""
<div class="section-heading">
Trusted by Retailers Worldwide
</div>
""", unsafe_allow_html=True)

s1,s2,s3,s4 = st.columns(4)

with s1:
    st.metric("Products Analyzed","1.2M+")

with s2:
    st.metric("Profit Recovered","$12M+")

with s3:
    st.metric("Inventory Optimized","95%")

with s4:
    st.metric("Retail Partners","500+")

# -------------------------
# BENEFITS
# -------------------------

st.markdown("""
<div class="section-heading">
Why InvenSense AI?
</div>
""", unsafe_allow_html=True)

left,right = st.columns(2)

with left:

    st.success("Reduce inventory holding costs")
    st.success("Improve inventory turnover")
    st.success("Increase margin recovery")
    st.success("Prevent dead stock accumulation")

with right:

    st.info("Predict demand trends")
    st.info("AI-powered recommendations")
    st.info("Simulate markdown strategies")
    st.info("Real-time inventory visibility")

# -------------------------
# FOOTER
# -------------------------

st.markdown("""
<div class="footer">

<h2>InvenSense AI</h2>

<p>
Helping fashion retailers transform inventory
into profit using artificial intelligence.
</p>

<p>
support@invensense.ai
</p>

<p>
© 2026 InvenSense AI
</p>

</div>
""", unsafe_allow_html=True)
