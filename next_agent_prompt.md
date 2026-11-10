Use $implement-with-checkboxes to implement only:
`.scratch/ticket-harness/issues/20-own-implementation-attempt-transitions.md`

**20: Own implementation-attempt transitions**

Work in `/home/ajkerr1/development/agentic_template`. Read the actual
[ticket](.scratch/ticket-harness/issues/20-own-implementation-attempt-transitions.md)
and [implementation workflow](.agents/skills/custom/implement-with-checkboxes/SKILL.md).
This handoff starts no assignment, harness run, QA session or acceptance.

## Starting state and eligibility

Follow [AGENTS.md](AGENTS.md), [domain guidance](docs/agents/domain.md),
[GLOSSARY.md](GLOSSARY.md), relevant [ADRs](docs/adr/),
[tracker conventions](docs/agents/issue-tracker.md) and
[readiness guidance](docs/agents/triage-labels.md). Capture your own starting HEAD
as the fixed whole-ticket review baseline; historical ticket baselines do not
replace it. Inspect/preserve the actual worktree and unrelated changes.

Approved **oop-v2 / review-process-1** is recorded in the
[approval](.scratch/ticket-harness/approval.md),
[index](.scratch/ticket-harness/README.md),
[proposal](.scratch/ticket-harness/ticket-proposal.md) and
[milestones](.scratch/ticket-harness/milestones.md). M1 (10–24) is the earliest
required milestone without human acceptance. Tickets 10–19 are completed; 20 is
open, unclaimed, agent-ready and next in preferred prerequisite-ready order.
M1 still requires 20–24, its actual cumulative assessment and explicit human QA;
later required milestones remain gated by acceptance.
Verify prerequisites 05,06,19 from their actual criteria/checks/reviews and ancestors:

- 05: [completion](.scratch/ticket-harness/evidence/05-completion.md), implementation
  `34a49b7090a77d689a67c4230cc8b5f12c9c9f35`, bookkeeping
  `2a454df53b60927757c7e69c6f6bbdc7949b2d74`.
- 06: [completion](.scratch/ticket-harness/evidence/06-completion.md), implementation
  `dc1018e07f03c967ed686707c4d7f5a9660a6332`, bookkeeping
  `4ed073dcd46a4497229985b8ae53f8bd10d7d7f2`.
- 19: [criterion evidence](.scratch/ticket-harness/evidence/19-completion.md),
  [assessment](.scratch/ticket-harness/reviews/ticket-19.md),
  [final checks](.scratch/ticket-harness/evidence/19-repair-c5-checks.log),
  [Spec](.scratch/ticket-harness/evidence/19-review-spec-03.md),
  [Standards](.scratch/ticket-harness/evidence/19-review-standards-03.md).
  Implementation `e90abb64ab95c5b15cdb0949b03c6a948365339b`, first repair
  `ce4e57d77be6dfd695f0ecb15284c5e9d5792b93`, final repair `8e2c82679a2314e31ebff69accab3743f55f996d`,
  bookkeeping `c63570666b21cb5cb8c6063c4f328c9273aaa15b`.

Historical checks prove their recorded source. Preserve completed requirements,
original reports, append-only histories, archives and frozen QA evidence. If an
intended authoring file is an active-run input, report that exact mutation blocker.
Do not start another ticket or M2; ticket completion and plan approval do not
accept M1, authorize promotion or permit a push.

## Roles, evaluated guidance and checkpoints

Use fresh **GPT-6.1 Sol** assignments: **Medium implementation and repairs**, no
worker override, independently configured **High Spec** and **High Standards**.
Target <=250000 active-context tokens per assignment; report unavailable settings
and telemetry. Configuration does not prove runtime enforcement/delivery.
Worker/repair/Standards add [OOP](.agents/skills/microsoft/microsoft_oop/SKILL.md),
[codebase design](.agents/skills/matt-pocock/codebase-design/SKILL.md) and
[test strategy](.agents/skills/custom/test-strategy/SKILL.md). Spec uses agreed
behavior/coverage contracts. Authors use writing-for-agents/skill-creator when
applicable; preserve upstream skills unchanged.

Use [evaluated guidance](docs/agents/reviewer-evaluation.md): exact substantive
**G2** with final **C5** [declaration](.scratch/ticket-harness/evidence/19-evaluation-g5/declaration.md),
[manifest](.scratch/ticket-harness/evidence/19-evaluation-g5/source-manifest.json),
[original reports/index](.scratch/ticket-harness/evidence/19-evaluation-g5/README.md)
and [per-case results](.scratch/ticket-harness/evidence/19-evaluation-g5/results.md).
C5 aggregate is `332ddabe972f596d86cd09eda809bd2f93d1f57602f01d75ed9f39f2b182510d`.
Five evolving eight-case corpora/two guidance versions retain every failed trial,
miss, invalid control and differing axis interpretation. The final corpus has one
independent observation per axis; it is no general detection/reliability/runtime
guarantee. New refactor reviews must assess actual source; corpus outcomes are
not an answer pattern or acceptance for ticket 20.

The new [evaluate-reviewers skill](.agents/skills/custom/evaluate-reviewers/SKILL.md)
supports future calibration authoring, with [reusable lessons](docs/agents/reviewer-evaluation.md#lessons-for-evaluation-authors).
It was authored separately from frozen G2/C5 reviewer inputs. Its bounded
preparation-only observation is not a new corpus trial or automatic per-ticket gate.
Use ordinary implementation Spec/Standards reviews for this refactor.

Apply [ownership/scope](docs/agents/ownership-review.md),
[review records/templates](docs/agents/review-records.md),
[architecture checkpoints](docs/agents/architecture-checkpoints.md) and
[review index](.scratch/ticket-harness/reviews/README.md). Shared ownership guidance
owns substantive inspection; records own identity/history/authority; checkpoints
own when broader work gates progression. Record entry callers, owners, every
writer/consumer, persistence/restoration and invalidation; explain migrated and
unchanged responsibilities. Missing consequential decisions remain human-owned.

Actual findings `review-ticket-19/spec-01/F1` and `review-ticket-19/spec-02/F1` are
independently fixed/revalidated at final ticket 19 source; preserve
[full history](.scratch/ticket-harness/evidence/19-finding-history.md). No unresolved
actual findings, missing required ticket 19 reports, pending relevant revalidation
or actual human decisions remain. Historical fixture findings stay scoped to their
original intentionally defective snapshots. Original raw EOF handling and failed
checks remain preserved; this supplies no exemption for new authored source.

Ticket 19 recorded all four actual-workflow triggers No; executable owners/schemas
were unchanged. Reassess **each trigger at ticket 20 start and after implementation**:
new lifecycle, persistence/restoration path, shared mutable state, additional
writer. A positive trigger requires broader affected-workflow assessment before
integration; no trigger needs no unconditional third reviewer. Both ordinary
ticket axes remain independent.

Real **M1 cumulative assessment remains unperformed**, QA not requested/accepted.
Before eventual readiness establish actual feature-start provenance (distinct
from your ticket baseline), exact source and substantive inspection of **all
ticket_harness Python files**. Missing/stale reports or source provenance holds
readiness. Assessment complete, findings dispositioned, candidate ready and
milestone accepted remain separate; exact-candidate acceptance is human-owned.

## Bounded implementation and compatibility

The ticket's seven original criteria control. Read scoped spec:
[state/decision ownership](.scratch/ticket-harness/spec.md#state-and-decision-ownership),
[refactor verification](.scratch/ticket-harness/spec.md#oop-refactor-verification),
[ticket lifecycle](.scratch/ticket-harness/spec.md#ticket-lifecycle),
[exact revisions](.scratch/ticket-harness/spec.md#independent-checks-and-exact-revisions),
[QA/promotion](.scratch/ticket-harness/spec.md#feature-to-development-promotion-and-human-qa)
and [safe continuation](.scratch/ticket-harness/spec.md#corrections-and-safe-continuation).

Give each attempt operations owning Running/Verifying/Rejected/Done transitions,
revision/changed-file observations, inclusive/exclusive gate ranges, mirrored
current-ticket state and validated human-decision attachment. Migrate all relevant
entry callers within this slice, including failures before submission.
Existing flow begins in `tickets.execute`; `_Run.check` currently selects the last
history item for a decision and `agents.report` edits canonical gate status.
Inspect actual definitions/usages and consumers instead of relying on these
navigation hints or imposing private names/layout.

Runner retains check execution, report validation, evidence registration/source
invalidation and failure precedence. Parsing returns report/failure information;
runner alone records final canonical gate status/content/diagnostics. A validated
handoff crosses to its identified owning attempt; no positional history selection
or direct lifecycle-record mutation. Preserve initial/later repairs, either review
axis/nonzero exits, immediate human-decision stop, malformed-decision rejection,
optional/nonblocking behavior, process/timeout/report/integrity precedence and
bounded repairs. Preserve public CLI/exit behavior, JSON keys/values, artifact
names, history, protected inputs/caller state and meaningful intermediate atomic
persistence. Encapsulate real transitions, with no getter/setter-only facade,
inheritance framework or unrestricted runner coupling. Do not implement 21–24,
runtime 33/34, orchestration or QA acceptance.

## Verification, reviews and completion

Read [Python environment](docs/agents/python-environment.md) before Python,
dependencies or checks; use its absolute reusable micromamba prefix. Apply
[testing policy](docs/agents/testing.md), test-strategy and
[documented checks](docs/ticket-harness.md#python-and-checks). Map criteria to
existing public CLI/scripted-process/real isolated-Git coverage before adding
tests; retain check/CLI/record/ref evidence from required executions. Relevant
existing cases are in test_repairs, test_human_decisions, test_optional_suggestions,
test_timeouts, test_dependencies and test_reports. Add tests only for distinct
missing behavior using TDD at the approved seam; do not couple tests to private
classes or assignment order.

Establish/retain genuine pre-refactor deliberate checkpoint producer/source
provenance before runtime changes and continue it with final source, following
[ticket 15 evidence](.scratch/ticket-harness/evidence/15-completion.md) and refactor
verification. Do not fabricate a post-refactor checkpoint as compatibility proof.
Final executable change requires full pytest, strict mypy, Ruff lint/format,
whitespace and explicit gates on final source; packaging follows actual impact.

After checks pass, commit implementation before separate fresh High Spec/Standards
whole-ticket review from your original baseline. Supply contracts, affected and
unchanged flows, coverage/checks, exact source, prior full keys/history and omitted
scope. Preserve originals before aggregation. Resolve blockers through fresh
Medium repairs, renew checks/commit and re-review the whole ticket; optional
suggestions remain optional. Do not infer human scope/risk/QA authority.

Only after every criterion/gate passes reconcile unchanged criterion wording,
set Status completed, retain previous ready-for-agent in completion comment and
preserve Blocked by. Link criterion/check/review evidence from index and commit
bookkeeping separately. Then automatically use create-next-agent-prompt, verify
eligibility again and commit only generated handoff separately. Never begin the
next ticket. Return implementation/bookkeeping/handoff commits, actual checks,
separate review outcomes, criterion evidence, unchecked items, unresolved full
finding keys and next prompt path/selection or exact checkpoint/blocker.
