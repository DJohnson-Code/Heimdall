from langchain.agents import create_agent

from heimdall.agent.tools import build_tools
from heimdall.config.agent_model import model
from heimdall.schemas.schemas import ResearchResult
from heimdall.config.agent_prompt import RESEARCH_AGENT_SYSTEM_PROMPT



def build_research_agent():
    """Build the Heimdall topic research agent."""
    return create_agent(
        model=model, 
        tools=build_tools(), 
        system_prompt=RESEARCH_AGENT_SYSTEM_PROMPT, 
        response_format=ResearchResult, 
    )


