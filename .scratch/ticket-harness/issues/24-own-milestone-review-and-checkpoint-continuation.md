# 24: Own milestone review and checkpoint continuation

**What to build:** Give one milestone review ownership of its tested candidate, exact QA request, frozen evidence identities, decision observations and deliberate stop/continuation lifecycle. Fresh preparation and restoration enter the same review rules. Complete caller migration while retaining runner-owned checks and existing human authority over promotion.

**Blocked by:** [15: Continue after a deliberate QA stop](15-continue-from-a-planned-qa-checkpoint.md); [23: Own the complete run lifecycle](23-own-the-complete-run-lifecycle.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](../spec.md).

**Milestone:** M1. Follow [membership and QA](../milestones.md#m1-a-complete-qa-controlled-git-cycle) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Independent Spec and Standards reviewers inherit High. All roles inherit GPT-6.1 Sol and the 250,000 active-context target.

**Role guidance:** Inherit [development defaults](../spec.md#role-configuration). For implementation, repair and Standards, add [object-oriented design](../../../.agents/skills/microsoft/microsoft_oop/SKILL.md), [codebase design](../../../.agents/skills/matt-pocock/codebase-design/SKILL.md), and [test strategy](../../../.agents/skills/custom/test-strategy/SKILL.md). Spec review uses the agreed spec and testing contracts; no additional skill selection. These development additions do not select runtime instructions for target-repository agents.

**Context:** [ownership contracts](../spec.md#state-and-decision-ownership), [refactor verification](../spec.md#oop-refactor-verification), [ticket lifecycle](../spec.md#ticket-lifecycle), [independent checks](../spec.md#independent-checks-and-exact-revisions), [QA and promotion](../spec.md#feature-to-development-promotion-and-human-qa), and [safe continuation](../spec.md#corrections-and-safe-continuation). Respect [domain terms](../../../GLOSSARY.md) and [ADR-0002](../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

**Review amendment:** [development review contract](../spec.md#ownership-contracts-and-cross-module-review); [checkpoint rules](../spec.md#cumulative-architecture-checkpoints); [review records](../spec.md#review-work-findings-and-decisions).

## Acceptance criteria

- [ ] A milestone review keeps its candidate/feature/development identities, request content and digest, evidence identities and last observed decision together. Fresh and restored reviews use the same approval, unchanged-source/evidence and expected-ref rules; the caller receives an explicit stopped-versus-promoted outcome instead of a Boolean whose meaning depends on implementation knowledge. Use the run-owned verification export/restoration interface from ticket 23 instead of reading the runner's internal verified-check collection.
- [ ] Only an explicit matching, unconsumed human approval advances both expected feature/development refs to the exact regression-tested candidate. Missing, unreadable, malformed, mismatched, stale and replayed decisions retain observable waiting/rejection behavior without consuming ticket repairs or starting later milestones.
- [ ] Deliberate stop preserves the existing checkpoint version/format, identities, observations and archived lineage. Continue in a new process validates all approved inputs, record/request/evidence/source identities, both refs and exclusive ownership, without replaying completed assignments, completed baseline work or consumed decisions.
- [ ] Continue a genuine deliberate checkpoint written by pre-refactor code as well as one written by the new code. After JSON restoration, later source invalidation updates the canonical gate in the durable run record rather than a detached copy; changed evidence/checkpoints/refs cannot authorize continuation or promotion.
- [ ] Milestone preparation/regression/promotion failure observations, indefinite waits, stop exit behavior, status, ticket-Done versus milestone-promoted versus feature-complete distinctions, command interfaces and record/artifact formats remain compatible.
- [ ] Keep runner-owned checking and source-validation authority. Do not introduce arbitrary crash recovery, background execution, correction-plan execution, new approval authority, or later milestone features in this refactor. Update code wayfinding to describe the final responsibilities.

- [ ] Use the evaluated review workflow from tickets 16–19: record the relevant ownership change, independent cross-module review scope, immutable reports and finding dispositions; perform a cumulative assessment when the shared risk triggers apply. Preserve a navigable rationale-to-change-to-verification history and carry unresolved findings into the next handoff.

## Verification

Map existing exact approval/promotion, stale/replay rejection, clean stop/new-process continuation, post-restore gate invalidation, changed checkpoint/evidence/ref rejection and repeated-stop lineage cases. Prior art: `tests/test_milestones.py`, `tests/test_qa_promotion.py`, `tests/test_continuation.py` and `tests/test_transaction.py`. Retain provenance for a disposable pre-refactor checkpoint and its continuation with the final implementation; reuse existing compatibility evidence only when it actually covers that source. No live Codex or new private seam is needed.

Use the existing public CLI with scripted external processes, real temporary Git repositories, and observable Git/record outcomes. Map criteria to existing coverage first; add cases only for distinct uncovered failures. Design review verifies ownership and encapsulation without tests that require particular private classes or method names. Follow [refactor verification](../spec.md#oop-refactor-verification) for the full suite, static checks, evidence and independent reviews on the final source.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Preserve completed tickets 01–15 and their evidence. Ticket completion does not accept M1; after all M1 work is verified, prepare QA or a waiting handoff. Do not start M2 before explicit human acceptance of M1.

## Comments

User pause/resume checkpoint: unverified WIP `0385516c20fc54d054c8e3fe6aca9ddcb6bfcf76`; original fixed baseline `ed017ae0c2b96769f31c710cfb4ff4708989b446`. [Pause/evidence/remaining work](../evidence/24-pause.md) and [assessment/history](../reviews/ticket-24.md) retain both original review rounds and open alias findings. Full559 check interrupted130 after225 captured cases; no completion inferred. All owned test processes stopped. Readiness remains ready-for-agent and all seven criteria unchecked pending complete final checks and fresh whole-ticket independent reviews. Resume through root next_agent_prompt.md; no M1 acceptance or later-milestone execution implied.
