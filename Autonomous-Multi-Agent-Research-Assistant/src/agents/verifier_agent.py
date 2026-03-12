class VerifierAgent:
    def __init__(self):
        pass

    def verify(self, analysis_result: dict, retrieved_chunks: list[dict]) -> dict:
        """
        Verify whether the analysis has supporting evidence.
        """
        if not retrieved_chunks:
            return {
                "verified": False,
                "confidence": "Low",
                "evidence_count": 0,
                "message": "No supporting evidence found."
            }

        evidence_count = len(retrieved_chunks)

        if evidence_count >= 2:
            confidence = "High"
            verified = True
            message = "The analysis is supported by multiple retrieved chunks."
        else:
            confidence = "Medium"
            verified = True
            message = "The analysis is supported by limited retrieved evidence."

        return {
            "verified": verified,
            "confidence": confidence,
            "evidence_count": evidence_count,
            "message": message
        }