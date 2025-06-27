# scripts/query.py

from scripts.faiss_indexer import search_index
from scripts.rag_chain import get_answer_from_chunks

def query_vector_store(question: str, file_type="pdf") -> str:
    try:
        matches = search_index(question, index_type=file_type, top_k=3)
        sources = "\n".join([f"{i+1}. {m}" for i, m in enumerate(matches)])
    except Exception as e:
        sources = f"[ERROR] Could not retrieve chunks: {e}"

    try:
        answer = get_answer_from_chunks(question)
    except Exception as e:
        answer = f"[ERROR] LLM failed: {e}"

    return f"📄 **Top Matches:**\n{sources}\n\n💬 **Answer:**\n{answer}"

