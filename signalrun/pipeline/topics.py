from pydantic import BaseModel, ConfigDict, Field

class TopicConfig(BaseModel): 
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    rss_sources: list[str] = Field(default_factory=list)
    trusted_sources: list[str] = Field(default_factory=list)
    search_queries: list[str] = Field(default_factory=list)
    max_articles: int = Field(ge=1, le=10)
    freshness_days: int = Field(ge=1, le=30)

    model_config = ConfigDict(extra="forbid")


ai_topic = TopicConfig(
    name = "AI",
    description = ("Recent developments in artificial intelligence, including major model releases, "
    "AI infrastructure, agent systems, open-source models, AI tooling, research breakthroughs, "
    "safety/regulation updates, and practical impacts on software engineering."),
    rss_sources = [
        "https://openai.com/news/rss.xml",
        "https://huggingface.co/blog/feed.xml",
    ], 
    trusted_sources = [
        "openai.com",
        "anthropic.com",
        "deepmind.google",
        "huggingface.co",
        "ai.googleblog.com",
    ],
    search_queries = [
        "latest AI model releases",
        "AI agents developer tools news",
        "open source LLM releases",
        "AI infrastructure inference serving news",
        "AI regulation safety policy updates",
    ], 
    max_articles = 10, 
    freshness_days = 5, 
)

general_topic = TopicConfig()

