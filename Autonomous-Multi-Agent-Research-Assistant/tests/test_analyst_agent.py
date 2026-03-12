import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.agents.analyst_agent import AnalystAgent
from src.agents.retriever_agent import RetrieverAgent

retriever = RetrieverAgent(top_k=2)
analyst = AnalystAgent()

subtask = "What are the benefits of AI in healthcare?"
retrieved_chunks = retriever.retrieve(subtask)

result = analyst.analyze(subtask, retrieved_chunks)

print("Analyst Agent Output:\n")
print("Subtask:", result["subtask"])
print("Summary:", result["summary"])
print("\nKey Points:")
for i, point in enumerate(result["key_points"], start=1):
    print(f"{i}. {point}")