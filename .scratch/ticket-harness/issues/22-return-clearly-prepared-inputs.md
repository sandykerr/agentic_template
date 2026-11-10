# 22: Return clearly prepared inputs

**What to build:** Make input preparation return one explicit, complete result containing validated execution settings, approved snapshots, normalized requirements, ticket selection, completion evidence and applicable worker settings. Keep raw settings separate from calculated values, and make all callers use the checked plan returned by validation. Complete caller migration while preserving current input acceptance, rejection, capture and execution behavior.

**Blocked by:** [02: Reject invalid requirements before starting work](02-reject-invalid-inputs-before-execution.md); [12: Execute only the first eligible milestone](12-execute-only-the-current-qa-milestone.md); [19: Evaluate reviewers on known and acceptable designs](19-evaluate-reviewers-on-known-and-acceptable-designs.md).

**Status:** completed

**Plan version:** [oop-v2](../spec.md).

**Milestone:** M1. Follow [membership and QA](../milestones.md#m1-a-complete-qa-controlled-git-cycle) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Independent Spec and Standards reviewers inherit High. All roles inherit GPT-6.1 Sol and the 250,000 active-context target.

**Role guidance:** Inherit [development defaults](../spec.md#role-configuration). For implementation, repair and Standards, add [object-oriented design](../../../.agents/skills/microsoft/microsoft_oop/SKILL.md), [codebase design](../../../.agents/skills/matt-pocock/codebase-design/SKILL.md), and [test strategy](../../../.agents/skills/custom/test-strategy/SKILL.md). Spec review uses the agreed spec and testing contracts; no additional skill selection. These development additions do not select runtime instructions for target-repository agents.

**Context:** [ownership contracts](../spec.md#state-and-decision-ownership), [refactor verification](../spec.md#oop-refactor-verification), [ticket lifecycle](../spec.md#ticket-lifecycle), [independent checks](../spec.md#independent-checks-and-exact-revisions), [QA and promotion](../spec.md#feature-to-development-promotion-and-human-qa), and [safe continuation](../spec.md#corrections-and-safe-continuation). Respect [domain terms](../../../GLOSSARY.md) and [ADR-0002](../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

**Review amendment:** [development review contract](../spec.md#ownership-contracts-and-cross-module-review); [checkpoint rules](../spec.md#cumulative-architecture-checkpoints); [review records](../spec.md#review-work-findings-and-decisions).

## Acceptance criteria

- [x] The input-loading interface provides the complete prepared result and makes its filesystem preparation requirements explicit. The run consumes that result without repeating preparation rules or externally filling calculated fields into raw configuration. Existing configuration and approved input files remain byte-for-byte unchanged.
- [x] One input preparation operation still validates executable commands, captures approved files and identities, normalizes tickets, validates dependency graphs and completion evidence, and establishes eligible selection and worker settings. Missing, malformed, conflicting or changed inputs retain existing diagnostics, invalid-input behavior and rejection before workers, checks or branch advancement.
- [x] All plan consumers use the checked plan returned by validation, including first-milestone selection. Normalized membership, dependency order, role defaults and worker overrides remain governed together by plan validation; callers need not rely on mutation of the original plan object. Requiring validation to become a pure function is not part of this ticket.
- [x] Legacy runs without a plan, versioned plans, externally completed prerequisites, explicit selections and primary-ticket handling retain their current behavior. Readiness, completion evidence, selected prerequisites, metadata conflicts, default/override inheritance and later-milestone eligibility rules remain intact.
- [x] Snapshot hashes, copied input names, output separation, persisted configuration/checkpoint contents and status output remain compatible. Any new in-memory result representation is translated into the existing JSON-safe saved shape so pre-existing checkpoints and later restoration keep working.
- [x] Pure parsing, normalization, graph checks and transformations remain ordinary functions where they own no independent lifecycle. The change introduces neither a configuration framework nor a new testing seam, and the full public CLI path is usable after this ticket.

- [x] Use the evaluated review workflow from tickets 16–19: record the relevant ownership change, independent cross-module review scope, immutable reports and finding dispositions; perform a cumulative assessment when the shared risk triggers apply. Preserve a navigable rationale-to-change-to-verification history and carry unresolved findings into the next handoff.

## Verification

Map existing preflight/configuration, duplicate metadata, graph/selection/completion-evidence and plan-validation cases in `tests/test_preflight.py`, `tests/test_dependencies.py` and `tests/test_milestones.py`. In particular, preserve invalid-plan rejection before processes/ref changes, normalized first-group selection and worker-setting metadata. Check the implementation diff to confirm callers use the returned checked plan and prepared result; avoid tests that assert a particular result class or require mutation-free validation.

Use the existing public CLI with scripted external processes, real temporary Git repositories, and observable Git/record outcomes. Map criteria to existing coverage first; add cases only for distinct uncovered failures. Design review verifies ownership and encapsulation without tests that require particular private classes or method names. Follow [refactor verification](../spec.md#oop-refactor-verification) for the full suite, static checks, evidence and independent reviews on the final source.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Preserve completed tickets 01–15 and their evidence. Ticket completion does not accept M1; after all M1 work is verified, prepare QA or a waiting handoff. Do not start M2 before explicit human acceptance of M1.

## Comments

Completed at implementation `33fa0ea6e667a3879564ed4628c10f6d59ada21b`, reviewed
from fixed original baseline `803c6ff9a4e5e057124aefc5bb96f2c9518162dd`. Previous
readiness: `ready-for-agent`; original criterion wording and Blocked by retained.
[Seven-criterion evidence and exact checks](../evidence/22-completion.md),
[ownership/coverage](../evidence/22-implementation-report.md),
[criterion observations](../evidence/22-criterion-evidence.md) and
[assessment](../reviews/ticket-22.md) establish completion. Full suite: **544 passed
in 709.21s**, strict mypy/Ruff lint/format/whitespace passed; 126 focused tests passed.
Genuine pre-edit checkpoint continued under final source with preserved prior work.
Separate fresh High [Spec](../evidence/22-review-spec-01.md) and
[Standards](../evidence/22-review-standards-01.md): each **0 blocking / 0 optional**;
[immutable originals](../evidence/22-review-round1-capture.json) and
[explicit finding history](../evidence/22-finding-history.md). All four start/final
architecture triggers independently No. No unchecked criterion, unresolved full key,
pending relevant revalidation or human-owned decision remains. Implementation and
bookkeeping commits are separate. Next eligible work is 23 after completed 15/21/22;
generating its separately committed handoff starts no assignment. M1 still needs
23–24, actual cumulative assessment and explicit human QA; no acceptance, promotion
or push is inferred.
