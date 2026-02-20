from langchain_core.prompts import PromptTemplate
from backend.agent.schemas import AgentResponse

def get_prompt(parser):
    return PromptTemplate(
        template="""
You are an AI agent.

Answer the question ONLY using the provided context.

You MUST return your answer strictly in the JSON format below.
Do NOT add extra keys.
Do NOT change field names.
Do NOT return explanations outside JSON.

{format_instructions}

Question:
{question}

Context:
{context}
""",
        input_variables=["question", "context"],
        partial_variables={
            "format_instructions": parser.get_format_instructions()
        },
    )