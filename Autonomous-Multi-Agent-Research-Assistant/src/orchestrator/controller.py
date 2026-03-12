from src.agents.planner_agent import PlannerAgent
from src.agents.retriever_agent import RetrieverAgent
from src.agents.analyst_agent import AnalystAgent
from src.agents.verifier_agent import VerifierAgent
from src.agents.writer_agent import WriterAgent
from src.agents.web_search_agent import WebSearchAgent


class ResearchOrchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.retriever = RetrieverAgent(top_k=2)
        self.analyst = AnalystAgent()
        self.verifier = VerifierAgent()
        self.writer = WriterAgent()
        self.web_search = WebSearchAgent()

    def run(self, query: str) -> dict:
        if not query.strip():
            return {
                "query": query,
                "subtasks": [],
                "sections": [],
                "final_report": "No query provided."
            }

        subtasks = self.planner.plan(query)
        report_sections = []
        sections = []

        for subtask in subtasks:
            retrieved_chunks = self.retriever.retrieve(subtask)
            analysis_result = self.analyst.analyze(subtask, retrieved_chunks)
            verification_result = self.verifier.verify(analysis_result, retrieved_chunks)
            written_section = self.writer.write_section(analysis_result, verification_result)
            web_results = self.web_search.search(subtask, max_results=3)

            report_sections.append(written_section)
            sections.append({
                "subtask": subtask,
                "retrieved_chunks": retrieved_chunks,
                "analysis_result": analysis_result,
                "verification_result": verification_result,
                "written_section": written_section,
                "web_results": web_results
            })

        final_report = ("\n" + "=" * 80 + "\n").join(report_sections)

        return {
            "query": query,
            "subtasks": subtasks,
            "sections": sections,
            "final_report": final_report
        }