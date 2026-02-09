import streamlit as st

# 🔹 Import logic
from parser import extract_numbers_roles, detect_metric
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
    numbers = extract_numbers(user_question)

    if metric == "Numeric Distribution" and len(numbers) >= 2:
        result = numeric_distribution(numbers[0], numbers[1])

    elif metric == "Market Share" and len(numbers) >= 2:
        result = market_share(numbers[0], numbers[1])

    elif metric == "Contribution" and len(numbers) >= 2:
        result = contribution(numbers[0], numbers[1])

    elif metric == "Growth" and len(numbers) >= 2:
        result = growth(numbers[0], numbers[1])

    else:
        st.warning("I understood the question, but I need more numbers to calculate.")

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

