from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

from backend.config import FAISS_PATH
from backend.rag.loaders import load_document

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

def ingest_uploaded_file(file_path: str):
    docs = load_document(file_path)
    docs = splitter.split_documents(docs)

    try:
        db = FAISS.load_local(
            FAISS_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )
        db.add_documents(docs)
    except Exception:
        db = FAISS.from_documents(docs, embeddings)

    db.save_local(FAISS_PATH)