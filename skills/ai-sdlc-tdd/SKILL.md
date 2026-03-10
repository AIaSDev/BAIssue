---
name: ai-sdlc-tdd
description: Execute strict Test-Driven Development during AI-SDLC Phase 3 (DEVELOP).
---

# TDD Loop Skill

Use this skill in **Phase 3 — DEVELOP**.

## Goal
Implement the current use case with strict test-first development.

## Order
1. Integration tests
2. Unit tests
3. Code generation
4. Review

## TDD Loop
### RED
- Write or adjust a failing unit test in `tests/unit/`.
- Run the unit tests and confirm failure for the intended reason.

### GREEN
- Implement the smallest possible change in `src/` to satisfy the failing test.
- Run the unit tests again and confirm success.

### REFACTOR
- Improve naming, duplication, and structure without changing behavior.
- Re-run the unit tests and keep them green.

## Integration First
Before the unit-level TDD loop:
- Write or adjust integration tests in `tests/integration/`.
- Use the current UC spec and acceptance criteria.
- Verify interface and persistence behavior.

## Review Checkpoint
Offer a review after each step:
- after integration tests
- after unit tests
- after code generation
- after refactoring

## Commands
- Unit tests: `pytest -q tests/unit`
- Integration tests: `pytest -q tests/integration`
- Full pyramid: `pytest -q tests/unit tests/integration tests/e2e`

## Rules
- Do not generate implementation before tests exist.
- Keep tests deterministic and fast.
- Respect Clean Architecture boundaries.
- Domain code must not import framework code.
- Stop and ask if acceptance criteria are ambiguous.

## Expected Result
- Integration tests updated
- Unit tests green locally
- Minimal implementation complete
- Code reviewed before Phase 4