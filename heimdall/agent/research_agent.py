from langchain.agents import create_agent

from heimdall.agent.tools import TOOLS
from heimdall.config.agent_model import model
from heimdall.config.agent_prompt import RESEARCH_AGENT_SYSTEM_PROMPT




def build_research_agent(response_format=None):
    """Build the Heimdall topic research agent."""
    return create_agent(
        model=model, 
        tools=TOOLS, 
        system_prompt=RESEARCH_AGENT_SYSTEM_PROMPT, 
        response_format=response_format,
    )


