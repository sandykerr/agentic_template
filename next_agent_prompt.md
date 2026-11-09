Use $implement-with-checkboxes to implement only:
`.scratch/ticket-harness/issues/16-record-review-work-findings-and-decisions.md`

**16: Record review work, findings and decisions**

Work in `/home/ajkerr1/development/agentic_template`. Read the actual
[ticket](.scratch/ticket-harness/issues/16-record-review-work-findings-and-decisions.md)
and follow the current
[implementation workflow](.agents/skills/custom/implement-with-checkboxes/SKILL.md).
Generating this handoff starts no implementation, reviewer evaluation, harness run
or human QA session.

## Starting state and eligibility

Follow [AGENTS.md](AGENTS.md), its linked tracker/readiness/domain guidance,
[GLOSSARY.md](GLOSSARY.md) and applicable [ADRs](docs/adr/). Capture your own
starting HEAD as the fixed review baseline and inspect/preserve the actual
worktree. At handoff creation HEAD was
`152b0c4577269789a419079c6261c69f9a0695fd`; this historical reference does not
replace your starting-baseline capture.

The approved plan is **oop-v2 / review-process-1**: see the
[approval](.scratch/ticket-harness/approval.md),
[index](.scratch/ticket-harness/README.md),
[proposal](.scratch/ticket-harness/ticket-proposal.md) and
[milestones](.scratch/ticket-harness/milestones.md).
M1, tickets **10–24**, is the earliest required milestone with human acceptance
pending. Completed 10–15 retain their evidence; 16 is open, unclaimed,
`ready-for-agent` and first in the approved preferred order. Its completed
prerequisites are 10 and 11:

- **10:** implementation `70a01220dfac353ebea639ae85daac08d5eed8b2`, bookkeeping
  `fe036e320508f5d5f461bfff344bc3f0061d154e`;
  [criterion evidence](.scratch/ticket-harness/evidence/10-completion.md) and
  [actual checks plus independent Spec/Standards reports](.scratch/ticket-harness/evidence/10-checks.log).
- **11:** implementation `552fcd6b87909b96ac7bcd6a878d0db6bbbd2869`, bookkeeping
  `bb982c0e2b9a44493405fb1c5dca6b985d80cd43`;
  [criterion evidence](.scratch/ticket-harness/evidence/11-completion.md),
  [checks](.scratch/ticket-harness/evidence/11-checks.log),
  [Spec](.scratch/ticket-harness/evidence/11-review-spec.md) and
  [Standards](.scratch/ticket-harness/evidence/11-review-standards.md).

At prompt creation these four commits were ancestors of HEAD; both prerequisite
tickets had six verified criteria, passing standalone checks and independent
reviews with zero blockers. Recheck relevant evidence against your starting
state; historical results do not verify ticket 16. Historical issue numbers in
completion evidence retain their original scope; use the current index for work.

The approved plan publication remains **uncommitted**: spec/index/proposal and
milestone edits, new/renamed issues, archives, glossary/reference updates and
publication records are pre-existing work. The custom architecture-review skill
and draft directories are also uncommitted. Preserve them; do not stage the
publication wholesale as ticket-16 implementation. Isolate your own edits to dirty
shared files for review/commits, preserving unrelated content. If active harness
inputs would need mutation, preserve them and report the exact blocker. The
publication record's original handoff hash describes the earlier published pointer;
this user-requested handoff refresh supersedes that pointer without rewriting its
historical publication evidence.

## Scoped contracts and roles

Read the spec's
[review records](.scratch/ticket-harness/spec.md#review-work-findings-and-decisions),
[ownership/scope](.scratch/ticket-harness/spec.md#ownership-contracts-and-cross-module-review),
[architecture checkpoints](.scratch/ticket-harness/spec.md#cumulative-architecture-checkpoints),
[reviewer evaluation](.scratch/ticket-harness/spec.md#reviewer-evaluation),
[verification](.scratch/ticket-harness/spec.md#review-process-verification) and
[role configuration](.scratch/ticket-harness/spec.md#role-configuration).
Later-work sections define boundaries; implement only ticket 16.

Use fresh **GPT-6.1 Sol** assignments: **Medium implementation/repair** and
independently configured **High Spec** and **High Standards**. Ticket 16 has no
override. Target at most **250,000 active-context tokens per agent**, with headroom
for verification/handoff; report missing model/configuration rather than guessing.
These development settings do not establish runtime profile or skill delivery.
Apply the ticket's test-strategy/codebase-design role guidance and, when authoring
skills, writing-for-agents and the installed skill-creator. Keep upstream skills
unchanged. Bootstrap under existing independent implementation reviews, applying
new record requirements as they land; do not claim 17–19 are implemented.

## Bounded outcome and all six criteria

The ticket's unchanged wording is authoritative. Deliver usable repo-owned
contracts/templates/navigation and evidence covering:

1. A review work item with identity, originating ticket(s)/milestone, purpose,
   baseline/assessed source, reviewer axis/settings/instruction identity,
   lifecycle, inspected/omitted scope, reports and unresolved findings. Routine
   Spec/Standards reports attach to their ticket assessment; cross-ticket
   assessments have their own work item. Review IDs do not consume implementation
   IDs or form a separate scheduler.
2. Immutable original source-identified reports/evidence; compound finding keys
   using review/report identity plus report-local ID; append-only disposition
   history with actor, reason, evidence, revision and links. Re-review appends
   superseding observations rather than rewriting reports.
3. Open, fixed, deferred-to-linked-ticket, accepted-with-reason and
   awaiting-human-decision dispositions. Fixed requires independent verification
   of the exact repair revision; changed source requires revalidation. Completed
   assessment and unresolved findings remain separately visible.
4. Human authority over consequential risk, blocker deferral, ownership/scope
   changes and required amendments. Review decisions remain separate from QA
   decisions and cannot silently authorize integration/promotion. Agents may
   perform only already-authorized repairs and record evidence/proposals.
5. Navigable concern → evidence → disposition/reason → ticket/repair → commit →
   independent verification → milestone-assessment links. Demonstrate all six
   cases: fixed finding, deferred optional finding, explicit human risk decision,
   duplicate local IDs, reopened concern after source change, and completed review
   with outstanding findings.
6. Records within the existing feature tracker/evidence context, with review
   lifecycle separate from ticket readiness. Preserve historical reports,
   completed tickets, captured inputs and frozen QA evidence. During a run, new
   artifacts belong in harness-owned output; authoring links cannot mutate active
   inputs or frozen evidence.

Internal layout remains a worker choice. Use an isolated miniature tracker with
actual saved Markdown records and source/report identities. Clearly label example
identities and human decisions as synthetic; they do not accept real risk or a
development milestone. Defer broader review-scope enforcement (17), architecture
gating (18), actual reviewer calibration (19), refactors (20–24), runtime review
scheduling/wire changes (33), and live-agent proof (34). Preserve current runtime
contracts. No external tracker, signing infrastructure or new framework is needed.

## Environment, checks and evidence

Before Python, dependencies or checks read
[environment guidance](docs/agents/python-environment.md) and reuse its absolute
micromamba environment. Follow [testing policy](docs/agents/testing.md),
[test-strategy](.agents/skills/custom/test-strategy/SKILL.md) and
[documented checks](docs/ticket-harness.md#python-and-checks).

For this documentation/skill/template scope, map criteria to existing coverage,
validate documents/skills, links/anchors and routing, then exercise the six
history/navigation cases in an isolated miniature tracker. Retain helper sources,
actual command/exit results, final source identities, observations and artifacts
for criterion-specific evidence. Reuse 10/11's standalone-workflow approach without
relabelling old checks as verification of new source. Scripted examples establish
record behavior, not actual reviewer judgment; calibration belongs to 19.

Do not manufacture runtime tests or replay the runtime suite for standalone prose
work. If executable harness changes are necessary within scope, use TDD at the
approved public CLI/scripted-external-process/real-isolated-Git/observable-record
seam. Preserve required final-source full pytest, strict mypy, Ruff lint/format,
whitespace and explicit ticket gates; packaging/installed checks follow policy
and impact. Plan evidence capture before required verification.

## Review, completion and handoff

After checks pass, commit only ticket-16 implementation before `$code-review`,
which reviews committed changes. Supply your captured original baseline, ticket
and scoped spec explicitly. Obtain separate fresh High Spec/Standards reviews;
fixture reviewers are not substitutes. For test changes provide the coverage map,
testing policy and test-strategy review guidance. Resolve blockers through fresh
Medium repairs, renew affected required checks, commit fixes and re-review the
whole implementation against the original baseline. Record optional suggestions.

After verification/reviews, reconcile all six acceptance markers, set
`**Status:** completed`, record previous `ready-for-agent` in the completion
comment, and preserve `Blocked by:`. Link criterion evidence, actual checks,
implementation commits and both independent review outcomes from the ticket and
index. Commit only this ticket's bookkeeping separately from implementation,
isolating it from pre-existing publication changes. Missing required evidence
leaves criteria unchecked and completion pending with the exact blocker.

Only after implementation and bookkeeping are committed and complete, follow the
implementation workflow's automatic `$create-next-agent-prompt` step and separate
handoff commit. Re-evaluate eligibility: 17 is expected next only if current
prerequisites/order still permit it. Carry open reviews/findings; do not launch
another assignment automatically.

M1 human QA remains not requested/accepted. Its boundary follows all required
10–24 outcomes and the required cumulative architecture assessment; M2 25–29
remains gated until explicit M1 acceptance. Later groups, final QA and independent
E1's priority after verified real-agent 34 follow the published plan. Ticket Done,
record examples and plan approval do not accept a candidate or complete the feature.

Return implementation/bookkeeping/handoff commits, actual check/review outcomes,
criterion evidence, unchecked items, unresolved findings and the next prompt or
exact blocker. Preserve approval/checkpoint history and unrelated changes. Do not
push or author human QA acceptance.
