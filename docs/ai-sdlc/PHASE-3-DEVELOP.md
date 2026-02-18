# PHASE 3 — DEVELOP

**Goal:** Implement the current UC via strict test-first development.

## Order (per task)
1) Integration test (boundary behaviour)  
2) Unit tests (domain + use case)  
3) Code (Red → Green → Refactor)  
4) Review (offer review after each step)

## Actions
- Write/adjust integration tests for the UC boundary.
- Write failing unit tests (domain + application).
- Generate minimal code to pass unit tests.
- Run unit tests locally after code generation: `pytest -q tests/unit`.
- Refactor with tests green.

## AI-assisted test creation
- Variant A: Spec → Agent → Review
- Variant B: Comment → Completion → Refine

## Output
- Unit tests green locally; integration tests updated.
- Update docs/TASKS.md and set to **CURRENT PHASE = 4** when ready.