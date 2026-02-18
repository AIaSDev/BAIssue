# PHASE 2 — DESIGN

**Goal:** Define architecture, boundaries, and task slicing for the current UC.

## Actions
- Validate docs/PROJECT.md (Clean Architecture direction).
- Confirm framework + libraries (ask proactively if missing).
- Identify ports/adapters needed (interfaces ↔ infrastructure).
- Slice UC into vertical tasks in docs/TASKS.md:
  Integration test(s) → Unit tests → Implementation.

## Output
- Architecture stable (or revised in docs/PROJECT.md).
- Update docs/TASKS.md and set to **CURRENT PHASE = 3**.

## Clean Architecture Rules
- domain has no framework imports
- infrastructure depends inward
- no circular deps; refactor violations immediately