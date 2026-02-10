"""
Issue repository port (abstract interface).

This module defines the repository interface (port) for issue persistence.
Concrete implementations are provided in the infrastructure layer.

Following the Dependency Inversion Principle:
- The application layer depends on this abstraction
- Infrastructure layer implements this abstraction
- Dependencies point inward (toward the domain/application)
"""
from abc import ABC, abstractmethod
from typing import Optional

from app.domain.issue import Issue, IssueStatus


class IssueRepository(ABC):
    """
    Abstract repository interface for issue persistence.
    
    This is a port in Clean Architecture terminology.
    It defines the contract for issue storage without
    specifying implementation details.
    """
    
    @abstractmethod
    def create(self, issue: Issue) -> Issue:
        """
        Create a new issue.
        
        Args:
            issue: Issue entity to create (id should be None)
            
        Returns:
            Created issue with assigned id
        """
        ...

    @abstractmethod
    def get_by_id(self, issue_id: int) -> Optional[Issue]:
        """
        Retrieve an issue by its ID.
        
        Args:
            issue_id: Unique identifier of the issue
            
        Returns:
            Issue entity if found, None otherwise
        """
        ...

    @abstractmethod
    def list_all(self) -> list[Issue]:
        """
        Retrieve all issues.
        
        Returns:
            List of all issue entities
        """
        ...

    @abstractmethod
    def set_status(self, issue_id: int, status: IssueStatus) -> Optional[Issue]:
        """
        Update the status of an issue.
        
        Args:
            issue_id: Unique identifier of the issue
            status: New status to set
            
        Returns:
            Updated issue if found, None otherwise
        """
        ...

    @abstractmethod
    def delete(self, issue_id: int) -> bool:
        """
        Delete an issue.
        
        Args:
            issue_id: Unique identifier of the issue
            
        Returns:
            True if issue was deleted, False if not found
        """
        ...