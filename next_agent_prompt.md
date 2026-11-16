Use $implement-with-checkboxes to implement only:
`.scratch/ticket-harness/issues/26-review-and-safely-retire-routine-ticket-evidence.md`

**26: Review and safely retire routine ticket evidence.** This handoff prepares
eligible work; it starts no implementation, cleanup execution or human QA.

## Start and eligibility

Follow [AGENTS.md](AGENTS.md), [GLOSSARY.md](GLOSSARY.md), both ADRs and the
[tracker](docs/agents/issue-tracker.md). Capture your actual starting HEAD as the
fixed whole-ticket review baseline and preserve the dirty worktree. Current
bookkeeping is `2278467d5f45a54461ce19d543b07ff638238933`; this historical reference
is not a substitute for recording your own baseline.

Read the [ticket](.scratch/ticket-harness/issues/26-review-and-safely-retire-routine-ticket-evidence.md),
[workflow policy/decision order](.scratch/ticket-harness/evidence-workflow-spec.md#policy-and-decision-order),
[shared implementation and ownership contract](.scratch/ticket-harness/spec.md#shared-implementation-and-verification-contract),
[role configuration](.scratch/ticket-harness/spec.md#role-configuration) and
[EC1 membership/QA](.scratch/ticket-harness/milestones.md#ec1-a-small-working-capture-to-deletion-path).
These are the supplied evidence-policy-1 inputs; their uncommitted authoring,
archive, navigation and skill changes remain separate from product commits.

M1 is accepted at `88e4cd8aabc78e76e66efc02983fec3900ab0a23`; see the actual
[human decision](.scratch/ticket-harness/evidence/m1-final-review-01/m1-qa-decision.md).
Prerequisite ticket 25 is verified complete: product
`febd86321851e2acec994237f9d1a1adea824c55`, original checkpoint `3b0c1ab`,
bookkeeping `2278467`. Recheck [criterion evidence](.scratch/ticket-harness/evidence/ticket-25/25-completion.md),
[routine assessment](.scratch/ticket-harness/reviews/ticket-25.md),
[triggered architecture assessment](.scratch/ticket-harness/reviews/EC1-capture-architecture-01.md)
and [review index](.scratch/ticket-harness/reviews/README.md). Ticket 26 is the
remaining EC1 member; actual human EC1 acceptance gates ticket 27. After 26,
prepare the cumulative assessment and QA handoff rather than starting EC2.

## Bounded implementation

Cover every acceptance criterion in the ticket. Publish standing evidence policy
and a narrow working inventory → assessment → fresh review → preview → guarded
Python deletion path consuming ticket 25 registrations. Preserve separate proposals,
reviewer approvals, actual successes/failures and retained source/result identity
within each authoritative JSON artifact. Establish eligibility from required facts
and fixed reasons; durable records, unresolved uses, unique needed content, unknown
facts and stale identities remain protected.

Preview preserves files. Execution acts only on explicitly approved, unchanged,
eligible files; agents assess meaning and Python performs deletion. Update maintained
navigation only after successful removal, with `(deleted)`, reason and retained
result where available. Reconcile actual versus approved paths and protected
survivors, including failure outcomes. Keep historical reports and frozen inputs
unchanged. This slice authorizes no lossy substantive replacement or merge.

Prepare a small isolated EC1 sample and inspection instructions. Keep human labels
hidden from assessors and the fresh reviewer until their original decisions are
saved; actual human comparison is later EC1 acceptance. Demonstrate eligible deletion,
protected/unknown retention, stale/incomplete refusal and a failed removal through
the approved public CLI/process/real-Git/filesystem/JSON seam. Parallel assessment,
merge review, trigger reassessment, broad calibration and runtime adoption remain
with their separately scoped later work.

Use [capture-evidence](.agents/skills/custom/capture-evidence/SKILL.md) and the
[implemented helper contract](docs/agents/evidence-capture.md) before new evidence.
Ticket 25 provides [shared EC1 capture](.scratch/ticket-harness/evidence/evidence-capture-workflow/EC1/evidence-review.json)
and [ticket 26 references](.scratch/ticket-harness/evidence/ticket-26/evidence-review.json).
`CaptureStore` owns captures/receipts/shared links under the evidence-directory
lock; producers own exclusive payloads. Extend later decision/execution namespaces
without competing writers or inheriting old approval for new bytes. Record owners,
writers, invariants, save/restore, invalidation and partial failures before changes;
resolve consequential ownership changes through the human decision boundary.

## Roles and verification

Fresh GPT-6.1 Sol assignments: Medium implementation/repair, independent High Spec
and High Standards, each targeting at most 250,000 active tokens. Product evidence
assessment/fresh High review remains separate from implementation source reviews.
Report unavailable configuration/backend enforcement/telemetry without inventing it.
Apply [development review](docs/agents/review-records.md), codebase-design and
[test-strategy](.agents/skills/custom/test-strategy/SKILL.md). Assess all four
architecture triggers at start and after implementation; triggered broader review
precedes integration. Cumulative EC1 review is still required before QA readiness,
from accepted M1 `88e4cd8`, with all package files/affected workflows and carried keys.

Before Python, dependencies or checks, read [environment](docs/agents/python-environment.md)
and [testing policy](docs/agents/testing.md). Follow the actual ADAPT host check,
[compute skill](.agents/skills/custom/adapt-compute/SKILL.md), current capacity,
architecture/resource fit and exact checkout/source/environment verification.
Forest203 x86_64 SSH terminal **43198** was retained at this checkout; inspect its
liveness/capacity and reuse if suitable. It reserves no resources. No Slurm allocation
is live. A lost terminal does not prove a workload stopped: inspect recorded state
before retry. Only one agent owns commands through a terminal; reviewers send needed
scoped probes to that owner.

Forest203 `/tmp` and `/var/tmp` were observed noexec. Recheck mount/capacity and use
suitable executable node-local scratch for Git hooks/executable fixtures; retained
`TMPDIR` was `/dev/shm/ticket25-resume-cC4Wm4`. Bound BLAS/OpenMP threads and process
concurrency, retain required observations in shared storage, and keep requested SSH
connections open. Use checkout-local uv `.venv/bin/python`; dependency versions are
pinned, and useful dependency changes require consistent environment definitions.

Map coverage before TDD at the approved public seam. Keep required final-source full
pytest, strict mypy, Ruff lint/format and whitespace gates, explicit ticket cases,
installed checks when packaging changes and skill/link/routing checks for guidance.
Capture actual commands, exits, identities and necessary observations during those
runs. Ticket 25's 589/full and all required checks verify only its bound source;
its [canonical index](.scratch/ticket-harness/evidence/ticket-25/25-evidence-index.md)
retains failed/interrupted runs and exact-input recovery separately. Historical
01–24 evidence retains its actual provenance; no retrospective compute-policy replay.

## Review, completion and handoff

After required checks, commit scoped implementation before fresh separate Spec and
Standards review from your fixed baseline. Collect both original reports before a
fresh Medium repair; preserve all failed/rejected rounds and renew affected/full
required gates on final source. Triggered broader assessment is a separate fresh
High Standards assignment. Ticket 25 has no open finding or deferred blocker:
[all five original full keys](.scratch/ticket-harness/evidence/ticket-25/25-finding-history.md)
are independently fixed at `febd863`; its whole-ticket reviews and early all-eleven-
file architecture renewal are clean. Changed relevant source needs renewed review;
that early assessment does not replace the future EC1 cumulative checkpoint.

Only after every criterion/check/review passes, reconcile acceptance markers,
completed status, prior readiness, criterion evidence and index, preserving
`Blocked by:` history. Commit only this ticket's bookkeeping separately, then use
[create-next-agent-prompt](.agents/skills/custom/create-next-agent-prompt/SKILL.md)
for a separately committed EC1 QA/preparation handoff. No live EC1 QA request,
candidate, decision or acceptance exists yet; the authorized QA workflow must
prepare exact inputs, cumulative review and human calibration/acceptance. Keep
candidate preparation/promotion and actual approval recording with their owners.
Report commits, observed checks, independent outcomes, unresolved criteria/keys or
explicit absence, and the next checkpoint. Preserve unrelated work and publish
externally only under separate authorization.
