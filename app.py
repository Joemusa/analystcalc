import streamlit as st

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
if metric and not roles:
    explanation = generate_metric_response(metric.lower().replace(" ", "_"))
    if explanation:
        st.markdown(explanation)





