---
name: ai-sdlc-2-design
description: Determine minimal architecture components for the current use case.
---

# PHASE 2 — DESIGN

## Decision records and Fast Track

For eligible Fast Track work, confirm that existing architecture is sufficient
and record why DESIGN is shortened or skipped in `docs/TASKS.md`. If the change
requires an architecture decision, return to the regular flow. The active task
entry may replace the UC input for this scoped check; the regular steps below
do not require creating a UC solely for Fast Track.

For the regular flow, inspect existing ADRs relevant to the use case. Create an
ADR only for a consequential choice involving boundaries, technology or a
cross-cutting constraint; ordinary implementation details do not need one.
Create `docs/adr/ADR-NNN-short-title.md` on demand, choosing an unused number.
Use these sections: Status (Proposed, Accepted or Superseded), Context,
Alternatives, Decision and Consequences. Record the human decision and its
review reference when accepted; never infer acceptance from an agent proposal.

After human acceptance, update the current architecture in `docs/PROJECT.md`
and propose only affected durable rules plus ADR links in `AGENTS.md`, following
its review policy. Keep these changes together for review. Preserve superseded
ADRs and link their replacements. Do not duplicate the decision rationale.
No ADR directory or document is required until an actual decision needs one.

## Goal

Identify the **minimal architecture components** required for the current use case.

Do not generate implementation details.

---

## Input

Current use case

docs/specs/UC-[NNN]-[NAME].md

Architecture reference

docs/PROJECT.md

If the UC does not exist → ask the user.

---

## Steps

1. Read the use case.

2. Determine required components:

domain  
application  
interfaces  
infrastructure  

Examples:

- domain entity
- use case service
- repository interface
- persistence adapter
- API endpoint

3. Ensure the architecture in `docs/PROJECT.md` is sufficient.

Update it **only if necessary**.

Prefer **extending existing artifacts** instead of creating new ones.

---

## Rules

- Respect Clean Architecture  

  domain ← application ← interfaces ← infrastructure

- Do not implement code.
- Do not generate tests.
- Keep architecture descriptions minimal.

---

## Output

Architecture verified or minimally updated.

Update:

docs/TASKS.md

Set:

PHASE → 2
