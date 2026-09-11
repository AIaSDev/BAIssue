# AGENTS.md — AI-SDLC Router

Repository state lives in:

docs/TASKS.md

Agents maintain task state; changes to this router follow the review rules below.

---

## Phases

0 BOOTSTRAP  
1 SPECIFY  
2 DESIGN  
3 DEVELOP  
4 VALIDATE  
5 DEPLOY  

Phases may be **skipped or repeated**.

Typical iteration:

SPECIFY → DESIGN → DEVELOP → VALIDATE  
VALIDATE → SPECIFY (iteration)  
DEPLOY → SPECIFY (feedback)

---

## Fast Track

Use Fast Track only for small, localized changes within existing behavior and
architecture (for example, a typo or a regression fix). Do not use it for new
features, public contract changes, data migrations, security changes, dependency
changes or architecture decisions. If scope grows or eligibility is unclear,
return to the regular flow.

Record the scope, eligibility reason, acceptance criterion and validation plan
in the existing specification or a short Fast Track entry in `docs/TASKS.md`.
Load that entry as the active context when no use-case specification applies.
SPECIFY may be shortened and DESIGN skipped with a recorded reason; do not create
a new UC solely for this route. For behavior changes, write a regression test
before changing code and run relevant tests. For documentation-only changes,
check content and links; code tests are not required. Record actual results and
omitted checks with reasons. Fast Track does not bypass required CI, review,
release or deployment authorization, and does not claim full release readiness.

## Architecture decisions and collaboration

Agents must update `docs/TASKS.md` as work progresses. Changes to `AGENTS.md`
require an explicitly approved rule change or human review before merge; agents
may propose a diff, but must not silently change their own operating rules.

For consequential architecture choices, use the DESIGN skill to propose an ADR.
Keep decision history in `docs/adr/`, current architecture in `docs/PROJECT.md`,
and only durable, actionable constraints with ADR links in `AGENTS.md`.
An authorized human accepts the decision. Include the ADR, affected architecture
documentation and proposed agent-rule changes in the same reviewed change.
Do not treat proposed decisions as accepted or copy the full ADR into other files.
When superseding a decision, preserve its history and update affected links/rules.
Before merge, reconcile parallel changes to decisions, agent rules and active
task state; `docs/TASKS.md` is not a multi-agent locking mechanism.

## Context Load Order

1. docs/TASKS.md  
2. docs/PROJECT.md  
3. docs/specs/UC-[NNN]-[NAME].md (or the eligible Fast Track task entry)

The human-readable method documentation is maintained at:
https://docs.aisl.science/learning-and-resources/ai-sdlc

---

## Phase → Skill

0 → skills/ai-sdlc-0-bootstrap  
1 → skills/ai-sdlc-1-specify  
2 → skills/ai-sdlc-2-design  
3 → skills/ai-sdlc-3-develop  
4 → skills/ai-sdlc-4-validate  
5 → skills/ai-sdlc-5-deploy  

---

## Commands

Run tests

`pytest -q`

Build container

`docker build -t app:local .`

Run container

`docker run --rm -p 8000:8000 app:local`

---

## Rules

- Use **English** for all generated content.
- Prefer **updating existing artifacts** instead of creating new ones.
- Only create artifacts **if they do not exist**.
- Keep artifacts **minimal**.
- Avoid unnecessary comments in code.
- Follow **TDD** (tests before code).
- Respect **Clean Architecture**  
  domain ← application ← interfaces ← infrastructure
- Prefer **small vertical slices** (one UC end-to-end).

If requirements or architecture are unclear → ask the user.
