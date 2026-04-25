from pydantic import BaseModel, ConfigDict, Field, HttpUrl
from uuid import UUID 
from datetime import datetime 


class FeedItem(BaseModel): 
    title: str 
    url: HttpUrl
    source: str = Field(min_length=1)
    published_at: datetime | None = None
    snippet: str | None = None 

    model_config = ConfigDict(extra="allow")

class ArticleCandidate(FeedItem):
    title: str = Field(min_length=1)
    snippet: str = Field(min_length=1)

    model_config = ConfigDict(extra="forbid")

class NewsArticle(BaseModel): 

    id: UUID
    title: str
    url: HttpUrl
    source: str = Field(min_length=1)
    published_at: datetime | None = None
    category: str = Field(default="general") 

    model_config = ConfigDict(from_attributes=True, extra="forbid")

class DigestEntry(BaseModel):
    

    title: str
    source: str
    summary: str = Field(min_length=1)
    link: HttpUrl

    model_config = ConfigDict(extra="forbid")