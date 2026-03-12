import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()


class WebSearchAgent:
    def __init__(self):
        self.api_key = os.getenv("TAVILY_API_KEY")
        self.client = TavilyClient(api_key=self.api_key) if self.api_key else None

    def search(self, query: str, max_results: int = 3):
        if not query.strip():
            return []

        if not self.client:
            return [{
                "title": "Tavily API key missing",
                "url": "",
                "content": "Add TAVILY_API_KEY in your .env file to enable web search."
            }]

        try:
            response = self.client.search(query=query, max_results=max_results)
            return response.get("results", [])
        except Exception as e:
            return [{
                "title": "Web search error",
                "url": "",
                "content": str(e)
            }]