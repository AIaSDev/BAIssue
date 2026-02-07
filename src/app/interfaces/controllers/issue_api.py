from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.entities.issue import IssueStatus
from app.frameworks.persistence.sqlalchemy_repository import SQLAlchemyIssueRepository
from app.use_cases.issue_service import IssueService

router = APIRouter(prefix="/issues", tags=["issues"])


class IssueCreate(BaseModel):
    title: str
    body: Optional[str] = None


class IssueResponse(BaseModel):
    id: int
    title: str
    body: Optional[str]
    status: IssueStatus
    created_at: datetime
    updated_at: datetime


def _service(db: Session) -> IssueService:
    return IssueService(SQLAlchemyIssueRepository(db))


@router.post("", response_model=IssueResponse, status_code=201)
def create_issue(payload: IssueCreate, db: Session = Depends(get_db)):
    try:
        return _service(db).create_issue(payload.title, payload.body)
    except ValueError as e:
        raise HTTPException(400, str(e))


@router.get("", response_model=list[IssueResponse])
def list_issues(db: Session = Depends(get_db)):
    return _service(db).list_issues()


@router.get("/{issue_id}", response_model=IssueResponse)
def get_issue(issue_id: int, db: Session = Depends(get_db)):
    issue = _service(db).get_issue(issue_id)
    if issue is None:
        raise HTTPException(404, "Issue not found")
    return issue


@router.patch("/{issue_id}/close", response_model=IssueResponse)
def close_issue(issue_id: int, db: Session = Depends(get_db)):
    issue = _service(db).close_issue(issue_id)
    if issue is None:
        raise HTTPException(404, "Issue not found")
    return issue


@router.patch("/{issue_id}/reopen", response_model=IssueResponse)
def reopen_issue(issue_id: int, db: Session = Depends(get_db)):
    issue = _service(db).reopen_issue(issue_id)
    if issue is None:
        raise HTTPException(404, "Issue not found")
    return issue


@router.delete("/{issue_id}", status_code=204)
def delete_issue(issue_id: int, db: Session = Depends(get_db)):
    if not _service(db).delete_issue(issue_id):
        raise HTTPException(404, "Issue not found")