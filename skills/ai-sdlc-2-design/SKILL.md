---
name: ai-sdlc-2-design
description: Determine minimal architecture components for the current use case.
---

# PHASE 2 — DESIGN

Input: active UC and `docs/PROJECT.md`; ask if the UC is missing.

## Actions

1. Identify required domain, application, interface and infrastructure components.
2. Verify the architecture; update only where needed.
3. Record significant choices in `docs/adr/ADR-NNN-short-title.md` using an unused number: status, context, alternatives, decision, consequences.
4. After human acceptance, update `docs/PROJECT.md` and propose durable rules with ADR links in `AGENTS.md`. Preserve superseded ADRs.

Fast Track: confirm existing architecture in the task; skip full DESIGN with a reason.

## Output

Architecture verified or minimally updated. No implementation or tests.

Record phase 2 and status in `docs/TASKS.md` per `AGENTS.md`.
