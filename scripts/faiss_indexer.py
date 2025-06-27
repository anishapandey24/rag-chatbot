# scripts/faiss_indexer.py

import os
import pickle
from pathlib import Path
import faiss
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def create_faiss_index(documents, index_type='pdf'):
    """
    Create and save FAISS index from documents.
    """
    vector_store = FAISS.from_documents(documents, model)
    save_dir = f"index/faiss/{index_type}"
    os.makedirs(save_dir, exist_ok=True)

    vector_store.save_local(save_dir)

    # Save raw chunks
    with open(os.path.join(save_dir, "chunks.pkl"), "wb") as f:
        pickle.dump(documents, f)

def load_faiss_index(index_type='pdf'):
    """
    Load an existing FAISS index from disk.
    """
    index_dir = f"index/faiss/{index_type}"
    if not Path(index_dir).exists():
        raise FileNotFoundError(f"No index found at: {index_dir}")

    return FAISS.load_local(index_dir, model, allow_dangerous_deserialization=True)

def search_index(query, index_type='pdf', top_k=3):
    """
    Search the FAISS index for top_k similar chunks.
    """
    vector_store = load_faiss_index(index_type)
    results = vector_store.similarity_search(query, k=top_k)
    return [doc.page_content for doc in results]
