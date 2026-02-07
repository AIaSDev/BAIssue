from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.core.database import Base


class IssueModel(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable=True)
    status = Column(String(16), nullable=False, default="open")
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None))
    updated_at = Column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
        onupdate=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
    )