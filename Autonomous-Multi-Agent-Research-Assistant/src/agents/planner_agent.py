class PlannerAgent:
    def __init__(self):
        pass

    def plan(self, query: str) -> list[str]:
        """
        Break a research query into smaller subtopics.
        """
        if not query.strip():
            return []

        return [
            f"What is the overview of {query}?",
            f"What are the main benefits of {query}?",
            f"What are the main risks or challenges of {query}?",
            f"What are some real-world examples of {query}?",
        ]