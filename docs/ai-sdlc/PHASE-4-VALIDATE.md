# PHASE 4 — VALIDATE

**Goal:** Automated verification + release-ready artifact.

## Order
1) E2E tests (full flow)  
2) Dockerfile (deployable image)  
3) GitHub Actions:
   - Add CI workflow as `.github/workflows/ci.yml`. with unit + integration
   - Add release workflow as `.github/workflows/release.yml`. with build image + run E2E against image + publish package

## Quality Gates
- Coverage ≥ 80% (recommended)
- Pyramid guideline: Unit ~70%, Integration ~20%, E2E ~10%
- All checks green

## Output
- Green CI and green release workflow.
- Update docs/TASKS.md and set to **CURRENT PHASE = 5**.