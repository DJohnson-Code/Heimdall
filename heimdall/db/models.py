from __future__ import annotations

from datetime import datetime 
from sqlalchemy import String, DateTime, func 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from uuid import UUID

class Base(DeclarativeBase): 
    pass 

class SentArticle(Base):
    __tablename__ = "sent_articles"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(500))
    url: Mapped[str] = mapped_column(String(900), unique=True)
    date_sent: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default = func.now(), 
    )
