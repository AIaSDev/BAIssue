---
name: ai-sdlc-0-bootstrap
description: Initialize or align a repository for AI-SDLC based on the intended system.
---

# PHASE 0 — BOOTSTRAP

Confirm purpose, language, framework and runtime; ask if unclear.

## Actions

1. Inspect existing code, tests, structure and dependencies.
2. Reuse the stack's conventional structure with Clean Architecture boundaries and unit, integration and E2E tests. Create only what is missing.
3. Configure dependencies and a reproducible development environment.
4. Update `docs/PROJECT.md`: purpose, architecture, install, test, run and release commands.
5. Verify installation and applicable project checks; configure CI to run them.
6. Remove unused files only with user confirmation.

## Output

Repository and development environment aligned with the intended system; record verified results or blockers.

Record phase 0 and status in `docs/TASKS.md` per `AGENTS.md`.
