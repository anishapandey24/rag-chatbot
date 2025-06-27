from pathlib import Path
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter

def chunk_text(text: str, source: str, chunk_size=1000, chunk_overlap=200):
    """Split raw text into a list of Document objects."""
    doc = Document(page_content=text, metadata={"source": source})
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents([doc])
