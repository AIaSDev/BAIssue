---
name: ai-sdlc-3-develop
description: Implement the current use case using strict TDD.
---

# PHASE 3 — DEVELOP

## Goal

Implement the current use case using **Test-Driven Development**.

---

## Source of Truth

docs/TASKS.md  
docs/specs/UC-[NNN]-[NAME].md  
docs/PROJECT.md

---

## Test Derivation

Derive tests from the UC.

Acceptance → Integration tests  
Domain rules → Unit tests  
Use case logic → Unit tests  

Locations

tests/integration  
tests/unit  

Prefer **extending existing test files**.

Create new files only if necessary.

---

## Order

1. Integration tests  
2. Unit tests  
3. Implementation

Follow TDD:

RED → GREEN → REFACTOR

---

## Commands

Run unit tests

`pytest -q tests/unit`

---

## Rules

- Tests before code.
- Keep code minimal.
- Avoid unnecessary comments.
- Prefer updating existing tests and code.
- Respect Clean Architecture  

  domain ← application ← interfaces ← infrastructure

- Ask the user if requirements are unclear.

---

## Output

Implementation complete.

Unit tests pass.

Update:

docs/TASKS.md

Set:

PHASE → 3