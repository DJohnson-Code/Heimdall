from sqlalchemy.orm import Session
from sqlalchemy import select
from heimdall.db.models import SentArticle


def previously_sent_articles(session: Session, urls: list[str]) -> set[str]:
    if not urls:
        return set()
    
    stmt = select(SentArticle.url).where(SentArticle.url.in_(urls))
    return set(session.scalars(stmt).all())