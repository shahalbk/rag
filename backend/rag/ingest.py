import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from backend.config import DOCS_PATH, FAISS_PATH
from backend.rag.loaders import load_document


# ----------------------------
# Embeddings
# ----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ----------------------------
# Load documents
# ----------------------------
documents = []

for file in os.listdir(DOCS_PATH):
    file_path = os.path.join(DOCS_PATH, file)

    if file.endswith((".txt", ".pdf", ".docx")):
        documents.extend(load_document(file_path))

# ----------------------------
# Split documents
# ----------------------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

# ----------------------------
# Create FAISS index (fresh)
# ----------------------------
db = FAISS.from_documents(docs, embeddings)
db.save_local(FAISS_PATH)

print("FAISS index created from documents folder.")