from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(text: str):
    """
    Generate embedding using a local free model.
    """
    if not text.strip():
        return []

    embedding = model.encode(text)
    return embedding.tolist()