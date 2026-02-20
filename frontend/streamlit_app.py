import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="🧠 Agentic RAG System",
    layout="centered"
)

st.title("🧠 Agentic RAG System")
st.caption("Local • Offline • FAISS + Qwen3")

# ---------------------------
# 📂 Upload documents
# ---------------------------
st.subheader("📂 Upload documents")

uploaded_file = st.file_uploader(
    "Upload PDF, DOCX, or TXT",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:
    with st.spinner("Indexing document..."):
        files = {"file": uploaded_file}
        res = requests.post(f"{BACKEND_URL}/upload", files=files)

    if res.status_code == 200:
        st.success(f"Indexed: {uploaded_file.name}")
    else:
        st.error("Upload failed")

# ---------------------------
# ❓ Ask a question
# ---------------------------
st.subheader("❓ Ask a question")

question = st.text_input("Enter your question")

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            res = requests.post(
                f"{BACKEND_URL}/ask",
                json={"question": question}
            )

        if res.status_code != 200:
            st.error("Backend error")
        else:
            data = res.json()

            # ---------------------------
            # 🧠 Answer section
            # ---------------------------
            st.markdown("### 🧠 Answer")
            st.markdown(f"**{data['topic']}**")
            st.write(data["summary"])

            # ---------------------------
            # 📚 Sources
            # ---------------------------
            if data["sources"]:
                st.markdown("### 📚 Sources")
                for src in data["sources"]:
                    st.markdown(f"- `{src}`")

            # ---------------------------
            # 🛠 Tools used
            # ---------------------------
            st.markdown("### 🛠 Tools Used")
            st.write(", ".join(data["tools_used"]))