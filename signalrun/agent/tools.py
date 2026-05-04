from langchain_core.tools import tool


@tool
def search(query: str): 
    pass


@tool 
def fetch(items: str): 
    pass