from parser import extract_numbers, detect_metric
from calculations import (
    numeric_distribution,
    market_share,
    contribution,
    growth
)

import streamlit as st
from calculations import (
    numeric_distribution,
    market_share,
    contribution,
    growth
)

st.set_page_config(page_title="Calculation Engine", layout="centered")
st.title("📊 Calculation Engine")

metric = st.selectbox(
    "Choose a metric",
    [
        "Numeric Distribution",
        "Market Share",
        "Contribution",
        "Growth"
    ]
)

if metric == "Numeric Distribution":
    a = st.number_input("Stores stocking the product", min_value=0)
    b = st.number_input("Total stores", min_value=0)
    if st.button("Calculate"):
        result = numeric_distribution(a, b)

elif metric == "Market Share":
    a = st.number_input("Brand sales", min_value=0.0)
    b = st.number_input("Total market sales", min_value=0.0)
    if st.button("Calculate"):
        result = market_share(a, b)

elif metric == "Contribution":
    a = st.number_input("Part value", min_value=0.0)
    b = st.number_input("Total value", min_value=0.0)
    if st.button("Calculate"):
        result = contribution(a, b)

elif metric == "Growth":
    a = st.number_input("Current value", min_value=0.0)
    b = st.number_input("Previous value", min_value=0.0)
    if st.button("Calculate"):
        result = growth(a, b)

if "result" in locals() and result:
    st.divider()
    st.subheader(result["metric"])
    st.write("**Formula:**", result["formula"])
    st.write("**Calculation:**", result["calculation"])
    st.success(f"Result: {result['result']} {result['unit']}")
