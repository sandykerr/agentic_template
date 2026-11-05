# 04: Promote only the exact verified candidate

**What to build:** Verification evidence stays bound to the submitted revision and approved requirements, and an external branch change or failed candidate cannot be overwritten by integration.

**Blocked by:** [01: Complete one scripted ticket through every gate](01-complete-one-scripted-ticket-cycle.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Independent checks and exact revisions](../spec.md#independent-checks-and-exact-revisions); [Requirements, configuration, and run records](../spec.md#requirements-configuration-and-run-records); [Agent contracts and access](../spec.md#agent-contracts-and-access).

**Scope:** Protect the existing submission-to-integration transaction and its input snapshots, without adding crash recovery or concurrent ticket execution.

## Acceptance criteria

- [ ] Record approved input identities and detect attempts to alter the requirements or harness-owned state from an agent assignment.
- [ ] Bind lightweight checks and both review results to the submitted revision, and the broader suite to the candidate revision.
- [ ] Advance integration only to the tested candidate when the expected previous integration revision is still current.
- [ ] If the integration branch changes externally, a merge fails, or candidate verification fails, preserve evidence and leave the current integration branch unchanged by this operation.
- [ ] Source changes after a review invalidate that review's approval and require renewed verification.
- [ ] Leave unrelated caller work and rejected work inspectable, with no unverified revision marked Done.

## Verification

Use public runs with controlled branch movement, input tampering, failed candidate checks, and source-revision changes; inspect Git identities and run records.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).
