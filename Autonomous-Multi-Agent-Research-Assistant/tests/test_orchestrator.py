import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.orchestrator.controller import ResearchOrchestrator

orchestrator = ResearchOrchestrator()

query = "AI in healthcare"
result = orchestrator.run(query)

print("Orchestrator Output:\n")
print("Query:", result["query"])

print("\nSubtasks:")
for i, subtask in enumerate(result["subtasks"], start=1):
    print(f"{i}. {subtask}")

print("\nFinal Report:")
print(result["final_report"])