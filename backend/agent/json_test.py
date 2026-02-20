from langchain_ollama import ChatOllama
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

from backend.agent.schemas import AgentResponse

parser = PydanticOutputParser(pydantic_object=AgentResponse)

format_instructions = parser.get_format_instructions()

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a strict JSON API.\n"
        "You must output EXACTLY the JSON schema below.\n"
        "Do not add or remove fields.\n"
        "Do not rename fields.\n"
        "{format_instructions}"
    ),
    ("human", "Explain what FastAPI is.")
])

llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0
)

chain = prompt | llm | parser

result = chain.invoke({"format_instructions": format_instructions})
print(result)