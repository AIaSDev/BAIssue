"""
Domain entities for the issue tracker.

This module contains pure domain logic with no external dependencies.
Following Clean Architecture:
- No framework dependencies (FastAPI, SQLAlchemy, etc.)
- Contains business rules and validation
- Center of the dependency graph (nothing depends on outer layers)
"""
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional


class IssueStatus(str, Enum):
    """
    Issue status enumeration.
    
    Valid states for an issue in the system.
    """
    OPEN = "open"
    CLOSED = "closed"


@dataclass
class Issue:
    """
    Issue domain entity.
    
    Represents a single issue in the system with its business rules.
    This is a pure domain object with no framework dependencies.
    
    Attributes:
        id: Unique identifier (None for new issues)
        title: Issue title (required, non-empty)
        body: Optional issue description
        status: Current issue status
        created_at: Timestamp when issue was created
        updated_at: Timestamp when issue was last updated
        
    Raises:
        ValueError: If title is empty or contains only whitespace
    """
    id: Optional[int]
    title: str
    body: Optional[str]
    status: IssueStatus
    created_at: datetime
    updated_at: datetime

    def __post_init__(self):
        """
        Validate domain rules after initialization.
        
        Business rule: Issue title cannot be empty.
        """
        if not self.title or not self.title.strip():
            raise ValueError("Issue title cannot be empty")