import streamlit as st
import google.generativeai as genai



genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Chat with Gemini ✨")

# Get user input
prompt = st.chat_input("Say something to Gemini...")

# If user enters a prompt
if prompt:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            response = st.session_state.chat.send_message(prompt)
            reply = response.text
        except Exception as e:
            reply = "⚠️ Error: " + str(e)

        message_placeholder.markdown(reply)

        # Save model reply
        st.session_state.messages.append({"role": "assistant", "content": reply})
