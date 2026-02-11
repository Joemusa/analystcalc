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
# 🧠 NATURAL LANGUAGE INPUT
# =========================================================
st.subheader("🧠 Ask in plain English")

user_question = st.text_input(
    "Example: Calculate numeric distribution if 120 stores stock the product out of 400"
)

result = None

if user_question:

    metric = detect_metric(user_question)
    roles = extract_number_roles(user_question)

    # -----------------------------------------------------
    # 🔹 IF USER JUST WANTS TO KNOW HOW TO CALCULATE
    # -----------------------------------------------------
    if metric and len(roles) == 0:
        explanation = generate_metric_response(metric.lower().replace(" ", "_"))
        st.markdown(explanation)

    # -----------------------------------------------------
    # 🔹 CALCULATION MODE
    # -----------------------------------------------------
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
# 🔹 RESULT DISPLAY (ENHANCED TRAINING OUTPUT)
# =========================================================
if result:
    guide = metric_guide(result["metric"])

    st.divider()
    st.subheader(result["metric"])

    # Formula
    st.markdown("### 📐 Formula")
    st.code(guide["formula"])

    # User Calculation
    st.markdown("### 🧮 Your Calculation")
    st.write(result["calculation"])
    st.success(f"Result: {result['result']} {result['unit']}")

    # Business Explanation
    st.markdown("### 📘 Business Meaning")
    st.write(guide["explanation"])

    # Arbitrary Example
    example_a, example_b = guide["example_values"]

    if result["metric"] == "Numeric Distribution":
        example_result = (example_a / example_b) * 100
        example_calc = f"({example_a} ÷ {example_b}) × 100 = {example_result:.2f}%"

    elif result["metric"] == "Market Share":
        example_result = (example_a / example_b) * 100
        example_calc = f"({example_a} ÷ {example_b}) × 100 = {example_result:.2f}%"

    elif result["metric"] == "Contribution":
        example_result = (example_a / example_b) * 100
        example_calc = f"({example_a} ÷ {example_b}) × 100 = {example_result:.2f}%"

    elif result["metric"] == "Growth":
        example_result = ((example_a - example_b) / example_b) * 100
        example_calc = f"(({example_a} - {example_b}) ÷ {example_b}) × 100 = {example_result:.2f}%"

    st.markdown("### 🧪 Example")
    st.write(example_calc)




