from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    Docx2txtLoader,
)
from pathlib import Path

def load_document(file_path: str):
    ext = Path(file_path).suffix.lower()

    if ext == ".txt":
        return TextLoader(file_path).load()

    if ext == ".pdf":
        return PyPDFLoader(file_path).load()

    if ext == ".docx":
        return Docx2txtLoader(file_path).load()

    raise ValueError("Unsupported file type")