---
name: ai-sdlc-5-deploy
description: Verify or collaboratively define the continuous deployment workflow.
disable-model-invocation: true
---

# PHASE 5 — DEPLOY

## Goal

Verify or define the **continuous deployment (CD) workflow** for the validated artifact.

Deployment must be configured **together with the user**.

---

## Check

Inspect the workflow referenced in the prompt or located in:

.github/workflows/

If a CD workflow exists:

- verify trigger mechanism (e.g. `workflow_dispatch`, release, push)
- verify deployment step
- verify required secrets
- update only if necessary

If no workflow exists:

- collaborate with the user to define a deployment workflow
- propose a minimal GitHub Actions workflow
- confirm platform and secrets before creating it

---

## Rules

- Always collaborate with the user.
- Do not overwrite workflows without confirmation.
- Prefer updating existing workflows.
- Never store secrets in the repository.

---

## Output

One of:

- CD workflow verified
- CD workflow updated
- New CD workflow created with user approval

Update:

docs/TASKS.md

CURRENT PHASE → 1