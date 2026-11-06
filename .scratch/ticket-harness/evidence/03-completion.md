# Ticket 03 completion evidence

Implemented only [03: Reject invalid agent reports and review evidence](../issues/03-validate-agent-reports-and-review-evidence.md).
The broader release and neighboring transaction, repair, decision, timeout, scheduling, and live-backend features remain outstanding.

## Revisions and scope

- Fixed review baseline: `9a61ec62389e7cb1dcbf440adfbdbf2c30009e72`, captured before editing.
- Implementation checkpoint: `5b04187`, committed before independent review.
- Review fixes: `2a27565` (reject numeric overflow), then final implementation `07094fa` (reject excessive nesting before retaining parsed data).
- Every review used `git diff 9a61ec62389e7cb1dcbf440adfbdbf2c30009e72...HEAD`; all implementation changes are committed. No runtime changes followed final review.
- Files: `ticket_harness/agents.py`, `ticket_harness/runner.py`, `tests/test_cli.py`, `tests/test_reports.py`, and [CLI/report contract documentation](../../../docs/ticket-harness.md#assignment-and-report-contracts).
- Ticket 01 prerequisite implementation/completion evidence and ticket 02 compatibility were verified. The pre-existing skill relocation and handoff file were preserved outside implementation/bookkeeping commits. No active harness run using these approved feature inputs was found; test runs use disposable target requirements.

## Acceptance evidence

[Saved actual CLI/Git observations](03-fixture-observations.json) record 18 final-revision scenarios, including exit codes, durable records, assignment identities, process stdout/stderr, status comparisons, and integration references. Original assignments, input snapshots, logs, worktrees, and rejected changes remain at `/tmp/ticket-harness-03-evidence-5b_71dnl/` on this machine. Committed observations remain useful if those diagnostic `/tmp` artifacts are removed.

| Criterion | Verified implementation and observable evidence |
| --- | --- |
| Implementation outcomes, identity, and required evidence | Exact values and JSON types are required for role/ticket/attempt/base/current revision. All implementation evidence fields are required and typed; submitted outcomes need acceptance evidence, while human-decision-needed outcomes need unresolved questions. Tests independently vary missing fields, types, blank/numeric list entries, result values, and identity across all roles. Saved `submitted`, `human-decision`, `incomplete-human-decision`, and `missing-implementation-evidence` scenarios show the distinction. A valid decision report is retained as valid but stops at implementation, with no submission/review/repair. |
| Review axis/revision identity and complete findings | `role` is the review axis, preserving the existing contract. Exact identity checks reject stale base reports and wrong axes/tickets/attempts/revisions. Every optional or blocking finding requires a unique stable ID, classification, location, requirement, consequence, evidence, resolution, and actual boolean human-decision flag. Tests vary every finding field independently across both axes, including missing blocker consequence/evidence, blank evidence, and duplicate IDs. Saved stale/mismatched/incomplete/optional/blocking cases show invalid reports separately from valid blocking findings. |
| Empty findings only in complete current reviews | Original passing fixture still passes with complete empty reviews for the submitted Git revision. Identity tests use these otherwise-valid empty reviews and reject every missing/mismatched/wrong-type identity field. Missing findings and non-list findings reject independently for both axes. |
| Invalid reports cannot pass on exit zero; nonzero cannot claim success | CLI coverage includes absent/malformed/scalar reports, missing identity/evidence, boolean attempt, wrong types, stale source revisions, duplicate keys, nonfinite tokens, numeric overflow in nested metadata, and excessive nesting. Complete successful stdout with exit 7 rejects for implementation and both reviews. Saved nonzero/malformed/missing/overflow/deep scenarios retain gate exit/status/diagnostics. Excessively nested reports are rejected before attaching an unsavable object; raw stdout remains available. Accepted 100-container boundary is tested for every role. |
| Git authority and harness-only Done | Saved `git-overrides-claims` completes despite invented file/revision/state claims: harness ticket changes contain only actual `value.txt`, with a real captured submission and tested candidate/Done revision. Tests assert actual Git diffs and check/review revision identities; claimed check success cannot override an independent failed check. Unsupported results such as Done/completed reject before capture. |
| Durable invalid outcomes/artifacts with no integration advance | All 15 non-success saved scenarios exit 1, record incomplete/Blocked, preserve logs and available parsed reports or raw stdout, expose identical status records, and leave integration at the actual base. Caller changes are preserved in every scenario. Test rejection assertions verify failed gate, stage, no Done, unchanged integration/caller work, log files, and status equality. Deep valid/mismatched reports now also persist actionable invalid status rather than leaving a running record. |

Evidence validates report shape and identity, not the truth of arbitrary claims. Git and harness-run checks remain independent authorities. Extra diagnostic metadata is allowed within the documented JSON/nesting constraints. This slice introduces no automatic repair, broader human-decision workflow, or process sandbox.

## Checks and TDD

All Python used the documented reusable `.micromamba/envs/dev/bin/python`; check tools used `/tmp/ticket-harness-env/bin/`. No dependencies were changed and no network/model calls were required.

| Actual command | Result |
| --- | --- |
| `.micromamba/envs/dev/bin/python -m pytest tests/test_reports.py -q` | Focused suite passed through implementation (161 cases before the last review additions); subsequent focused checks covered each new regression. |
| `.micromamba/envs/dev/bin/python -m pytest tests/test_reports.py -q -k ambiguous` | Exit 0: 12 cases after numeric-overflow fix. |
| `.micromamba/envs/dev/bin/python -m pytest tests/test_reports.py -q -k nesting` | Exit 0: 9 cases after durability fix, covering excessive valid/mismatched reports and the accepted boundary. |
| `.micromamba/envs/dev/bin/python -m pytest -q` | Exit 0: complete suite **256 passed in 79.59s** at `07094fa` (183 report cases plus the original 73 CLI/preflight cases). |
| `/tmp/ticket-harness-env/bin/mypy` | Exit 0: strict mode, no issues in 7 source files. |
| `/tmp/ticket-harness-env/bin/ruff check ticket_harness tests examples` | Exit 0: all checks passed. |
| `/tmp/ticket-harness-env/bin/ruff format --check ticket_harness tests examples` | Exit 0: 12 files already formatted. |
| `git diff --check` | Exit 0 for implementation and tracking. |
| `XDG_CACHE_HOME=$PWD/.micromamba/cache .micromamba/envs/dev/bin/python -m pip install --no-deps --no-build-isolation --target /tmp/ticket-harness-03-verified-installed .` | Exit 0: wheel built and installed at final implementation. |
| `PYTHONPATH=/tmp/ticket-harness-03-verified-installed /tmp/ticket-harness-03-verified-installed/bin/ticket-harness --help` | Exit 0: installed run/status entry point. |
| `.micromamba/envs/dev/bin/python /tmp/observe-ticket-03.py` | Exit 0: 18 final-revision CLI/Git scenarios; saved observations identify `07094fa`. |

Red/green slices at the agreed public seam: missing implementation evidence initially completed incorrectly; incomplete optional findings initially completed incorrectly; boolean attempt initially matched integer 1; rejected reports initially lacked parsed evidence/diagnostics; valid human-decision reports initially appeared invalid; nonzero complete stdout initially lacked a retained report; duplicate/nonfinite JSON initially passed. Each failing slice was followed by implementation and passing focused CLI checks/typechecking. Independent review then supplied two further genuine failing regressions: overflow metadata (three role cases) and deeply nested valid/mismatched reports (six cases leaving status running). Both were fixed and independently re-reviewed. Schema coverage varies one invalid condition at a time through external agents and real Git repositories; no parser-internal tests or fixture-review substitutes were used.

## Standards

Fresh independent `/root/review_standards`: no findings at checkpoint `5b04187`.

Fresh independent `/root/review_standards_final`, reviewing the full diff through `2a27565`, then re-reviewing committed `07094fa`:

> No Standards findings in `07094fa` or the full implementation since `9a61ec6`.
>
> The nesting limit belongs in report validation and runs before parsed evidence enters durable records. Its iterative implementation preserves serialization headroom without adding unnecessary abstractions. The contract and documentation describe the limit, and CLI tests cover durable rejection and the accepted boundary across all roles. No documented-standard breach or baseline code smell warrants a finding.

Standards sources: AGENTS.md, domain guidance/glossary/ADR-0001, applicable design/ownership rules in `docs/harness-design.md`, scoped cohesive-module and custom-design policy sections in the spec, Python-environment guidance, pyproject checks, and the complete code-review smell baseline. No CODING_STANDARDS.md or CONTRIBUTING.md exists. Tool-enforced concerns were excluded. Fixture standards apply to fixture target code only.

## Spec

Separate fresh `/root/review_spec` found numeric exponent overflow could bypass the nonfinite-number ban and save Infinity. Fixed in `2a27565` and independently confirmed.

Separate fresh `/root/review_spec_final` found deeply nested extra metadata could prevent durable rejection serialization. Fixed in `07094fa`, then re-reviewed against the original baseline:

> No remaining Spec findings against baseline `9a61ec6`.
>
> Commit `07094fa` resolves the durability finding: excessive nesting is rejected before parsed data enters the gate record, preserving raw stdout and durable failure diagnostics. The documented 100-level boundary remains accepted.
>
> Independently reran all 21 nesting, malformed JSON, duplicate-key, nonfinite-number, and numeric-overflow CLI cases; all passed. No missing requirements, scope creep, or incorrect behavior found within ticket 03's scope.

Both axes assessed committed implementation independently under the 250K active-context target, with the assigned ticket and scoped spec requirements supplied explicitly. Standards: 0 findings outstanding, no optional suggestions. Spec: 2 blocking findings fixed and re-reviewed, 0 outstanding. No unchecked criteria or unresolved decisions remain after the final checks. Later-ticket features remain deferred.
