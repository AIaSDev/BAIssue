---
name: ai-sdlc-0-bootstrap
description: Initialize repository structure for AI-SDLC.
---

# PHASE 0 — BOOTSTRAP

## Goal

Prepare the repository for the AI-SDLC workflow.

---

## Input

Confirm with the user:

- language
- framework
- runtime

---

## Steps

1. Ensure project structure (Clean Architecture)

src/domain  
src/application  
src/interfaces  
src/infrastructure  

tests/unit  
tests/integration  
tests/e2e  

Create missing directories only.

---

2. Ensure dependency manager

Check if one exists:

requirements.txt  
pyproject.toml  
package.json  

Create only if missing.

---

3. Ensure documentation

Update if present:

docs/PROJECT.md

Add minimal:

- architecture
- run command
- dependencies

Create file only if missing.

---

## Output

Repository ready for AI-SDLC.

Update:

docs/TASKS.md

Set:

PHASE → 1