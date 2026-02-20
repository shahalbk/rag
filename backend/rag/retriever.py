from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from backend.config import FAISS_PATH

# ---------------------------------
# Embeddings (MUST match ingest.py)
# ---------------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------------------------------
# Load FAISS index
# ---------------------------------
db = FAISS.load_local(
    FAISS_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)

# ---------------------------------
# Retrieval with similarity scores
# Returns: List[(Document, score)]
# Lower score = more relevant
# ---------------------------------
def retrieve(query: str, k: int = 3):
    """
    Retrieve top-k documents with similarity scores.

    Returns:
        List of (Document, score)
    """
    return db.similarity_search_with_score(query, k=k)