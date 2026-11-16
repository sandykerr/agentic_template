# Handoff: M1 after repair verification

Prepared 2026-11-13 after the human requested completed verification, updated
documentation and a persistent `$handoff` before leaving this chat. The human
explicitly selected `.scratch`, overriding the handoff skill's temporary-directory
default. This is the latest continuation entry point; the earlier
[repair handoff](handoff-m1-caller-index-repair-and-final-verification.md) supplies
approved scope, baseline provenance and broader QA requirements.

## Completed in this conversation

The human first requested inspection of evidence, then a concise acceptance plan,
source identity verification and completion of verification with recorded results.
All requested verification is now complete. No code/test changes, dependency
installation, repair checkpoint commit, independent review, candidate preparation,
promotion or M2 implementation was performed in this conversation.

- Source identity verification: all 28 source/test/configuration hashes and 50
  instruction hashes match the frozen repair. The three-file patch is byte-identical.
- Full suite: **563 passed, zero failures/errors/skips**, 2878.13 seconds
  (47m58s), exit 0. The wrapper duration is 2880.29 seconds.
- Strict mypy, Ruff lint, Ruff format and whitespace: exit 0 each.
- Each check's before/after source and instruction hashes match the frozen repair;
  a final direct comparison also passed. Required checks have not become stale
  merely because subsequent evidence/review bookkeeping changed.

Use [verification outcome](evidence/m1-index-repair-01/verification-completion.md),
[aggregate JSON](evidence/m1-index-repair-01/verification-completion-result.json)
and the [bundle README](evidence/m1-index-repair-01/README.md) rather than duplicating
commands/results or treating the earlier partial logs as completed runs.
The successful run's command/log/JUnit and source snapshots have the prefix
`completion-full-suite-retry`; the other four gates use `completion-mypy`,
`completion-lint`, `completion-format` and `completion-whitespace`.

## Environment and evidence lessons

Use current AGENTS and `docs/agents/python-environment.md`: checkout-local uv
`.venv/bin/python`, with existing dependencies already present. Read
`docs/agents/testing.md` before tests or scope selection. `/tmp` is `noexec` in
this environment; Git hook tests require executable temporary storage. The
successful full-suite record identifies the absolute checkout-local `TMPDIR`.

The checkout is accessible through `/panfs` and `/explore` aliases. The first
completion attempt failed inside the historical evidence plugin after 11 passes
(exit 3), because `Path.relative_to` compared the aliases lexically. Its logs,
result and XML remain retained. A separate `completion_capture.py` resolves paths
before relative conversion and writes new observations to
`completion-suite-observations/`. No application/test assertion or selection was
changed. Original `m1_capture.py` and historical `suite-observations/` bytes were
preserved, checked against `completion-observations-original-backup/`.

The successful full suite used that fresh helper. Its captured observations
include all four caller-index regressions, restored-source invalidation,
invalid-input rejection and the two-milestone exact-acceptance/continuation case.
The prior same-source scoped failed-baseline capture remains historical evidence,
not a new observation from this conversation. No historical writer was rerun.

## Workspace and remaining boundary

HEAD remains `e2b0a260fa192a7b51edc5f4cc5692c6340444c2`. Repair implementation is
still uncommitted in `ticket_harness/git.py`, `ticket_harness/records.py` and
`tests/test_transaction.py`. `docs/ticket-harness/agents.md` contains the separately
attributed environment-isolation explanation from the preceding session.
Environment/README/AGENTS/requirements edits and unrelated untracked recovery or
guidance files were already present; preserve them. Inspect `git status` rather
than assuming a clean tree or broadly staging it. No push occurred.

Current tracking is in [repair assessment](reviews/M1-index-repair-01.md),
[cumulative assessment](reviews/M1-architecture-01.md) and append-only
[finding history Event05](reviews/M1-architecture-01-history.md#event05--repair-checks-completed-independent-review-still-pending).
These documents and the evidence navigation were updated with actual passes.
Earlier Event04 and original reviewer reports remain historical originals.

**F1 remains open/blocking:** `review-M1-architecture-01/standards-01/F1`.
Passing tests and the prior worker's claim are not independent repair verification.
M1 is unaccepted and M2 remains ineligible. The human's earlier code/documentation
review is complete, but there is no exact repaired-candidate acceptance.

## Next execution

1. Read AGENTS, glossary/ADRs and the current review-records policy. Confirm the
   frozen source still matches before reusing these checks. Do not replay the full
   suite solely for prose bookkeeping; source/config/dependency changes require
   renewal according to policy.
2. Prepare scoped committed review input without incorporating unrelated changes.
   Fixed repair baseline is `e2b0a260fa192a7b51edc5f4cc5692c6340444c2`;
   fixed cumulative baseline is `1a623bad0b08241367948948b731b9e1f5114671`.
   They have different purposes and must remain distinct.
3. Obtain fresh independent Spec and Standards reports, plus the required fresh
   High cumulative Standards assessment over the whole affected workflow and all
   package Python files. Follow actual skill/review policy for assignments and
   role configuration; preserve original outputs and exact input identities.
   Review settings and approved authority are linked in the preceding handoff.
   No independent review was started in this conversation.
4. Address any findings, renew checks when required, and only record F1 fixed
   after the mandated independent exact-source verification. Do not reopen
   completed ticket 24 or select M2 as a substitute for cumulative repair work.
5. Prepare fresh exact-candidate QA under `milestones.md`, recording real source,
   candidate and request identities and required behavior observations. Inspect
   `prepare-qa.py` before using it; it remains unexecuted. Old disposable demo paths
   are historical, not live resumable runs. Present repair changes and the tested
   candidate for human request-specific acceptance; no scripted decision accepts M1.

## Suggested skills

Call the skill tool if available, otherwise read the named `SKILL.md`:

- **code-review**: fresh separate review axes and scoped committed inputs.
- **review-architecture**: required cumulative assessment, not merely a diagram.
- **test-strategy**: reuse exact-source check evidence and choose renewal if needed.
- **diagnosing-bugs**, then **tdd**: only if a concrete failure requires more repair.
- **handoff**: refresh this continuation record after actual next-session outcomes.
- **create-next-agent-prompt**: if preparing the later QA handoff, apply its eligibility
  checks; the root `next_agent_prompt.md` is older context and was not refreshed here.
