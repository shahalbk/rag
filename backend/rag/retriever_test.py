from backend.rag.retriever import retrieve

docs = retrieve("leave policy")

for d in docs:
    print("-----")
    print(d.page_content)
    print(d.metadata)