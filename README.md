# BAIssue

A minimal **FastAPI** issue tracker (Business AI wordplay) demonstrating **Clean Architecture** with **SQLite** (development & CI) and **PostgreSQL** (production) support.

This repository is the **AI-SDLC reference implementation** for the module. It is an example application to inspect and extend, not the student project template.

- [AI-SDLC method documentation](https://docs.aisl.science/learning-and-resources/ai-sdlc)
- [AI-SDLC project template](https://github.com/AIaSDev/ai-sdlc-template)
- [Module organisation](https://github.com/AIaSDev)

## Agent setup

Run `bash scripts/setup-skills.sh` from the repository root.
Choose **1** for `.agents/skills` (Copilot/Codex), **2** for `.claude/skills`,
or **3** for both. The script links to the canonical `skills/` directory and
falls back to copying if links are unavailable. Existing destinations are kept;
copies must be refreshed manually after skill changes. Verify discovery in your
agent; setup does not install or configure the agent itself.

For non-interactive setup, pass the same selection, for example `bash scripts/setup-skills.sh 1`. Selections 2 and 3 also create a missing `CLAUDE.md` containing `@AGENTS.md`; an existing file is preserved. Shared instructions and skills are not modified.

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
│   └── entities.py                 # Entities entity with validation and status
├── application/                    # Application services (business logic)
│   ├── use_cases.py                # Use cases / business logic
│   └── repositories/               # Repository interfaces
│       └── repository.py
├── interfaces/
│   └── api/                        # HTTP layer (FastAPI router)
│       └── api.py                  # API routes with service creation
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
python -m uvicorn app.main:app --reload
```

Open:
- UI: http://localhost:8000/ui
- API docs: http://localhost:8000/docs

## Testing

### Unit tests
- No FastAPI
- No SQLAlchemy
- Uses an in-memory repository for testing.

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

## AI-SDLC role

BAIssue demonstrates the complete repository-local workflow in a working Python application:

- `AGENTS.md` routes the lifecycle phases.
- `docs/TASKS.md` records the current phase and use case.
- `docs/PROJECT.md` describes the application architecture and commands.
- `docs/specs/` contains executable use-case specifications.
- `skills/ai-sdlc-*` contains the phase-specific execution guidance.

Use the [AI-SDLC template](https://github.com/AIaSDev/ai-sdlc-template) when starting a new project. Consult BAIssue for concrete architectural and testing examples.

## Example AI-SDLC walkthrough

The following prompts show one complete AI-SDLC pass through this reference
application. They are deliberately small: each phase reads the repository
state, performs only the work belonging to that phase and updates the relevant
workflow artefact.

The examples explicitly name the shared instructions, phase and skill so each prompt can be used independently. A configured agent may load instructions and discover skills automatically. `Use skill:` is a plain-language request, not a universal tool command; the canonical `skills/.../SKILL.md` path identifies the same guidance. Execute only the selected phase and review its output before selecting the next.

### 0. Bootstrap the project

```text
Follow AGENTS.md.

Execute phase 0 BOOTSTRAP.

System:
Extend the existing issue tracker.

Constraints:
- Prefer adapting existing structure and files
- Do not create unnecessary files
- Ask before removing anything
- Keep all artifacts minimal

Use skill: ai-sdlc-0-bootstrap
```

Expected result: the application context and architecture are recorded in
`docs/PROJECT.md`. After verification, `docs/TASKS.md` records
`PHASE: 0` and `STATUS: done`. Select SPECIFY explicitly next,
with `PHASE: 1` and `STATUS: ready`.

### 1. Specify a use case

```text
Follow AGENTS.md.

Execute phase 1 SPECIFY.

User story:
Users can add comments to an issue via the REST API and web app.
A comment contains text, author name, and timestamp.
Users can list comments for an issue.

Use skill: ai-sdlc-1-specify
```

Expected result: one executable use-case specification is created or updated
in `docs/specs/`, including scope, acceptance criteria and test intent. No code
is generated in this phase.

### 2. Design the slice

```text
Follow AGENTS.md.

Execute phase 2 DESIGN for the current use case.

Use skill: ai-sdlc-2-design
```

Expected result: the required domain, application, interface and infrastructure
components are identified and `docs/PROJECT.md` is updated if needed.
Slicing the work into vertical tasks in `docs/TASKS.md` is recommended,
but is not an explicit output of the DESIGN skill.

### 3. Develop with TDD

```text
Follow AGENTS.md.

Execute phase 3 DEVELOP for the current use case.

Use skill: ai-sdlc-3-develop
```

Expected result: integration tests, unit tests and implementation are produced
in that order. The tests are derived from the acceptance criteria and the
domain rules.

### 4. Validate the release

```text
Follow AGENTS.md.

Execute phase 4 VALIDATE for the current use case.

Use skill: ai-sdlc-4-validate
```

Expected result: local tests, end-to-end tests, the container build and the
GitHub Actions workflows provide release evidence.

### 5. Deploy the validated artifact

```text
Follow AGENTS.md.

Execute phase 5 DEPLOY for the current use case.

Use skill: ai-sdlc-5-deploy

CD workflow: .github/workflows/cd-render.yml
```

Expected result: deployment triggers, required secrets, post-deployment checks
and recovery expectations are documented before deployment is run.

### Working principle

```text
Specification → Tests → Code → Validation → Release → Deployment
```

The prompts are examples for this reference application. For a new project,
replace the system description, user story, technology-specific commands and
deployment workflow with the project context recorded in `docs/PROJECT.md`.

## License

This project is intended for **educational use**.
