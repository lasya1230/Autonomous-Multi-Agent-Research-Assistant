class WriterAgent:
    def __init__(self):
        pass

    def write_section(self, analysis_result: dict, verification_result: dict) -> str:
        """
        Create a readable research section from analysis and verification results.
        """
        subtask = analysis_result.get("subtask", "No subtask")
        summary = analysis_result.get("summary", "No summary available.")
        key_points = analysis_result.get("key_points", [])

        verified = verification_result.get("verified", False)
        confidence = verification_result.get("confidence", "Low")
        message = verification_result.get("message", "No verification message.")

        section = f"Subtask: {subtask}\n\n"
        section += f"Summary: {summary}\n\n"
        section += "Key Points:\n"

        if key_points:
            for i, point in enumerate(key_points, start=1):
                section += f"{i}. {point}\n"
        else:
            section += "No key points available.\n"

        section += f"\nVerified: {verified}\n"
        section += f"Confidence: {confidence}\n"
        section += f"Verification Message: {message}\n"

        return section