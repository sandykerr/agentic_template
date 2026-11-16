# 27: Assess evidence in parallel and consolidate fresh review

**What to build:** Tool-guided parallel assessment of ticket evidence with one
shared inventory/reference report and a fresh final reviewer who consolidates
worker proposals and decides eligible cleanup across related files.

**Blocked by:** [26: Review and safely retire routine ticket evidence.](26-review-and-safely-retire-routine-ticket-evidence.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](../spec.md); [evidence workflow spec](../evidence-workflow-spec.md).

**Milestone:** EC2; requires human EC1 acceptance.

**Agent context limit:** 250,000 active tokens; [role defaults](../spec.md#role-configuration).

**Worker reasoning:** Inherit Medium for implementation and repair; workflow
assessors Medium and the fresh evidence reviewer High.

**Role guidance:** Shared contract; TDD and test-strategy; explicit policy criteria
and existing review-evaluation guidance for preparation of the EC2 human comparison.

**Context:** Structured records; parallel assessment; content-based classification;
cross-ticket dependencies, protected survivors and shared evidence.

## Acceptance criteria

- [ ] Generate one inventory/reference report and fixed non-overlapping worker assignments. Workers apply the same criteria/reason codes, save separate temporary proposals and flag external dependencies without deleting files or editing sibling proposals.
- [ ] Supply a fresh final reviewer the proposals and relevant originals for cross-file synthesis, conflict resolution and final approval. Consolidate into one authoritative JSON per ticket/shared folder with worker provenance; shared decisions remain referenced rather than copied.
- [ ] Inspect content and uses of mixed logs, archives and source copies. Preserve original reviews, sole needed content, unexplained failures, active/continuable-run requirements and completion records consumed by later work. Unknown eligibility stays blocked.
- [ ] Treat reference discovery as bounded evidence, not proof of no consumer. A missing temporary run directory does not establish deletion eligibility. Account for cross-assignment and cross-ticket dependencies before approval.
- [ ] Distinguish exact duplicate content from differing versions and required paths. Route substantive replacement/merge candidates to review-needed status with originals retained until the later supported approval path is available.
- [ ] Keep incomplete assignments, conflicts, stale content and unmet conditions visible and protected while independently eligible groups can proceed. Preserve original protected content, historical records and required symlink targets during execution.
- [ ] Demonstrate actual independent parallel worker assessments and a fresh High review on a bounded isolated sample, alongside scripted tool-contract tests. Missing real assignments/settings are a concrete verification gap, not a scripted substitute.
- [ ] Prepare the EC2 blinded human comparison, recording the worker and final-reviewer choices before revealing human labels. Carry disagreement and limitations into QA without claiming general reliability.

## Verification

Exercise disjoint work, conflicting/incomplete proposals, cross-ticket evidence,
embedded reviews in routine-looking files, archive content, differing versions and
stale approvals. Show consolidation and guarded deletion with protected survivors
unchanged. Run shared checks and independent implementation reviews; actual agent
judgments are additionally inspected at EC2 QA.

## Shared requirements and handoff

Follow the [scoped evidence contract](../evidence-workflow-spec.md#parallel-assessment-fresh-review-and-execution), [approved shared verification/ownership contract](../spec.md#shared-implementation-and-verification-contract), and [milestone gates](../milestones.md). Apply the current [AGENTS.md compute routing](../../../AGENTS.md#adapt-compute), [environment](../../../docs/agents/python-environment.md), [testing policy](../../../docs/agents/testing.md) and [development review contract](../../../docs/agents/review-records.md). Map coverage and run required final-source checks; preserve separate fresh Spec/Standards reviews and actual provenance.

Use the [worker handoff](../README.md#worker-handoff). Reconcile acceptance and completion only from verified evidence. Ticket completion and review approval do not accept a milestone. Select the next action through the published milestone gates; do not automatically start later work.
