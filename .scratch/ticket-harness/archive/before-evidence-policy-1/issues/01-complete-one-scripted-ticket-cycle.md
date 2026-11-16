# 01: Complete one scripted ticket through every gate

**What to build:** Run one approved fixture ticket from the CLI through a scripted implementation, independent checks, separate Spec and Standards reviews, a passing candidate merge, and recorded completion.

**Blocked by:** None (can start immediately).

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Public interface and approval](../spec.md#public-interface-and-approval); [Ticket lifecycle](../spec.md#ticket-lifecycle); [Independent checks and exact revisions](../spec.md#independent-checks-and-exact-revisions).

**Scope:** One successful ticket in a real temporary Git repository. Establish only the Python project, input/report contracts, worktrees, artifacts, and run/status behavior required by that tracer bullet.

## Acceptance criteria

- [x] Provide a reproducible Python project/check setup and public run/status operations with a minimal documented fixture input.
- [x] Record the approved inputs and starting revision separately from agent-editable source; use a fresh scripted external process for each assignment.
- [x] Independently run the baseline suite, lightweight ticket checks, separate Spec and Standards reviews, and the candidate integration suite.
- [x] Capture the submitted changes in Git and advance the integration branch only to the candidate that passed the required gates; success records that revision as Done.
- [x] A required gate returning failure cannot advance the integration branch or produce a successful completion result.
- [x] Status reads the recorded outcome and artifact locations without launching agents or changing the caller's work.

## Verification

Drive the public CLI with scripted external agents and a real disposable Git repository. Show a passing cycle and a representative rejected gate. Keep general repairs, graph scheduling, and live Codex for their owning tickets.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).

## Comments

### Completion — 2026-11-06

Implemented the ticket-01 scripted vertical slice in checkpoint `b09e324`, with final implementation commit `1666920` resolving the optional Standards cleanup. Review baseline was captured before editing: `1a623bad0b08241367948948b731b9e1f5114671`. The checkpoint was committed before the two independent reviews.

All six acceptance criteria are verified in the [completion evidence](../evidence/ticket-01/01-completion.md), with [saved actual CLI/Git/gate observations](../evidence/ticket-01/01-fixture-observations.json). The passing run completed every gate and recorded integration/Done at tested candidate `0ef4b6f61c35bf1c0d6ba356f10bc4c1dce2a3ab`. A separate rejected candidate suite returned exit 1, preserved its evidence, and left integration at baseline `6148f5f8e0d8d0353e305bf0939c19b4a7cbc5c8`. Tests also cover failures at baseline, implementation, lightweight checks, and both review axes. Approved snapshots, fresh assignments, preserved caller work, and read-only status were verified through public CLI/Git/report outcomes.

Checks: complete suite **8 passed**; strict mypy, Ruff lint, Ruff formatting, and whitespace checks all exited 0. Wheel build/install and installed CLI entry-point smoke check passed. Python/tests used micromamba; check tools used an isolated micromamba prefix.

Independent review outcomes: **Spec: no findings. Standards: no blocking findings; one optional duplicate-ignore cleanup fixed in `1666920` and re-reviewed with no residual findings.** Full outcomes and standards/spec sources are recorded in the evidence. No runtime changes followed review.

Only ticket 01 is complete. Repairs, dependency scheduling, live Codex, comprehensive validation, and later access-boundary protections remain with their owning tickets. Approved requirements and the `ready-for-agent` readiness label are unchanged. Concurrent unrelated Python setup edits were preserved outside these commits. No unresolved questions for this slice.
