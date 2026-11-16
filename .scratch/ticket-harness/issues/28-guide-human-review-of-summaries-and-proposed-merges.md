# 28: Guide human review of summaries and proposed merges

**What to build:** The `review-evidence` skill and structured review queue that
let humans efficiently inspect proposed replacements, approve reviewed merges,
request changes or defer, with Python executing only still-valid approvals.

**Blocked by:** [27: Assess evidence in parallel and consolidate fresh review.](27-assess-evidence-in-parallel-and-consolidate-fresh-review.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](../spec.md); [evidence workflow spec](../evidence-workflow-spec.md).

**Milestone:** EC3; requires human EC2 acceptance.

**Agent context limit:** 250,000 active tokens; [role defaults](../spec.md#role-configuration).

**Worker reasoning:** Inherit Medium for implementation and repair.

**Role guidance:** Shared contract; TDD, test-strategy and skill-creation/writing
guidance. The fresh evidence reviewer independently checks substantive replacements.

**Context:** Similar versions and proposed merges; guided human review; JSON facts,
review decisions, derived views and explicit unknown-versus-zero semantics.

## Acceptance criteria

- [ ] Agents prepare useful summaries or merged files with source identities, retained facts, useful differences, omissions and concise reasons. Label lossy derivatives, preserve unknown/absent values versus observed zero/empty collections and keep originals until applicable checks and approvals pass.
- [ ] A fresh reviewer compares substantive replacements against originals and corrects inaccurate or incomplete content before approval. Do not replace durable original independent reviews or human approvals with summaries.
- [ ] Human milestone QA receives proposed merges, reviewed content and omissions without manually merging. Original deletion requires that human approval plus valid fresh review and current file identities; changes require renewed applicable approval.
- [ ] Deliver a review skill backed by a generated queue, with overview, related groups, small batches, inspectable sources and approve/keep/request-changes/defer choices. Batch approvals name explicit items sharing a rationale; routine eligible cleanup remains inspectable without requiring human approval of every batch.
- [ ] Save human decisions in authoritative review artifacts and resume without repeating unchanged completed items. Unanswered/deferred items remain protected; changed proposals cannot reuse approvals. The queue is a derived view, not another authoritative decision store.
- [ ] Support blinded early calibration before recommendations are revealed, then recommendation-first ordinary review. Cleanup approval never writes candidate acceptance, promotes refs or substitutes for a finding disposition.
- [ ] Demonstrate proposed merge through fresh review, human approval, preview and Python deletion, including correction of a misleading summary and refusal of stale/unapproved replacement. Record execution and navigation truthfully on success and failure.

## Verification

Validate the skill using realistic isolated requests: related groups, bounded
batches, inspect differences, correction, pause/resume, deferral and stale content.
Compare missing attempts against observed zero attempts and verify protected
originals remain intact. Use scripted human decision artifacts for routine tests;
actual human decisions belong to calibration/QA. Run shared implementation gates.

## Shared requirements and handoff

Follow the [scoped evidence contract](../evidence-workflow-spec.md#guided-human-evidence-review), [approved shared verification/ownership contract](../spec.md#shared-implementation-and-verification-contract), and [milestone gates](../milestones.md). Apply the current [AGENTS.md compute routing](../../../AGENTS.md#adapt-compute), [environment](../../../docs/agents/python-environment.md), [testing policy](../../../docs/agents/testing.md) and [development review contract](../../../docs/agents/review-records.md). Map coverage and run required final-source checks; preserve separate fresh Spec/Standards reviews and actual provenance.

Use the [worker handoff](../README.md#worker-handoff). Reconcile acceptance and completion only from verified evidence. Ticket completion and review approval do not accept a milestone. Select the next action through the published milestone gates; do not automatically start later work.
