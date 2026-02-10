from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.issue_use_cases import IssueService
from app.infrastructure.database import get_db
from app.infrastructure.persistence.sqlalchemy_repository import SQLAlchemyIssueRepository


def get_issue_service(db: Session = Depends(get_db)) -> IssueService:
    repo = SQLAlchemyIssueRepository(db)
    return IssueService(repo)