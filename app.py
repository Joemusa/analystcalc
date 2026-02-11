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

def metric_guide(metric):

    guides = {

        "numeric_distribution": {
            "title": "Numeric Distribution",
            "formula": "Numeric Distribution (%) = (Number of stores stocking the product ÷ Total stores in universe) × 100",
            "example": {
                "stocking_stores": 120,
                "total_stores": 400
            },
            "explanation": "Numeric Distribution measures how widely a product is available across the market. It tells us reach, not sales."
        },

        "growth": {
            "title": "Growth",
            "formula": "Growth (%) = ((Current Period - Previous Period) ÷ Previous Period) × 100",
            "example": {
                "current": 100000,
                "previous": 80000
            },
            "explanation": "Growth shows how much performance increased or decreased compared to the previous period."
        },

        "contribution": {
            "title": "Contribution",
            "formula": "Contribution (%) = (Product Sales ÷ Total Category Sales) × 100",
            "example": {
                "product_sales": 50000,
                "category_sales": 200000
            },
            "explanation": "Contribution shows the share of a product relative to the total category."
        }
    }

    return guides.get(metric, None)


