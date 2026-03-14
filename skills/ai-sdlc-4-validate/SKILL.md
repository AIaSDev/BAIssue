---
name: ai-sdlc-4-validate
description: Verify the system and prepare a release-ready artifact.
---

# PHASE 4 — VALIDATE

## Goal

Verify the system and produce a **release-ready container artifact**.

---

## Source of Truth

Current use case:

docs/TASKS.md

Architecture:

docs/PROJECT.md

---

## Steps

### 1. End-to-End Tests

Create or update tests in:

tests/e2e/

E2E tests must validate the **complete system behaviour** using real HTTP calls.

---

### 2. Docker Image

Check if a Dockerfile exists.

If present:

- verify correctness
- update if necessary

If missing:

Create:

Dockerfile

The container must start the application and expose the API.

---

### 3. CI Workflow

Check if CI exists:

.github/workflows/ci.yml

If present:

- verify it runs
  - unit tests
  - integration tests

If missing:

Create CI workflow.

---

### 4. Release Workflow

Check if release workflow exists:

.github/workflows/release.yml

If present:

- verify container build
- verify E2E tests run against container
- verify artifact publishing

If missing:

Create release workflow.

---

## Quality Gates

Recommended:

Coverage ≥ 80%

Testing Pyramid guideline:

- Unit ≈ 70%
- Integration ≈ 20%
- E2E ≈ 10%

All workflows must pass.

---

## Rules

- Do not duplicate existing workflows.
- Prefer updating existing files.
- E2E tests must run against the **built container**.
- CI must pass before continuing.

---

## Output

- E2E tests created or updated
- Dockerfile verified or created
- CI workflow verified or created
- Release workflow verified or created

All checks green.

Update:

docs/TASKS.md

Set:

CURRENT PHASE → 5