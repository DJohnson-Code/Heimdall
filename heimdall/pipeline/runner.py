import json
from heimdall.pipeline.topics import DAILY_TOPICS
from heimdall.schemas.schemas import ArticleCandidate
from heimdall.agent.research_agent import build_research_agent


def run() -> list[ArticleCandidate]:
    heimdall = build_research_agent()

    all_candidates = []

    for topic in DAILY_TOPICS[:]: 
        print(f"Researching topic: {topic.name}")

        result = heimdall.invoke({
            "messages": [{"role": "user", "content": topic.name}]
        })

        print(f"Finished topic: {topic.name}")

        final_text = result["messages"][-1].content
        raw_candidates = json.loads(final_text)

        if not isinstance(raw_candidates, list):
            raise ValueError("Research agent returned non-list JSON")

        candidates = [
            ArticleCandidate.model_validate(candidate)
            for candidate in raw_candidates
        ]

        all_candidates.extend(candidates)

    return all_candidates




        
