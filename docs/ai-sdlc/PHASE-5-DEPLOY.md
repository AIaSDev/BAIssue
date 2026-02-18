# PHASE 5 — DEPLOY

**Goal:** Deliver the validated artifact to a cloud platform via CD.

## Actions
- Add CD workflow (e.g., Render) as `.github/workflows/cd-[name].yml`.
- Deploy from a tagged release or protected main branch.
- Add a smoke check (health endpoint) post-deploy.
- Document required secrets (names only).

## Output
- Deployment automated and repeatable.
- Update docs/TASKS.md and set to **CURRENT PHASE = 1**.