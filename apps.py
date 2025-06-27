import streamlit as st
import os
from scripts.ingest import ingest_and_index
from scripts.query import query_vector_store  # renamed for clarity

st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("📚 RAG Chatbot with File Ingestion and Question Answering")

# --- File Upload Section ---
st.header("📥 Upload File for Indexing")

uploaded_file = st.file_uploader("Choose a file to ingest", type=["pdf", "csv", "txt", "docx", "jpg", "png"])
if uploaded_file:
    file_path = os.path.join("data/raw", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Ingesting and indexing..."):
        ingest_and_index(file_path)
    st.success(f"✅ {uploaded_file.name} ingested and indexed successfully!")

# --- Chat Section ---
st.header("💬 Ask a Question")

query = st.text_input("Enter your question")
file_type = st.selectbox("Select file type to search in", options=["pdf", "docx", "xlsx", "csv", "txt", "image"])

if st.button("Get Answer"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            result = query_vector_store(query, file_type)
            st.markdown(result)
