---
name: ai-sdlc-0-bootstrap
description: Initialize or align a repository for AI-SDLC based on the intended system.
---

# PHASE 0 — BOOTSTRAP

## Goal

Align the repository with the **intended system** and prepare it for AI-SDLC.

---

## Required Input

Clarify with the user:

- system / app purpose
- language
- framework
- runtime

If unclear → ask before proceeding.

---

## Actions

### 1. Inspect repository

Check existing:

- structure (src/, tests/, docs/)
- dependency files
- existing code and tests

---

### 2. Align structure (minimal changes)

Ensure Clean Architecture:

src/app/domain  
src/app/application  
src/app/interfaces  
src/app/infrastructure  

tests/unit  
tests/integration  
tests/e2e  

Rules:

- create only missing directories
- reuse existing structure if compatible
- do not duplicate or restructure unnecessarily

---

### 3. Dependencies

Check for:

requirements.txt  
pyproject.toml  
package.json  

Rules:

- reuse if present
- create minimal file only if missing

---

### 4. Documentation

Ensure:

docs/PROJECT.md

Rules:

- update if exists
- create minimal version if missing

Content:

- system purpose
- architecture
- run command

---

### 5. Cleanup (only with user confirmation)

Identify:

- unused files
- irrelevant boilerplate
- mismatching structure

Ask the user before removing anything.

---

## Output

Repository aligned with intended system.

Update:

docs/TASKS.md

Set:

CURRENT PHASE → 1

---

## Rules

- Prefer adapting existing artifacts over creating new ones.
- Keep all artifacts minimal.
- Do not remove files without explicit user confirmation.
- Ask if the system scope or architecture is unclear.