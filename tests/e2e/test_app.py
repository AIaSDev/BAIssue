import os
import time
import httpx
import pytest

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8001")


@pytest.fixture(scope="session")
def client():
    # simple wait loop (container startup)
    for _ in range(30):
        try:
            r = httpx.get(f"{BASE_URL}/health", timeout=1)
            if r.status_code == 200:
                break
        except Exception:
            time.sleep(0.5)
    else:
        raise RuntimeError("API did not start")

    with httpx.Client(base_url=BASE_URL) as c:
        yield c


def test_create_issue(client):
    r = client.post("/issues", json={"title": "E2E Issue"})
    assert r.status_code == 201
    data = r.json()
    assert data["title"] == "E2E Issue"
    assert data["status"] == "open"


def test_close_issue(client):
    r = client.post("/issues", json={"title": "Closable"})
    issue_id = r.json()["id"]

    r = client.patch(f"/issues/{issue_id}/close")
    assert r.status_code == 200
    assert r.json()["status"] == "closed"


def test_delete_issue(client):
    r = client.post("/issues", json={"title": "Delete me"})
    issue_id = r.json()["id"]

    r = client.delete(f"/issues/{issue_id}")
    assert r.status_code == 204