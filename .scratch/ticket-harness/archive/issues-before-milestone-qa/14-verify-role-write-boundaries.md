# Historical ticket definition

Superseded by the approved QA-first plan. This is the previous unimplemented definition of ticket 14; use the [current ticket](../../issues/36-verify-role-write-boundaries.md) for work. Source: `84982495be5d4943301e165f8419421391e75d18:.scratch/ticket-harness/issues/14-verify-role-write-boundaries.md`. Relative links were adjusted for this archive location.

# 14: Verify implementation and review access boundaries

**What to build:** The live backend enforces writable implementation worktrees and read-only reviewer source while protecting approved inputs, run records, and integration ownership.

**Blocked by:** [13: Complete one real Codex ticket with configured role profiles](13-run-a-real-codex-ticket-cycle.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../../README.md#agent-context-policy).

**Context:** [Agent contracts and access](../spec-before-milestone-qa.md#agent-contracts-and-access); [Codex execution](../spec-before-milestone-qa.md#codex-execution); [Requirements, configuration, and run records](../spec-before-milestone-qa.md#requirements-configuration-and-run-records).

**Scope:** Exercise and tighten role permissions using the installed backend in disposable repositories; preserve the established harness-owned commit/integration model.

## Acceptance criteria

- [ ] Verify that an implementation worker can make intended source changes in its assigned worktree.
- [ ] Verify reviewer source access is read-only and does not require source mutation to produce its report.
- [ ] Attempt controlled out-of-scope writes to disposable sentinel locations representing sibling source, approved requirements, and harness state; verify they are refused or detected before any acceptance.
- [ ] Keep shared Git integration references and authoritative run-state changes under harness ownership.
- [ ] Reject an assignment if required access/instruction delivery cannot be established; do not silently widen permissions to make the fixture pass.
- [ ] Record concrete backend/sandbox evidence and keep caller work and approved requirements unchanged.

## Verification

Combine deterministic role-configuration tests with explicit live sandbox probes against disposable sentinels. Inspect the actual files/references and role results rather than accepting the agent's own permission claims.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../../README.md#worker-handoff).
