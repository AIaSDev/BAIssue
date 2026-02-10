"""
Issue use cases (application services).

This module contains the business logic for issue management.
Following Clean Architecture:
- Depends only on domain entities and repository interfaces (ports)
- Independent of frameworks (FastAPI, SQLAlchemy)
- Contains the core application rules

Dependency Injection:
- IssueService receives IssueRepository via constructor injection
- Does NOT create its own repository (follows DI principles)
"""
from datetime import datetime, timezone
from typing import Optional

from app.domain.issue import Issue, IssueStatus
from app.application.repositories.issue_repository import IssueRepository


class IssueService:
    """
    Application service for issue management.
    
    This service orchestrates business operations on issues.
    It depends on the IssueRepository abstraction (port),
    not on concrete implementations.
    
    Constructor injection ensures dependencies are provided externally,
    making the service testable and following DI principles.
    """
    
    def __init__(self, repository: IssueRepository):
        """
        Initialize service with a repository.
        
        Args:
            repository: Issue repository implementation (injected dependency)
        """
        self.repository = repository

    def create_issue(self, title: str, body: Optional[str] = None) -> Issue:
        """
        Create a new issue with the given title and optional body.
        
        Business rules:
        - New issues start with OPEN status
        - Timestamps are set to current UTC time
        - Title is validated by the domain entity
        
        Args:
            title: Issue title (required, non-empty)
            body: Optional issue description
            
        Returns:
            Created issue with assigned ID
            
        Raises:
            ValueError: If title is empty (domain validation)
        """
        now = datetime.now(timezone.utc).replace(tzinfo=None)
        issue = Issue(
            id=None,
            title=title,
            body=body,
            status=IssueStatus.OPEN,
            created_at=now,
            updated_at=now,
        )
        return self.repository.create(issue)

    def get_issue(self, issue_id: int) -> Optional[Issue]:
        """
        Retrieve an issue by its ID.
        
        Args:
            issue_id: Unique identifier of the issue
            
        Returns:
            Issue if found, None otherwise
        """
        return self.repository.get_by_id(issue_id)

    def list_issues(self) -> list[Issue]:
        """
        Retrieve all issues.
        
        Returns:
            List of all issues
        """
        return self.repository.list_all()

    def close_issue(self, issue_id: int) -> Optional[Issue]:
        """
        Close an issue by setting its status to CLOSED.
        
        Args:
            issue_id: Unique identifier of the issue
            
        Returns:
            Updated issue if found, None otherwise
        """
        return self.repository.set_status(issue_id, IssueStatus.CLOSED)

    def reopen_issue(self, issue_id: int) -> Optional[Issue]:
        """
        Reopen a closed issue by setting its status to OPEN.
        
        Args:
            issue_id: Unique identifier of the issue
            
        Returns:
            Updated issue if found, None otherwise
        """
        return self.repository.set_status(issue_id, IssueStatus.OPEN)

    def delete_issue(self, issue_id: int) -> bool:
        """
        Delete an issue.
        
        Args:
            issue_id: Unique identifier of the issue
            
        Returns:
            True if issue was deleted, False if not found
        """
        return self.repository.delete(issue_id)