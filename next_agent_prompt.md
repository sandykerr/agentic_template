Use $implement-with-checkboxes to implement only:
.scratch/ticket-harness/issues/06-surface-human-decisions-without-retrying.md

Ticket: **06: Stop for decisions outside approved contracts**.

Follow AGENTS.md and the ticket's scoped sections in .scratch/ticket-harness/spec.md:

- Public interface and approval
- Agent contracts and access
- Bounded failures and timeouts

Keep each agent below the feature's 250K active-context target. Read docs/agents/python-environment.md before Python, dependency installation, or checks and use its reusable micromamba environment. Read GLOSSARY.md and relevant ADRs before code exploration/design.

Before changing code:

- Capture your starting HEAD as the fixed review baseline. Historical commits below are context, not a replacement for your baseline.
- Inspect the worktree and preserve unrelated edits. The pre-existing relocation from .agents/skills/implement-with-checkboxes/ to .agents/skills/custom/ remains unstaged (deleted old skill plus untracked custom directory); inspect the actual state before staging anything.
- Verify prerequisite 05 from implementation, checked criteria, actual checks, separate independent reviews, completion evidence and bookkeeping. Its implementation is `34a49b7`, bookkeeping `2a454df`; see .scratch/ticket-harness/evidence/05-completion.md and .scratch/ticket-harness/evidence/05-fixture-observations.json. All six criteria and its header are completed. Prerequisite context: 03 implementation `07094fa`/bookkeeping `9604651`, 04 final implementation `8d345bd`/bookkeeping `237d6ff`, with their evidence in the same directory. Tickets 01/02 have legacy ready-for-agent headers but verified completion evidence; do not treat them as unfinished prerequisites.
- Read docs/ticket-harness.md, docs/harness-design.md, and ticket_harness/{runner,agents,records,git,inputs}.py. Inspect public tests in tests/test_repairs.py, tests/test_reports.py, tests/test_transaction.py, tests/test_cli.py and tests/test_preflight.py as needed. The preceding final implementation passed 362 tests (58 repair cases plus 304 prerequisite cases); that is historical evidence, not proof of your changes.

Implement only the human-decision outcome and handoff within the existing one-ticket cycle, covering every criterion with observable evidence:

- Recognize a valid human-decision-needed report from implementation or either review axis.
- Preserve current work and record the precise unresolved decision, relevant approved contract, and available evidence.
- Block the affected ticket immediately rather than consuming remaining repairs to invent requirements or change an approved interface.
- Keep approved spec, ticket, and standards unchanged, and leave integration untouched in response to a decision request.
- Expose the decision through status and the final report, with attempt counts reflecting only work actually performed.

Current behavior and contracts to extend carefully:

- A valid implementation report with result `human-decision-needed` already stops before capture/review/repair, including on nonzero exit; its unresolved_questions are retained. Both review axes already require complete findings with typed `human_decision_needed` booleans, but the runner currently treats blocking review findings as repairable regardless of that flag. Inspect the existing report contracts before deciding what changes are needed; preserve exact assignment identity and distinguish structurally valid reports from process/gate success.
- `max_repairs` is a configurable nonnegative integer, default 2. Every repair uses a fresh process and a distinct worktree with current working contents, including uncommitted changes after invalid reports. Initial assignment is attempt 1, repairs 2/3/etc. Repairs keep role `implementation`; assignment revision is the starting source commit while base_revision stays fixed. `repair_context` supplies the previous failure and all captured rejected revisions; `check_results` supplies full gate history and concrete report/output evidence.
- `run.json.attempts` preserves source/start/submitted/candidate identities, state/failure and gate_start/gate_end ranges; the top-level ticket exposes the latest attempt. Gates and operations record attempt identity (baseline 0). Initial artifact/worktree names remain unchanged, while repairs use collision-free `attempt-2-`, `attempt-3-`, etc. prefixes. Preserve all earlier prompts, reports, command output, source and diagnostics.
- The existing tests' shared TicketFixture explicitly sets `max_repairs: 0` for prerequisite rejection scenarios. The repair fixture removes that field to test the default allowance. Human-decision tests must exercise available repair allowance so immediate stopping is proved rather than masked by a zero limit. Include a decision arising in a later repair and keep history/counters accurate.

Preserve prerequisite invariants:

- Git and harness-run checks own source/revision evidence; agent claims cannot declare Done or override observed changes/checks. Missing/invalid reports and process failures remain bounded by the existing single repair allowance; a decision request must not become success.
- Report validation still rejects malformed/incomplete/stale/mistyped identities or evidence, nonzero success claims, duplicate/nonfinite/overflow JSON and nesting above 100 object/array levels. Complete review identity/typed findings remain mandatory. Do not turn invalid human-decision-like data into trusted decision evidence or skip report validation.
- Approved sources/snapshots stay bound to recorded content identities. records.protect brackets external processes and hook-capable Git worktree/submission/merge operations, restores harness-owned evidence after saving rejected contents, and leaves rejected source inspectable. Preserve deletion/directory-replacement handling and protection of earlier-attempt artifacts.
- Every repaired submission requires a new captured revision, applicable lightweight checks, both fresh reviews and the exact candidate suite. Changed source or hidden index flags invalidate approvals; no stale approval can authorize changed source.
- Candidate parents/tree match reviewed source; the suite tests that candidate; promotion uses compare-and-swap with hooks disabled for final ref update. Preserve external integration changes, the approved baseline/requirements, caller HEAD/index/files and rejected work. A repair cannot authorize a new baseline or requirements.
- Preflight rejection and failed shared baseline start no worker/repair attempt. An invalidated shared baseline stops before starting another repair. Status stays a read-only view of durable records.

Use $tdd at the already agreed public CLI/Git/report seam: scripted external processes and real temporary Git repositories. Write one failing behavioral test, implement that slice, and repeat. Script ambiguity/approved-contract conflicts from implementation, Spec and Standards roles with repair allowance available. Assert immediate Blocked/incomplete handoff, precise contract/decision/evidence, preserved current work and prior history, unchanged approved inputs/integration, no subsequent repair or verification processes, correct actual attempt counts, and matching read-only status/final output. Cover decisions during a later repair as well as an initial attempt, and preserve ordinary successful and exhausted repair behavior. Test public observations, not parser internals, internal mocks, or scripted fixture reviewers as a substitute for implementation review.

Document affected assignment/report and run/status contracts. Follow the existing combined design policy and cohesive module ownership, choosing the simplest functional/object implementation that preserves approved interfaces; do not resolve consequential design choices the human still owns.

This ticket does not add optional-suggestion reporting workflows (07), process timeouts (08), dependency scheduling/continuation (09/10), new design/role skill delivery or live Codex profiles (11–13), OS role-access enforcement (14), concurrent execution, or crash recovery/resume. Numeric timeout configuration is not part of this slice merely because its scoped failure section discusses timeouts. Retain current optional-finding and ordinary bounded-repair behavior while handling explicit human decisions.

Run focused tests and strict typechecking throughout implementation, then the complete suite and documented checks through the reusable Python environment. Verify availability of /tmp/ticket-harness-env/bin/mypy and /tmp/ticket-harness-env/bin/ruff rather than assuming temporary tools persist. Required checks include pytest, strict mypy, Ruff lint/format and whitespace; verify packaging/installed CLI when appropriate.

After checks pass, commit only the implementation checkpoint before $code-review, whose review uses the committed diff. Supply your captured baseline, ticket 06 and scoped spec requirements explicitly. Obtain separate fresh Spec and Standards reviews; fix blocking findings, rerun affected checks, commit fixes and re-review changed code against the original baseline. Record optional suggestions separately. Fixture reviewer scripts do not replace these implementation reviews.

After verified implementation and review, follow docs/agents/issue-tracker.md Completion bookkeeping. Verify every criterion at the current revision with required checks/reviews before checking it. Set ticket 06 to **Status:** completed only when all gates pass, retain its previous ready-for-agent label in the completion comment and preserve Blocked by as dependency history. Record criterion-specific evidence, implementation/fix commits, actual checks, separate review outcomes and unresolved items; link evidence from .scratch/ticket-harness/README.md. Reconcile markers, header, comment and index, then commit only this ticket's bookkeeping separately.

After implementation and bookkeeping commits exist and completion is fully verified, follow the implementation skill's automatic $create-next-agent-prompt step and commit that handoff separately. Do not start the next ticket. The feature's early ticket-17 priority applies only after prerequisite 13 is complete; it does not displace ticket 06 now.

Do not modify approved inputs belonging to an active harness run; report that condition as a blocker. Do not push. If any gate remains blocked, leave unverified criteria unchecked and report the exact blocker. Claim completion only after implementation, checks, separate reviews, commits and bookkeeping are finished. Report implementation/bookkeeping/handoff commit references, check and separate review outcomes, unchecked criteria, and next_agent_prompt.md with its selected ticket or no-eligible-ticket status.
