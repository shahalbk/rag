from langchain_ollama import ChatOllama
from langchain_core.output_parsers import PydanticOutputParser

from backend.agent.schemas import AgentResponse
from backend.agent.prompts import get_prompt
from backend.tools.rag_search import rag_search
from backend.tools.web_search import web_search

# LLM
llm = ChatOllama(
    model="qwen3:8b",
    temperature=0
)

# Parser
parser = PydanticOutputParser(pydantic_object=AgentResponse)

# Prompt
prompt = get_prompt(parser)

def run_agent(question: str) -> AgentResponse:
    # 1️⃣ Try internal RAG first
    rag_results = rag_search(question)

    if rag_results:
        context = "\n\n".join(r["content"] for r in rag_results)

        result = (prompt | llm | parser).invoke({
            "question": question,
            "context": context
        })

        result.sources = list({r["source"] for r in rag_results})
        result.tools_used = ["faiss"]
        return result

    # 2️⃣ Fallback to web
    web_context = web_search(question)

    result = (prompt | llm | parser).invoke({
        "question": question,
        "context": web_context
    })

    result.sources = []
    result.tools_used = ["duckduckgo"]
    return result