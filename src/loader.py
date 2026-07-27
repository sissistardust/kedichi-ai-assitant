from pathlib import Path

from langchain_community.document_loaders import TextLoader


KNOWLEDGE_FOLDER = Path("knowledge")


def load_documents():
    documents = []

    if not KNOWLEDGE_FOLDER.exists():
        return documents

    for md_file in KNOWLEDGE_FOLDER.glob("*.md"):
        loader = TextLoader(str(md_file), encoding="utf-8")
        documents.extend(loader.load())

    return documents
