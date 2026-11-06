Use $implement-with-checkboxes to implement only:
.scratch/ticket-harness/issues/05-repair-rejected-submissions-within-budget.md

Ticket: **05: Repair rejected submissions within a bounded allowance**.

Follow AGENTS.md and the ticket's scoped sections in .scratch/ticket-harness/spec.md:

- Bounded failures and timeouts
- Independent checks and exact revisions
- Ticket lifecycle

Keep each agent below the feature's 250K active-context target. Read docs/agents/python-environment.md before Python, dependency installation, or checks, and use its reusable micromamba environment. Read the domain glossary and relevant ADRs before exploration/design.

Before changing code:

- Capture your starting HEAD as the fixed review baseline. Historical commits below are context, not a replacement for your baseline.
- Inspect the worktree and preserve unrelated edits. The preceding work left the pre-existing relocation from .agents/skills/implement-with-checkboxes/ to .agents/skills/custom/ unstaged; inspect its actual current state before assuming it is clean or staging it.
- Verify prerequisites 03 and 04 from their implementation, checked criteria, checks, independent reviews, completion evidence, and bookkeeping. Ticket 03's final implementation is 07094fa, bookkeeping 9604651; see .scratch/ticket-harness/evidence/03-completion.md. Ticket 04's checkpoint is dc27eb2, final implementation/review fixes 8d345bd, bookkeeping 237d6ff; see .scratch/ticket-harness/evidence/04-completion.md and .scratch/ticket-harness/evidence/04-fixture-observations.json. Both ticket headers are completed. Tickets 01/02 have legacy ready-for-agent headers but verified completion evidence; do not mistake those labels for unfinished prerequisites.
- Read docs/ticket-harness.md and ticket_harness/{runner,agents,records,git,inputs}.py. Inspect the current public tests in tests/test_cli.py, tests/test_reports.py, tests/test_transaction.py, and tests/test_preflight.py as needed. The preceding implementation passed 304 tests; that is historical evidence, not proof of your changes.

Implement one ticket's automatic repair loop, covering every acceptance criterion with observable evidence:

- Make the repair allowance configurable, defaulting to two repairs after the initial submission. A worker's internal editing/testing does not consume additional attempts.
- Give every repair a fresh process/context, the current changes, rejected revision identities, and concrete check/review failure evidence.
- Support repair after lightweight-check failures, either review axis, and candidate-integration failures.
- Capture a repaired submission revision and repeat the applicable lightweight checks, both fresh reviews, and the candidate suite before integration. Previous approvals cannot authorize changed source.
- Preserve rejected changes and complete attempt history when the allowance is exhausted; leave the ticket Blocked and return an incomplete result.
- Demonstrate both successful repair and exhausted allowance. Missing/invalid reports and process failures must remain bounded by the same failure policy, without an unlimited secondary retry path.

The current runner, assignment identity, and artifact/worktree names assume one attempt. Extend their public contracts only as needed for the approved loop. Keep every attempt's prompts, reports, command output, revisions, and diagnostics inspectable; do not overwrite earlier evidence when starting another attempt. Document affected configuration, assignment, and run/status fields. Use the existing combined design policy and cohesive module ownership rather than introducing speculative abstractions or resolving architectural choices the human still owns.

Preserve all prerequisite invariants:

- Git and harness-run checks own source/revision evidence; agent claims cannot declare Done or override observed changes/checks.
- Report validation rejects malformed/incomplete/stale/mistyped reports, nonzero exits, duplicate/nonfinite/overflow JSON, and nesting above 100 object/array levels. Attempt identity must remain exact through repairs. A valid human-decision-needed report currently stops before capture/review/repair; retain that behavior pending ticket 06.
- Approved sources/snapshots remain bound to recorded content identities. records.protect brackets external processes and hook-capable Git worktree/submission/merge operations, restores harness-owned evidence after saving rejected contents, and leaves rejected source inspectable. Deleted snapshots and snapshots replaced by directories are handled durably.
- Checks/reviews remain bound to their submitted revision; all verified sources are rechecked, including detection of index flags that hide edits. Repairs must not inherit stale approvals or conceal changed source.
- Candidate parents/tree match reviewed source, the broader suite tests the exact candidate, and promotion uses compare-and-swap with hooks disabled for the final ref update. Preserve external branch changes and the existing stop/no-overwrite behavior; a repair cannot silently authorize a changed baseline or altered requirements. Keep caller HEAD, index, working files, and rejected work intact.
- Preflight rejection and failed shared baseline still start no worker/repair attempt. Status remains a read-only view of durable records.

Use $tdd at the already agreed public CLI/Git/report seam: scripted external processes and real temporary Git repositories. Write one failing behavioral test, implement that slice, and repeat. Script a successful repair from a rejected submission and exhaustion across required gate types; inspect supplied failure evidence, fresh processes/attempt identities, repaired content, renewed lightweight checks and both review axes, candidate identities, final integration/Done, and complete preserved history. Assert bounded outcomes for invalid reports/process failures and preserve valid human-decision stopping behavior. Test public observations, not parser internals, internal mocks, or scripted fixture reviewers as a substitute for implementation review.

This ticket does not add broader human-decision handling (06), optional-suggestion reporting workflows (07), process timeouts (08), dependency scheduling (09/10), live Codex/role profiles or new role-skill delivery (11–13), OS role-access enforcement (14), concurrent ticket execution, or crash recovery/resume. Numeric timeout configuration is not part of this slice merely because the scoped failures section also discusses timeouts.

Run focused tests and strict typechecking throughout implementation, then the complete suite and documented checks using the reusable Python environment. The preceding run found /tmp/ticket-harness-env/bin/mypy and /tmp/ticket-harness-env/bin/ruff; verify availability rather than assuming temporary tools persist. Required checks include pytest, strict mypy, Ruff lint/format, and whitespace; verify packaging/installed CLI when appropriate.

After checks pass, commit only the implementation as a checkpoint before $code-review, whose review uses the committed diff. Supply your captured baseline, ticket 05, and scoped spec requirements explicitly. Obtain separate fresh Spec and Standards reviews; fix blocking findings, rerun affected checks, commit fixes, and re-review changed code against the original baseline. Record optional suggestions separately.

After verified implementation and review, follow docs/agents/issue-tracker.md Completion bookkeeping. Verify every acceptance criterion from the current revision and required independent reviews before checking it. Set ticket 05 to **Status:** completed only when all criteria/gates pass, retain its previous ready-for-agent label in the completion comment, and preserve Blocked by as dependency history. Record criterion-specific evidence, implementation/fix commits, actual checks, separate review outcomes, and unresolved items; link evidence from .scratch/ticket-harness/README.md. Reconcile markers, header, comment, and index, then commit only this ticket's bookkeeping separately.

After implementation and bookkeeping commits exist and completion is fully verified, follow the implementation skill's automatic $create-next-agent-prompt step and commit that handoff separately. Do not start the next ticket. The feature's early ticket-17 priority applies only after prerequisite 13 is complete; it does not displace ticket 05 now.

Do not modify approved inputs belonging to an active harness run; report that condition as a blocker. Do not push. If any gate remains blocked, leave unverified criteria unchecked and report the exact blocker. Claim completion only after implementation, checks, independent reviews, commits, and bookkeeping are finished. Report implementation/bookkeeping/handoff commit references, check and separate review outcomes, unchecked criteria, and next_agent_prompt.md with its selected ticket or no-eligible-ticket status.
