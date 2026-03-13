# AGENTS.md — AI‑SDLC Router

Do not modify this file. Repository state lives in `docs/TASKS.md`.

## Current Phase
See `docs/TASKS.md`.

Valid phases:
- 0 BOOTSTRAP
- 1 SPECIFY
- 2 DESIGN
- 3 DEVELOP
- 4 VALIDATE
- 5 DEPLOY

## Context Load Order
1. docs/TASKS.md
2. docs/PROJECT.md
3. docs/specs/UC-[XXX].md

## Phase → Skill Mapping

- 0 BOOTSTRAP → skills/ai-sdlc-0-bootstrap  
- 1 SPECIFY   → skills/ai-sdlc-1-specify  
- 2 DESIGN    → skills/ai-sdlc-2-design  
- 3 DEVELOP   → skills/ai-sdlc-3-develop  
- 4 VALIDATE  → skills/ai-sdlc-4-validate  
- 5 DEPLOY    → skills/ai-sdlc-5-deploy

## Commands

Unit + Integration (CI parity)
- pytest -q

Full pyramid
- pytest -q tests/unit tests/integration tests/e2e

Build container
- docker build -t app:local .

Run container
- docker run --rm -p 8000:8000 app:local

## Guardrails

- TDD first (tests before code)
- Testing pyramid guideline: Unit ~70%, Integration ~20%, E2E ~10%
- Clean Architecture direction: domain ← application ← interfaces ← infrastructure
- No merge without green CI
- Prefer vertical slices (one UC end‑to‑end)

If phase, UC, or architecture is unclear → ask targeted questions.