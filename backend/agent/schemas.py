from pydantic import BaseModel
from typing import List

class AgentResponse(BaseModel):
    topic: str
    summary: str
    sources: List[str]
    tools_used: List[str]


class ToolDecision(BaseModel):
    tool: str  # "faiss" or "duckduckgo"
    reason: str