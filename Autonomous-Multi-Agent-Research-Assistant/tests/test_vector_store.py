import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.rag.document_loader import load_document
from src.rag.text_chunker import chunk_text
from src.rag.embedding_generator import generate_embedding
from src.rag.vector_store import SimpleVectorStore

file_path = "data/raw_docs/sample.txt"
text = load_document(file_path)

chunks = chunk_text(text, chunk_size=100, overlap=20)

store = SimpleVectorStore()

for i, chunk in enumerate(chunks, start=1):
    embedding = generate_embedding(chunk)
    store.add_item(
        text=chunk,
        embedding=embedding,
        metadata={"chunk_number": i, "source": file_path}
    )

items = store.get_all_items()

print("Stored items:", len(items))
print("First item metadata:", items[0]["metadata"])
print("First item text:", items[0]["text"])
print("Embedding length:", len(items[0]["embedding"]))