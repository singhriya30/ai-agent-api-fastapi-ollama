import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "http://127.0.0.1:8000/ai-agent"
API_KEY = os.getenv("API_KEY")

st.set_page_config(page_title="AI Agent Chat", layout="centered")

st.title(" AI Agent with Tools")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Ask something...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Send request to FastAPI backend
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "prompt": user_input
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        ai_reply = response.json()["response"]
    else:
        ai_reply = "Error: Unable to get response"

    # Show AI response
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    with st.chat_message("assistant"):
        st.write(ai_reply)
