---
name: ai-sdlc-3-develop
description: Implement the current use case via strict Test-Driven Development.
---

# PHASE 3 — DEVELOP

## Goal

Implement the current use case using **strict Test-Driven Development (TDD)**.

---

## Source of Truth

Current UC:

docs/TASKS.md

Use case specification:

docs/specs/UC-[NNN]-[NAME].md

Architecture reference:

docs/PROJECT.md

---

## Test Derivation

Generate tests directly from the UC specification.

Mapping:

Acceptance Criteria → Integration tests  
Domain rules → Unit tests  
Use case logic → Unit tests

Test locations:

tests/integration/  
tests/unit/

Each acceptance criterion must be covered by **at least one integration test**.

If related tests already exist → **extend the existing test file instead of creating a new one**.

---

## Execution Order

1. Integration tests (system boundary)  
2. Unit tests (domain + application)  
3. Implementation  
4. Refactor

---

## TDD Loop

RED  
Write failing tests.

GREEN  
Implement minimal code to satisfy tests.

REFACTOR  
Improve structure without changing behaviour.

---

## Commands

Run unit tests

pytest -q tests/unit

Run integration tests

pytest -q tests/integration

Run full test pyramid

pytest -q tests/unit tests/integration tests/e2e

---

## Rules

- Never implement code before tests exist.
- Tests must be deterministic and fast.
- Prefer extending existing test files instead of creating duplicates.
- Respect Clean Architecture boundaries.
- Domain must not import frameworks.
- Infrastructure must depend inward.
- If acceptance criteria are unclear → ask the user.

---

## Output

- Integration tests created or updated
- Unit tests green locally
- Minimal implementation complete

Update:

docs/TASKS.md

Set:

CURRENT PHASE → 4