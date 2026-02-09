import streamlit as st

# 🔹 Import logic
from parser import extract_number_roles, detect_metric
from calculations import (
    numeric_distribution,
    market_share,
    contribution,
    growth
)

# 🔹 Page setup
st.set_page_config(page_title="Calculation Engine", layout="centered")
st.title("📊 Calculation Engine")

# =========================================================
# 🧠 NATURAL LANGUAGE INPUT (THIS IS THE NEW PART)
# =========================================================
st.subheader("🧠 Ask in plain English")

user_question = st.text_input(
    "Example: Calculate numeric distribution if 120 stores stock the product out of 400"
)

result = None  # shared result container

if user_question:
    metric = detect_metric(user_question)
    roles = extract_number_roles(user_question)

    if metric == "Numeric Distribution" and "stocking" in roles and "total_stores" in roles:
        result = numeric_distribution(
            roles["stocking"],
            roles["total_stores"]
        )

    elif metric == "Market Share" and "brand_sales" in roles and "market_sales" in roles:
        result = market_share(
            roles["brand_sales"],
            roles["market_sales"]
        )

    elif metric == "Contribution" and len(roles) >= 2:
        values = list(roles.values())
        result = contribution(values[0], values[1])

    elif metric == "Growth" and "current" in roles and "previous" in roles:
        result = growth(
            roles["current"],
            roles["previous"]
        )

    else:
        st.warning("I understood the metric, but not all required values.")


# =========================================================
# 🔹 MANUAL DROPDOWN UI (EXISTING PART)
# =========================================================
st.divider()
st.subheader("🔢 Or calculate manually")

metric_choice = st.selectbox(
    "Choose a metric",
    [
        "Numeric Distribution",
        "Market Share",
        "Contribution",
        "Growth"
    ]
)

if metric_choice == "Numeric Distribution":
    a = st.number_input("Stores stocking the product", min_value=0)
    b = st.number_input("Total stores", min_value=0)
    if st.button("Calculate", key="nd"):
        result = numeric_distribution(a, b)

elif metric_choice == "Market Share":
    a = st.number_input("Brand sales", min_value=0.0)
    b = st.number_input("Total market sales", min_value=0.0)
    if st.button("Calculate", key="ms"):
        result = market_share(a, b)

elif metric_choice == "Contribution":
    a = st.number_input("Part value", min_value=0.0)
    b = st.number_input("Total value", min_value=0.0)
    if st.button("Calculate", key="contrib"):
        result = contribution(a, b)

elif metric_choice == "Growth":
    a = st.number_input("Current value", min_value=0.0)
    b = st.number_input("Previous value", min_value=0.0)
    if st.button("Calculate", key="growth"):
        result = growth(a, b)

# =========================================================
# 🔹 RESULT DISPLAY (SHARED)
# =========================================================
if result:
    st.divider()
    st.subheader(result["metric"])
    st.write("**Formula:**", result["formula"])
    st.write("**Calculation:**", result["calculation"])
    st.success(f"Result: {result['result']} {result['unit']}")

