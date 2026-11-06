# 13: Present a tested feature-to-dev candidate

**What to build:** Prepare the current feature revision against the current development branch, run configured local regression checks, and emit an exact QA request with instructions and plan/milestone/source/base/candidate identities. Keep dev unchanged and later work waiting. A failed or changed candidate is not QA-ready; source-changing conflict resolution renews applicable reviews.

**Blocked by:** [12: Execute only the first eligible milestone](12-execute-only-the-current-qa-milestone.md).

**Status:** ready-for-agent

**Milestone:** M1. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R04](../ticket-proposal.md#r04-present-a-tested-feature-to-dev-candidate).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [feature to development promotion and human qa](../spec.md#feature-to-development-promotion-and-human-qa); [independent checks and exact revisions](../spec.md#independent-checks-and-exact-revisions).

## Acceptance criteria

- [ ] Prepare a candidate combining the completed milestone's feature revision and current development base without advancing dev or admitting later work.
- [ ] Run configured local regression gates on that exact candidate before issuing a QA request; preserve per-ticket candidate checks as a separate gate.
- [ ] Record run/plan/milestone/feature/development/candidate identities, planned human checks, acceptance conditions and actual regression evidence in the request.
- [ ] Failed regression, external branch movement, or an invalidated candidate cannot be presented as ready or promoted; preserve evidence and do not overwrite refs.
- [ ] Conflict resolution that changes reviewed source renews applicable checks and reviews before QA. Demonstrate passing, failed, and changed-base cases at the public Git/report seam.

## Verification

Public Git/report observations cover a passing request, a rejected regression gate, and a changed development base. Preserve per-ticket candidate checks as a separate required gate.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.
