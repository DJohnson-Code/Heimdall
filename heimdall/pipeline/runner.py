from heimdall.pipeline.topics import DAILY_TOPICS
from heimdall.schemas.schemas import ArticleCandidate
from heimdall.agent.research_agent import build_research_agent


def run() -> list[ArticleCandidate]:
    heimdall = build_research_agent()

    all_candidates = []

    for topic in DAILY_TOPICS: 
        print(f"Researching topic: {topic.name}")

        result = heimdall.invoke({
            "messages": [{"role": "user", "content": topic.name}]
        })

        print(f"Finished topic: {topic.name}")

        research_result = result["structured_response"]

        all_candidates.extend(research_result.candidates)

    return all_candidates





        
