---
name: ai-sdlc-2-design
description: Determine minimal architecture components for the current use case.
---

# PHASE 2 — DESIGN

## Goal

Identify the **minimal architecture components** required for the current use case.

Do not generate implementation details.

---

## Input

Current use case

docs/specs/UC-[NNN]-[NAME].md

Architecture reference

docs/PROJECT.md

If the UC does not exist → ask the user.

---

## Steps

1. Read the use case.

2. Determine required components:

domain  
application  
interfaces  
infrastructure  

Examples:

- domain entity
- use case service
- repository interface
- persistence adapter
- API endpoint

3. Ensure the architecture in `docs/PROJECT.md` is sufficient.

Update it **only if necessary**.

Prefer **extending existing artifacts** instead of creating new ones.

---

## Rules

- Respect Clean Architecture  

  domain ← application ← interfaces ← infrastructure

- Do not implement code.
- Do not generate tests.
- Keep architecture descriptions minimal.

---

## Output

Architecture verified or minimally updated.

Update:

docs/TASKS.md

Set:

PHASE → 2