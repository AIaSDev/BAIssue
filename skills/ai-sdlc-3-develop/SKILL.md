---
name: ai-sdlc-3-develop
description: Implement the current use case via strict Test-Driven Development.
---

# PHASE 3 — DEVELOP

## Goal
Implement the current use case using strict TDD.

Source of truth:
docs/specs/UC-[XXX].md

Architecture reference:
docs/PROJECT.md

---

## Test Derivation (from UC)

Generate tests directly from the UC specification.

Acceptance Criteria → Integration tests  
Domain rules → Unit tests  
Use case logic → Unit tests

Locations:

tests/integration/  
tests/unit/

Each acceptance criterion should be covered by at least one integration test.

---

## Order

1. Integration tests (boundary behaviour)  
2. Unit tests (domain + application)  
3. Code (Red → Green → Refactor)  
4. Review

---

## TDD Loop

RED  
Write failing unit tests.

GREEN  
Implement minimal code to satisfy tests.

REFACTOR  
Improve structure without changing behaviour.

---

## Commands

Unit tests

pytest -q tests/unit

Integration tests

pytest -q tests/integration

Full pyramid

pytest -q tests/unit tests/integration tests/e2e

---

## Rules

- Do not implement code before tests exist.
- Tests must be deterministic and fast.
- Respect Clean Architecture boundaries.
- Domain must not import frameworks.
- If acceptance criteria are unclear → ask questions.

---

## Output

- Integration tests created/updated
- Unit tests green locally
- Minimal implementation complete

Update docs/TASKS.md → CURRENT PHASE = 4