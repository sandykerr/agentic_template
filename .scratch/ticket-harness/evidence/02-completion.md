# Ticket 02 completion evidence

Implemented only [02: Reject invalid requirements before starting work](../issues/02-reject-invalid-inputs-before-execution.md). The verified implementation revision is `b11fd20f37dbb18730278bd271cf3d47d05f6e82`.

## Baseline, prerequisites, and scope

- Fixed review baseline captured before edits: `0efc06333ca0996fa8953d69c3ae682a86e47ce7`. The initial worktree was clean; no unrelated changes needed preservation.
- Ticket 01 implementation (`b09e324`, `1666920`), checked criteria, completion comment, and [completion evidence](01-completion.md) were present. Its original eight CLI tests and strict typecheck passed before editing.
- Read the ticket, its scoped spec sections (Public interface and approval; Requirements, configuration, and run records), domain/glossary/ADR, tracker/readiness conventions, current CLI/input/report documentation, implementation, and existing tests before changing code.
- No active harness run using these approved inputs was found. Repository worktree inspection before implementation and bookkeeping showed only this main checkout. Approved source requirements remained unchanged throughout implementation and review; bookkeeping followed verification outside a harness run.
- Checkpoint `855a4c8` — `Reject invalid ticket bundles before harness execution` — was committed after passing checks and before the first independent reviews.
- Review fix `dfdb1a6` — `Validate relative executables against the approved base tree` — resolved the initial caller-only executable availability defect.
- Final review fix `b11fd20` — `Reject executable paths with ambiguous runtime resolution` — resolved relative PATH and lexical/runtime path differences. All three implementation commits were reviewed against the original baseline, never a moving baseline.
- Changed implementation files: `ticket_harness/inputs.py`, `ticket_harness/agents.py`, `ticket_harness/runner.py`, `tests/test_preflight.py`, and [CLI/input documentation](../../../docs/ticket-harness.md).
- Comprehensive agent-report validation, transaction hardening, repairs, dependency scheduling/automatic prerequisite execution, and live Codex remain deferred. This ticket validates dependency eligibility and executes only the one selected ticket.

## Criterion-specific verification

All evidence below applies to the final verified implementation revision, whose full suite and independent reviews passed. Behavioral tests use the agreed public CLI, scripted external agents, real temporary Git repositories, and Git/report observations; none tests parser internals.

| Acceptance criterion (unchanged wording) | Evidence |
| --- | --- |
| Normalize stable ticket IDs, titles, readiness labels, dependencies, acceptance requirements, and check references into one documented contract. | The [canonical input contract](../../../docs/ticket-harness.md#canonical-input-contract) specifies JSON configuration, supported plain/bold Markdown metadata, numeric ID normalization, authoring readiness vocabulary, dependency references/links, acceptance checklist text, check references/defaults, normalized `run.json.requirements`, and prerequisite completion records. `test_authoring_metadata_normalizes_without_treating_checkboxes_as_execution_state` asserts the complete normalized entry; `test_only_referenced_checks_run_and_are_supplied_to_assignments` verifies actual check selection and assignment contents. The saved `valid-normalized` CLI observation shows ID `1` normalized to `01`, checked acceptance text retained, comments excluded, all six gates passed, and Done/integration at `f775b8a32443e97f4c28cf251bc213af16eb4938`. |
| Reject duplicate IDs, missing dependency references, dependency cycles, contradictory metadata, missing acceptance requirements, and unusable check configuration with actionable diagnostics. | [Preflight CLI tests](../../../tests/test_preflight.py) independently exercise duplicate normalized IDs; missing dependency; two-ticket, self, and unselected cycles; duplicate Status/JSON/check references; filename/heading, ID/Title, and dependency title/link contradictions; duplicate headings/acceptance sections; missing/empty/example-only acceptance; unsupported front matter; unknown checks; invalid fields, names, argument arrays, missing executables, and refs. Executable repair regressions cover untracked files, caller-only executable permissions, relative PATH search, and ambiguous `..`, `/`, `/.` runtime paths, while accepting a tracked executable absent from the dirty caller checkout. Each rejected test asserts its actionable diagnostic. Saved observations retain actual messages for each major category and the review regressions. |
| Keep triage readiness distinct from dependency satisfaction: non-agent-ready work and selections with unsatisfied prerequisites cannot silently execute. | `test_non_agent_ready_selection_rejects_even_with_no_dependencies` rejects all four other configured readiness labels. `test_bundle_can_contain_human_ready_work_without_executing_it` accepts human-ready context while running only the selected agent-ready ticket. `test_titled_markdown_dependencies_normalize_and_reject_unsatisfied_prerequisites` proves checked acceptance boxes do not satisfy prerequisites. `test_prerequisite_completion_requires_current_integrated_done_evidence` rejects incomplete, unintegrated, and stale evidence. `test_prerequisite_done_in_an_integrated_run_permits_only_the_selected_ticket` first obtains genuine harness Done evidence, then successfully executes exactly one follow-up assignment using that integrated prerequisite. Saved `non-agent-ready` and `unsatisfied-prerequisite` observations both exit 1 at inputs, attempt 0. |
| Do not launch a worker or change integration references when preflight rejects the inputs. | Every rejection uses the CLI test's shared `reject` assertions: nonzero exit, `invalid-input`, `failure.stage == inputs`, attempt 0, empty gates, no assignment artifacts, absent external-agent launch marker, no Done revision, byte-identical `git show-ref`, unchanged worktree list/caller Git status, and read-only status matching the record. All 18 saved invalid observations independently confirm these invariants, including the executable cases discovered in review. |
| Demonstrate valid and invalid bundles through CLI outcomes in real temporary repositories. | Final complete suite: **73 passed**, consisting of the original eight ticket-01 cycle/rejection tests and 65 ticket-02 preflight cases. [Saved fixture observations](02-fixture-observations.json) contain 19 actual CLI scenarios (one passing and 18 rejecting), revision identities, failure messages, agent-launch observations, Git refs, worktree/caller preservation, status equality, and raw run-record locations. Valid dependency evidence and unselected human-ready context additionally pass in the suite. |

The standalone observation runner imported no harness internals. Its final execution used revision `b11fd20` and retained disposable repositories, approved snapshots, command logs, and run records under `/tmp/ticket-harness-02-evidence-3v6qxg0p/`. Committed JSON preserves the relevant observations even if those temporary diagnostic artifacts are later removed. Earlier observation runs were superseded by this final-revision run.

## TDD and checks

Each new behavior was exercised at the public CLI before implementing its slice. The initial missing-acceptance test demonstrated an incorrect successful run before the guard was added. Subsequent red/green slices covered normalization, metadata conflicts, references/check execution, command configuration, bundle IDs, missing dependencies, cycles, dependency links/titles, completion eligibility, acceptance ambiguities, and review-discovered executable failures. Broader parameter cases exercise one invalid condition per repository. Fixture reviewer scripts test harness gates; they were never substituted for the independent implementation reviews below.

Commands ran from the repository root using the documented reusable micromamba Python. Static tools used the existing isolated micromamba prefix documented for checks; no environment/dependency changes were needed.

| Command | Actual result |
| --- | --- |
| `.micromamba/envs/dev/bin/python -m pytest -q` (initial complete suite) | Exit 0; original **8 passed**, before code changes. |
| `.micromamba/envs/dev/bin/python -m pytest tests/test_preflight.py -q` | Exit 0; repeatedly during implementation, reaching **58 passed** at the initial checkpoint. Later repair slices ran focused executable cases before the complete final suite. |
| `.micromamba/envs/dev/bin/python -m pytest tests/test_preflight.py -k 'relative or caller_relative_path' -q` | Exit 0; **6 passed** during executable repairs; the additional `/.` case was subsequently demonstrated red, fixed, and verified by the full suite. |
| `.micromamba/envs/dev/bin/python -m pytest` | Exit 0 at final implementation; **73 passed in 14.52s**, Python 3.12.16 / pytest 9.2.0. Final independent Spec reviewer also reran the suite: **73 passed**. |
| `/tmp/ticket-harness-env/bin/mypy` | Exit 0; strict mode, no issues in 7 source files. Repeated during implementation and after repairs. |
| `/tmp/ticket-harness-env/bin/ruff check ticket_harness tests examples` | Exit 0; all checks passed. |
| `/tmp/ticket-harness-env/bin/ruff format --check ticket_harness tests examples` | Exit 0; 11 files formatted. |
| `git diff --check` | Exit 0 for implementation and review repairs; rerun for bookkeeping. |
| `XDG_CACHE_HOME=/home/ajkerr1/development/agentic_template/.micromamba/cache .micromamba/envs/dev/bin/python -m pip install --no-deps --no-build-isolation --target /tmp/ticket-harness-02-verified-installed .` | Exit 0; final-revision wheel built and installed without fetching dependencies. |
| `PYTHONPATH=/tmp/ticket-harness-02-verified-installed /tmp/ticket-harness-02-verified-installed/bin/ticket-harness --help` | Exit 0; installed run/status entry point works. |
| `.micromamba/envs/dev/bin/python /tmp/ticket-harness-02-observe.py` | Exit 0; 19 actual CLI/Git scenarios, final revision confirmed in committed observations. |

## Standards

Final independent fresh reviewer `/root/review_standards_verified`, reviewing the entire committed `git diff 0efc06333ca0996fa8953d69c3ae682a86e47ce7...HEAD` at `b11fd20`:

> No Standards findings.
>
> Reviewed the full baseline-to-HEAD diff, including both executable-resolution repairs, against AGENTS.md, domain/ADR guidance, documented Python style and ownership rules, and the combined design guidance. No documented standard breaches or actionable Fowler smell findings emerged.
>
> Input parsing, normalization, dependency validation, and executable eligibility remain cohesive within inputs.py; lifecycle execution stays in runner.py. The changes preserve approved-input ownership and avoid unnecessary abstractions.
>
> This was a read-only review. I did not rerun the previously reported passing checks.

Earlier independent fresh Standards reviewers `/root/review_standards` at `855a4c8` and `/root/review_standards_final` at `dfdb1a6` also reported no findings.

Standards sources were supplied explicitly: `AGENTS.md`, domain instructions/glossary/ADR-0001, `docs/harness-design.md`, Python-environment guidance, `pyproject.toml`, current input documentation, tracker/readiness conventions, the combined Matt Pocock/Microsoft design references, and the full Fowler smell baseline. No repo `CODING_STANDARDS.md` or `CONTRIBUTING.md` was found. Fixture standards were scoped to the fixture; tool-enforced checks were kept separate.

## Spec

Final separate independent fresh reviewer `/root/review_spec_verified`, reviewing the same complete original-baseline diff at `b11fd20`:

> No Spec findings, blocking or optional.
>
> Reviewed the entire baseline-to-HEAD diff against ticket 02, the scoped spec sections, authoring conventions, glossary, and ADR-0001. Normalization, contradictory-input rejection, prerequisite eligibility, check selection, and executable validation satisfy the scoped requirements. The executable-resolution repairs address the previously identified caller/worktree differences.
>
> Invalid CLI bundles are tested for actionable diagnostics, zero assignments and gates, attempt 0, unchanged Git references, and no added worktrees. Valid bundles exercise normalized records and prerequisite completion evidence.
>
> Independent verification: 73 tests passed using the reusable Python environment. No files changed.

Review history and resolution:

- `/root/review_spec` at `855a4c8` reported one blocking finding: an untracked relative executable in the caller checkout passed preflight, allowing implementation before a lightweight-check failure. Fixed in `dfdb1a6` with base-tree availability/mode checks and public CLI regressions.
- `/root/review_spec_final` at `dfdb1a6` independently confirmed that repair but reported one remaining blocking finding with two reproductions: relative PATH search and a normalized path such as `./missing/../local-check` could validate a different path from runtime. Fixed in `b11fd20` through explicit documented rejection, with red/green CLI regressions also covering `/` and `/.` suffixes.
- The final fresh reviewer assessed both repairs and the entire original-baseline implementation, with no residual findings. No runtime code changed after that review.

Spec reviewers received ticket 02 and its exact scoped spec requirements explicitly. Every review used a fresh focused context and stayed below the 250K active-context target. No fixture agent report counted as an implementation review.

Standards: 0 findings, no worst issue. Spec: 2 blocking findings across earlier rounds, both fixed; final review 0 findings, no residual worst issue. No optional suggestions or unresolved items. All five acceptance criteria are verified; no unchecked criteria remain. No push was performed.
