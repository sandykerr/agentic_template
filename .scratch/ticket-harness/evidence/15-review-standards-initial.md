# Ticket 15 Standards review

Fixed baseline: `90255aaf6faf9aedce18f7159093f5dbfde294b7`.
Reviewed implementation: `36ed3e72c278cf147c84ae9c282cd2899af23ad0` (entire baseline-to-HEAD diff).
Independent fresh GPT-6.1 Sol High Standards assignment, 250K active-context target; no Spec review read, subagents, implementation edits, staging or commits.

**Result: one blocking finding; zero optional suggestions.**

**STD15-01 — Blocking: restore canonical gate ownership after deserialization.**
Location: `ticket_harness/runner.py:292–294`, interacting with `validate_sources()` at lines 132–144 and checkpoint serialization in `ticket_harness/checkpoints.py:81–87`.

Rule: `docs/ticket-harness.md:584–589` explicitly requires changed verified worktrees to mark the affected gate `passed: false`, `verification_status: "invalidated"`, with a diagnostic. The spec's independent-checks/exact-revisions and inspectable run-record requirements preserve this contract across continuation. The combined design policy also requires explicit ownership and enforcement of invariants.

JSON deserialization creates separate dictionaries for `checkpoint["verified"]` and `record["gates"]`. Restoration retains the former, so `validate_sources()` mutates detached evidence while saving the latter. Independently reproduced through public CLI processes: stop at M1, continue, edit the baseline worktree, request another stop. The runner exits 1/incomplete with "Verified source changed", but its durable baseline gate still reports `passed: true`, without invalidation status or diagnostic. Promotion safely stops; the documented gate record is nevertheless incorrect, compromising downstream status/evidence inspection.

Resolution: restore verified-source associations to their canonical run gate entries, using a stable gate identity/index or equivalent explicit ownership. Add a public CLI regression invalidating an earlier verified source after continuation and assert the durable affected gate fields. No human design decision is required. Evidence: [reproduction](15-standards-restored-evidence-repro.json), [script](15-standards-restored-evidence-repro.py).

Coverage assessment: existing CLI/process/real-Git seam, isolated writable repositories and owned-process cleanup are preserved. The 15 mutation cases exercise distinct validation failures; repeated-stop and replay cases cover meaningful interactions. No additional concrete redundancy, fixture-isolation or brittle-assertion blocker was found. General smell heuristics did not establish further mandatory changes.

Audit provenance: [independent audit](15-standards-audit.json) and [script](15-standards-audit.py) verify 23 current/committed source hashes, nine final gate source maps/exits, all 122 retained raw observation hashes/outcomes, three successful checkpoint archives and consumed-decision hashes, nine installed sources, wheel/backend hashes, and five original historical logs. Recorded final suite: 543 passed/785.01s; not repeated. The unrelated tracker hash remains `3803de99e541e60d2e9f733d5c98b009a43e60a9584e3819adffc55eae0214ce`. Applicable AGENTS/domain/ADRs, scoped spec/proposal, full handoff, combined design lenses and testing policy/strategy were read. Development M1 acceptance and deferred runtime capabilities remain outside this review.
