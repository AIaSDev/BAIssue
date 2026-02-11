from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.domain.issue import IssueStatus
from app.application.issue_use_cases import IssueService


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


class IssueAPI:
    def __init__(self, issue_service_dependency):
        self.router = APIRouter(prefix="/issues", tags=["issues"])
        self.issue_service_dependency = issue_service_dependency
        self._register_routes()

    def _register_routes(self):
        self.router.add_api_route(
            "",
            self._create_issue_endpoint(),
            methods=["POST"],
            response_model=IssueResponse,
            status_code=201
        )
        self.router.add_api_route(
            "",
            self._list_issues_endpoint(),
            methods=["GET"],
            response_model=List[IssueResponse]
        )
        self.router.add_api_route(
            "/{issue_id}",
            self._get_issue_endpoint(),
            methods=["GET"],
            response_model=IssueResponse
        )
        self.router.add_api_route(
            "/{issue_id}/close",
            self._close_issue_endpoint(),
            methods=["PATCH"],
            response_model=IssueResponse
        )
        self.router.add_api_route(
            "/{issue_id}/reopen",
            self._reopen_issue_endpoint(),
            methods=["PATCH"],
            response_model=IssueResponse
        )
        self.router.add_api_route(
            "/{issue_id}",
            self._delete_issue_endpoint(),
            methods=["DELETE"],
            status_code=204
        )

    def _create_issue_endpoint(self):
        def endpoint(
            payload: IssueCreate,
            service: IssueService = Depends(self.issue_service_dependency),
        ):
            return self.create_issue(payload, service)
        return endpoint

    def _list_issues_endpoint(self):
        def endpoint(
            service: IssueService = Depends(self.issue_service_dependency),
        ):
            return self.list_issues(service)
        return endpoint

    def _get_issue_endpoint(self):
        def endpoint(
            issue_id: int,
            service: IssueService = Depends(self.issue_service_dependency),
        ):
            return self.get_issue(issue_id, service)
        return endpoint

    def _close_issue_endpoint(self):
        def endpoint(
            issue_id: int,
            service: IssueService = Depends(self.issue_service_dependency),
        ):
            return self.close_issue(issue_id, service)
        return endpoint

    def _reopen_issue_endpoint(self):
        def endpoint(
            issue_id: int,
            service: IssueService = Depends(self.issue_service_dependency),
        ):
            return self.reopen_issue(issue_id, service)
        return endpoint

    def _delete_issue_endpoint(self):
        def endpoint(
            issue_id: int,
            service: IssueService = Depends(self.issue_service_dependency),
        ):
            return self.delete_issue(issue_id, service)
        return endpoint

    def create_issue(self, payload: IssueCreate, service: IssueService):
        try:
            return service.create_issue(payload.title, payload.body)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    def list_issues(self, service: IssueService):
        return service.list_issues()

    def get_issue(self, issue_id: int, service: IssueService):
        issue = service.get_issue(issue_id)
        if issue is None:
            raise HTTPException(status_code=404, detail="Issue not found")
        return issue

    def close_issue(self, issue_id: int, service: IssueService):
        issue = service.close_issue(issue_id)
        if issue is None:
            raise HTTPException(status_code=404, detail="Issue not found")
        return issue

    def reopen_issue(self, issue_id: int, service: IssueService):
        issue = service.reopen_issue(issue_id)
        if issue is None:
            raise HTTPException(status_code=404, detail="Issue not found")
        return issue

    def delete_issue(self, issue_id: int, service: IssueService):
        if not service.delete_issue(issue_id):
            raise HTTPException(status_code=404, detail="Issue not found")
