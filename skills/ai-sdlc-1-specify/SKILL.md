---
name: ai-sdlc-1-specify
description: Create or update a minimal use case specification.
---

# PHASE 1 — SPECIFY

## Goal

Create or update a **minimal use case specification**.

---

## Input

User story or feature description.

If missing → ask the user.

---

## Use Case File

docs/specs/UC-[NNN]-[NAME].md

Rules:

- NNN = sequential number (001, 002, …)
- NAME = short uppercase identifier
- words separated with `-`

Determine the next number by scanning:

docs/specs/

If a UC for the feature already exists → **update it instead of creating a new one**.

---

## Steps

1. Open template

docs/specs/UC-TEMPLATE.md

2. Create or update the UC with minimal content:

Intent  
Actors  
Preconditions  
Flow  
Errors  
Acceptance  
Tests

Do not add unnecessary text.

---

## Rules

- Prefer **updating existing UC files**.
- Create a new UC only if none exists.
- Do not invent functionality.
- Ask the user if requirements are unclear.
- Do **not generate code or tests**.

---

## Output

UC specification created or updated.

Update:

docs/TASKS.md

Set:

PHASE → 1