---
name: ai-sdlc-2-design
description: Define architecture boundaries and slice the use case into implementation tasks.
---

# PHASE 2 — DESIGN

## Goal

Translate the use case specification into a concrete architecture and task plan.

---

## Required Input

Current use case:

docs/specs/UC-[NNN]-[NAME].md

If the UC does not exist → stop and ask the user.

---

## Actions

1. Read:

docs/specs/UC-[NNN]-[NAME].md

2. Validate architecture rules in:

docs/PROJECT.md

Clean Architecture direction:

domain ← application ← interfaces ← infrastructure

3. Determine required components:

- domain entities
- application use cases
- repository interfaces (ports)
- infrastructure adapters
- API endpoints

4. Slice the implementation into **vertical tasks** in this order:

1. Integration tests  
2. Unit tests  
3. Implementation

---

## Output

Update:

docs/TASKS.md

Define tasks for the current UC.

Example:

1. Integration tests [TODO]  
2. Unit tests [TODO]  
3. Implementation [TODO]  
4. Review fixes [TODO]

Then set:

CURRENT PHASE → 3

---

## Rules

- Respect Clean Architecture dependency direction.
- Do not implement code.
- Do not generate tests yet.
- If architecture decisions are unclear → ask the user.