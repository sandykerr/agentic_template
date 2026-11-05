# 01: Complete one scripted ticket through every gate

**What to build:** Run one approved fixture ticket from the CLI through a scripted implementation, independent checks, separate Spec and Standards reviews, a passing candidate merge, and recorded completion.

**Blocked by:** None (can start immediately).

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Public interface and approval](../spec.md#public-interface-and-approval); [Ticket lifecycle](../spec.md#ticket-lifecycle); [Independent checks and exact revisions](../spec.md#independent-checks-and-exact-revisions).

**Scope:** One successful ticket in a real temporary Git repository. Establish only the Python project, input/report contracts, worktrees, artifacts, and run/status behavior required by that tracer bullet.

## Acceptance criteria

- [ ] Provide a reproducible Python project/check setup and public run/status operations with a minimal documented fixture input.
- [ ] Record the approved inputs and starting revision separately from agent-editable source; use a fresh scripted external process for each assignment.
- [ ] Independently run the baseline suite, lightweight ticket checks, separate Spec and Standards reviews, and the candidate integration suite.
- [ ] Capture the submitted changes in Git and advance the integration branch only to the candidate that passed the required gates; success records that revision as Done.
- [ ] A required gate returning failure cannot advance the integration branch or produce a successful completion result.
- [ ] Status reads the recorded outcome and artifact locations without launching agents or changing the caller's work.

## Verification

Drive the public CLI with scripted external agents and a real disposable Git repository. Show a passing cycle and a representative rejected gate. Keep general repairs, graph scheduling, and live Codex for their owning tickets.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).
