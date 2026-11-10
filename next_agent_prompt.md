Use $implement-with-checkboxes to implement only:
`.scratch/ticket-harness/issues/21-own-ticket-execution-and-bounded-repairs.md`

**21: Own ticket execution and bounded repairs**

Work in `/home/ajkerr1/development/agentic_template`. Read the actual
[ticket](.scratch/ticket-harness/issues/21-own-ticket-execution-and-bounded-repairs.md)
and [implementation workflow](.agents/skills/custom/implement-with-checkboxes/SKILL.md).
This handoff starts no assignment, harness run, QA session or acceptance.

## Starting state and eligibility

Follow [AGENTS.md](AGENTS.md), [domain guidance](docs/agents/domain.md),
[GLOSSARY.md](GLOSSARY.md), relevant [ADRs](docs/adr/),
[tracker conventions](docs/agents/issue-tracker.md) and
[readiness guidance](docs/agents/triage-labels.md). Capture your own starting HEAD
as the fixed whole-ticket review baseline; historical baselines do not replace it.
Inspect/preserve the actual worktree and unrelated changes.

Approved **oop-v2 / review-process-1** is recorded in the
[approval](.scratch/ticket-harness/approval.md),
[index](.scratch/ticket-harness/README.md),
[proposal](.scratch/ticket-harness/ticket-proposal.md) and
[milestones](.scratch/ticket-harness/milestones.md). M1 (10–24) is the earliest
required milestone without human acceptance. Tickets 10–20 are completed; 21 is
open, unclaimed, agent-ready and next in preferred prerequisite-ready order.
Verify prerequisite 20 from its actual seven criteria, checks, reviews and ancestors:

- Implementation `0aa2660505e4233ca2e321cee439ba51b150e055`;
  bookkeeping `0f5652d6d1a41e8ff2376eb649d8b6e19b081759`.
- [Completion](.scratch/ticket-harness/evidence/20-completion.md),
  [criterion evidence](.scratch/ticket-harness/evidence/20-criterion-evidence.md),
  [assessment](.scratch/ticket-harness/reviews/ticket-20.md),
  [Spec original](.scratch/ticket-harness/evidence/20-review-spec-01.md),
  [Standards original](.scratch/ticket-harness/evidence/20-review-standards-01.md),
  [immutable capture](.scratch/ticket-harness/evidence/20-review-round1-capture.json).
- [Final checks](.scratch/ticket-harness/evidence/20-final-check-results.json):
  544 passed in 703.66s, strict mypy, Ruff lint/format and whitespace all passed
  on working bytes independently matched to the implementation Git blobs.
  No tests changed. Spec independently reproduced 18 scoped cases; Standards
  inspected source and retained artifacts without another full-suite run.

Historical checks prove their recorded source, not ticket 21. Preserve original
reports, append-only histories, completed requirements, archives and frozen QA
inputs. If an intended authoring file belongs to an active run, report the exact
mutation blocker. M1 still needs 21–24, actual cumulative assessment and explicit
human QA; later milestones stay gated. No promotion or push is authorized.

## Roles, evaluated guidance and checkpoints

Use fresh **GPT-6.1 Sol** assignments: **Medium implementation and repairs**, no
worker override, independently configured **High Spec** and **High Standards**.
Target <=250000 active-context tokens per assignment; report unavailable settings
and telemetry. Configuration does not prove delivery or runtime enforcement.
Worker/repair/Standards add [OOP](.agents/skills/microsoft/microsoft_oop/SKILL.md),
[codebase design](.agents/skills/matt-pocock/codebase-design/SKILL.md) and
[test strategy](.agents/skills/custom/test-strategy/SKILL.md). Spec uses agreed
behavior/coverage contracts. Use writing-for-agents/skill-creator for applicable
authoring; preserve upstream skills unchanged.

Apply [ownership/scope](docs/agents/ownership-review.md),
[review records/templates](docs/agents/review-records.md),
[architecture checkpoints](docs/agents/architecture-checkpoints.md) and the
[review index](.scratch/ticket-harness/reviews/README.md). Record entry callers,
owners, every writer/consumer, save/restore and invalidation, with changed and
unchanged responsibility reasoning. Missing consequential decisions remain human-owned.

Use [evaluated guidance](docs/agents/reviewer-evaluation.md): substantive **G2**,
final **C5** [declaration](.scratch/ticket-harness/evidence/19-evaluation-g5/declaration.md),
[manifest](.scratch/ticket-harness/evidence/19-evaluation-g5/source-manifest.json),
[original reports/index](.scratch/ticket-harness/evidence/19-evaluation-g5/README.md)
and [results](.scratch/ticket-harness/evidence/19-evaluation-g5/results.md).
C5 aggregate is `332ddabe972f596d86cd09eda809bd2f93d1f57602f01d75ed9f39f2b182510d`.
Five evolving eight-case corpora/two guidance versions preserve failed trials,
misses, invalid controls and differing judgments. One independent final observation
per axis is finite evidence, not a detection/reliability/runtime guarantee.
Assess actual ticket-21 source; corpus outcomes are no answer pattern. The
[evaluate-reviewers skill](.agents/skills/custom/evaluate-reviewers/SKILL.md) is for
future calibration authoring, not an extra ordinary-ticket gate.

Ticket 20's four start/final triggers were **No**, independently confirmed:
existing lifecycle, persistence paths and shared records stayed; writers migrated
to the approved owner. Reassess **each trigger at ticket 21 start and after changes**:
new lifecycle, persistence/restoration path, shared mutable state, additional writer.
A positive trigger requires a fresh broader affected-workflow assessment before
integration; negative triggers require no unconditional third reviewer. Ordinary
Spec/Standards remain independent. No unresolved actual finding, missing required
20 report, pending relevant revalidation or human decision remains; see
[20 history](.scratch/ticket-harness/evidence/20-finding-history.md). Ticket 19's
prior fixed keys and historical fixture findings retain their own source scopes.

Real **M1 cumulative assessment remains unperformed**, QA not requested/accepted.
Before eventual readiness establish actual feature-start provenance (distinct from
your ticket baseline), exact source and substantive inspection of **all
`ticket_harness` Python files**. Missing/stale required work holds readiness.
Assessment completion, findings dispositioned, candidate ready and human milestone
acceptance remain separate observations.

## Bounded implementation and compatibility

The ticket's seven original criteria control. Read scoped spec:
[state/decision ownership](.scratch/ticket-harness/spec.md#state-and-decision-ownership),
[refactor verification](.scratch/ticket-harness/spec.md#oop-refactor-verification),
[ticket lifecycle](.scratch/ticket-harness/spec.md#ticket-lifecycle),
[exact revisions](.scratch/ticket-harness/spec.md#independent-checks-and-exact-revisions),
[QA/promotion](.scratch/ticket-harness/spec.md#feature-to-development-promotion-and-human-qa)
and [safe continuation](.scratch/ticket-harness/spec.md#corrections-and-safe-continuation).

Give one ticket execution ownership of the complete cycle and bounded repair
policy through a small interface. Keep its original approved base, current attempt,
repair starting revision, previous source and failure context together. The runner
coordinates eligible tickets and retains checking; ticket workflow must no longer
obtain unrestricted runner access to manipulate shared state. Use the existing
attempt operations and complete caller migration. Inspect actual definitions and
usages; private class/method/file choices remain implementation decisions.

Current entry is `tickets.execute`, called by `_Run` workflow. Ticket 20's attempt
owner now coordinates lifecycle observations and current-ticket projection;
`_Run.check` receives the identified owner for validated decisions. `agents.report`
returns observations without canonical gate mutation. Preserve that ownership,
runner check execution/validation/invalidation and failure precedence. See the
[affected-flow inventory](.scratch/ticket-harness/evidence/20-implementation-report.md).
Avoid getter/setter-only facades, callback bags, unrestricted runner coupling and
inheritance frameworks.

Preserve the fixed original ticket base across attempts, while repairs use the
observed rejected submission or preserved uncommitted work. Fresh worktrees and
assignments receive correct failure/rejected revisions, ticket-scoped evidence and
configured checks. Initial plus configured repairs stays bounded. Maintain
repair-or-stop distinctions for gate/Git/process/timeout failures, exhaustion,
human decisions, environment/integrity and external ref/HEAD movement.

Changed submissions repeat applicable checks, both reviews and exact candidate
suite. Only successful expected-old integration advancement records the tested
candidate Done and unlocks dependents. Later tickets use current verified integration;
existing fail-fast behavior after a blocked ticket stays until ticket 29. Preserve
CLI/exit behavior, artifact naming, baseline reuse, attempt numbering, half-open
gate ranges, record/checkpoint schemas, history, protected inputs and caller work,
and meaningful atomic observations. Readiness calculations and Git primitives
remain functions where they have no independent state lifetime. Do not implement
22–24, blocked-work isolation 29, runtime 33/34, orchestration or QA acceptance.

## Verification, reviews and completion

Apply [efficient ticket development](docs/agents/development-efficiency.md) before
review/repair dispatch: finish local diagnosis/checks and retain one canonical
packet, collect both originals before a fresh repair, investigate repeated causes
before another dispatch. Ticket 20 used one implementation and one clean pair;
no outstanding repair or repeated-failure diagnosis carries into this ticket.

Read [Python environment](docs/agents/python-environment.md) before Python,
dependencies or checks; use the absolute reusable prefix. Apply
[testing policy](docs/agents/testing.md), test-strategy and
[documented checks](docs/ticket-harness.md#python-and-checks). Map criteria first to
existing public CLI/scripted-process/isolated-Git cases in test_repairs,
test_dependencies, test_transaction and test_timeouts, with affected decision/report
coverage as needed. Add cases only for distinct uncovered failures using TDD at
that approved seam; no private-class tests or manufactured failures for covered
behavior. Use focused development checks. Full pytest, strict mypy, Ruff lint/format
and whitespace remain required at the final implementation checkpoint; repeat only
when relevant changes/failures/uncertainty invalidate evidence. Packaging follows
actual impact. Bookkeeping alone receives document/link/source-consistency checks.

Arrange capture before required execution: retain command/exit/source/test hashes,
logs and necessary CLI/Git/record/ref evidence from that same run. Establish a
genuine pre-refactor deliberate checkpoint with producer/source provenance before
runtime edits, retain the real fixture through cleanup and continue it under final
source. [Ticket 15 prior art](.scratch/ticket-harness/evidence/15-completion.md) and
[20 preservation history](.scratch/ticket-harness/evidence/20-checkpoint/preservation-history.md)
show capture needs. Ticket 20's original pre-edit fixture was lost; its successful
continuation used a later producer executing exact baseline source, with both
original loss and timing limit retained. Do not relabel that history or fabricate a
post-refactor-produced checkpoint as compatibility proof for 21.

After final checks, commit implementation before fresh High Spec/Standards
whole-ticket review from your own original baseline. Supply ownership/coverage,
unchanged flows, exact source/check evidence, full prior keys/history and omitted
scope. Preserve originals before aggregation. Blocking findings use fresh Medium
repairs, renewed applicable final gates/commit and fresh whole-ticket axes;
optional suggestions remain optional. Human scope/risk/QA authority stays human-owned.

Only after every criterion/gate passes, reconcile unchanged criterion wording,
set Status completed, retain prior readiness in the completion comment and preserve
Blocked by. Link criterion/check/review evidence from the feature index; commit
bookkeeping separately. Then automatically use create-next-agent-prompt, verify
eligibility again and commit only the generated handoff separately. Never begin
another ticket as part of handoff creation. Return implementation/bookkeeping/handoff
commits, actual checks, separate review outcomes, criterion evidence, unchecked
items, unresolved full finding keys and next prompt path/selection or exact blocker.
