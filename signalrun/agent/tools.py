import feedparser
from langchain_core.tools import tool

from signalrun.pipeline.topics import DAILY_TOPICS, TopicConfig


def get_topic_by_name(topic_name: str) -> TopicConfig:
    """Return the configured topic matching ``topic_name`` case-insensitively."""
    normalized_topic_name = topic_name.strip().casefold()

    for configured_topic in DAILY_TOPICS:
        if configured_topic.name.casefold() == normalized_topic_name:
            return configured_topic

    valid_topics = ", ".join(t.name for t in DAILY_TOPICS)
    raise ValueError(
        f"{topic_name!r} is not a configured topic. Valid topics: {valid_topics}"
    )


@tool(description="Searches rss feeds for articles connected to the topic_name and query parameters.")
def search_rss(topic_name: str, query: str) -> list[dict]:
    """Search configured RSS sources for recent articles related to a topic and query."""

