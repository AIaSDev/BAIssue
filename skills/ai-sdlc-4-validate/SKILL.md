---
name: ai-sdlc-4-validate
description: Verify repository readiness for release.
---

# PHASE 4 — VALIDATE

## Goal

Verify that the repository is **release-ready**.

Focus on **checking existing artifacts**.

---

## Source of Truth

docs/TASKS.md  
docs/PROJECT.md  

---

## Steps

### 1. Run Local Tests

Run

`pytest -q tests/unit tests/integration`

Verify:

- unit tests pass
- integration tests pass

---

### 2. Verify E2E Tests

Check:

tests/e2e/

Extend existing tests if needed.

Create tests only if none exist.

---

### 3. Verify Dockerfile

Check:

Dockerfile

Verify the container builds and starts the application.

Create only if missing.

---

### 4. Verify CI

Check:

.github/workflows/ci.yml

CI should run:

- unit tests  
- integration tests

Create only if missing.

---

### 5. Verify Release Workflow

Check:

.github/workflows/release.yml

Verify it:

- builds the container
- runs E2E tests
- publishes the artifact

Create only if missing.

---

## Rules

- Prefer **verifying and extending existing artifacts**.
- Create files only if they do not exist.
- Avoid duplicate workflows.

---

## Output

Repository verified.

Update:

docs/TASKS.md

Set:

PHASE → 4