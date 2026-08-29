from heimdall.pipeline.topics import DAILY_TOPICS
from heimdall.schemas.schemas import ArticleCandidate, FetchedArticle
from heimdall.agent.research_agent import build_research_agent


def run() -> list[ArticleCandidate]:

    all_candidates: list[ArticleCandidate] = []

    article_cache: dict[str, FetchedArticle] = {}

    for topic in DAILY_TOPICS: 
        heimdall = build_research_agent(article_cache)
        print(f"Researching topic: {topic.name}")

        result = heimdall.invoke({
            "messages": [{
                "role": "user",
                "content": (
                    f"Topic: {topic.name}\n"
                    f"Maximum final candidates: {topic.max_articles}"
                ),
            }]
        })

        print(f"Finished topic: {topic.name}")

        research_result = result["structured_response"]

        all_candidates.extend(research_result.candidates[:topic.max_articles])

    return all_candidates





        
