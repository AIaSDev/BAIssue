---
name: ai-sdlc-4-validate
description: Verify repository readiness for release.
---

# PHASE 4 — VALIDATE

Input: active UC/task and `docs/PROJECT.md`.

## Actions

1. Run project unit and integration tests.
2. Verify acceptance coverage and run E2E tests; extend existing tests as needed.
3. Verify the release artifact builds and starts.
4. Verify CI runs unit and integration tests.
5. Verify the release workflow tests the same commit, builds and E2E-tests the artifact before authorized publication.

Reuse existing artifacts and workflows; create only what is missing.

Fast Track: run planned checks; record results and omissions with reasons.
Keep required CI/review; do not claim full release readiness or publish incidentally.

## Output

Readiness supported by recorded checks; distinguish verified results from unexecuted checks.

Record phase 4 and status in `docs/TASKS.md` per `AGENTS.md`.
