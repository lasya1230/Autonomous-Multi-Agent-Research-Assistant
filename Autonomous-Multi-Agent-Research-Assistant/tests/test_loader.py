import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.rag.document_loader import load_document

file_path = "data/raw_docs/sample.txt"

text = load_document(file_path)

print("Loaded Text:")
print(text)