"""
Database configuration and session management.

This module provides:
- SQLAlchemy engine and session configuration
- Database initialization utilities
- FastAPI dependency for database sessions
"""
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, declarative_base
from sqlalchemy.pool import StaticPool

from app.infrastructure.config import DATABASE_URL

Base = declarative_base()

is_sqlite = DATABASE_URL.startswith("sqlite")

engine_kwargs = {}
if is_sqlite:
    engine_kwargs["connect_args"] = {"check_same_thread": False}
    # Stable in-memory DB for CI/integration tests
    if DATABASE_URL in ("sqlite:///:memory:", "sqlite+pysqlite:///:memory:"):
        engine_kwargs["poolclass"] = StaticPool

engine = create_engine(DATABASE_URL, **engine_kwargs)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def init_db() -> None:
    """
    Initialize database tables (dev/CI convenience).
    
    Creates all tables defined in SQLAlchemy models.
    This is useful for development and testing but should not be
    used in production (use proper migrations instead).
    """
    from app.infrastructure.persistence import sqlalchemy_models  # ensure models are imported
    Base.metadata.create_all(bind=engine)


def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency that yields a database session.
    
    This dependency:
    1. Creates a new database session
    2. Yields it to the requesting route/dependency
    3. Ensures the session is properly closed after use
    
    Usage:
        @router.get("/items")
        def get_items(db: Session = Depends(get_db)):
            return db.query(Item).all()
    
    Yields:
        Database session that will be automatically closed
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()