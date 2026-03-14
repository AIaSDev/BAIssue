---
name: ai-sdlc-0-bootstrap
description: Initialize repository structure and architecture baseline.
---

# PHASE 0 — BOOTSTRAP

## Goal
Initialize a repository for the **AI-SDLC workflow**.

---

## Required Input

Confirm with the user:

- language
- framework
- runtime

---

## Steps

1. Create project structure (Clean Architecture)

src/domain/  
src/application/  
src/interfaces/  
src/infrastructure/

tests/unit/  
tests/integration/  
tests/e2e/

2. Initialize dependency manager

Examples:

- requirements.txt
- pyproject.toml
- package.json

3. Initialize documentation

Update:

docs/PROJECT.md

Add:

- architecture overview
- run commands
- dependencies

---

## Output

Repository initialized.

Update:

docs/TASKS.md

Set:

CURRENT PHASE → 1