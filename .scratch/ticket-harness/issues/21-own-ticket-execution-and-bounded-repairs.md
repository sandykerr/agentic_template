# 21: Own ticket execution and bounded repairs

**What to build:** Give one ticket execution ownership of its complete implementation, verification and bounded repair cycle. Keep the original approved base, current attempt, repair starting revision, previous source worktree and failure context together. Use the attempt lifecycle delivered by ticket 20; finish the caller migration so existing selected-ticket runs stay green.

**Blocked by:** [20: Own implementation-attempt transitions](20-own-implementation-attempt-transitions.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](../spec.md).

**Milestone:** M1. Follow [membership and QA](../milestones.md#m1-a-complete-qa-controlled-git-cycle) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Independent Spec and Standards reviewers inherit High. All roles inherit GPT-6.1 Sol and the 250,000 active-context target.

**Role guidance:** Inherit [development defaults](../spec.md#role-configuration). For implementation, repair and Standards, add [object-oriented design](../../../.agents/skills/microsoft/microsoft_oop/SKILL.md), [codebase design](../../../.agents/skills/matt-pocock/codebase-design/SKILL.md), and [test strategy](../../../.agents/skills/custom/test-strategy/SKILL.md). Spec review uses the agreed spec and testing contracts; no additional skill selection. These development additions do not select runtime instructions for target-repository agents.

**Context:** [ownership contracts](../spec.md#state-and-decision-ownership), [refactor verification](../spec.md#oop-refactor-verification), [ticket lifecycle](../spec.md#ticket-lifecycle), [independent checks](../spec.md#independent-checks-and-exact-revisions), [QA and promotion](../spec.md#feature-to-development-promotion-and-human-qa), and [safe continuation](../spec.md#corrections-and-safe-continuation). Respect [domain terms](../../../GLOSSARY.md) and [ADR-0002](../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

**Review amendment:** [development review contract](../spec.md#ownership-contracts-and-cross-module-review); [checkpoint rules](../spec.md#cumulative-architecture-checkpoints); [review records](../spec.md#review-work-findings-and-decisions).

## Acceptance criteria

- [ ] A ticket execution owns the complete cycle and repair policy through a small interface. The runner coordinates eligible tickets and retains checking; ticket workflow code no longer obtains unrestricted access to the runner merely to manipulate its shared state.
- [ ] The original ticket base remains fixed across attempts, while a repair starts from the observed rejected submission or preserved uncommitted work as applicable. Fresh assignments and worktrees receive the correct failure, rejected revisions, ticket-scoped evidence and configured check selection.
- [ ] Initial assignment plus configured repairs remains bounded. Repairable gate/Git/process/timeout failures, exhausted allowance, human decisions, environment/integrity failures and external ref/HEAD movement retain their existing repair-or-stop decisions and preserved history.
- [ ] Every changed submission receives renewed applicable checks, both independent reviews and an exact candidate suite. Earlier approval cannot authorize a repaired source; approved inputs, earlier evidence and the caller worktree stay protected.
- [ ] Only successful expected-old advancement of the integration branch records the exact tested candidate as Done and unlocks dependents. Later tickets use the current verified integration revision; existing fail-fast behavior after a blocked ticket remains unchanged until the separate blocked-work-isolation ticket.
- [ ] CLI behavior, single-/multi-ticket artifact names, baseline reuse, attempt numbering, gate ranges and saved record formats remain compatible. Existing readiness calculations and Git primitives remain functions where they provide no independent state lifetime.

- [ ] Use the evaluated review workflow from tickets 16–19: record the relevant ownership change, independent cross-module review scope, immutable reports and finding dispositions; perform a cumulative assessment when the shared risk triggers apply. Preserve a navigable rationale-to-change-to-verification history and carry unresolved findings into the next handoff.

## Verification

Map existing successful repair, invalid-report preservation, repair exhaustion, later-ticket fixed-base/history, evidence invalidation and external-integration scenarios. Prior art: `tests/test_repairs.py`, `tests/test_dependencies.py`, `tests/test_transaction.py` and `tests/test_timeouts.py`. This ticket does not implement later independent-work scheduling or add private-class tests.

Use the existing public CLI with scripted external processes, real temporary Git repositories, and observable Git/record outcomes. Map criteria to existing coverage first; add cases only for distinct uncovered failures. Design review verifies ownership and encapsulation without tests that require particular private classes or method names. Follow [refactor verification](../spec.md#oop-refactor-verification) for the full suite, static checks, evidence and independent reviews on the final source.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Preserve completed tickets 01–15 and their evidence. Ticket completion does not accept M1; after all M1 work is verified, prepare QA or a waiting handoff. Do not start M2 before explicit human acceptance of M1.
