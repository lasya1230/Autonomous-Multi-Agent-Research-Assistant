import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.agents.retriever_agent import RetrieverAgent
from src.agents.analyst_agent import AnalystAgent
from src.agents.verifier_agent import VerifierAgent

retriever = RetrieverAgent(top_k=2)
analyst = AnalystAgent()
verifier = VerifierAgent()

subtask = "What are the benefits of AI in healthcare?"
retrieved_chunks = retriever.retrieve(subtask)
analysis_result = analyst.analyze(subtask, retrieved_chunks)
verification_result = verifier.verify(analysis_result, retrieved_chunks)

print("Verifier Agent Output:\n")
print("Verified:", verification_result["verified"])
print("Confidence:", verification_result["confidence"])
print("Evidence Count:", verification_result["evidence_count"])
print("Message:", verification_result["message"])