# 16: Record review work, findings and decisions

**What to build:** Make review work, source-identified reports, findings and their decisions navigable in the existing local tracker. Provide a repo-owned record contract and usable templates/navigation so the human can follow a concern through its disposition, repair commit, verification and milestone evidence without a second issue system.

**Blocked by:** [10: Turn one grilling session into an approved plan](10-produce-approved-harness-inputs-with-planning-skill.md); [11: Stop development handoffs at human checkpoints](11-stop-development-handoffs-at-qa-milestones.md).

**Status:** completed

**Plan version:** [oop-v2](../spec.md), approved review-process-1 revision.

**Milestone:** M1. Follow [membership and human QA](../milestones.md) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Spec and Standards reviewers independently inherit High. Use GPT-6.1 Sol, fresh assignments and the 250,000 active-context target.

**Role guidance:** Inherit [project role defaults](../spec.md#role-configuration), [test strategy](../../../.agents/skills/custom/test-strategy/SKILL.md) and [codebase design](../../../.agents/skills/matt-pocock/codebase-design/SKILL.md) for implementation/repair and Standards. Skill authors additionally follow [writing for agents](../../../.agents/skills/matt-pocock/writing-for-agents/SKILL.md) and [skill creation](/home/ajkerr1/.codex/skills/.system/skill-creator/SKILL.md) where applicable. Preserve upstream skills unchanged; repo-owned wrappers/references carry project-specific policy.

**Context:** [review contract](../spec.md#review-work-findings-and-decisions); [ownership and review scope](../spec.md#ownership-contracts-and-cross-module-review); [architecture checkpoints](../spec.md#cumulative-architecture-checkpoints); [reviewer evaluation](../spec.md#reviewer-evaluation); [verification](../spec.md#review-process-verification); [role defaults](../spec.md#role-configuration). Respect [domain terms](../../../GLOSSARY.md), [ADR-0001](../../../docs/adr/0001-reusable-harness-and-local-integration.md) and [ADR-0002](../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

## Acceptance criteria

- [x] Define one review work item for an assessment scope, with identity, linked originating ticket(s)/milestone, purpose, fixed baseline, assessed revision, reviewer axis/settings/instruction identity, status, inspected/omitted scope, report links and current unresolved findings. Routine ticket Spec/Standards reports attach to the ticket assessment; cross-ticket architecture assessments have their own review work item. Reviews are not selected implementation tickets and do not consume or renumber implementation IDs.
- [x] Retain original reports and evidence as immutable source-identified snapshots. Key a finding by review/report identity plus its report-local ID so different axes, attempts or reviews may reuse local IDs safely. Maintain an append-only disposition history with actor, reason, evidence, affected revision and links; correction or re-review appends a superseding observation rather than rewriting the original report.
- [x] Support recorded dispositions open, fixed, deferred to a linked ticket, accepted with a reason, and awaiting a human decision. Fixed requires independent verification for the exact repair revision; a later changed revision needs revalidation. Review completion means its assessment/report is complete, while unresolved findings and integration/milestone eligibility remain separately visible.
- [x] Preserve human authority: agents may perform authorized repairs and record evidence or proposals; accepting consequential risk, deferring an integration-blocking finding, changing an ownership contract or expanding scope requires an explicit human decision and any necessary approved amendment. A review disposition is not QA acceptance and cannot grant promotion authority or silently turn a blocker into permission to integrate.
- [x] Publish a compact navigable chain from originating scope to finding/evidence, decision/reason, linked implementation ticket or repair, commit and verification, and eventual milestone assessment. Demonstrate a fixed finding, a deferred optional finding, an explicit human risk decision, duplicate report-local IDs, a reopened concern on changed source and a completed review with outstanding findings.
- [x] Keep review records in the existing feature tracker context and evidence locations, with review-specific lifecycle fields documented separately from ticket readiness. Historical reports/completed tickets and captured run inputs remain unchanged. During a harness run, new review artifacts belong to harness-owned output; post-run tracker links never mutate active approved inputs or frozen QA evidence.

## Verification

Use the standalone document/skill/workflow validation approach established by completed planning and handoff work. Create an isolated miniature tracker with real Markdown review records and source/report identities, exercise the six history/navigation cases above, and inspect retained artifacts. This ticket implements the development record contract and templates, not runtime scheduling or a new report wire schema.

Use the [testing policy](../../../docs/agents/testing.md), [Python environment](../../../docs/agents/python-environment.md) and [shared review-process verification](../spec.md#review-process-verification). Validate documents, skills, source links and isolated workflow observations for guidance changes; executable harness changes retain the full final-source suite, strict typing, lint, format, whitespace and independent implementation reviews. Preserve actual command results, source/guidance/model identities and raw observations; scripted reviewers cannot establish reviewer judgment.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Carry pending reviews and unresolved findings without rewriting prior reports. Ticket completion does not accept a milestone. Select further work only through [milestone eligibility](../milestones.md); no automatic next-milestone execution or human acceptance is authorized.

## Comments

Completed against implementation `3c8d4ab52c5da112552275d1d5fffdef001c1451`;
previous readiness: `ready-for-agent`. All six acceptance criteria verified in
[criterion-specific completion evidence](../evidence/ticket-16/16-completion.md).
[Actual checks](../evidence/ticket-16/16-checks.log) passed standalone document/skill and
six-case workflow validation (316 links/anchors); runtime suite is outside this
standalone documentation scope. Separate fresh High [Spec](../evidence/ticket-16/16-review-spec.md)
and [Standards](../evidence/ticket-16/16-review-standards.md) reviews each found zero blocking
or optional findings. [Assessment and report provenance](../reviews/ticket-16.md)
are retained. No unchecked criteria or unresolved real findings remain. Declared
dependencies are preserved. Implementation, bookkeeping and handoff commits are
separate; ticket completion does not accept M1 or launch ticket 17.

M1 QA preparation, 2026-11-12: this ticket contributes to [cumulative assessment review-M1-architecture-01](../reviews/M1-architecture-01.md) at `d02e61e`, fixed feature-start baseline `1a623ba`. [Current QA preparation and observations](../evidence/m1-qa-01/qa-guide.md). Ticket completion retains its original verification; this cross-ticket assessment and actual human QA are separate gates.
