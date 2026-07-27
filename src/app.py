import streamlit as st
from langchain_openai import ChatOpenAI

from config import OPENAI_API_KEY, OPENAI_MODEL
from rag import create_vector_store

st.set_page_config(
    page_title="Dedè - Kedichi AI Assistant",
    page_icon="🐱",
)

st.title("🐱 Dedè - Kedichi AI Assistant")

st.write(
    "Welcome! I'm Dedè, your AI assistant for Kedichi."
)

if not OPENAI_API_KEY:
    st.error("OpenAI API key not found.")
    st.stop()

vector_store = create_vector_store()

question = st.text_input("Ask a question about Kedichi:")

if question:
    if vector_store is None:
        st.warning("No PDF documents were found in the knowledge folder.")
    else:
        docs = vector_store.similarity_search(question, k=3)

        context = "\n\n".join(doc.page_content for doc in docs)

        llm = ChatOpenAI(
            api_key=OPENAI_API_KEY,
            model=OPENAI_MODEL,
            temperature=0,
        )

        prompt = f"""
You are Dedè, the AI assistant for Kedichi.

Answer the user's question using ONLY the information below.

Context:
{context}

Question:
{question}
"""

        response = llm.invoke(prompt)

        st.subheader("Answer")
        st.write(response.content)
