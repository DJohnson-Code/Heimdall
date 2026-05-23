from heimdall.pipeline.topics import DAILY_TOPICS
from heimdall.config.agent_prompt import RESEARCH_AGENT_SYSTEM_PROMPT
from heimdall.agent.tools import TOOLS
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-5.4",
)

research_agent = create_agent(
    model, 
    tools=TOOLS, 
    system_prompt=RESEARCH_AGENT_SYSTEM_PROMPT,  
)