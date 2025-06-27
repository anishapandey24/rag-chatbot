from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def embed_chunks(docs: list[Document]) -> list[list[float]]:
    if not docs:
        return []
    texts = [doc.page_content for doc in docs]
    return model.embed_documents(texts)

