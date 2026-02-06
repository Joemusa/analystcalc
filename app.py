import streamlit as st
import requests
import os

# -----------------------------
# CONFIG
# -----------------------------
MAKE_WEBHOOK_URL = os.getenv("MAKE_WEBHOOK_URL")

st.set_page_config(
    page_title="Analytics Calculation Assistant",
    layout="centered"
)

# -----------------------------
# UI
# -----------------------------
st.title("📊 Analytics Calculation Assistant")

st.write(
    "Ask how to calculate analytics metrics like contribution, "
    "numeric distribution, growth, etc."
)

question = st.text_input(
    "Enter your question",
    placeholder="e.g. How do I calculate numeric distribution?"
)

submit = st.button("Get Answer")

# -----------------------------
# LOGIC
# -----------------------------
if submit:
    if not question.strip():
        st.warning("Please enter a question.")
    elif not MAKE_WEBHOOK_URL:
        st.error("Webhook URL is not configured.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    MAKE_WEBHOOK_URL,
                    json={"question": question},
                    timeout=90  # important for Make + AI
                )

                # Check HTTP status
                if response.status_code != 200:
                    st.error(f"Request failed with status {response.status_code}")
                    st.write(response.text)
                else:
                    # Parse JSON safely
                    try:
                        data = response.json()
                        answer = data.get("answer")

                        if answer:
                            st.markdown(answer)
                        else:
                            st.warning("No answer returned from the service.")
                            st.write(data)

                    except Exception as json_error:
                        st.error("Failed to parse JSON response.")
                        st.write("Raw response:")
                        st.write(response.text)
                        st.write(json_error)

            except Exception as request_error:
                st.error("Unable to reach the service.")
                st.write(request_error)
