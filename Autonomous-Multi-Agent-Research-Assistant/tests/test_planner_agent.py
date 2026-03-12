import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.agents.planner_agent import PlannerAgent

planner = PlannerAgent()

query = "AI in healthcare"
subtasks = planner.plan(query)

print("Planner Output:\n")

for i, task in enumerate(subtasks, start=1):
    print(f"{i}. {task}")