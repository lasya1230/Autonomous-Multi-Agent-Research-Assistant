import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.rag.document_loader import load_document
from src.rag.text_chunker import chunk_text

file_path = "data/raw_docs/sample.txt"
text = load_document(file_path)

chunks = chunk_text(text, chunk_size=100, overlap=20)

print("Total Chunks:", len(chunks))
print("\nChunks:\n")

for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk {i}:")
    print(chunk)
    print("-" * 40)