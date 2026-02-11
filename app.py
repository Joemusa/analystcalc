import streamlit as st
from parser import detect_metric, extract_number_roles
from calculations import (
    numeric_distribution,
    market_share,
    contribution,
    growth,
    weighted_distribution
)

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="DataOrbis Internal KPI Assistant",
    page_icon="📊",
    layout="centered"
)

st.title("📊 DataOrbis Internal KPI Assistant")
st.caption("Sales & Distribution Metrics Knowledge Tool")
st.divider()

# =====================================================
# METRIC GUIDE (EXPLANATION MODE)
# =====================================================

def metric_guide(metric):

    guides = {

        "Weighted Distribution": {
            "formula": "Weighted Distribution (%) = (Weighted Sales ÷ Total Weighted Sales) × 100",
            "example_calc": "(300,000 ÷ 1,000,000) × 100 = 30.00%",
            "explanation": "Weighted Distribution measures the quality of distribution. It reflects distribution weighted by store size or category sales, not just number of stores.",
            "image": "assets/weighted_distribution.png"
        },

        "Growth": {
            "formula": "Growth (%) = ((Current Period - Previous Period) ÷ Previous Period) × 100",
            "example_calc": "((120,000 - 100,000) ÷ 100,000) × 100 = 20.00%",
            "explanation": "Growth shows percentage change between two time periods.",
            "image": "assets/growth.png"
        },

        "Numeric Distribution": {
            "formula": "Numeric Distribution (%) = (Stores Stocking ÷ Total Stores) × 100",
            "example_calc": "(120 ÷ 400) × 100 = 30.00%",
            "explanation": "Numeric Distribution measures product reach across stores.",
            "image": "assets/numeric_distribution.png"
        },

        "Contribution": {
            "formula": "Contribution (%) = (Product Sales ÷ Total Category Sales) × 100",
            "example_calc": "(50,000 ÷ 200,000) × 100 = 25.00%",
            "explanation": "Contribution shows the share of a product within its category.",
            "image": "assets/contribution.png"
        }

    }

    return guides.get(metric, None)


# =====================================================
# DISPLAY FUNCTION
# =====================================================

def display_explanation(metric):

    guide = metric_guide(metric)

    if not guide:
        st.warning("Metric not recognised.")
        return

    st.subheader(f"📊 {metric}")

    st.markdown("### 📐 Formula")
    st.info(guide["formula"])

    st.markdown("### 🧮 Example Calculation")
    st.write(guide["example_calc"])

    st.markdown("### 📝 Explanation")
    st.write(guide["explanation"])

    with st.expander("📷 View BI System Logic"):
        st.image(guide["image"], use_container_width=True)


# =====================================================
# NATURAL LANGUAGE INPUT
# =====================================================

st.subheader("🧠 Ask in plain English")

user_question = st.text_input(
    "Example: How to calculate weighted distribution"
)

if user_question:

    metric = detect_metric(user_question)
    roles = extract_number_roles(user_question)

    # EXPLANATION MODE (No numbers provided)
    if metric and not roles:
        display_explanation(metric)

    # CALCULATION MODE (Numbers provided)
    elif metric and roles:

        value1 = roles.get("value1")
        value2 = roles.get("value2")

        if metric == "Weighted Distribution":
            result = weighted_distribution(value1, value2)

        elif metric == "Numeric Distribution":
            result = numeric_distribution(value1, value2)

        elif metric == "Growth":
            result = growth(value1, value2)

        elif metric == "Contribution":
            result = contribution(value1, value2)

        else:
            result = None

        if result:
            st.subheader(f"📊 {result['metric']}")
            st.markdown("### 📐 Formula")
            st.info(result["formula"])

            st.markdown("### 🧮 Calculation")
            st.write(result["calculation"])

            st.success(f"Result: {result['result']} {result['unit']}")

    else:
        st.warning("Metric recognised, but insufficient data provided.")





