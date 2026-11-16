# 30: Calibrate and adopt the complete evidence workflow

**What to build:** Demonstrate the complete capture-to-cleanup workflow against
human judgments, refine criteria from observed disagreements, and finish adoption
and navigation so the postponed operator tickets can consume a verified local
evidence workflow.

**Blocked by:** [29: Reassess retained evidence during ticket completion.](29-reassess-retained-evidence-during-ticket-completion.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](../spec.md); [evidence workflow spec](../evidence-workflow-spec.md).

**Milestone:** EC3, final evidence-feature acceptance with cumulative EC1–EC3 coverage.

**Agent context limit:** 250,000 active tokens; [role defaults](../spec.md#role-configuration).

**Worker reasoning:** Inherit Medium for implementation and repair; actual workflow
assessors Medium and fresh final evidence reviewer High.

**Role guidance:** Shared contract, test-strategy, reviewer-evaluation guidance and
applicable skill-writing guidance. Preserve normal independent implementation reviews.

**Context:** Human calibration; complete testing decisions; concise bookkeeping
and integration with postponed open work.

## Acceptance criteria

- [ ] Reuse the early EC1/EC2 observations and complete a representative human-labeled sample covering delete, keep, merge proposed and unsure. Keep labels hidden until worker and final reviewer decisions are saved, compare both stages and let the human settle disagreements.
- [ ] Repeat assessments on the unchanged sample with fresh agents and report decision consistency, actual settings, limitations and disagreements. Refine criteria from observed failures and recheck affected behavior; identical prose and universal reliability claims are not success criteria.
- [ ] Demonstrate the complete capture, inventory, parallel proposal, fresh consolidation, human review, reassessment, preview and Python execution path. Include eligible deletion, protected evidence, misleading summary, differing versions, cross-assignment dependency, incomplete approval and post-assessment file change. Keeping everything fails the useful-cleanup criterion.
- [ ] Demonstrate protected survivors, navigation status, actual execution failures and concise notes. Keep disputed calibration evidence protected; successful scripted tool checks do not stand in for real agent judgments or actual human QA.
- [ ] Finish policy, capture/review skill and development handoff routing so future tickets use consistent criteria and destinations without conflicting lossless-versus-retirement instructions. Preserve frozen-input and continuation contracts and keep automatic harness cleanup out of scope.
- [ ] Report working-tree counts/logical bytes separately from allocated space and Git history if reporting size; do not claim remote-storage savings from local deletion. Capture ordinary results concisely in existing completion/evidence navigation.
- [ ] Prepare EC3 cumulative verification and human acceptance covering all accepted-spec user stories, prior checkpoint results and postponed-ticket integration. Do not declare EC3 accepted, run later work or clean unrelated current evidence merely because checks pass.

## Verification

Use the shared public CLI seam for tool behavior and actual independent agents for
judgment calibration. Human input is a required dependency of calibration; report
a concrete pending step if it is unavailable. Any code/guidance correction renews
affected verification and normal final-source gates as required. Validate both
skills and current links; source reviews and final cumulative architecture
assessment remain separate from evidence calibration.


## Shared requirements and handoff

Follow the [scoped evidence contract](../evidence-workflow-spec.md#testing-decisions), [approved shared verification/ownership contract](../spec.md#shared-implementation-and-verification-contract), and [milestone gates](../milestones.md). Apply the current [AGENTS.md compute routing](../../../AGENTS.md#adapt-compute), [environment](../../../docs/agents/python-environment.md), [testing policy](../../../docs/agents/testing.md) and [development review contract](../../../docs/agents/review-records.md). Map coverage and run required final-source checks; preserve separate fresh Spec/Standards reviews and actual provenance.

Use the [worker handoff](../README.md#worker-handoff). Reconcile acceptance and completion only from verified evidence. Ticket completion and review approval do not accept a milestone. Select the next action through the published milestone gates; do not automatically start later work.
