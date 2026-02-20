from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0
)

res = llm.invoke("Reply only with OK")
print(res)