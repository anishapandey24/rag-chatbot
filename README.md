# 📚 RAG Chatbot – Retrieval-Augmented Generation with Streamlit & Mistral

This project implements a **Retrieval-Augmented Generation (RAG)** chatbot that allows users to **upload their own documents** (PDFs, DOCX, CSVs, etc.), index them using **FAISS**, and query them through an LLM (**Mistral-7B via LlamaCpp**). It includes a clean **Streamlit interface** for file ingestion and chat-based question-answering.

---

## 🚀 Features

- 📤 Upload files (`pdf`, `docx`, `txt`, `csv`, `xlsx`, `jpg`, `png`)
- 🔎 Vector indexing with FAISS using per-file-type logic
- 🧠 Chat interface powered by **Mistral 7B (via LlamaCpp)**
- 🧼 Deduplication of chunks before embedding
- 🧾 Modular pipeline for preprocessing, chunking, embedding, and searching
- 🖥️ Clean Streamlit UI for demo and real-time use

---

## 🗂️ Project Structure

## How to Run
```bash
PYTHONPATH=. python3 -m scripts.run_pipeline data/raw/
## run the streamlit 
PYTHONPATH=. streamlit run streamlit_app/app.py

