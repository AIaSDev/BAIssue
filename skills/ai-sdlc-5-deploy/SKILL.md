---
name: ai-sdlc-5-deploy
description: Verify or collaboratively define the deployment workflow.
disable-model-invocation: true
---

# PHASE 5 — DEPLOY

## Goal

Verify the **continuous deployment workflow** for the validated artifact.

Deployment is defined **together with the user**.

---

## Check

Inspect:

.github/workflows/

If a CD workflow exists:

- verify trigger
- verify deployment step
- verify required secrets

Update only if necessary.

If no workflow exists:

- ask the user for deployment platform
- propose a minimal workflow
- create only after confirmation

---

## Rules

- Prefer **verifying existing workflows**.
- Do not overwrite workflows without confirmation.
- Never store secrets in the repository.

---

## Output

Deployment workflow verified or updated.

Update:

docs/TASKS.md

Set:

PHASE → 5