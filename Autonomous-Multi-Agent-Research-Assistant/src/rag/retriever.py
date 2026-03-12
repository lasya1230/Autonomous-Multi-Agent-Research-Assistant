import math
from typing import List, Dict, Any

from src.rag.embedding_generator import generate_embedding
from src.rag.vector_store import SimpleVectorStore


def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return dot_product / (norm1 * norm2)


def retrieve_similar_chunks(query: str, top_k: int = 3) -> List[Dict[str, Any]]:
    store = SimpleVectorStore()
    items = store.get_all_items()

    if not items:
        return []

    query_embedding = generate_embedding(query)

    scored_items = []
    for item in items:
        score = cosine_similarity(query_embedding, item["embedding"])
        scored_items.append({
            "text": item["text"],
            "metadata": item["metadata"],
            "score": score
        })

    scored_items.sort(key=lambda x: x["score"], reverse=True)

    return scored_items[:top_k]