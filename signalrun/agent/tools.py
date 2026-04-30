from langchain_core.tools import tool


@tool
def search(topic: str): 
    pass


@tool 
def fetch(items: str): 
    pass