import json
import os
from typing import List, Dict, Any


class SimpleVectorStore:
    def __init__(self, storage_path: str = "data/processed_chunks/vector_store.json"):
        self.storage_path = storage_path
        self.data = []
        self._load()

    def _load(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r", encoding="utf-8") as file:
                self.data = json.load(file)
        else:
            self.data = []

    def _save(self):
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        with open(self.storage_path, "w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=2)

    def add_item(self, text: str, embedding: List[float], metadata: Dict[str, Any] = None):
        item = {
            "text": text,
            "embedding": embedding,
            "metadata": metadata or {}
        }
        self.data.append(item)
        self._save()

    def get_all_items(self):
        return self.data