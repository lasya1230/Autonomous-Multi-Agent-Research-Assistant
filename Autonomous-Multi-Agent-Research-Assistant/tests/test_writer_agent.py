import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.agents.retriever_agent import RetrieverAgent
from src.agents.analyst_agent import AnalystAgent
from src.agents.verifier_agent import VerifierAgent
from src.agents.writer_agent import WriterAgent

retriever = RetrieverAgent(top_k=2)
analyst = AnalystAgent()
verifier = VerifierAgent()
writer = WriterAgent()

subtask = "What are the benefits of AI in healthcare?"
retrieved_chunks = retriever.retrieve(subtask)
analysis_result = analyst.analyze(subtask, retrieved_chunks)
verification_result = verifier.verify(analysis_result, retrieved_chunks)

final_section = writer.write_section(analysis_result, verification_result)

print("Writer Agent Output:\n")
print(final_section)