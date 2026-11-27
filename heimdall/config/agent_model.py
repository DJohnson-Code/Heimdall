from langchain_openai import ChatOpenAI


model = ChatOpenAI(
    model="gpt-5.4",
)

summarizer_model = ChatOpenAI(
    model="gpt-5.4",
    max_retries=0,
)