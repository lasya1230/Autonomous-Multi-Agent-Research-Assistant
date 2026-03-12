class AnalystAgent:
    def __init__(self):
        pass

    def analyze(self, subtask: str, retrieved_chunks: list[dict]) -> dict:
        """
        Analyze retrieved chunks and create a simple summary.
        """
        if not retrieved_chunks:
            return {
                "subtask": subtask,
                "summary": "No relevant information found.",
                "key_points": []
            }

        texts = [item["text"] for item in retrieved_chunks]

        combined_text = " ".join(texts)

        key_points = []
        for text in texts:
            short_text = text.strip().replace("\n", " ")
            if short_text:
                key_points.append(short_text[:120])

        return {
            "subtask": subtask,
            "summary": combined_text[:300],
            "key_points": key_points
        }