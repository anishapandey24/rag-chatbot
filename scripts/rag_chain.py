from scripts.faiss_indexer import search_index
from langchain_community.llms import LlamaCpp

def get_answer_from_chunks(query: str, index_type: str = "pdf", top_k: int = 10) -> str:
    """
    Retrieves chunks, builds a prompt that fits in 4096-token window,
    and generates response using Mistral (via LlamaCpp).
    """

    if not query.strip():
        return "⚠️ Please enter a valid question."

    try:
        raw_chunks = search_index(query, index_type=index_type, top_k=top_k)
        if not raw_chunks:
            return "ℹ️ No relevant information found in the indexed documents."

        # Trim to fit Mistral context window (4096 tokens ≈ 3500 words)
        context_list = []
        total_words = 0
        max_words = 3500

        for chunk in raw_chunks:
            chunk_words = len(chunk.split())
            if total_words + chunk_words > max_words:
                break
            context_list.append(chunk)
            total_words += chunk_words

        context = "\n\n".join(context_list)

        prompt = f"""[INST] You are a helpful assistant. Use the following context to answer the question.\n\nContext:\n{context}\n\nQuestion: {query} [/INST]"""

        llm = LlamaCpp(
            model_path="/Users/anishapandey/Desktop/vectorization_project/models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
            n_ctx=4096,
            n_batch=512,
            temperature=0,
            max_tokens=512,
            top_p=0.95,
            repeat_penalty=1.1,
            verbose=False,
            n_gpu_layers=-1
        )

        response = llm.invoke(prompt)
        return response.strip()

    except Exception as e:
        return f"❌ Error during response generation: {e}"

