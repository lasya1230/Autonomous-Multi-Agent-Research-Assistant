from src.rag.retriever import retrieve_similar_chunks


class RetrieverAgent:
    def __init__(self, top_k: int = 2):
        self.top_k = top_k

    def retrieve(self, subtask: str):
        """
        Retrieve relevant chunks for a given subtask.
        """
        if not subtask.strip():
            return []

        results = retrieve_similar_chunks(subtask, top_k=self.top_k)
        return results