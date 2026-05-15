from urllib.parse import urlparse

import feedparser
from langchain_core.tools import tool

from signalrun.pipeline.topics import DAILY_TOPICS, TopicConfig
from signalrun.schemas.schemas import FeedItem


def topic_helper(topic_name: str) -> TopicConfig:
    """Return the configured topic matching ``topic_name`` case-insensitively."""
    normalized_topic_name = topic_name.strip().casefold()

    for configured_topic in DAILY_TOPICS:
        if configured_topic.name.casefold() == normalized_topic_name:
            return configured_topic

    valid_topics = ", ".join(t.name for t in DAILY_TOPICS)
    raise ValueError(
        f"{topic_name!r} is not a configured topic. Valid topics: {valid_topics}"
    )

def source_from_url(url: str) -> str:
    """Return the domain/source name from an article URL."""
    return urlparse(url).netloc.lower().removeprefix("www.")


@tool(description="Searches rss feeds for articles related to the topic_name.")
def search_rss(topic_name: str) -> list[dict]:
    """Search the configured RSS sources for recent articles related to the topic."""

    topic = topic_helper(topic_name)

    rss_output: list[dict] = []

    for feed_url in topic.rss_sources: 
        feed = feedparser.parse(feed_url)

        for entry in feed.entries: 
            title = entry.get("title")
            url = entry.get("link")
            snippet = (
                entry.get("summary")
                or entry.get("description")
                or ""
            )

            if not title or not url or not snippet: 
                continue

            feed_item = FeedItem(
                title=title,
                url=url,
                source=source_from_url(url),
                snippet=snippet,
            )

            rss_output.append(feed_item.model_dump(mode="json"))

    return rss_output[: topic.max_articles]


if __name__ == "__main__":
    result = search_rss.invoke({"topic_name": "AI"})

    for item in result:
        print(item["title"])
        print(item["url"])
        print(item["source"])
        print()