import streamlit as st
from scripts.ingest import ingest_and_index
from scripts.faiss_indexer import search_index
from scripts.rag_chain import get_answer_from_chunks

st.set_page_config(page_title="📚 RAG Chatbot", layout="wide")
st.title("📚 RAG Chatbot with File Ingestion")
st.markdown("Ingest files and ask questions across all documents using Retrieval-Augmented Generation.")

# --- File Upload ---
uploaded_file = st.file_uploader("📤 Upload a file", type=["pdf", "docx", "txt", "csv", "xlsx", "jpg", "png"])

if uploaded_file:
    file_ext = uploaded_file.name.split(".")[-1].lower()
    with open(f"data/raw/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("🔄 Ingesting and indexing..."):
        status = ingest_and_index(f"data/raw/{uploaded_file.name}")

    if status == 'processed':
        st.success("✅ File ingested and indexed!")
        st.session_state['last_index_type'] = file_ext  # save the type
    elif status == 'unsupported':
        st.error("❌ Unsupported file type.")
    else:
        st.warning("⚠️ File could not be ingested.")

st.markdown("---")

# --- Chat Interface ---
st.subheader("💬 Ask a question about your files")
query = st.text_input("🔍 Your question")

if query:
    index_type = st.session_state.get("last_index_type", "pdf")  # fallback to 'pdf' if not set

    with st.spinner("🔎 Searching the vector store..."):
        top_chunks = search_index(query, index_type=index_type, top_k=5)

    st.write("📄 **Top Matching Chunks**")
    for i, chunk in enumerate(top_chunks, 1):
        with st.expander(f"Match {i}"):
            st.write(chunk)

    with st.spinner("🤖 Generating answer..."):
        response = get_answer_from_chunks(query, index_type=index_type, top_k=5)
        st.markdown("### 🧠 Answer")
        st.success(response)
