import os
import streamlit as st

try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
    USE_LOCAL_MODEL = True
except Exception:
    model = None
    USE_LOCAL_MODEL = False


def get_secret(key_name: str):
    try:
        return st.secrets[key_name]
    except Exception:
        return os.getenv(key_name)


def simple_fallback_embedding(text: str):
    """
    Lightweight fallback embedding if sentence-transformers is unavailable.
    """
    text = text.lower()
    vector = [0.0] * 64

    for i, ch in enumerate(text):
        vector[i % 64] += (ord(ch) % 50) / 50.0

    return vector


def generate_embedding(text: str):
    if not text.strip():
        return []

    if USE_LOCAL_MODEL and model is not None:
        embedding = model.encode(text)
        return embedding.tolist()

    return simple_fallback_embedding(text)
