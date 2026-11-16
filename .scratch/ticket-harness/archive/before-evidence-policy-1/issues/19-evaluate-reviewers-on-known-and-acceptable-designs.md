# 19: Evaluate reviewers on known and acceptable designs

**What to build:** Evaluate the strengthened development reviewers against known failures, design risks and acceptable implementations before using them on the five refactors. Retain the case contracts, actual fresh reviewer inputs/outputs, misses, false positives and guidance changes so the human can judge what the evaluation establishes.

**Blocked by:** [17: Review ownership across affected modules](17-review-ownership-across-affected-modules.md); [18: Gate development on cumulative architecture review](18-gate-development-on-cumulative-architecture-review.md).

**Status:** completed

**Plan version:** [oop-v2](../spec.md), approved review-process-1 revision.

**Milestone:** M1. Follow [membership and human QA](../milestones.md) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Spec and Standards reviewers independently inherit High. Use GPT-6.1 Sol, fresh assignments and the 250,000 active-context target.

**Role guidance:** Inherit [project role defaults](../spec.md#role-configuration), [test strategy](../../../.agents/skills/custom/test-strategy/SKILL.md) and [codebase design](../../../.agents/skills/matt-pocock/codebase-design/SKILL.md) for implementation/repair and Standards. Skill authors additionally follow [writing for agents](../../../.agents/skills/matt-pocock/writing-for-agents/SKILL.md) and [skill creation](/home/ajkerr1/.codex/skills/.system/skill-creator/SKILL.md) where applicable. Preserve upstream skills unchanged; repo-owned wrappers/references carry project-specific policy.

**Context:** [review contract](../spec.md#review-work-findings-and-decisions); [ownership and review scope](../spec.md#ownership-contracts-and-cross-module-review); [architecture checkpoints](../spec.md#cumulative-architecture-checkpoints); [reviewer evaluation](../spec.md#reviewer-evaluation); [verification](../spec.md#review-process-verification); [role defaults](../spec.md#role-configuration). Respect [domain terms](../../../GLOSSARY.md), [ADR-0001](../../../docs/adr/0001-reusable-harness-and-local-integration.md) and [ADR-0002](../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

## Acceptance criteria

- [x] Prepare a small source-identified corpus with at least four concern cases and four acceptable controls, with expected relevant review axis and rationale recorded before evaluation. Concerns cover detached restored gate evidence, positional attempt selection, duplicated lifecycle-record edits and externally coordinated initialization; controls cover cohesive Git validation, pure plan/parsing transformations, atomic file/process primitives and explicit owned transitions.
- [x] Assess the relevant cases with actual fresh development reviewer assignments using the agreed model/role settings and exact guidance identities. Supply cases/contracts without the evaluator answer key, preserve axis independence and retain raw reports. Scripted reviewer output, deterministic text matching and source-link validation alone cannot establish judgment quality.
- [x] For the declared required corpus, detect every seeded required correctness/ownership concern with source-specific evidence and a proportionate classification/remedy; acceptable controls receive no unsupported blocking finding. Optional observations are judged on evidence, not counted as failures merely for existing. The evaluator explains each expected/observed match and mismatch rather than scoring findings by count alone.
- [x] Record missed concerns, unsupported blockers and guidance revisions without deleting failed trials. A required miss or false blocker prevents this ticket completing; revise guidance or surface the unresolved limitation, then evaluate the final guidance on the complete declared corpus. Report the finite case set and actual repetitions; no guarantee of future detection or runtime backend effectiveness is inferred.
- [x] Publish the evaluated guidance version and corpus references through planning and next-agent handoffs so subsequent refactors 20–24 can consume them. Preserve ordinary autonomous repairs and human design/QA authority. This ticket completes on the declared corpus evaluation and usable handoff; actual refactor review/decision evidence belongs to tickets 20–24 and M1 QA, not a prerequisite for completing this ticket.
- [x] Keep M1 evaluation separate from harness live-backend availability. Actual runtime role/instruction delivery and enforcement must later be verified by tickets 33/34; this development evaluation uses isolated reviewer assignments and does not launch a harness run, fabricate acceptance or add private module tests.

## Verification

Use standalone skill/workflow evaluation with actual development reviewers and isolated writable case fixtures where needed; reviewers receive read-only source snapshots. Retain corpus source/contracts, expected axes, assignment/settings/guidance identities, raw outputs, evaluator reasoning and all trial outcomes. Preserve the CLI/real-Git seam for executable harness changes; this evaluation is a distinct, explicit evidence requirement for review guidance, not a substitute for runtime tests.

Use the [testing policy](../../../docs/agents/testing.md), [Python environment](../../../docs/agents/python-environment.md) and [shared review-process verification](../spec.md#review-process-verification). Validate documents, skills, source links and isolated workflow observations for guidance changes; executable harness changes retain the full final-source suite, strict typing, lint, format, whitespace and independent implementation reviews. Preserve actual command results, source/guidance/model identities and raw observations; scripted reviewers cannot establish reviewer judgment.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Carry pending reviews and unresolved findings without rewriting prior reports. Ticket completion does not accept a milestone. Select further work only through [milestone eligibility](../milestones.md); no automatic next-milestone execution or human acceptance is authorized.

## Comments

Completed and verified at final implementation `8e2c82679a2314e31ebff69accab3743f55f996d`,
following checkpoints `e90abb6` and `ce4e57d`. Previous readiness: `ready-for-agent`.
Declared `Blocked by:` history and all criterion wording preserved.

All six criteria map to [completion evidence](../evidence/ticket-19/19-completion.md): exact
predeclared G2/C5 source/key, actual fresh independent High corpus reports, all
required detections/four supported clean controls, all five source versions and
failed trial/adjudication histories, planning/implementation/both-handoff routing
and development/runtime separation. [Final actual checks](../evidence/ticket-19/19-repair-c5-checks.log)
pass three skill validators, syntax, identity/preservation/routing and 182 links,
protecting 6742 prior paths. The preserved immutable C3 EOF blank/default whitespace
failure and precise two-part passing whitespace checks are explicitly disclosed;
no broad/default-whole-diff pass is claimed.

Separate fresh final High [Spec](../evidence/ticket-19/19-review-spec-03.md) and
[Standards](../evidence/ticket-19/19-review-standards-03.md) each report 0 new blockers/0 optional,
independently verify both original actual full keys fixed at final source, and
accept finite G2/C5 evaluation, skill/probe limits and bounded EOF handling.
[Assessment](../reviews/ticket-19.md) and
[append-only history](../evidence/ticket-19/19-finding-history.md) retain all original reports,
differing axes and exact repair verification. No unresolved actual key, unchecked
criterion, missing required ticket report, pending relevant revalidation or actual
human decision remains.

User-requested reusable [evaluate-reviewers skill](../../../.agents/skills/custom/evaluate-reviewers/SKILL.md)
is wired conditionally through the existing evaluation reference reached from
custom planning/implementation/handoff workflows. Use it for future calibration
or corpus authoring; ordinary implementation keeps its existing independent axes.
The [separate preparation-only observation](../evidence/ticket-19/19-repair-c5-skill-observation.md)
and tested/final byte distinction are preserved. No retroactive C5 use, extra
per-ticket gate or runtime role selection is claimed.

Implementation, completion bookkeeping and generated next handoff are separate
commits. Next eligible preferred ticket 20 has completed 05/06/19 prerequisites;
the handoff starts no next assignment. M1 cumulative assessment/source provenance
and human QA remain unperformed; no acceptance, promotion or push authorized.

### Later workflow-efficiency follow-up

The separately completed [workflow-efficiency follow-up](../archive/workflow-efficiency/README.md)
applied lessons from this ticket to preparation, diagnosis and evidence reuse in
the ordinary development workflow. Its original independent reviews and checks
are archived with this feature. It does not change this ticket's completed
criteria or frozen evaluation results. Use the current
[development procedure](../../../docs/agents/review-records.md#prepare-review-and-repair) for new
work; runtime adoption remains tickets 33/34.

M1 QA preparation, 2026-11-12: this ticket contributes to [cumulative assessment review-M1-architecture-01](../reviews/M1-architecture-01.md) at `d02e61e`, fixed feature-start baseline `1a623ba`. [Current QA preparation and observations](../evidence/m1-qa-01/qa-guide.md). Ticket completion retains its original verification; this cross-ticket assessment and actual human QA are separate gates.
