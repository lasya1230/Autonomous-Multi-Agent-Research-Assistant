import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.agents.retriever_agent import RetrieverAgent

agent = RetrieverAgent(top_k=2)

subtask = "What are the benefits of AI in healthcare?"
results = agent.retrieve(subtask)

print("Retriever Agent Output:\n")

for i, item in enumerate(results, start=1):
    print(f"Result {i}")
    print("Score:", item["score"])
    print("Metadata:", item["metadata"])
    print("Text:", item["text"])
    print("-" * 50)