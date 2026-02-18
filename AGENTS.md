# AGENTS.md — AI-SDLC Router

Do not modify this file. Repo status lives in docs/TASKS.md.

## Current Phase
See docs/TASKS.md

Valid phases: 1 SPECIFY, 2 DESIGN, 3 DEVELOP, 4 VALIDATE, 5 DEPLOY.

## Context Load Order
1. docs/TASKS.md
2. docs/PROJECT.md
3. docs/ai-sdlc/PHASE-[X-NAME].md (current phase indicated in docs/TASKS.md)
4. docs/specs/UC-[XXX].md (current use case indicated in docs/TASKS.md)

## Commands
- Unit + Integration (CI parity): `pytest -q`
- Full pyramid locally: `pytest -q tests/unit tests/integration tests/e2e`
- Build container: `docker build -t app:local .`
- Run container: `docker run --rm -p 8000:8000 app:local`

## Guardrails
- TDD first (tests before code).
- Testing Pyramid guideline: Unit ~70%, Integration ~20%, E2E ~10%.
- Clean Architecture dependency direction: domain ← application ← interfaces ← infrastructure.
- No merge without green CI.
- Prefer small vertical slices (one UC end-to-end).

If the phase, UC, spec, or architecture is unclear: stop and ask targeted questions.