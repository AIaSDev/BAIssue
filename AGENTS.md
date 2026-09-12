# AI-SDLC Router

## State and context

Read `docs/TASKS.md`, `docs/PROJECT.md`, then the active UC or Fast Track task.
Use project commands from `docs/PROJECT.md`; do not assume a technology stack.

PHASE selects the phase for the current branch/task in `docs/TASKS.md`.
STATUS: ready → in-progress → done (verified output), or blocked (reason).
Keep PHASE on completion; explicitly select the next phase as ready.
Phases may repeat or be skipped with a reason.
Changes to this router require human review.

## Phases

0. [BOOTSTRAP](skills/ai-sdlc-0-bootstrap/SKILL.md)
1. [SPECIFY](skills/ai-sdlc-1-specify/SKILL.md)
2. [DESIGN](skills/ai-sdlc-2-design/SKILL.md)
3. [DEVELOP](skills/ai-sdlc-3-develop/SKILL.md)
4. [VALIDATE](skills/ai-sdlc-4-validate/SKILL.md)
5. [DEPLOY](skills/ai-sdlc-5-deploy/SKILL.md)

Typical loop: SPECIFY → DESIGN → DEVELOP → VALIDATE → SPECIFY.
Deployment feedback returns to SPECIFY.

## Fast Track

- Small corrections only; no feature, API, data, security, dependency or architecture changes.
- Record scope, reason, acceptance and checks in the existing UC or task.
- Shorten SPECIFY; skip DESIGN with a reason. Scope grows → regular flow.
- Keep required CI and review.

## Rules

- Write English; keep artifacts and comments minimal. Update existing files first.
- Use TDD and small vertical slices. Respect Clean Architecture: domain ← application ← interfaces ← infrastructure.
- Ask about unclear requirements or architecture.
- Human-approved decisions → ADRs; current architecture → `docs/PROJECT.md`.
- Durable rules and ADR links → `AGENTS.md`, with human review.
- Update related artifacts together; preserve decision history and reconcile parallel changes.
- Release and deployment require explicit authorization; never commit secrets.

For method details, see [AI-SDLC](https://docs.aisl.science/learning-and-resources/ai-sdlc).
