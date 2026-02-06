if submit and question.strip():
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                MAKE_WEBHOOK_URL,
                json={"question": question},
                timeout=90
            )

            st.write("Status code:", response.status_code)
            st.write("Raw response text:")
            st.write(response.text)

            # Try JSON parsing explicitly
            try:
                data = response.json()
                st.success("Parsed JSON:")
                st.write(data)
                st.markdown(data.get("answer", "No answer key found"))
            except Exception as e:
                st.error("JSON parsing failed")
                st.write(str(e))

        except Exception as e:
            st.error("Request failed")
            st.write(str(e))

        except Exception:
            st.error("Unable to reach the service. Please try again later.")
