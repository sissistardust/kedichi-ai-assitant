from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


KNOWLEDGE_FOLDER = Path("knowledge")


def load_documents():
    documents = []

    if not KNOWLEDGE_FOLDER.exists():
        return documents

    for pdf_file in KNOWLEDGE_FOLDER.glob("*.pdf"):
        loader = PyPDFLoader(str(pdf_file))
        documents.extend(loader.load())

    return documents
