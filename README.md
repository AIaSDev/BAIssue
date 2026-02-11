# BAIssue

A minimal **FastAPI** issue tracker (Business AI wordplay) demonstrating **Clean Architecture** with **SQLite** (development & CI) and **PostgreSQL** (production) support.

## What is this?

**BAIssue** is a small REST API for managing issues (a minimal subset of GitHub Issues). It is designed primarily for **education** and demonstrates:

- Clean Architecture terminology and layering
- Clear separation of concerns
- Testability (unit tests + integration tests + optional E2E tests)
- Minimal configuration and tooling
- CI, tag-based releases, and manual CD with Docker + Render

## Architecture overview

The project follows **Clean Architecture**, with dependencies pointing inward.

```
src/app/
├── domain/                         # Pure domain entities
│   └── issue.py                    # Issue entity with validation and status
├── application/                    # Application services (business logic)
│   ├── issue_use_cases.py          # Issue use cases / business logic
│   └── repositories/               # Repository interfaces
│       └── issue_repository.py
├── interfaces/
│   └── api/                        # HTTP layer (FastAPI router)
│       └── issue_api.py            # API routes with service creation
├── infrastructure/
│   ├── config.py                   # Environment-based configuration (.env optional)
│   ├── database.py                 # SQLAlchemy engine, session, Base
│   ├── persistence/                # Database implementations
│   │   ├── sqlalchemy_models.py    # SQLAlchemy ORM models
│   │   └── sqlalchemy_repository.py
│   └── web/                        # FastAPI application wiring
│       ├── app.py                  # App factory and wiring
│       └── static/                 # Minimal static web UI
│           └── index.html
└── main.py                         # Application entry point
```

### Dependency rule

- **Domain** and **application** layers do not depend on FastAPI or SQLAlchemy.
- **Interfaces** define boundaries and dependency injection points.
- **Infrastructure** implements technical details (web server, database, persistence).

## Web UI and API docs

| Path | Purpose |
|------|---------|
| `/ui` | Minimal web interface (HTML + JavaScript) |
| `/docs` | Swagger / OpenAPI documentation |
| `/` | Redirects to `/ui` |
| `/health` | Simple health check |

The UI is intentionally minimal and exists only to demonstrate API consumption.

## API endpoints

### Issues

- `POST /issues` – Create an issue
- `GET /issues` – List all issues
- `GET /issues/{issue_id}` – Get a single issue
- `DELETE /issues/{issue_id}` – Delete an issue
- `PATCH /issues/{issue_id}/close` – Close an issue
- `PATCH /issues/{issue_id}/reopen` – Reopen an issue

Issue status is represented using an enum:

```
open | closed
```

## Environment configuration

Configuration is done **exclusively via environment variables**. A `.env` file is optional; if present, it can be loaded via `python-dotenv`. If it does not exist, the app still runs with defaults.

### Example `.env`

```dotenv
# -------------------------------------------------
# Database configuration
# -------------------------------------------------
# Development (SQLite file)
# DATABASE_URL=sqlite:///./app.db

# CI / Integration tests (SQLite in-memory)
# DATABASE_URL=sqlite:///:memory:

# Production (PostgreSQL)
DATABASE_URL=postgresql://user:password@host:5432/baissue
```

Notes:
- Many providers use `postgresql://...` (or legacy `postgres://...`). The app normalizes these to SQLAlchemy’s driver URL internally.
- **Never commit `.env`** (keep it in `.gitignore`).

## Running locally

### Prerequisites
- Python 3.11+
- pip

### Installation

```bash
pip install -r requirements.txt
```

### Start the application

By default, SQLite is used (`app.db`):

```bash
export PYTHONPATH=$PWD/src
uvicorn app.main:app --reload
```

Open:
- UI: http://localhost:8000/ui
- API docs: http://localhost:8000/docs

## Testing

### Unit tests
- No FastAPI
- No SQLAlchemy
- Uses a fake in-memory repository

```bash
export PYTHONPATH=$PWD/src
pytest -q tests/unit
```

### Integration tests
- FastAPI TestClient (requires `httpx`)
- SQLite in-memory database

```bash
export PYTHONPATH=$PWD/src
export DATABASE_URL=sqlite:///:memory:
pytest -q tests/integration
```

### E2E tests (Docker-based)
E2E tests run against a **running Docker container** via real HTTP (using `httpx`).

```bash
export BASE_URL=http://127.0.0.1:8001
pytest -q tests/e2e
```

In CI, the E2E job:
1) builds the Docker image  
2) runs the container on port 8001  
3) executes `pytest -q tests/e2e`  

## Docker

### Build
```bash
docker build -t baissue .
```

### Run (SQLite)
```bash
docker run -p 8000:8000 baissue
```

### Run (PostgreSQL)
```bash
docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql://user:password@host:5432/baissue \
  baissue
```

## CI, releases, and CD

### Continuous integration
Workflow: **`.github/workflows/ci.yml`**
- Unit tests
- Integration tests (SQLite in-memory)
- Optional E2E tests (Docker-based)

### Releases & images (GHCR)
Workflow: **`.github/workflows/release.yml`**
- Tag-based releases: push a tag `vX.Y.Z`
- Creates a GitHub Release (auto-generated notes)
- Publishes Docker images to **GitHub Container Registry (GHCR)**

```bash
git tag v0.1.0
git push origin v0.1.0
```

Images:
- `ghcr.io/<owner>/baissue:v0.1.0`
- `ghcr.io/<owner>/baissue:latest`

### Manual continuous deployment (Render)
Workflow: **`.github/workflows/cd-render.yml`**
- Deployment is **manual** (`workflow_dispatch`)
- Render deploys the **latest GHCR image**
- Triggered via a **Render Deploy Hook** URL stored as a GitHub secret

## License

This project is intended for **educational use**.