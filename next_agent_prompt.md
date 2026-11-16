Use $implement-with-checkboxes to implement only:
`.scratch/ticket-harness/issues/25-guide-and-record-human-milestone-qa.md`

**25: Guide a human through milestone QA.** This is a prepared assignment;
ticket25 has not started. Do not automatically execute another ticket afterward.

## Starting state and eligibility

Follow [AGENTS.md](AGENTS.md), [GLOSSARY](GLOSSARY.md), relevant ADRs and the
[tracker](docs/agents/issue-tracker.md). Inspect/preserve unrelated work and capture
your starting HEAD as the fixed whole-ticket review baseline. Do not use historical
M1 source as that ticket baseline. Existing user environment/requirements/README
and recovery-file edits are unrelated to this assignment; do not broadly stage them.

Approved plan: [oop-v2 / review-process-1 spec](.scratch/ticket-harness/spec.md),
[approval](.scratch/ticket-harness/approval.md),
[membership and QA](.scratch/ticket-harness/milestones.md).
M1 tickets10–24 are verified complete and **M1 is accepted 2026-11-16**.
[Actual human decision and fulfilled condition](.scratch/ticket-harness/evidence/m1-final-review-01/m1-qa-decision.md)
accept source `88e4cd8aabc78e76e66efc02983fec3900ab0a23`, development request
`41a556a9352d44a3922a9c41f30f36af`. Both exact demo decisions were human-approved;
final promotion/completion/no-replay conditions passed. This was an explicit
conditional human acceptance fulfilled by actual observations, not agent approval.

M2 order is25–29. Ticket25 is the first open, unclaimed ready-for-agent ticket.
Declared prerequisites10/14 are verified by their acceptance/completion records,
checks and independent reviews:
[10 completion](.scratch/ticket-harness/evidence/ticket-10/10-completion.md),
[14 completion](.scratch/ticket-harness/evidence/ticket-14/14-completion.md).
Preserve `Blocked by:` as dependency history. Read the actual ticket and its
[proposal slice R07](.scratch/ticket-harness/ticket-proposal.md#r07-guide-a-human-through-milestone-qa).
M2 acceptance remains required before M3; this handoff accepts no later milestone
and does not complete the overall feature.

## Scoped behavior and all acceptance criteria

Read [QA/promotion](.scratch/ticket-harness/spec.md#feature-to-development-promotion-and-human-qa),
[safe continuation](.scratch/ticket-harness/spec.md#corrections-and-safe-continuation),
[review work](.scratch/ticket-harness/spec.md#review-work-findings-and-decisions),
[ownership](.scratch/ticket-harness/spec.md#ownership-contracts-and-cross-module-review),
[runtime adoption](.scratch/ticket-harness/spec.md#runtime-review-adoption),
[architecture checkpoints](.scratch/ticket-harness/spec.md#cumulative-architecture-checkpoints)
and [actual request/decision contract](docs/ticket-harness/qa.md).

Implement only the focused QA-session skill, reusing existing guidance where
appropriate. Preserve these six ticket outcomes:

- Read the exact request/candidate; guide planned human checks, evidence inspection
  and observable acceptance conditions.
- Record findings; withhold acceptance until explicit human approval. Passing tests,
  agent recommendations and requests to self-approve grant no approval authority.
- Write only the precise decision artifact for matching current identities,
  preserving provenance and rejecting stale requests.
- Do not implement corrections or change product source/integration refs. Route
  findings to the versioned planning workflow.
- Validate isolated explicit-approval, withheld-approval, stale-request and
  self-approval-request examples without changing actual user work.
- Present source-identified review reports, open findings and disposition reasons
  alongside candidate evidence. Review decisions do not substitute for separate
  exact QA acceptance.

Use the existing runtime JSON contract: exactly `decision: APPROVED` and the
complete matching current request object, written atomically only after actual
approval. The QA-session skill owns human guidance/observations and decision
provenance; runtime QA/Git owners consume decisions and perform promotion. Do not
add background execution, correction implementation, real backend delivery or
runtime review enforcement from later tickets.

## Roles, ownership and review

Inherit approved development settings: GPT-6.1 Sol Medium for fresh implementation
and repair; fresh independent Spec High and Standards High. Ticket25 has no worker
override. Advisory ≤250K active context; report unavailable backend enforcement or
telemetry. Apply ticket/default guidance and record actual supplied instruction
identities. These development settings prove no runtime model profile or captured
skill delivery.

Use [development review contract](docs/agents/review-records.md): record guidance
responsibility, permitted writers, identity/staleness invariants, failures and
persistence/provenance or explicit absence. Assess all four architecture triggers
at start and after implementation, including prose-created responsibilities.
Obtain triggered broader assessment before integration and cumulative M2 assessment
before its future QA readiness. Missing ownership or consequential contract changes
need a human decision; internal file/module choices remain worker decisions.

The accepted M1 cumulative baseline for later M2 checkpoint work is exact
`88e4cd8` with its linked QA decision, not a newer prose commit. Prior M1 repair
baseline remains `e2b0a26`; original feature baseline remains `1a623ba`.
[Current cumulative assessment](.scratch/ticket-harness/reviews/M1-architecture-01.md),
[original repair/cumulative reports and hashes](.scratch/ticket-harness/evidence/m1-final-review-01/capture.json),
[append-only F1 history](.scratch/ticket-harness/reviews/M1-architecture-01-history.md).
Original cumulative F1 is independently fixed; no unresolved in-scope production
finding, deferral, waiver or pending relevant source revalidation remains.
Historical ticket24 three full keys and ticket19 two fixture keys retain their
original identities/judgments. G2/C5 is finite historical evaluation, not current
package proof or runtime guidance delivery. The missing old ticket19 Git object
and retained-control hash verification are disclosed in the cumulative original;
no new calibration campaign is authorized or necessary.

## Verification and completion

Before Python/checks read [environment](docs/agents/python-environment.md) and
[testing policy](docs/agents/testing.md); use checkout-local uv `.venv/bin/python`.
Read [test-strategy](.agents/skills/custom/test-strategy/SKILL.md) before selecting
coverage, [writing-for-agents](.agents/skills/matt-pocock/writing-for-agents/SKILL.md)
and the installed skill-creator when applicable; locate its actual path from the
session skill catalog.
Map existing guidance/examples before creating redundant cases. This ticket's
standalone skill/document changes need official skill validation, link/routing/
workflow checks and retained disposable examples, rather than an artificial
runtime TDD cycle or replay of unrelated passing suites. If executable behavior
changes, preserve the approved public CLI/scripted-process/real-Git seam, use TDD
for a distinct missing behavior, and run required full/static/explicit gates.
No new private test seam is authorized. Hook scenarios need executable TMPDIR.

Retain actual commands/results, source/instruction identity, examples and artifacts
in one canonical evidence index before independent review. After checks, commit
only this implementation, then use code-review with the captured original baseline
and complete ticket/spec. Obtain separate fresh Spec/Standards originals with
substantive inspected/omitted scope and findings. Preserve both before repairs;
repair blockers with a fresh Medium assignment, renew affected required checks,
commit and re-review whole-ticket scope from the original baseline. Optional
suggestions remain optional. Scripted example roles do not replace source review.

After every criterion/gate passes, reconcile acceptance markers/status/completion
comment/index with actual evidence and commit bookkeeping separately; otherwise
leave unverified criteria unchecked and readiness unchanged. Then automatically use
create-next-agent-prompt, select again through M2 eligibility, and commit the
handoff separately under the implementation workflow. Creating the handoff starts
no next ticket. Report implementation/bookkeeping/handoff commits, checks,
independent outcomes, unresolved criteria and next selection or exact blocker.
Do not push or promote a real development checkout without separate authorization.
