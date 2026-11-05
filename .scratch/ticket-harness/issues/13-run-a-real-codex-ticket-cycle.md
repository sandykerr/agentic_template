# 13: Complete one real Codex ticket with configured role profiles

**What to build:** A small ticket completes the existing verified cycle with actual fresh Codex implementation and review processes in a separate disposable target repository.

**Blocked by:** [08: Stop stalled assignments and check processes](08-stop-timed-out-process-trees.md); [12: Deliver focused implementation and Spec-review skills](12-deliver-focused-implementation-and-spec-review-contexts.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Codex execution](../spec.md#codex-execution); [Agent contracts and access](../spec.md#agent-contracts-and-access); [Public interface and approval](../spec.md#public-interface-and-approval).

**Scope:** Replace the scripted process at the existing external seam with the installed Codex CLI; preserve all current gate and role contracts.

## Acceptance criteria

- [ ] Verify the installed CLI invocation and launch fresh assignments without resuming or inheriting the parent development conversation.
- [ ] Apply explicit working directory, role-specific model/reasoning settings, sandbox, timeout, and output contract without silently substituting a different configured model.
- [ ] Capture machine-readable events and schema-validated final results as run artifacts.
- [ ] Explicitly deliver the custom implementation, Spec-review, Standards-review, and applicable design instructions across the repository boundary.
- [ ] Demonstrate a small actual Codex implementation followed by separate actual reviews and successful exact-candidate integration.
- [ ] Keep routine tests scripted and offline; make the authenticated real-Codex check explicit and record actual evidence or a concrete environment blocker rather than counting a skipped check as success.

## Verification

Run existing deterministic checks and the separate tiny real-Codex fixture. Report the CLI version/settings, supplied skill identities, check outcomes, reviewed/candidate revisions, and observed final integration.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).
