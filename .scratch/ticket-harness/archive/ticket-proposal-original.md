# Proposed implementation tickets

**Historical state:** Superseded seven-ticket proposal, subsequently expanded into the original 17 published issues. Use the [approved current plan](../ticket-proposal.md) for remaining work.

This breakdown implements the [first-version spec](spec-before-milestone-qa.md). Each ticket delivers an observable extension of the working cycle. The first ticket is a narrow tracer bullet across the entire path; it does not claim to complete the release.

## 01: Complete one scripted ticket through the full verification cycle

**Blocked by:** None.

**What it delivers:** A Python CLI can execute one approved fixture ticket using scripted external-agent responses, independently verify it, obtain separate Spec and Standards results, test its candidate merge, advance the integration branch, and report completion.

Acceptance:

- Establish a runnable Python project and the CLI's run/status seam.
- Normalize a minimal valid Markdown spec/ticket and project check configuration into documented input contracts.
- Snapshot approved inputs and keep execution records separately.
- Use real temporary Git repositories and isolated worktrees, leaving unrelated caller work untouched.
- Run baseline, lightweight checks, both reviews, and candidate integration checks in the required order.
- Capture the submitted changes into a commit and advance only to the exact passing candidate.
- Invalid input, a failed check, a blocking review, or an invalid report prevents integration and produces an inspectable failure.
- Status reports the observed result without executing agents.

This ticket includes the minimum schemas, records, and Git/process behavior needed for that complete path. General repair, scheduling, live Codex, and timeout behavior are added below.

## 02: Repair rejected submissions within a fixed allowance

**Blocked by:** 01.

**What it delivers:** A failed fixture submission is automatically repaired and reverified, or preserved as Blocked after the configurable allowance is exhausted.

Acceptance:

- Default to two repair attempts after the initial submission.
- Start each repair with a fresh assignment, current changes, and concrete failure evidence.
- Cover lightweight-check failures, either review axis, and candidate integration failures.
- Changed code receives renewed checks and both reviews.
- Optional suggestions are reported without triggering repair.
- Missing requirements or changes to approved contracts surface a human decision.
- Report every attempt and preserve rejected work without advancing integration.

## 03: Stop stalled stages and reject unreliable agent outcomes

**Blocked by:** 02.

**What it delivers:** Worker, reviewer, or check failures terminate within configured limits and produce bounded, diagnosable outcomes.

Acceptance:

- Apply positive configurable timeouts to each external stage.
- Stop timed-out process trees and preserve available output.
- Treat nonzero exits, missing or malformed reports, and incorrect assignment/revision identities as failures.
- Apply the bounded failure policy without introducing unlimited secondary retries.
- Distinguish ticket-local failures from shared environment/baseline failures.
- Demonstrate each case through scripted processes and real Git/report outcomes.

## 04: Execute a dependency graph while isolating blocked work

**Blocked by:** 02.

**What it delivers:** A sequential run processes multiple tickets in dependency order, continues unrelated work after a failure, and accurately reports waiting dependents.

Acceptance:

- Validate unique ticket IDs, dependency references, cycles, readiness labels, and check references.
- Select ready tickets using a stable documented order.
- Base each new implementation on the current verified integration revision.
- Unlock dependents only after prerequisite changes are integrated and Done.
- Preserve Blocked versus Pending distinctions.
- Finish with a nonzero incomplete outcome when selected work remains unresolved.
- Demonstrate a blocked ticket, a waiting dependent, and an unrelated successful ticket in the same fixture run.

## 05: Complete a real Codex ticket using custom implementation and review skills

**Blocked by:** 03.

**What it delivers:** The same cycle works with actual fresh Codex processes and repo-owned implementation, Spec review, Standards review, and shared code-design guidance in another target repository.

Acceptance:

- Add the live Codex backend through the existing external-process/report contract.
- Support role-specific model and reasoning configuration, access, events, and structured final reports.
- Create the custom execution/review skills and one authoritative combined design policy, retaining upstream references.
- Explicitly deliver required skill content and focused references across the repository boundary; record the supplied instructions.
- Keep implementation source writable only in its assigned worktree and reviewer source read-only.
- Use a small real-Codex fixture to demonstrate instruction delivery, role behavior, valid reports, and successful integration.
- Keep routine tests deterministic and independent of Codex authentication or network access.

The live fixture uses the existing local Codex environment; it is a separate explicitly run check, not part of every routine test invocation.

## 06: Produce harness-compatible requirements with the custom planning skill

**Blocked by:** 04, 05.

**What it delivers:** An interactive repo-owned planning skill turns a human-approved design into a spec and dependency-aware Markdown tickets that the harness can validate and execute.

Acceptance:

- Reuse the combined code-design policy rather than copying it into another competing source.
- Establish important interfaces, invariants, and test seams with the human.
- Produce vertical tickets with stable identifiers, readiness, acceptance requirements, and genuine dependency edges.
- Match the canonical input contract and local authoring conventions.
- Include a small example bundle that passes validation and completes a scripted sequential run.
- Preserve human approval of requirements and leave execution to intentional CLI invocation.

## 07: Demonstrate the first usable release from a clean checkout

**Blocked by:** 06.

**What it delivers:** A developer can install the harness, configure a separate small target repository, run the deterministic acceptance demonstration, and explicitly run the real-Codex check.

Acceptance:

- Document installation, configuration, role settings, check commands, stage limits, run/status usage, and artifact locations.
- Supply an executable example that demonstrates successful integration, bounded repair, a blocked ticket, and an unrelated successful ticket.
- Validate the complete deterministic suite from a clean checkout and run the small live check when the Codex environment is available.
- Demonstrate that requirements remain unchanged and integration references only passing candidates.
- Document the first release's limits: sequential tickets, inspectable records, and no interrupted-run recovery.
- Identify concurrency, recovery/resume, and failure emails as later slices without implementing them here.

## Dependency map

- 01 unlocks 02.
- 02 unlocks 03 and 04 independently.
- 03 unlocks 05.
- 04 and 05 unlock 06.
- 06 unlocks 07.

These are implementation dependencies. The harness being built still executes target tickets sequentially in its first release.

## Review requested

Confirm whether the ticket granularity is appropriate, whether each dependency genuinely gates its ticket, and whether any tickets should be merged or split. After approval, publish one numbered implementation issue per ticket using the configured local tracker.
