# PROJECT.md

## Purpose

BAIssue is a minimal FastAPI issue tracker for teaching Clean Architecture,
test-first development and the AI-SDLC in a working application. It supports
SQLite for development and CI and PostgreSQL for production.

This repository is a reference implementation. New student projects should
start from the [AI-SDLC project template](https://github.com/AIaSDev/ai-sdlc-template).
The canonical human-readable method documentation is maintained in
[AISL Docs](https://docs.aisl.science/learning-and-resources/ai-sdlc).

## Architecture

Dependencies point inward:

`domain ← application ← interfaces ← infrastructure`

- `src/app/domain` contains domain entities and rules.
- `src/app/application` contains use cases and repository interfaces.
- `src/app/interfaces` contains the HTTP boundary.
- `src/app/infrastructure` contains configuration, persistence and web wiring.

## Structure

- `docs/specs/` — executable use-case specifications
- `tests/unit/` — domain and application tests
- `tests/integration/` — API and persistence integration tests
- `tests/e2e/` — container-based end-to-end tests
- `.github/workflows/` — CI, release and manual deployment workflows

## Commands

Install:

```bash
pip install -r requirements.txt
```

Test:

```bash
export PYTHONPATH=$PWD/src
pytest -q tests/unit tests/integration
```

Start:

```bash
export PYTHONPATH=$PWD/src
python -m uvicorn app.main:app --reload
```

## Dependencies

Declared in `requirements.txt`. Runtime configuration is supplied through
environment variables; never commit credentials or `.env` files.
