from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from langchain_core.documents import Document

def remove_duplicates(
    docs: list[Document],
    embeddings: list[np.ndarray],
    threshold: float = 0.95
) -> tuple[list[Document], list[np.ndarray]]:
    unique_docs, unique_embs = [], []
    for doc, emb in zip(docs, embeddings):
        if all(cosine_similarity([emb], [ue])[0][0] < threshold for ue in unique_embs):
            unique_docs.append(doc)
            unique_embs.append(emb)
    return unique_docs, unique_embs
