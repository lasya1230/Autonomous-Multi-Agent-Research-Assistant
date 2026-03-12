import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.rag.retriever import retrieve_similar_chunks

query = "How is AI helping healthcare?"

results = retrieve_similar_chunks(query, top_k=2)

print("Top Results:\n")

for i, item in enumerate(results, start=1):
    print(f"Result {i}")
    print("Score:", item["score"])
    print("Metadata:", item["metadata"])
    print("Text:", item["text"])
    print("-" * 50)