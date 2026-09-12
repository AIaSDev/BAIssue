---
name: ai-sdlc-5-deploy
description: Verify or collaboratively define the deployment workflow.
---

# PHASE 5 — DEPLOY

## Actions

1. Inspect the existing deployment workflow: trigger, validated artifact, deployment, required secrets and post-deployment checks.
2. If absent, agree on the platform and workflow with the user before creating it.
3. Update minimally; do not overwrite workflows without confirmation.
4. Require explicit authorization before deployment; never store secrets in the repository.

## Output

Deployment workflow verified or updated. Report deployment and smoke-test results only if actually executed.

Record phase 5 and status in `docs/TASKS.md` per `AGENTS.md`.
