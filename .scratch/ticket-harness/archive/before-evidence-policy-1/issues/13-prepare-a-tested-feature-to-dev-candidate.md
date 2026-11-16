# 13: Present a tested feature-to-dev candidate

**What to build:** Prepare the current feature revision against the current development branch, run configured local regression checks, and emit an exact QA request with instructions and plan/milestone/source/base/candidate identities. Keep dev unchanged and later work waiting. A failed or changed candidate is not QA-ready; source-changing conflict resolution renews applicable reviews.

**Blocked by:** [12: Execute only the first eligible milestone](12-execute-only-the-current-qa-milestone.md).

**Status:** completed

**Milestone:** M1. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R04](../ticket-proposal.md#r04-present-a-tested-feature-to-dev-candidate).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [feature to development promotion and human qa](../spec.md#feature-to-development-promotion-and-human-qa); [independent checks and exact revisions](../spec.md#independent-checks-and-exact-revisions).

## Acceptance criteria

- [x] Prepare a candidate combining the completed milestone's feature revision and current development base without advancing dev or admitting later work.
- [x] Run configured local regression gates on that exact candidate before issuing a QA request; preserve per-ticket candidate checks as a separate gate.
- [x] Record run/plan/milestone/feature/development/candidate identities, planned human checks, acceptance conditions and actual regression evidence in the request.
- [x] Failed regression, external branch movement, or an invalidated candidate cannot be presented as ready or promoted; preserve evidence and do not overwrite refs.
- [x] Conflict resolution that changes reviewed source renews applicable checks and reviews before QA. Demonstrate passing, failed, and changed-base cases at the public Git/report seam.

## Verification

Public Git/report observations cover a passing request, a rejected regression gate, and a changed development base. Preserve per-ticket candidate checks as a separate required gate.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.

## Comments

### Verified completion

Previous readiness: `ready-for-agent`. Implementation `19ea4f1b0bbdc601653468212aaaa0a7211d5c6f`
was reviewed against the fixed starting baseline `fd292a988cde79532bb84714b5800e4baa5de127`.
All five criteria are verified in [completion evidence](../evidence/ticket-13/13-completion.md):
current feature/dev combination with unchanged dev and later work held; separate
exact-candidate regression; full request identities/human checks/actual evidence;
failed/moved/mutated candidate rejection with retained evidence and refs; and
source-changing conflict resolutions stopped for renewed checks/reviews before QA.
The slice does not claim automatic conflict-repair or renewed-review execution.

[Actual final checks (retirement summary)](../evidence/ticket-13/README.md#retired-evidence): **509 tests passed**, strict mypy,
Ruff lint/format and whitespace passed. [Twenty source hashes](../evidence/ticket-13/13-final-source-identity.json)
match the committed/current implementation; [88 final observations (compact historical results)](../evidence/ticket-13/13-scenario-results.json)
retain the passing, rejected, changed-base and conflict behavior. The interrupted
earlier suite and development checks are explicitly superseded by renewed final gates.
Separate fresh High [Spec](../evidence/ticket-13/13-review-spec.md) and
[Standards](../evidence/ticket-13/13-review-standards.md) reviews found zero blockers;
Standards recorded one optional duplicate status assertion cleanup, without
mandatory rework. No unchecked criterion or required unresolved item remains.

Declared `Blocked by:` is retained as dependency history. Ticket 14 is next in
M1, without launching it here. Ticket completion does not accept M1 or complete
the feature; human acceptance and later milestone eligibility remain unchanged.

M1 QA preparation, 2026-11-12: this ticket contributes to [cumulative assessment review-M1-architecture-01](../reviews/M1-architecture-01.md) at `d02e61e`, fixed feature-start baseline `1a623ba`. [Current QA preparation and observations](../evidence/m1-qa-01/qa-guide.md). Ticket completion retains its original verification; this cross-ticket assessment and actual human QA are separate gates.
