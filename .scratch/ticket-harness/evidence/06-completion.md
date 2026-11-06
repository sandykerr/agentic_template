# Ticket 06 completion evidence

Implemented only [06: Stop for decisions outside approved contracts](../issues/06-surface-human-decisions-without-retrying.md).
Verified implementation: `dc1018e07f03c967ed686707c4d7f5a9660a6332`.

## Revisions and scope

- Fixed starting review baseline: `2adf9b5fd906e8337c5147e94ab5ceb35ac8dbef`, captured before changes.
- Implementation checkpoint: `dc1018e`, committed after checks and before separate fresh Spec and Standards reviews of the complete baseline-to-checkpoint diff. No fixes or runtime changes followed review.
- Files: `ticket_harness/{runner,agents}.py`, `tests/test_human_decisions.py`, and [public assignment/report/run/status contracts](../../../docs/ticket-harness.md).
- Prerequisite 05 verified from implementation `34a49b7`, bookkeeping `2a454df`, all six checked criteria/completed header, separate independent reviews, [completion evidence](05-completion.md), and [saved observations](05-fixture-observations.json). No runtime/test changes existed between that implementation and this ticket's baseline. Actual pre-change checks passed: **58 repair tests** and the complete **362-test suite**. Prerequisite 03 (`07094fa`/`9604651`) and 04 (`8d345bd`/`237d6ff`) evidence was also read. The legacy readiness headers on 01/02 do not negate their verified completion evidence.
- No active harness run using these feature inputs was found. All verification runs use separate disposable target requirements. The pre-existing skill relocation remains unstaged and outside ticket commits. No push was performed.

## Acceptance evidence

[19 saved actual CLI/Git observations](06-fixture-observations.json) identify `dc1018e`, exact assignment and revision identities, validated decision reports and approved-input snapshot/hash references, gate/process outcomes and diagnostics, actual attempt history/ranges, preserved source paths, final integration, and matching status. All scenario assertions and status comparisons passed. Diagnostic target repositories, source worktrees, prompts, stdout/stderr and durable run records remain at the recorded `/tmp/ticket-harness-test-*` paths; committed observations survive eventual temporary-directory cleanup.

| Criterion | Verified behavior and observable evidence |
| --- | --- |
| Recognize valid implementation or either-axis decisions | Twelve CLI scenarios span implementation/Spec/Standards, initial attempt/later repair, and exits 0/7. Each retains `report_status: valid`, marks the gate failed, and exposes the decision. Worker reports use existing unresolved questions/evidence; reviews use complete blocking findings with a typed true flag. Full report validation precedes recognition. Twenty-one additional invalid-decision cases cover incomplete reports/other findings, stale revision, boolean identity, mistyped evidence/flag, duplicate keys, overflow and excessive nesting across all roles; none creates trusted decision metadata, and all exhaust only the ordinary three-attempt bound. |
| Preserve work, precise decision, approved contract and evidence | `ticket.human_decision` and the affected attempt retain the complete validated report, actual role/attempt/revision, exact approved input source/snapshot/hash references and assignment/stdout/stderr paths. Worker summary/questions identify the approved ticket and unresolved value/interface choice; review requirement/consequence/evidence/resolution identify the conflict. Tests inspect retained `decision-work.txt`, current value, prior rejected submission contents, every earlier artifact, and repair context. The existing report schema is preserved; descriptive claims are not promoted to verified source/check facts. |
| Block immediately without repair churn | Every valid decision returns exit 1, incomplete/Blocked on attempt 1 or 2 with the default two-repair allowance still available. No next assignment/worktree, subsequent check/review gate or candidate operation starts. Implementation decisions stop before capture. Mixed-finding tests put an ordinary repairable blocker before a human-decision finding and preserve multiple precise decisions; the explicit decision still stops immediately. |
| Preserve approved inputs and integration | Tests compare original spec/ticket/standards bytes and every approved source/snapshot after each decision. Integration remains at the original base and no Done revision is recorded. Dirty caller HEAD/index, distinct staged/unstaged contents and untracked files survive. Existing approved-input/evidence integrity checks, source validation and Git promotion rules remain intact, with all prerequisite regression cases passing. |
| Expose decision and actual counters in status/final output | Run's returned JSON equals durable `run.json` and read-only status; status leaves run bytes and target status unchanged. Top-level ticket and attempt have matching handoffs. Attempt counters/ranges describe only actual assignments/gates. Later-repair scenarios retain attempt 1's rejected revision and failed check, use its current contents and repair evidence for attempt 2, then stop with one repair still available. Nonzero exits remain visible alongside the precise decision diagnostic. |

The two optional-flag regressions preserve existing nonblocking behavior and integration without consuming repairs; no new optional-suggestion reporting workflow was added. Ordinary successful repair, exhaustion, baseline/preflight rejection, invalid reports, source/evidence protection and exact candidate promotion remain covered by the original 362 tests. Timeout configuration, scheduling/continuation, live Codex/role skills, OS access enforcement, concurrency and recovery/resume are outside this slice.

## Checks and TDD

All Python used `/home/ajkerr1/development/agentic_template/.micromamba/envs/dev/bin/python` after reading the environment instructions. `/tmp/ticket-harness-env/bin/mypy` and `ruff` were verified available. No dependencies or network/model calls were added to the harness or fixtures.

| Actual check | Result |
| --- | --- |
| Pre-change `python -m pytest tests/test_repairs.py -q` | Exit 0: **58 passed in 84.19s**. |
| Pre-change `python -m pytest -q` | Exit 0: **362 passed in 269.62s**. |
| Focused `python -m pytest tests/test_human_decisions.py -q` | Exit 0: **37 passed in 51.55s**; later stronger preservation/diagnostic assertions passed in the full suite. The separate Spec reviewer independently reran all **37** at the checkpoint and passed. |
| Final `python -m pytest -q` | Exit 0: **399 passed in 232.26s**, including 37 decision cases and all 362 prerequisite cases. These files were committed unchanged as `dc1018e`. |
| `/tmp/ticket-harness-env/bin/mypy` | Exit 0 throughout: strict mode, no issues in 7 source files. |
| `/tmp/ticket-harness-env/bin/ruff check ticket_harness tests examples` | Exit 0: all checks passed. |
| `/tmp/ticket-harness-env/bin/ruff format --check ticket_harness tests examples` | Exit 0: 15 files formatted. |
| `git diff --check`, staged check and baseline-to-checkpoint whitespace check | Exit 0. |
| Reusable Python `-m pip install --no-deps --no-build-isolation --target /tmp/ticket-harness-06-installed .` | Exit 0: wheel built and installed without network; runtime files match the checkpoint. |
| Installed `ticket-harness --help`, from `/tmp` with installed-only `PYTHONPATH` | Exit 0: run/status entry point. |
| Installed CLI run/status decision scenario | Passed: Standards report with exit 7 produces Blocked/incomplete on attempt 1, status matches final JSON and integration stays unchanged. The installed package was invoked from `/tmp` with installed-only `PYTHONPATH`. |
| Reusable Python `/tmp/observe-ticket-06.py` at `dc1018e` | Exit 0: **19** actual CLI/Git scenarios passed; observations linked above. |

Red/green work used the already agreed public CLI/Git/report seam with scripted external processes and real temporary repositories. The first failing Spec decision test consumed all three attempts; its immediate-stop/handoff slice then passed. Expanding to worker decisions, nonzero exits and later repairs exposed missing worker handoff metadata and loss of the question in nonzero diagnostics; the next implementation slice made all 12 scenarios pass. Further cases verify mixed findings and preserved validation/optional behavior. A misplaced test-only status assertion was corrected before final verification. No parser-internal mocks or fixture reviewer scripts substitute for the independent implementation reviews below.

## Standards

Fresh independent `/root/review_standards_06`, using GPT-6.1 Sol and a fresh context below the feature's 250K target, reviewed the complete `2adf9b5...dc1018e` committed diff:

> No Standards findings.
>
> Reviewed all four changed files against the documented project rules and combined design guidance. Lifecycle decisions remain owned by `runner.py`; assignment guidance and report validation remain in `agents.py`. Tests exercise the public CLI/report seam, and the documentation describes the resulting handoff consistently.
>
> No supported baseline smells warrant an optional suggestion.
>
> Checks: read-only diff and source inspection. No additional tests run; parent-reported verification was not repeated.

Standards sources: AGENTS.md, domain/environment/tracker guidance, GLOSSARY.md, ADR-0001, `docs/harness-design.md`, cohesive-module and combined design-policy spec sections, `pyproject.toml`, public contracts, and the complete code-review smell baseline. Matt's deep-module vocabulary and Microsoft's OOP guidance supplied the combined design lens. No CODING_STANDARDS.md or CONTRIBUTING.md exists. Tool-enforced issues were kept separate.

## Spec

Separate fresh `/root/review_spec_06`, also GPT-6.1 Sol and below the context target, reviewed the same complete committed diff with ticket 06 and its scoped Public interface and approval, Agent contracts and access, and Bounded failures and timeouts requirements supplied explicitly:

> No findings.
>
> (a) Missing or partial requirements: none. All five ticket criteria are implemented, including decisions during later repairs, preserved work/history, unchanged approved inputs and integration, and durable status/final handoff with accurate attempts.
>
> (b) Scope creep: none. Changes stay within the existing one-ticket decision outcome, assignment instructions, records, documentation, and CLI scenarios.
>
> (c) Implemented requirements that look wrong: none. Whole-report and exact identity validation precede decision recognition. Valid decisions stop further processes and repairs even on nonzero exit, while process failure remains recorded. Ordinary blockers retain bounded repairs; optional findings retain nonblocking behavior.
>
> Blockers: none. Optional suggestions: none.
>
> Independently inspected the implementation diff and surrounding lifecycle, validation, protection, and record code. Focused verification using the reusable absolute Python: `tests/test_human_decisions.py` — **37 passed**. No files edited.

Standards: 0 blockers, 0 optional suggestions. Spec: 0 blockers, 0 optional suggestions. All five criteria are verified at `dc1018e`; no unchecked criteria or unresolved ticket-06 decisions remain. Implementation, checks and both reviews precede ticket bookkeeping. The next handoff is created only after the separate bookkeeping commit; it does not start the next ticket.
