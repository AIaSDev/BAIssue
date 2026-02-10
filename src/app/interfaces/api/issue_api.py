"""
FastAPI router for issue management endpoints.

This is the presentation layer in Clean Architecture.
It depends on the application layer (services) via dependency injection.

Dependency Injection:
- Route handlers receive IssueService via FastAPI's Depends mechanism
- The actual service construction is handled by get_issue_service factory
- No direct instantiation of dependencies in route handlers
"""
from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.domain.issue import IssueStatus
from app.interfaces.dependencies import get_issue_service
from app.application.issue_use_cases import IssueService

router = APIRouter(prefix="/issues", tags=["issues"])


class IssueCreate(BaseModel):
    """Request model for creating an issue."""
    title: str
    body: Optional[str] = None


class IssueResponse(BaseModel):
    """Response model for issue data."""
    id: int
    title: str
    body: Optional[str]
    status: IssueStatus
    created_at: datetime
    updated_at: datetime


@router.post("", response_model=IssueResponse, status_code=201)
def create_issue(
    payload: IssueCreate,
    service: IssueService = Depends(get_issue_service),
):
    """
    Create a new issue.
    
    The IssueService is injected via FastAPI's Depends mechanism.
    """
    try:
        return service.create_issue(payload.title, payload.body)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("", response_model=List[IssueResponse])
def list_issues(
    service: IssueService = Depends(get_issue_service),
):
    """
    List all issues.
    
    The IssueService is injected via FastAPI's Depends mechanism.
    """
    return service.list_issues()


@router.get("/{issue_id}", response_model=IssueResponse)
def get_issue(
    issue_id: int,
    service: IssueService = Depends(get_issue_service),
):
    """
    Get a single issue by ID.
    
    The IssueService is injected via FastAPI's Depends mechanism.
    """
    issue = service.get_issue(issue_id)
    if issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")
    return issue


@router.patch("/{issue_id}/close", response_model=IssueResponse)
def close_issue(
    issue_id: int,
    service: IssueService = Depends(get_issue_service),
):
    """
    Close an issue.
    
    The IssueService is injected via FastAPI's Depends mechanism.
    """
    issue = service.close_issue(issue_id)
    if issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")
    return issue


@router.patch("/{issue_id}/reopen", response_model=IssueResponse)
def reopen_issue(
    issue_id: int,
    service: IssueService = Depends(get_issue_service),
):
    """
    Reopen a closed issue.
    
    The IssueService is injected via FastAPI's Depends mechanism.
    """
    issue = service.reopen_issue(issue_id)
    if issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")
    return issue


@router.delete("/{issue_id}", status_code=204)
def delete_issue(
    issue_id: int,
    service: IssueService = Depends(get_issue_service),
):
    """
    Delete an issue.
    
    The IssueService is injected via FastAPI's Depends mechanism.
    """
    if not service.delete_issue(issue_id):
        raise HTTPException(status_code=404, detail="Issue not found")