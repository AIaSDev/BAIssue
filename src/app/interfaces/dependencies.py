"""
Dependency injection wiring for the application layer.

This module defines factory functions that wire together
the application's dependencies using FastAPI's Depends mechanism.
"""
from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.issue_use_cases import IssueService
from app.infrastructure.database import get_db
from app.infrastructure.persistence.sqlalchemy_repository import SQLAlchemyIssueRepository


def get_issue_service(db: Session = Depends(get_db)) -> IssueService:
    """
    Factory function that creates and configures an IssueService.
    
    This is a FastAPI dependency that:
    1. Receives a database session via Depends(get_db)
    2. Creates a SQLAlchemyIssueRepository with the session
    3. Returns an IssueService with the repository injected
    
    Usage in FastAPI routes:
        @router.get("/issues")
        def list_issues(service: IssueService = Depends(get_issue_service)):
            return service.list_issues()
    
    Args:
        db: Database session injected by FastAPI via Depends(get_db)
        
    Returns:
        Configured IssueService instance with injected repository
    """
    repo = SQLAlchemyIssueRepository(db)
    return IssueService(repo)