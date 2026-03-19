import pytest

from app.domain.entities import IssueStatus
from app.application.use_cases import IssueService
from in_memory_repository import InMemoryRepository


def test_create_issue_default_status_open():
    repo = InMemoryRepository()
    svc = IssueService(repo)

    issue = svc.create_issue("Test")
    assert issue.status == IssueStatus.OPEN


def test_close_issue():
    repo = InMemoryRepository()
    svc = IssueService(repo)

    issue = svc.create_issue("Test")
    closed = svc.close_issue(issue.id)

    assert closed.status == IssueStatus.CLOSED


def test_reopen_issue():
    repo = InMemoryRepository()
    svc = IssueService(repo)

    issue = svc.create_issue("Test")
    svc.close_issue(issue.id)
    reopened = svc.reopen_issue(issue.id)

    assert reopened.status == IssueStatus.OPEN


def test_delete_issue():
    repo = InMemoryRepository()
    svc = IssueService(repo)

    issue = svc.create_issue("Test")
    assert svc.delete_issue(issue.id) is True
    assert svc.get_issue(issue.id) is None


def test_delete_issue_not_found():
    repo = InMemoryRepository()
    svc = IssueService(repo)

    assert svc.delete_issue(999) is False


def test_create_issue_empty_title_raises():
    repo = InMemoryRepository()
    svc = IssueService(repo)

    with pytest.raises(ValueError):
        svc.create_issue("")