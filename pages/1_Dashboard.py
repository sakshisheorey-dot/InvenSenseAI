import streamlit as st
import pandas as pd
import plotly.express as px
from utils.sidebar import render_sidebar

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="🏠",
    layout="wide"
)

render_sidebar()

# ==================================
# CUSTOM CSS
# ==================================

st.markdown("""
<style>

.kpi-card{
    background:#161B22;
    padding:20px;
    border-radius:15px;
    text-align:center;
    border:1px solid #30363D;
}

.kpi-value{
    font-size:32px;
    font-weight:700;
    color:#D4AF37;
}

.kpi-label{
    color:#B8B8B8;
    font-size:15px;
}

.ai-box{
    background:#13293D;
    padding:20px;
    border-radius:15px;
    margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)

# ==================================
# HEADER
# ==================================

st.title("🏠 Executive Dashboard")

st.markdown(
"""
Real-time inventory intelligence and AI-driven business insights.
"""
)

st.write("")

# ==================================
# KPI DATA
# ==================================

inventory_value = "$1.24M"
healthy_products = 1248
watch_products = 318
at_risk_products = 92
profit_recovery = "$186K"
margin_saved = "18.7%"

# ==================================
# KPI ROW
# ==================================

c1,c2,c3,c4,c5,c6 = st.columns(6)

cards = [
    ("Total Inventory Value", inventory_value),
    ("Healthy Products", healthy_products),
    ("Watch List", watch_products),
    ("At Risk", at_risk_products),
    ("Profit Recovery", profit_recovery),
    ("Margin Saved", margin_saved)
]

for col,(label,value) in zip(
    [c1,c2,c3,c4,c5,c6],
    cards
):
    with col:
        st.markdown(
            f"""
            <div class='kpi-card'>
                <div class='kpi-value'>{value}</div>
                <div class='kpi-label'>{label}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.write("")
st.write("")

# ==================================
# CHART DATA
# ==================================

health_df = pd.DataFrame({
    "Status":[
        "Healthy",
        "Watch",
        "At Risk"
    ],
    "Products":[
        1248,
        318,
        92
    ]
})

risk_df = pd.DataFrame({
    "Category":[
        "Dresses",
        "Shirts",
        "Jackets",
        "Denim",
        "Footwear"
    ],
    "Risk Score":[
        45,
        60,
        82,
        28,
        55
    ]
})

sales_df = pd.DataFrame({
    "Week":[
        "W1",
        "W2",
        "W3",
        "W4",
        "W5",
        "W6"
    ],
    "Sales":[
        12000,
        14500,
        13800,
        16000,
        17500,
        19000
    ]
})

distribution_df = pd.DataFrame({
    "Category":[
        "Dresses",
        "Shirts",
        "Jackets",
        "Denim",
        "Footwear"
    ],
    "Inventory":[
        340,
        290,
        220,
        180,
        260
    ]
})

# ==================================
# CHARTS
# ==================================

left,right = st.columns(2)

with left:

    pie = px.pie(
        health_df,
        names="Status",
        values="Products",
        title="Inventory Health Distribution"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

with right:

    bar = px.bar(
        risk_df,
        x="Category",
        y="Risk Score",
        title="Category Risk Analysis"
    )

    st.plotly_chart(
        bar,
        use_container_width=True
    )

# ==================================
# SECOND ROW
# ==================================

left,right = st.columns(2)

with left:

    line = px.line(
        sales_df,
        x="Week",
        y="Sales",
        markers=True,
        title="Weekly Sales Trend"
    )

    st.plotly_chart(
        line,
        use_container_width=True
    )

with right:

    donut = px.pie(
        distribution_df,
        names="Category",
        values="Inventory",
        hole=0.5,
        title="Inventory Distribution"
    )

    st.plotly_chart(
        donut,
        use_container_width=True
    )

# ==================================
# AI INSIGHTS
# ==================================

st.subheader("🤖 AI Insights")

st.markdown(
"""
<div class='ai-box'>
⚠ Jackets category shows high inventory accumulation and declining demand.
<br><br>
Suggested markdown: 25%
<br>
Potential recovery: $42,000
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class='ai-box'>
📈 Denim products are outperforming forecast by 18%.
<br><br>
Recommended action:
Increase replenishment planning.
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class='ai-box'>
🚨 92 products classified as At-Risk.
<br><br>
Immediate intervention recommended.
</div>
""",
unsafe_allow_html=True
)


