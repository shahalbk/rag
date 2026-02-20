from typing import List, Dict
from backend.rag.retriever import retrieve


def rag_search(query: str, k: int = 3) -> List[Dict]:
    """
    Perform pure RAG search over internal documents.
    No LLM involved.
    """

    results = []
    docs_with_scores = retrieve(query, k=k)

    for doc, score in docs_with_scores:
        results.append(
            {
                "content": doc.page_content,
                "source": doc.metadata.get("source"),
                "score": score,
            }
        )

    return results