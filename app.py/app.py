import streamlit as st
from groq import Groq

st.set_page_config(page_title="JARVIS Jr AI", page_icon="🤖")
st.title("🤖 JARVIS Jr AI Assistant")

client = Groq(api_key=st.secrets["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"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask me anything...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.messages
    )

    bot_reply = response.choices[0].message.content

    st.chat_message("assistant").write(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    
