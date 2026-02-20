from pathlib import Path

# Project root (rag/)
BASE_DIR = Path(__file__).resolve().parent.parent

# RAG paths
DOCS_PATH = BASE_DIR / "backend" / "rag" / "docs"
FAISS_PATH = BASE_DIR / "faiss_index"

# Ollama config
OLLAMA_MODEL = "qwen2.5:7b"
OLLAMA_URL = "http://localhost:11434"