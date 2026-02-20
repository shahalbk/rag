from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import UploadFile, File
import shutil
import os
from backend.rag.ingest_uploaded import ingest_uploaded_file
from backend.agent.agent import run_agent

app = FastAPI(title="Local Agentic RAG")

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
def ask(request: QueryRequest):
    result = run_agent(request.question)
    return result.dict()

UPLOAD_DIR = "uploaded_docs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    ingest_uploaded_file(file_path)

    return {"status": "uploaded and indexed", "file": file.filename}