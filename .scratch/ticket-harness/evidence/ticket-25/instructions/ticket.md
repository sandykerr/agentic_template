# 25: Guide ticket and shared evidence creation

**What to build:** The `capture-evidence` skill and Python routing/registration
workflow that give evidence-producing agents consistent ticket or shared milestone
destinations and reliable provenance. Deliver independently usable capture before
the cleanup workflow is implemented.

**Blocked by:** [24: Own milestone review and checkpoint continuation (completed).](24-own-milestone-review-and-checkpoint-continuation.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](../spec.md); [evidence spec](../evidence-policy.md).

**Milestone:** EC1. M1 acceptance is already recorded; EC1 remains unaccepted.

**Agent context limit:** 250,000 active tokens; [role defaults](../spec.md#role-configuration).

**Worker reasoning:** Inherit Medium for implementation and repair.

**Role guidance:** Shared contract; TDD, test-strategy and skill-creation/writing
guidance; preserve existing independent review/capture requirements and applicable
compute routing from AGENTS.md.

**Context:** Evidence placement and historical identity; evidence creation skill;
authoritative JSON artifacts and protected output boundaries.

## Acceptance criteria

- [ ] Deliver a repo-owned capture skill that identifies the ticket and purpose before capture, delegates destination selection and registration to Python, and reuses existing test/review guidance rather than duplicating it.
- [ ] Write ticket evidence directly into its corresponding folder. Route genuinely shared evidence to descriptively named shared folders and milestone subfolders linked from relevant tickets, keeping one authoritative copy.
- [ ] Register source version, producing command or activity, observed result and file identity; preserve original captures and label derived content. Registration supplies facts, not retention or deletion approval.
- [ ] Allocate distinct capture locations for parallel producers and consolidate registrations without competing edits to authoritative review decisions. Existing captures are not overwritten and newly created files do not inherit old deletion approvals.
- [ ] Establish a JSON review artifact per ticket or shared evidence folder as applicable, with capture metadata clearly separated from later assessments, approvals and execution results. Ticket artifacts reference shared records without duplicating their decisions.
- [ ] Route applicable development workflows through the skill/helper. Respect approved-input and frozen-file boundaries and keep harness runtime adoption separate. Leave historical organization and embedded paths unchanged unless a concrete need and reader checks permit a move.
- [ ] Demonstrate capture through the skill into the correct folders with valid provenance and protected originals, including shared milestone evidence linked from relevant tickets. This ticket neither authorizes deletion nor depends on the later cleanup tool.

## Verification

Exercise ticket and shared capture, parallel producer destinations, provenance,
original/derived distinction and protected destinations through public commands
and filesystem/JSON outcomes. Validate the skill and instruction routing plus the
shared implementation gates. This independently verifiable slice supplies ticket
26 with real captured evidence, without claiming cleanup or runtime adoption.

## Shared requirements and handoff

Follow the [scoped evidence contract](../evidence-policy.md#evidence-creation-skill-and-helper), [approved shared verification/ownership contract](../spec.md#shared-implementation-and-verification-contract), and [milestone gates](../milestones.md). Apply the current [AGENTS.md compute routing](../../../AGENTS.md#adapt-compute), [environment](../../../docs/agents/python-environment.md), [testing policy](../../../docs/agents/testing.md) and [development review contract](../../../docs/agents/review-records.md). Map coverage and run required final-source checks; preserve separate fresh Spec/Standards reviews and actual provenance.

Use the [worker handoff](../README.md#worker-handoff). Reconcile acceptance and completion only from verified evidence. Ticket completion and review approval do not accept a milestone. Select the next action through the published milestone gates; do not automatically start later work.
