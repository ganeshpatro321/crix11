from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.tools import Tool
import os
from crewai_tools import SerperDevTool



def search_serper(query: str) -> str:
    """Search for information using Serper API."""
    try:
        search = GoogleSerperAPIWrapper(serper_api_key=os.environ.get("SERPER_API_KEY"))
        return search.run(query)
    except Exception as e:
        return f"Error running search: {str(e)}"


def get_search_tool(description="Search for IPL information", n_results=30):
    """Create a search tool with custom description."""
    return SerperDevTool(
        description=description,
        n_results=n_results
    )