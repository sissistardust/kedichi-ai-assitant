from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

from loader import load_documents
from config import OPENAI_API_KEY


def create_vector_store():
    documents = load_documents()

    if not documents:
        return None

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings(
        api_key=OPENAI_API_KEY
    )

    vector_store = FAISS.from_documents(
        chunks,
        embeddings,
    )

    return vector_store
