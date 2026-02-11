import streamlit as st

st.set_page_config(
    page_title="DataOrbis Metrics Assistant",
    page_icon="📊",
    layout="centered"
)

st.title("📊 DataOrbis Metrics Assistant")
st.caption("Internal Tool – Sales & Distribution KPI Calculator")

st.divider()

mode = st.radio(
    "Select Mode",
    ["Explain a Metric", "Calculate with My Numbers"]
)


# 🔹 Import logic
from parser import extract_number_roles, detect_metric
from calculations import (
    numeric_distribution,
    market_share,
    contribution,
    growth
)

def metric_guide(metric):

    guides = {

        "numeric_distribution": {
            "title": "Numeric Distribution",
            "formula": "Numeric Distribution (%) = (Number of stores stocking ÷ Total stores) × 100",
            "example": {"stocking_stores": 120, "total_stores": 400},
            "explanation": "Numeric Distribution measures product reach across stores."
        },

        "growth": {
            "title": "Growth (Year-on-Year)",
            "formula": "Growth (%) = ((Current - Previous) ÷ Previous) × 100",
            "example": {"current": 100000, "previous": 80000},
            "explanation": "Growth shows percentage increase or decrease versus prior period."
        },

        "contribution": {
            "title": "Contribution",
            "formula": "Contribution (%) = (Product Sales ÷ Total Category Sales) × 100",
            "example": {"product_sales": 50000, "category_sales": 200000},
            "explanation": "Contribution measures how much a product contributes to the total category."
        }
    }

    return guides.get(metric, None)
def generate_metric_response(metric):

    guide = metric_guide(metric)

    if not guide:
        return None

    title = guide["title"]
    formula = guide["formula"]
    explanation = guide["explanation"]
    example = guide["example"]

    if metric == "numeric_distribution":
        result = (example["stocking_stores"] / example["total_stores"]) * 100
        calculation = f"(120 ÷ 400) × 100 = {result:.2f}%"

    elif metric == "growth":
        result = ((example["current"] - example["previous"]) / example["previous"]) * 100
        calculation = f"((100,000 - 80,000) ÷ 80,000) × 100 = {result:.2f}%"

    elif metric == "contribution":
        result = (example["product_sales"] / example["category_sales"]) * 100
        calculation = f"(50,000 ÷ 200,000) × 100 = {result:.2f}%"

    else:
        return None

    return f"""
### 📊 {title}

**Formula:**  
{formula}

**Example Calculation:**  
{calculation}

**Explanation:**  
{explanation}
"""
# =========================================================
# 🧠 NATURAL LANGUAGE INPUT
# =========================================================
st.subheader("🧠 Ask in Plain English")

user_question = st.text_input(
    "Examples: \n"
    "- How to calculate year on year growth\n"
    "- Calculate numeric distribution if 120 stores stock out of 400\n"
    "- What is contribution?\n"
)


result = None  # shared result container

if user_question:

    metric = detect_metric(user_question)
    roles = extract_number_roles(user_question)

    # 1️⃣ If user only wants explanation (no numbers provided)
    if metric and not roles:
        explanation = generate_metric_response(
            metric.lower().replace(" ", "_")
        )
        st.markdown(explanation)

    # 2️⃣ If user provided numbers
    elif metric == "Growth" and "current" in roles and "previous" in roles:
        result = growth(roles["current"], roles["previous"])

    elif metric == "Numeric Distribution" and "stocking" in roles and "total_stores" in roles:
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

    else:
        st.warning("I understood the metric, but not all required values.")





