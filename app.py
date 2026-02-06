import streamlit as st
import requests
import os

# -----------------------------
# CONFIG
st.write("Webhook URL loaded:", https://hook.eu2.make.com/lbeu75blbrpwphhvm8un8pe36mam2xp3
)

# -----------------------------
st.write("Webhook URL loaded:", MAKE_WEBHOOK_URL)


st.set_page_config(page_title="Analytics Calculation Assistant")

# -----------------------------
# UI
# -----------------------------
st.title("📊 Analytics Calculation Assistant")

st.write("Ask how to calculate analytics metrics like contribution, distribution, growth, etc.")

question = st.text_input(
    "Enter your question",
    placeholder="e.g. How do I calculate numeric distribution?"
)

submit = st.button("Get Answer")

# -----------------------------
# LOGIC
# -----------------------------
if submit and question.strip():
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                MAKE_WEBHOOK_URL,
                json={"question": question},
                timeout=30
            )

            if response.status_code == 200:
                data = response.json()
                st.success("Answer")
                st.markdown(data.get("answer", "No answer returned."))
            else:
                st.error("Error communicating with the calculation service.")

        except Exception:
            st.error("Unable to reach the service. Please try again later.")
