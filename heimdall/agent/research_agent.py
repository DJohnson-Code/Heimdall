from langchain.agents import create_agent

from heimdall.agent.tools import build_tools
from heimdall.config.agent_model import model
from heimdall.schemas.schemas import ResearchResult
from heimdall.config.agent_prompt import RESEARCH_AGENT_SYSTEM_PROMPT



def build_research_agent(article_cache):
    """Build the Heimdall topic research agent."""
    return create_agent(
        model=model, 
        tools=build_tools(article_cache), 
        system_prompt=RESEARCH_AGENT_SYSTEM_PROMPT, 
        response_format=ResearchResult, 
    )


