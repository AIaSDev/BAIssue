---
name: ai-sdlc-1-specify
description: Convert a user story into a structured use case specification.
---

# PHASE 1 — SPECIFY

## Goal
Transform a user story into a **structured use case specification**.

## Required Input
User story or feature description.

If missing → ask the user before proceeding.

---

## Use Case Naming

Create files using:

docs/specs/UC-[NNN]-[NAME].md

Rules:

- NNN = next sequential number (001, 002, …)
- NAME = short uppercase identifier
- Words separated with `-`

Determine the next number by scanning existing files in:

docs/specs/

---

## Actions

1. Open template:

docs/specs/UC-TEMPLATE.md

2. Convert the user story into:

- Business intent
- Actors
- Preconditions
- Main flow
- Alternative flows
- Acceptance criteria
- Minimal NFRs

3. Map acceptance criteria to test intent:

- Unit
- Integration
- E2E

---

## Output

Create:

docs/specs/UC-[NNN]-[NAME].md

Then update:

docs/TASKS.md

Set:

CURRENT PHASE → 2

---

## Rules

- Do not invent functionality.
- Ask the user if requirements are unclear.
- Do **not** generate code or tests.