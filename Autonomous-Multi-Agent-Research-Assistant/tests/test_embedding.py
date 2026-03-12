import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.rag.embedding_generator import generate_embedding

sample_text = "Artificial Intelligence is changing healthcare."

embedding = generate_embedding(sample_text)

print("Embedding generated successfully.")
print("Embedding length:", len(embedding))
print("First 10 values:", embedding[:10])