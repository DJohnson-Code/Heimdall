from datetime import date, datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class FeedItem(BaseModel): 
    title: str = Field(min_length=1)
    url: HttpUrl
    source: str = Field(min_length=1)
    publisher: str | None = None
    published_at: datetime | None = None
    snippet: str | None = None

    model_config = ConfigDict(extra="forbid")

class ArticleCandidate(FeedItem):
    selection_reason: str = Field(min_length=1)

    model_config = ConfigDict(extra="forbid")

class FetchedArticle(BaseModel): 
    final_url: HttpUrl
    source: str = Field(min_length=1)
    article: str = Field(min_length=1, max_length=12000)
    truncated: bool 

    model_config = ConfigDict(extra="forbid")
class NewsArticle(BaseModel): 
    id: UUID = Field(default_factory=uuid4)
    article: str = Field(min_length=1)
    title: str = Field(min_length=1)
    url: HttpUrl
    publisher: str = Field(min_length=1)
    published_at: datetime

    model_config = ConfigDict(from_attributes=True, extra="forbid")

class ProcessedArticle(BaseModel):
    article_id: UUID
    title: str = Field(min_length=1)
    url: HttpUrl
    publisher: str = Field(min_length=1)
    published_at: datetime
    category: str = Field(min_length=1)
    summary: str = Field(min_length=1)
    relevance_score: int = Field(ge=0, le=100)

    model_config = ConfigDict(extra="forbid")

class DigestEntry(BaseModel):
    article_id: UUID
    title: str = Field(min_length=1)
    publisher: str = Field(min_length=1)
    summary: str = Field(min_length=1)
    article_url: HttpUrl 
    category: str = Field(min_length=1)
    published_at: datetime 

    model_config = ConfigDict(extra="forbid")

class Digest(BaseModel):
    date: date
    entries: list[DigestEntry]
    
    model_config = ConfigDict(extra="forbid")