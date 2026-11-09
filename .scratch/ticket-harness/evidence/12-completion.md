# Ticket 12 completion evidence

Implemented only [12: Execute only the first eligible milestone](../issues/12-execute-only-the-current-qa-milestone.md).
Verified implementation: `14cafef40726eba80d8648d98d9c263fde3a5d0b`.
Original fixed review baseline: `2e15004338b45d61719656de113c2cbfdea56345`.

## Scope, prerequisites and source identity

A fresh GPT-6.1 Sol Medium worker implemented the runtime plan validator, input capture, current-group scheduling and preparation-pending state, CLI coverage and public documentation. The implementation contains six files: `ticket_harness/inputs.py`, `ticket_harness/plans.py`, `ticket_harness/runner.py`, `tests/test_dependencies.py`, `tests/test_milestones.py`, and [public contracts](../../../docs/ticket-harness.md). The optional plan contract preserves legacy plan-free execution. Role settings are validated and captured; live model enforcement and skill delivery remain deferred.

[Prerequisite audit](12-prerequisite-audit.json) retains the actual helper/command/exit and verified historical identities: 09 implementation `7f4eac0` and bookkeeping `a45dac0`; 10 `70a0122` and `fe036e3`; 11 `552fcd6` and `bb982c0`, all ancestors of the original baseline. Each prerequisite has six checked criteria, completion evidence, actual check records and separate reviews. Raw observation hashes match their original implementation commits. Ticket 10's initial pre-numbering generation and subsequent final-source conformance audits remain distinct. These records establish prerequisites, not verification of ticket 12; ticket 09's historical 469 tests are not reused as a new result.

No active run using these feature inputs was identified: the checkout had only its main worktree and no run records outside historical evidence. Runtime fixtures used their own temporary repositories and synthetic approvals. The unrelated unstaged `docs/agents/issue-tracker.md` edit remains byte-identical, SHA256 `3803de99e541e60d2e9f733d5c98b009a43e60a9584e3819adffc55eae0214ce`, and is excluded from all commits.

[Final source/test identity](12-final-source-identity.json) and [consolidated observations](12-fixture-observations.json) retain all 20 relevant file hashes and the actual uncommitted test tree. Root and both reviewers independently matched every hash to committed `14cafef` and working bytes. No implementation change followed the final checks or independent reviews. The checkpoint preceded review; both fresh High reviewers assessed the entire six-file diff against the original baseline.

## Criterion-specific evidence

The [coverage map](12-coverage-map.md) was recorded before new tests. Existing dependency, repair, exact-candidate, protection and CLI/status coverage is reused. Thirty new public CLI cases target distinct milestone risks without duplicating those matrices. [78 retained final-suite scenarios](12-fixture-observations.json) include complete CLI observations, run records, assignment contents, gate output, actual branch tips and Git history. Temporary fixture paths were valid during execution and cleaned afterward; the observations preserve their contents and outcomes.

| Criterion | Verified evidence |
| --- | --- |
| Approved version, fixed membership, final coverage, dependencies, QA and worker settings | Two-group and single-final-group tests assert captured normalized version/approval, ordered membership, final cumulative coverage, actionable QA fields, independent Medium/High/High defaults and a worker override/context target. The plan JSON is included in immutable snapshots and delivered assignments. Overrides affect effective worker/repair settings without changing reviewer profiles; capture is not backend enforcement. |
| Reject invalid plans before processes or Git changes | Twenty-two invalid-plan cases, three duplicate-metadata cases and a transitive-context dependency case reject missing/duplicate membership, missing final coverage, later-group edges, conflicting version/milestone/reasoning, invalid roles/QA/selection and other malformed metadata. The 26 retained new preflight rejections have zero gates/launches and unchanged refs, with no worktree mutation. Existing bundle graph/readiness/check validation remains covered. |
| Existing ticket gates, latest verified feature revision, current group only | The two-group fixture executes M1's fixed preferred order 03 then 01. Each implementation starts at the preceding verified feature tip. Its lightweight gate and separate Spec/Standards gates identify the exact submission; its broader candidate gate identifies the exact Done candidate, whose parents are the previous feature tip and reviewed submission. One shared baseline plus ten ticket gates pass. M2 tickets 02/04 remain Pending, attempt zero, with no launches or delivered files. |
| Persist preparation-pending without later work, QA readiness or feature completion | Both successful planned scenarios persist `outcome: preparation_pending`, the milestone's exact feature revision, and `feature_complete: false`. No milestone candidate or QA request is invented; dev is unchanged. A single final group still waits. Failed current-candidate checks retain incomplete/Blocked and do not claim preparation-pending or start later work. Status returns the durable run record without execution. |
| Public CLI, scripted processes, real Git and preservation | The two-group test preserves staged, unstaged and untracked caller work and caller HEAD, exact plan source/snapshot bytes and hash, actual dev/feature revisions, cumulative delivered trees, merge parents and run/status equality. The mutation case restores the approved snapshot and stops immediately with retained tamper evidence; caller-owned changed source stays inspectable under the existing protection contract. All fixtures use isolated writable real repositories and external scripted processes. |

For the saved two-group execution, M1's feature revision is `6d00a1055a0837f8fda76bc154ad03d4fcd463a3`; dev remains at `ad523fdfdbf39116ad119dac5a06dbe362cecb01`. These are fixture identities, not this development repository's QA candidate or human acceptance.

## Actual checks and provenance

All Python used the documented reusable environment. [Commands/output](12-checks.log), [command exits/timings](12-check-results.json) and source identities were retained during checks. The reusable environment lacked mypy/Ruff; a default-network pip attempt failed DNS, then scoped escalated installation of pinned mypy 1.19.1 and Ruff 0.14.10 into `/tmp/ticket12-tools` succeeded. Command-local `PYTHONPATH` supplies those tools; the shared environment was unchanged.

| Actual command | Result |
| --- | --- |
| Reusable Python `-m pytest -q --durations=20` | Exit 0: **499 passed in 400.57s**, final source/test tree, with retained observations. |
| Reusable Python `-m mypy`, `PYTHONPATH=/tmp/ticket12-tools` | Exit 0: strict mode, eight source files. |
| Reusable Python `-m ruff check ticket_harness tests examples`, same tool path | Exit 0. |
| Reusable Python `-m ruff format --check ticket_harness tests examples`, same tool path | Exit 0: 20 files formatted. |
| `git diff --check`; original-baseline committed diff whitespace check | Exit 0. |

Packaging and entry points did not change, so installed packaging checks were not required under [testing policy](../../../docs/agents/testing.md). Existing packaging behavior is not claimed as newly tested.

Development red/green logs document missing plan support, malformed-plan validation and the transitive-edge regression. An integrity test initially expected caller-source restoration contrary to the established contract; its assertion was corrected to require snapshot restoration and retained source/tamper evidence. A prematurely started full run was interrupted with pytest exit 2 after 106.069 seconds. Its `*-interrupted` logs/identities are retained separately and never count as completion evidence. The renewed 499-test run above verifies the final tree. Raw iteration and interrupted observation directories remain archived under `/tmp/ticket12-checks/archived-observations/`; final observations are consolidated without replay or relabeling. Five historical display logs had trailing whitespace normalized for Git; [original log strings](12-log-originals.json) preserve their exact contents. The final check log required no normalization.

## Separate independent reviews

[Spec](12-review-spec.md): fresh `/root/review_spec_12`, GPT-6.1 Sol High, original baseline and `14cafef`. **0 blockers; 0 optional suggestions.** Independently verified all 20 hashes, all 78 consolidated observations against raw final artifacts, 26 preflight rejections and the two-group revision/gate/assignment/status chain. A public CLI sample passed **4 tests**, 26 deselected, in 5.34s; committed diff whitespace passed.

[Standards](12-review-standards.md): separate fresh `/root/review_standards_12`, GPT-6.1 Sol High, same original baseline and revision. **0 blockers; 0 optional findings.** Independently reran all **30 milestone tests**, passing in 7.90s; verified 20 hashes and 78 distinct final scenarios; assessed cohesive ownership, fixture isolation, coverage value and combined design policy.

Neither reviewer read the other's report or changed implementation. Both inspected required full-suite/static evidence without claiming to have independently repeated that full matrix. No repair assignment was required. Scripted runtime fixture reviewers remain distinct from these implementation reviews.

## Completion and next handoff

All five criteria and required gates are verified at `14cafef`. Ticket header, checked markers, completion comment and feature index agree; previous readiness is `ready-for-agent`, and `Blocked by:` remains dependency history. No unchecked criterion, unresolved blocker or optional suggestion remains. This evidence and ticket/index updates receive a separate bookkeeping commit; its identity is available from this file's Git history. The generated handoff receives a third separate commit. No push occurred.

Ticket 13 is the next prerequisite-ready M1 assignment. Do not launch it during handoff generation. Tickets 14–15 remain subsequent M1 work; at the boundary generate QA/waiting status and hold M2 for recorded human acceptance. E1 ticket 25 retains its separate priority immediately after verified 24 and does not gate release acceptance. Ticket 12 completion neither accepts M1 nor completes the feature. Candidate preparation/testing, QA decisions/promotion, planned continuation, QA corrections, background operation, independent work after blocks, live Codex and role skill capture remain later authorized slices.
