# AGENTS.md — AI-SDLC Router

Repository state lives in:

docs/TASKS.md

Agents must **not modify this file**.

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

## Context Load Order

1. docs/TASKS.md  
2. docs/PROJECT.md  
3. docs/specs/UC-[NNN]-[NAME].md  

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

Full test pyramid

`- pytest -q tests/unit tests/integration tests/e2e`

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