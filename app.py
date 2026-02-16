st.write(os.listdir())


import streamlit as st
import pandas as pd
from openai import OpenAI
import os

# ================================
# PAGE CONFIG
# ================================
st.set_page_config(
    page_title="DataOrbis Internal KPI Assistant",
    page_icon="📊",
    layout="centered"
)

st.title("📊 DataOrbis Internal KPI Assistant")
st.caption("Sales & Distribution Metrics Knowledge Tool")
st.divider()

# ================================
# LOAD KPI LIBRARY
# ================================
kpi_df = pd.read_excel("kpi_library.xlsx", sheet_name="KPIs")

# ================================
# KPI DETECTION FUNCTION
# ================================
def detect_kpi(question, kpi_df):
    question = question.lower()

    for _, row in kpi_df.iterrows():
        keywords = str(row["keywords"]).lower().split(",")
        for keyword in keywords:
            if keyword.strip() in question:
                return row

    return None

# ================================
# AI EXPLANATION FUNCTION
# ================================
client = OpenAI()

def generate_ai_explanation(kpi_row):

    prompt = f"""
    Explain the KPI below in simple business terms.

    KPI: {kpi_row['kpi_name']}
    Formula: {kpi_row['formula']}
    Description: {kpi_row['description']}

    Explain:
    1. What it measures
    2. Why it matters
    3. When to use it
    Keep it professional and under 150 words.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional BI analyst explaining KPIs."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


# ================================
# NATURAL LANGUAGE INPUT
# ================================
st.subheader("🧠 Ask in plain English")

user_question = st.text_input(
    "Example: How to calculate weighted distribution?"
)

if user_question:

    kpi_row = detect_kpi(user_question, kpi_df)

    if kpi_row is not None:

        st.divider()
        st.subheader(f"📊 {kpi_row['kpi_name']}")

        st.markdown("### 📐 Formula")
        st.info(kpi_row["formula"])

        st.markdown("### 🧮 Example Calculation")
        st.write(kpi_row["example_calculation"])

        st.markdown("### 📊 Unit")
        st.write(kpi_row["unit"])

        # AI Explanation
        st.markdown("### 🧠 Business Explanation")
        explanation = generate_ai_explanation(kpi_row)
        st.write(explanation)

        # Optional Screenshot (if column exists)
        if "image_path" in kpi_row and pd.notna(kpi_row["image_path"]):
            with st.expander("📷 View BI System Logic"):
                st.image(kpi_row["image_path"], use_container_width=True)

    else:
        st.warning("KPI not recognised. Please check your wording.")




