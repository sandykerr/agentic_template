# Review report envelope: review-ticket-21 / spec-01

| Field | Value |
| --- | --- |
| Assessment | `review-ticket-21`, [ticket 21](../issues/21-own-ticket-execution-and-bounded-repairs.md), approved oop-v2 / review-process-1, M1 |
| Report identity | `spec-01`, Spec axis, first independent whole-ticket review; fresh assignment/actor `/root/spec21` |
| Actual settings | Requested fresh GPT-6.1 Sol, High, advisory active-context target <=250000. Backend delivery/enforcement, enforced context cap and measured active-context telemetry are unavailable. Configuration is not proof of delivery. |
| Original baseline | `8574c6e5fb0a55ea3539e52c7c53044f1c036583` |
| Assessed source | `10b7050ec1fc06767e473b90217fa0d0bd100a0f` |
| Supplied instructions | [round-one identity manifest](21-review-round1-instructions.json), [common contract](21-review-common.md), [Spec instructions](21-review-spec-instructions.md), [canonical packet](21-review-packet.md). The manifest identifies 34 applicable instruction/packet files; independent audit matched their current bytes to every listed SHA-256. Source-committed guidance is read at the assigned source; retained authoring instructions are explicitly identified by the manifest. No backend delivery attestation is available. |
| Guidance identity | G2 substantive ownership/report guidance via [reviewer-evaluation](../../../docs/agents/reviewer-evaluation.md); final C5 aggregate `332ddabe972f596d86cd09eda809bd2f93d1f57602f01d75ed9f39f2b182510d`. Five evolving eight-case corpora, two guidance versions and one original per axis per corpus are finite calibration history, including failed trials and differing judgments; no reliability/runtime guarantee or answer pattern transfers here. Spec axis of [code-review](../../../.agents/skills/matt-pocock/code-review/SKILL.md), with repository whole-ticket/envelope requirements taking precedence. |
| Original output/evidence | This original report; independent [audit program](21-review-spec-01-audit.py) and [audit result](21-review-spec-01-audit.json). Root captures report digests outside this file and owns subsequent aggregation/dispositions. |
| Inspected scope | Whole runtime diff; complete `tickets.py` and `runner.py`; unchanged `git.py`, `agents.py`, `records.py`, CLI entry; input normalization/load/approved-input checks; QA checkpoint persist/restore, verified-reference handoff, milestone entry/promotion consumers. Relevant public repair/dependency/transaction/timeout/continuation scenarios, required-check logs, source manifests, capture/checkpoint scripts, seven representative archived observations, full archive identity audit and prior finding histories. |
| Omitted scope | No independent complete-package/M1 cumulative architecture assessment; no redesign of input preparation, run restoration or milestone review for tickets 22–24; no blocked-work scheduling 29, runtime enforcement/backend work 33/34, live-model exercise, packaging or orchestration. These are outside ticket 21. Unchanged preflight/parser/plan-validation internals were followed only as needed to establish inputs to this cycle. No exhaustive adversarial/platform matrix, whole-suite replay or new tests. |
| Prior observations | No unresolved actual inherited finding key or pending relevant revalidation. [Ticket 20 history](20-finding-history.md) records two clean originals at its own source. [Ticket 19 history](19-finding-history.md) preserves its fixed findings and exact revalidation; historical corpus failures retain their fixture scopes. No current-round sibling report was inspected and judgments were not coordinated. |

## Substantive assessment

The seven ticket criteria are satisfied by the inspected implementation and supporting observations, subject to the remaining independent-axis/record aggregation work owned by root. I found no missing or partial ticket behavior, unjustified behavior expansion, or implementation that defeats an approved outcome.

### Complete ownership and the caller boundary — criterion 1

[`_TicketExecution`](../../../ticket_harness/tickets.py#L148) owns the original base, active attempt, repair start, previous source and repair context for one ticket. Its `execute()` operation contains the entire ordered implementation/check/review/candidate/promotion/rejection loop and its allowance/stop decisions. The caller supplies the current verified integration revision once, then consumes only a successfully promoted revision. It does not coordinate repair-state field edits between calls.

[`_TicketVerification`](../../../ticket_harness/runner.py#L255) provides runner-owned checking, protected Git-operation naming/destinations, durable observations and source validation. Ticket code receives no `_Run` instance, run dictionary or verified registry. The adapter's private runner reference and fixed ticket identity support these concrete operations; it is not a bag of callbacks or a facade exposing arbitrary setters. `observe()` combines the stage observation with runner persistence, while `check()` retains substantial report/process/invalidation policy in `_Run.check`. Ticket workflow retains cycle policy. A repair-policy change belongs in the ticket owner; a report/timeout-precedence change belongs in runner checking. This division meets the scoped ownership contract without needing a private-class test or additional abstraction.

The unchanged `_Attempt` remains the lifecycle writer. The new owner constructs the attempt with canonical history/current-ticket/gate references and calls its source, submit, candidate, reject, human-decision and completion operations. Runner checking receives that identified owner directly; it does not select a positional last attempt. Ticket readiness initialization/unlock remain functions, and runner final failure classification still owns terminal Blocked/outcome observations.

### Fixed base, repaired work, fresh scope — criterion 2

`_base` is assigned once in construction and remains fixed across the loop. `_start_revision` begins at that base and is updated only from the rejected attempt's `repair_start()`. If a submission exists, repair starts from its observed submitted commit; otherwise it starts at the prior assignment revision and carries preserved working contents into a fresh detached worktree. `carry_changes()` excludes `.git` and leaves the rejected tree intact. Before another assignment, the preserved source HEAD must still equal the observed repair start.

The assignment distinguishes `base_revision` from `revision`; subsequent capture computes changed files against the original ticket base. The snapshot mapping is shallow-copied only to reorder the active ticket key. Entries are read, not rewritten, and runner protection uses the original canonical snapshots. Input loading establishes resolved, unique ticket paths and a corresponding normalized requirement, so active-ticket lookup is supported by actual validation rather than an assumed arbitrary dictionary shape.

Gate context is filtered to this ticket and the shared baseline. Rejected revisions are selected by ticket identity from all its attempts, including candidate revisions. Named checks are selected from that ticket's normalized requirements. Artifact/worktree naming remains runner-owned and incorporates ticket/attempt identity, so repairs and later tickets receive fresh processes/worktrees while earlier evidence remains inspectable.

### Bounded repairs and stop precedence — criterion 3

The loop permits exactly one initial attempt plus `max_repairs`; configuration enforces a nonnegative integer and retains the default two. Every rejection uses `_Attempt.reject` before recording observations. Ordinary gate/Git/report/process/timeout failures share that same allowance. There is no separate retry loop.

The unchanged runner checker handles complete validated human decisions, nonzero exits, timeouts, integrity damage and execution-environment failure before returning. Human decisions attach to the identified attempt and stop through `NonRepairableFailure`; timeout output is not trusted as a validated decision. Integrity/environment failures also stop without another repair. Source validation failures in shared baseline/earlier-ticket evidence remain terminal because they survive retirement of only the rejected ticket's verified entries. The repair path checks approved inputs first, retires current-ticket approvals, validates remaining references, compares integration to the fixed base, and checks rejected HEAD before creating another assignment. An integration-stage failure is terminal, preserving external movement. The local `stage` is copied back on rejection, preserving failure-stage reporting even when review/candidate worktree setup fails before a check executes.

### Renewed verification and protection — criterion 4

Every repair reenters capture, applicable named checks, fresh Spec and Standards worktrees/reports, candidate construction and exact candidate suite. Rejected gate dictionaries remain durable history, but `_Run.reject_checks` removes their ability to authorize a new source. `_Run.check` appends canonical gates and stores the same objects in `verified`; validation marks those dictionaries invalidated on source changes. Ticket code only reads the gate/history references supplied to it, apart from lifecycle writes delegated to `_Attempt`.

`require_reviewed_candidate` binds parents and tree to the original ticket base and exact reviewed submission, then requires clean source. The candidate suite must leave that exact revision unchanged. Approved originals/snapshots, harness records, assignments, earlier outputs and approved paths inside worktrees remain bracketed by the existing process/Git integrity protection. `capture` rejects worker-owned HEAD changes; approved-source path changes are checked against the cumulative ticket diff. The caller repository's HEAD/index/work files are not used as an implementation worktree. Existing trusted-process/boundary-observation limits remain documented; this refactor does not claim an operating-system sandbox.

### Expected-old integration and fail-fast dependencies — criterion 5

At [`tickets.py:280`](../../../ticket_harness/tickets.py#L280), approved inputs and all still-applicable sources are validated before hook-disabled expected-old `promote`. `_Attempt.complete` runs only after that atomic Git ref update succeeds. The ticket owner then returns the tested revision; [`runner.py:423`](../../../ticket_harness/runner.py#L423) immediately records it, unlocks dependents and atomically saves the full observation. No external command or save splits Done from the matching integration-revision/unlock observation. This preserves the existing observation contract, without claiming crash recovery between Git and durable JSON.

Each later ticket receives `record['integration_revision']` from that successful path. Failed expected-old advancement records neither Done nor a new integration revision. The outer catch preserves earlier Done work, marks the affected ticket Blocked and terminates the loop. Dependents stay Pending and independent Ready work is not launched: the ticket's explicit existing fail-fast requirement governs this slice despite the broader future blocked-work-isolation goal.

### Public compatibility and continuation — criterion 6

`_Attempt`, readiness functions, Git primitives and public record schemas are unchanged. Gate ranges still index the run-wide list; numbering resets per ticket and evidence names remain under `_Run.artifact_name`. The adapter maps `candidate-merge` to the existing candidate directory and strips `-worktree` for implementation/review destinations, preserving single-/multi-ticket names. Baseline checks are established once and retained unless invalidated.

There is no durable `_TicketExecution` or `_TicketVerification` representation. QA persistence still exports the existing version-1 JSON. On continuation, `_Run.restore_checks` reconnects verified entries to canonical restored gate dictionaries; a later ticket constructs a new execution from the current verified integration revision. The previously completed ticket's owner need not be reconstructed. The retained genuine checkpoint was produced before edits on the exact baseline, with both explicit fixture cleanup and automatic finalization suppressed; stopped and continued live Git fixtures were archived. Final-source continuation preserved two prior attempts and twelve gates exactly, retained one baseline, completed the remaining milestone, and recorded two synthetic fixture approvals. This verifies compatibility for the observed deliberate checkpoint; it does not accept the real development M1 or promise arbitrary interrupted-stage recovery.

### Evaluated review process and triggers — criterion 7

The canonical packet preserves baseline/source/check identity, criteria-to-existing-coverage mapping, ownership rationale, prior histories, omissions and independent review requirements. This original is saved before aggregation. Root remains responsible for the second axis, immutable capture/index links, any dispositions, and completion/handoff bookkeeping; their proper pending status is not a source defect or a fabricated completed review.

I independently agree with all four negative start/final trigger assessments: the existing ticket/attempt lifecycle gains its approved owner; no new lifecycle is introduced. No object adds a persisted/restored representation or restore route. Supplied lists/dictionaries/sets retain their canonical identity and existing writers. The adapter holds an existing runner reference and migrates scoped effects from the former ticket function; it does not add an independently shared state owner or another writer competing with an existing one. Moving successful integration-revision/unlock bookkeeping back to the runner removes the ticket function's broad record access. Thus no additional triggered cumulative assignment is required for ticket integration. The actual M1 feature-start provenance and all-package cumulative assessment remain unperformed and required before QA readiness.

## Evidence audit

I resolved both full revisions and inspected:

```text
git rev-parse 8574c6e5fb0a55ea3539e52c7c53044f1c036583 10b7050ec1fc06767e473b90217fa0d0bd100a0f
git diff --stat 8574c6e5fb0a55ea3539e52c7c53044f1c036583...10b7050ec1fc06767e473b90217fa0d0bd100a0f
git log 8574c6e5fb0a55ea3539e52c7c53044f1c036583..10b7050ec1fc06767e473b90217fa0d0bd100a0f --oneline
git diff 8574c6e5fb0a55ea3539e52c7c53044f1c036583...10b7050ec1fc06767e473b90217fa0d0bd100a0f -- ticket_harness/runner.py ticket_harness/tickets.py
```

All exited 0. The whole-ticket diff is nonempty: 42 files, predominantly retained evidence; its only runtime changes are `runner.py` and `tickets.py`. The log contains `10b7050 Own ticket execution and bounded repairs`. Tests and packaging configuration are unchanged.

Independent audit command, exit 0:

```text
PYTHONDONTWRITEBYTECODE=1 /home/ajkerr1/development/agentic_template/.micromamba/envs/dev/bin/python .scratch/ticket-harness/evidence/21-review-spec-01-audit.py > .scratch/ticket-harness/evidence/21-review-spec-01-audit.json
```

The retained program defines the exact audit: all 26 final runtime/test/example/config files match both assessed commit blobs and working bytes; 34 supplied instruction/packet hashes match; all 22 checkpoint-producer runtime/test hashes match original-baseline Git blobs. One streaming pass matches all 10,445 archived raw files to the manifest and identifies 544 scenario observations. Producer/continuation records independently preserve prior attempts/gates and show completed continuation. These are identity/record-consistency observations, separate from the source reasoning above.

I also inspected original archived observations for successful failed-check repair (`41y9thqr`), uncommitted preservation (`magi3a1r`), multi-ticket fixed-base repairs (`zycy7uwa`), third-attempt renewed verification after invalidation (`y5smhsqq`), external movement after rejection (`0cq9m0ed`), later candidate movement (`sjj0iaom`) and human-decision fail-fast (`e2q46xb1`). Paths are the corresponding `ticket21-final-raw/ticket-harness-test-ID/observations.json` members in [the original archive](21-final-raw.tar.gz). Their recorded public run/status exits, attempt failures, current/historical integration refs and clean caller statuses agree with their existing test assertions. This inspection is sampled substantive evidence; the archive-wide hash audit does not claim all 544 records received separate semantic examination.

Focused independent reproduction used the existing public CLI/real Git cases, without added tests or a private seam:

```text
PYTHONDONTWRITEBYTECODE=1 /home/ajkerr1/development/agentic_template/.micromamba/envs/dev/bin/python -m pytest -q -p no:cacheprovider tests/test_repairs.py::test_invalid_worker_report_preserves_uncommitted_changes_for_fresh_repair tests/test_repairs.py::test_failed_git_operations_have_per_attempt_diagnostics tests/test_dependencies.py::test_repairs_keep_ticket_local_attempts_fixed_bases_and_all_earlier_evidence tests/test_dependencies.py::test_later_candidate_cannot_overwrite_external_integration_movement
```

Result: **4 passed in 20.77s**, exit 0. This specifically checks preserved uncommitted work, bounded per-attempt Git diagnostics, correct later-ticket bases/check scope/history and expected-old protection after earlier Done work. No production/test files were changed.

I reused the actual final implementation checks in [21-final-check-results.json](21-final-check-results.json), inspected original logs `21-final-check-0.log` through `21-final-check-5.log`, and matched their source manifest to this commit. The recorded environment uses the absolute reusable Python 3.12.16 interpreter with pytest 9.2.0 and the existing `/tmp/ticket20-tools` mypy 1.19.1/Ruff 0.14.10 overlay, plus the identified capture plugin. Exact retained commands/results are:

| Command (Python prefix is `/home/ajkerr1/development/agentic_template/.micromamba/envs/dev/bin/python`) | Recorded result |
| --- | --- |
| `python -m pytest -q --durations=20 -p capture21` | 544 passed in 775.37s; exit 0 |
| `python -m mypy` | No issues in 10 source files; exit 0 |
| `python -m ruff check ticket_harness tests examples` | All checks passed; exit 0 |
| `python -m ruff format --check ticket_harness tests examples` | 24 files already formatted; exit 0 |
| `git diff --check` | Exit 0 on final working implementation |
| `git diff --check 8574c6e5fb0a55ea3539e52c7c53044f1c036583 -- ticket_harness tests examples` | Exit 0 |

The manifest's pre-check HEAD is the baseline because source was checked before the implementation commit; matching content hashes establish the tested bytes, rather than relabeling the baseline as the tested final tree. I did not rerun the full suite/statics. The earlier missing-tool invocations and interrupted capture audit remain recorded in the implementation/audit history; they do not replace these successful checks or imply a test/runtime failure. The capture plugin wraps fixture CLI/cleanup to retain observations and copies original process artifacts without rewriting their bytes; no assertion replacement or private production-test seam was introduced.

## Findings

**Blocking findings: 0. Optional suggestions: 0.** No new finding key is created. No actual prior finding is reopened, disposed, waived or relabeled by this report.

## Assessment result

**Spec assessment completed; clean within the stated whole-ticket and collaborator scope at `10b7050ec1fc06767e473b90217fa0d0bd100a0f`.** There is no unresolved in-scope assumption or demonstrated counterexample requiring a repair/human decision. Accepted-input and alias reasoning is grounded in validated configuration and inspected writers, not a narrower unstated input domain.

This report does not aggregate the sibling axis, complete root-owned bookkeeping, establish universal architecture/runtime correctness, accept M1, authorize promotion/push, or replace the pending real cumulative architecture and human QA work.
