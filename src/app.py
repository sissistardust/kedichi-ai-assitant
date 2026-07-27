import streamlit as st

st.set_page_config(
    page_title="Dedè - Kedichi AI Assistant",
    page_icon="🐱",
)

st.title("🐱 Dedè - Kedichi AI Assistant")

st.write(
    "Welcome! I'm Dedè, the AI assistant for Kedichi."
)

user_question = st.text_input(
    "Ask me a question about Kedichi:"
)

if user_question:
    st.info("The AI response will appear here soon.")
