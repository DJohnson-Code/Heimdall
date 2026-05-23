import httpx
import trafilatura
from urllib.parse import urlparse

import feedparser
from langchain_core.tools import tool

from heimdall.pipeline.topics import DAILY_TOPICS, TopicConfig
from heimdall.schemas.schemas import FeedItem

MAX_ARTICLE_CHARS = 12_000

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





Here's the Option B version. One "url" key everywhere — it's the final redirected URL when we have a response, and falls back to the input URL when the request itself failed.

Recommended fetch_article
@tool(description="Fetch article text from a URL.")
def fetch_article(url: str) -> dict:
    """Fetch one article URL and return extracted article text."""
    try:
        response = httpx.get(
            url,
            timeout=15,
            follow_redirects=True,
            headers={"User-Agent": "Heimdall/0.1"},
        )
        response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        return {
            "url": url,
            "ok": False,
            "error": "bad_status",
            "status_code": exc.response.status_code,
        }
    except httpx.RequestError as exc:
        return {
            "url": url,
            "ok": False,
            "error": "request_failed",
            "message": str(exc),
        }
    final_url = str(response.url)
    content_type = response.headers.get("content-type", "").lower()
    if "html" not in content_type:
        return {
            "url": final_url,
            "ok": False,
            "error": "unsupported_content_type",
            "content_type": content_type or "missing",
            "status_code": response.status_code,
        }
    article = trafilatura.extract(response.text) or ""
    if not article:
        return {
            "url": final_url,
            "ok": False,
            "error": "no_article_text_found",
            "status_code": response.status_code,
        }
    return {
        "url": final_url,
        "ok": True,
        "status_code": response.status_code,
        "source": source_from_url(final_url),
        "article": article[:MAX_ARTICLE_CHARS],
        "truncated": len(article) > MAX_ARTICLE_CHARS,
    }
    
