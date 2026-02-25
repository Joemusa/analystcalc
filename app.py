import streamlit as st
import pandas as pd
from openai import OpenAI

# ================================
# PAGE CONFIG
# ================================
st.set_page_config(
    page_title="DataOrbis Internal KPI Assistant",
    page_icon="📊",
    layout="centered"
)
st.markdown(
    "<h1 style='font-size:48px;'>📊 DataOrbis Internal KPI Assistant</h1>",
    unsafe_allow_html=True
)

st.title("📊 DataOrbis Internal KPI Assistant")
st.caption("Sales & Distribution Metrics Knowledge Tool")
st.divider()

# ================================
# LOAD KPI LIBRARY (GOOGLE SHEET)
# ================================
@st.cache_data(ttl=60)  # Refresh every 60 seconds
def load_data():
    try:
        url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT3mFh7RblUtcE32W8U1q5-RnHgSEnec06RHKJOaAt_DdwPYNxtCL0QfSJ_6ab0Pd6YLlTIxo4AT9l5/pub?output=csv"
        df = pd.read_csv(url)

        # Normalize column names (VERY IMPORTANT)
        df.columns = df.columns.str.strip().str.lower()

        return df

    except Exception as e:
        st.error("Failed to load Google Sheet.")
        st.write(e)
        return pd.DataFrame()


df = load_data()
# Stop app if sheet failed
if df.empty:
    st.stop()

# ================================
# KPI DETECTION FUNCTION
# ================================
import re

def clean_text(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', str(text).lower())

def detect_kpi(user_question, df):
    question = clean_text(user_question)

    best_match = None
    highest_score = 0

    for _, row in df.iterrows():

        combined_text = clean_text(
            f"{row.get('kpi_name', '')} "
            f"{row.get('keywords', '')} "
            f"{row.get('description', '')}"
        )

        score = 0

        # Word-level scoring
        for word in question.split():
            if word in combined_text:
                score += 2

        # Exact phrase bonus
        if question in combined_text:
            score += 5

        # Penalise wrong context (Store vs Depot)
        if "store" in question and "depot" in combined_text:
            score -= 2
        if "depot" in question and "store" in combined_text:
            score -= 2

        if score > highest_score:
            highest_score = score
            best_match = row

    if highest_score > 0:
        return best_match

    return None

# ================================
# AI EXPLANATION FUNCTION
# ================================
client = OpenAI()

def generate_ai_explanation(kpi_row):

    prompt = f"""
    Explain the KPI below in simple business terms.

    KPI: {kpi_row.get('kpi_name')}
    Formula: {kpi_row.get('formula')}
    Description: {kpi_row.get('description')}

    Explain:
    1. What it measures
    2. Why it matters
    3. When to use it

    Keep it professional and under 100 words.
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
# USER INPUT
# ================================
st.subheader("🧠 Ask in plain English")

user_question = st.text_input(
    "Example: How to calculate weighted distribution?"
)

# ================================
# KPI RESPONSE SECTION
# ================================
if user_question:

    kpi_row = detect_kpi(user_question, df)

    if kpi_row is not None and pd.notna(kpi_row.get("kpi_name")):

        st.divider()
        st.subheader(f"📊 {kpi_row.get('kpi_name')}")

        # Formula
        if pd.notna(kpi_row.get("formula")):
            st.markdown("### 📐 Formula")
            st.info(kpi_row.get("formula"))

        # Example
        if pd.notna(kpi_row.get("example_calculation")):
            st.markdown("### 🧮 Example Calculation")
            st.write(kpi_row.get("example_calculation"))

        # Unit
        if pd.notna(kpi_row.get("unit")):
            st.markdown("### 📊 Unit")
            st.write(kpi_row.get("unit"))

        # AI Explanation
        if pd.notna(kpi_row.get("description")):
            st.markdown("### 🧠 Business Explanation")
            explanation = generate_ai_explanation(kpi_row)
            st.write(explanation)

        # Path (NEW COLUMN SUPPORT)
        if "path" in df.columns:
            path_value = kpi_row.get("path")

    if pd.notna(path_value) and str(path_value).strip() != "":
        st.markdown("### 📂 Source Calculation Path")
        st.code(path_value)

        # Optional Screenshot
        if "image_path" in df.columns and pd.notna(kpi_row.get("image_path")):
            with st.expander("📷 View BI System Logic"):
                st.image(kpi_row.get("image_path"), use_container_width=True)

    else:
        st.warning("KPI not recognised. Please check your wording.")




