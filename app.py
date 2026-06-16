import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="InvenSense AI",
    page_icon="📦",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.stApp{
    background-color:#0B0B0B;
}

.main-title{
    font-size:70px;
    font-weight:800;
    text-align:center;
    color:white;
}

.gold{
    color:#D4AF37;
}

.subtitle{
    text-align:center;
    color:#B0B0B0;
    font-size:22px;
    max-width:900px;
    margin:auto;
}

.section-title{
    text-align:center;
    color:white;
    font-size:42px;
    font-weight:700;
    margin-top:50px;
    margin-bottom:30px;
}

.feature-card{
    background:#151515;
    padding:25px;
    border-radius:20px;
    border:1px solid #2A2A2A;
}

.metric-card{
    background:#151515;
    padding:20px;
    border-radius:20px;
    text-align:center;
}

.footer{
    text-align:center;
    color:#A0A0A0;
    margin-top:80px;
    padding:40px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# NAVBAR
# =====================================================

nav1, nav2 = st.columns([3,2])

with nav1:
    st.markdown(
        "<h1 style='color:#D4AF37;'>InvenSense AI</h1>",
        unsafe_allow_html=True
    )

with nav2:
    st.markdown(
        """
        <div style="text-align:right;padding-top:20px;color:white;">
        Features &nbsp;&nbsp;&nbsp;
        Pricing &nbsp;&nbsp;&nbsp;
        About &nbsp;&nbsp;&nbsp;
        Contact &nbsp;&nbsp;&nbsp;
        Sign In
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# =====================================================
# HERO
# =====================================================

st.markdown(
"""
<div style='text-align:center;'>

<h3 class='gold'>
AI-Powered Fashion Retail Intelligence
</h3>

<h1 class='main-title'>
Reduce Dead Stock.<br>
<span class='gold'>
Recover Lost Profit.
</span>
</h1>

<p class='subtitle'>
Transform excess inventory into opportunity using intelligent
inventory analytics, AI-powered markdown recommendations and
real-time business insights.
</p>

</div>
""",
unsafe_allow_html=True
)

st.write("")

c1,c2,c3 = st.columns([1,2,1])

with c2:
    b1,b2 = st.columns(2)

    with b1:
        st.button(
            "🚀 Start Free Analysis",
            use_container_width=True
        )

    with b2:
        st.button(
            "📅 Book Demo",
            use_container_width=True
        )

# =====================================================
# FEATURES
# =====================================================

st.markdown(
"<div class='section-title'>Powerful Features</div>",
unsafe_allow_html=True
)

f1,f2,f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class='feature-card'>
    <h2>📦</h2>
    <h3>Inventory Health Tracking</h3>

    Monitor inventory risk levels,
    identify slow-moving products,
    and prevent dead stock accumulation.
    </div>
    """,
    unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class='feature-card'>
    <h2>🤖</h2>
    <h3>AI Recommendations</h3>

    Receive intelligent markdown
    suggestions that maximize
    recovery while preserving margins.
    </div>
    """,
    unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class='feature-card'>
    <h2>📊</h2>
    <h3>Advanced Analytics</h3>

    Explore demand trends,
    inventory performance,
    and category risk analysis.
    </div>
    """,
    unsafe_allow_html=True)

# =====================================================
# PLATFORM PREVIEW
# =====================================================

st.markdown(
"<div class='section-title'>Platform Preview</div>",
unsafe_allow_html=True
)

preview1,preview2 = st.columns(2)

with preview1:
    st.info("📦 Inventory Health Tracker")
    st.info("🤖 AI Recommendations")

with preview2:
    st.info("📉 Markdown Simulator")
    st.info("📊 Analytics Dashboard")

# =====================================================
# STATS
# =====================================================

st.markdown(
"<div class='section-title'>Trusted by Retailers Worldwide</div>",
unsafe_allow_html=True
)

m1,m2,m3,m4 = st.columns(4)

m1.metric("Products Analyzed","1.2M+")
m2.metric("Profit Recovered","$12M+")
m3.metric("Inventory Optimized","95%")
m4.metric("Retail Partners","500+")

# =====================================================
# BENEFITS
# =====================================================

st.markdown(
"<div class='section-title'>Why InvenSense AI?</div>",
unsafe_allow_html=True
)

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

# =====================================================
# FOOTER
# =====================================================

st.markdown(
"""
<div class='footer'>

<h2 style='color:#D4AF37;'>
InvenSense AI
</h2>

Helping fashion retailers transform inventory
into profit using artificial intelligence.

<br><br>

support@invensense.ai

<br><br>

© 2026 InvenSense AI

</div>
""",
unsafe_allow_html=True
)


