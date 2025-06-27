import sys, os
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from vect_utils.file_router import extract_text
from scripts.chunker import chunk_text
from scripts.embedder import embed_chunks
from scripts.deduplication import remove_duplicates
from scripts.faiss_indexer import create_faiss_index

def ingest_and_index(file_path: str) -> str:
    docs = extract_text(file_path)

    if docs == 'unsupported':
        print(f"❌ Unsupported file: {file_path}")
        return 'unsupported'

    if not docs:
        print(f"⚠️ Skipping file due to empty or failed text extraction: {file_path}")
        return 'skipped'

    try:
        # Force re-chunking into smaller parts if needed
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        split_docs = splitter.split_documents(docs)

        # Embed and deduplicate
        embs = embed_chunks(split_docs)
        docs_u, embs_u = remove_duplicates(split_docs, embs)

        # Save index by file type
        ext = Path(file_path).suffix.lower().lstrip(".")
        create_faiss_index(docs_u, index_type=ext)

        return 'processed'

    except Exception as e:
        print(f"❌ Failed to process {file_path}: {e}")
        return 'skipped'

if __name__ == "__main__":
    ingest_and_index(sys.argv[1])
