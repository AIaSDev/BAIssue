# PROJECT.md

## Purpose
Short description of this repository (1–2 sentences).

## Architecture (Clean Architecture)
Dependency direction: **domain ← application ← interfaces ← infrastructure**

Suggested layout:
- `src/domain/` — entities + pure domain rules (no framework imports)
- `src/application/` — use cases + ports
- `src/interfaces/` — API, controllers, presenters
- `src/infrastructure/` — DB, external services, framework adapters

## Tests (Testing Pyramid)
- `tests/unit/` — domain + application (fast, most tests)
- `tests/integration/` — interface ↔ infra boundaries (DB/API contracts)
- `tests/e2e/` — full system flows against a built artifact

## Run
- Install: (add project-specific steps)
- Test: `pytest -q`
- Start: (add command)

## Dependencies
List the primary frameworks/libraries and where they are declared (e.g., requirements.txt / pyproject.toml).