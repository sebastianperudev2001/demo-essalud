import streamlit as st
import requests

st.title("Demo Essalud")

# Input field for user question
user_input = st.text_input("Pregunta algo")

# Button to submit the question
submit_button = st.button("Submit")

if submit_button and user_input:
    # Define API endpoint URL
    url = "https://wmkqh5kxqc.execute-api.us-east-1.amazonaws.com/dev"

    # Send POST request with user question
    params = {
        "prompt": user_input  # Replace with your prompt value
    }
    response = requests.get(url, params=params)

    # Parse JSON response
    if response.status_code == 200:
        bedrock_response = response.json().get("body")
        st.text_area("Chatbot Response:", value=bedrock_response, height=200, max_chars=None, key=None)
    else:
        st.error("Error: Failed to get response from API")
