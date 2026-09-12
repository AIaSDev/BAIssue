---
name: ai-sdlc-1-specify
description: Create or update a minimal use case specification.
---

# PHASE 1 — SPECIFY

Input: user story or feature description; ask if missing or unclear.

## Actions

1. Update the existing UC; otherwise use `docs/specs/UC-TEMPLATE.md`.
2. Name new files `docs/specs/UC-[NNN]-[NAME].md`: next unused number, short uppercase hyphenated name.
3. Include intent, actors, preconditions, flow, errors, acceptance and tests. Do not invent functionality.

Fast Track: use the existing UC/task with acceptance and planned checks; no new UC required.

## Output

Minimal specification. No implementation or executable tests.

Record phase 1 and status in `docs/TASKS.md` per `AGENTS.md`.
