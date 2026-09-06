from google.adk.agents import Agent
from app.core.llm import get_llm
from app.tools.patent_tools import search_patents


def create_research_agent():
    return Agent(
        name="patent_research_agent",
        model=get_llm(),
        description="An agent that helps research and analyze patents.",
        instruction="""
        You are a helpful patent research assistant.
        When user asks about a technology or patent, use the search_patent tool.
        Always summarise the results clearly and highlight the most relevant patents.
        Be precise and technical.
        """,
        tools=[search_patents],
    )
