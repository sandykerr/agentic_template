# 04: Promote only the exact verified candidate

**What to build:** Verification evidence stays bound to the submitted revision and approved requirements, and an external branch change or failed candidate cannot be overwritten by integration.

**Blocked by:** [01: Complete one scripted ticket through every gate](01-complete-one-scripted-ticket-cycle.md)

**Status:** completed

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Independent checks and exact revisions](../spec.md#independent-checks-and-exact-revisions); [Requirements, configuration, and run records](../spec.md#requirements-configuration-and-run-records); [Agent contracts and access](../spec.md#agent-contracts-and-access).

**Scope:** Protect the existing submission-to-integration transaction and its input snapshots, without adding crash recovery or concurrent ticket execution.

## Acceptance criteria

- [x] Record approved input identities and detect attempts to alter the requirements or harness-owned state from an agent assignment.
- [x] Bind lightweight checks and both review results to the submitted revision, and the broader suite to the candidate revision.
- [x] Advance integration only to the tested candidate when the expected previous integration revision is still current.
- [x] If the integration branch changes externally, a merge fails, or candidate verification fails, preserve evidence and leave the current integration branch unchanged by this operation.
- [x] Source changes after a review invalidate that review's approval and require renewed verification.
- [x] Leave unrelated caller work and rejected work inspectable, with no unverified revision marked Done.

## Verification

Use public runs with controlled branch movement, input tampering, failed candidate checks, and source-revision changes; inspect Git identities and run records.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).

## Comments

### Completion — 2026-11-06

All six acceptance criteria are verified at implementation `8d345bd`, following checkpoint `dc27eb2` and review fixes. Fixed review baseline: `6c8df5cd23f35d7d164fea5e9e5d224f8bed4cf0`. Previous readiness label: `ready-for-agent`; `Blocked by:` remains dependency history.

The [criterion-specific completion evidence](../evidence/ticket-04/04-completion.md) and [16 actual CLI/Git observations (compact historical results)](../evidence/ticket-04/04-scenario-results.json) verify approved-input identities and tampering detection, revision-bound checks/reviews, exact candidate compare-and-swap, preserved external branch movement and failed merges/candidates, approval invalidation after source changes, and preserved caller/rejected work without unverified Done. Hook-capable Git operations share evidence protection; hidden index flags cannot conceal edits; final promotion cannot run hooks after verification. Rejected bytes/directories, logs, snapshots, source worktrees, and observed Git identities remain inspectable.

Checks at the final implementation: complete suite **304 passed**; focused transaction suite **48 passed**; strict mypy, Ruff lint/format, whitespace, wheel/install, and installed CLI smoke checks all passed. The original CLI/preflight/report contracts remain passing. Python used the documented reusable environment.

Separate independent reviews of the committed implementation against the original baseline: **Spec: two blockers fixed, original public reproductions rerun, no outstanding findings. Standards: no blockers; two optional readability suggestions addressed, no outstanding findings.** Full outcomes and review sources are in the evidence. No runtime changes followed final review.

No unchecked criteria or unresolved ticket-04 decisions remain. Completion bookkeeping occurs outside any active harness run using these approved feature inputs. The pre-existing skill relocation is preserved. Automatic repairs and all neighboring deferred features remain with their owning tickets; no push was performed.
