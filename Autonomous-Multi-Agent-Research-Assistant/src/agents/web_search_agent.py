import os
import streamlit as st
from tavily import TavilyClient


def get_secret(key_name: str):
    try:
        return st.secrets[key_name]
    except Exception:
        return os.getenv(key_name)


class WebSearchAgent:
    def __init__(self):
        self.api_key = get_secret("TAVILY_API_KEY")
        self.client = TavilyClient(api_key=self.api_key) if self.api_key else None

    def search(self, query: str, max_results: int = 3):
        if not query.strip():
            return []

        if not self.client:
            return [{
                "title": "Tavily API key missing",
                "url": "",
                "content": "Add TAVILY_API_KEY in Streamlit secrets or .env to enable web search."
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
