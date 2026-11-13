# Development review

Apply when planning consequential state, implementing/repairing it, assigning
reviews, recording findings, or preparing integration and QA handoffs. This is the
repo-owned application of the approved [review](../../.scratch/ticket-harness/spec.md#review-work-findings-and-decisions),
[ownership](../../.scratch/ticket-harness/spec.md#ownership-contracts-and-cross-module-review)
and [checkpoint](../../.scratch/ticket-harness/spec.md#cumulative-architecture-checkpoints)
contracts; it does not establish runtime enforcement. Follow [domain guidance](../../AGENTS.md#domain),
ADRs, target standards and the approved plan.

## Planning and implementation

Record or link each consequential state's owner/invariants, all permitted writers
(including initialization/recovery), invariant-preserving operations/order,
persistence/restoration (shared identity and invalidation, or explicitly no durable
state), and observable failures/partial transitions/outcome recorder. Trace entry
callers, owner operations, writers/readers, save/restore and invalidation before
implementation. Explain changed ownership/writer migration or why existing ownership
remains correct; prose changes identify their guidance responsibility.

Consequential missing/incompatible ownership, changed invariants or expanded scope
need a human decision with source, consequences and options. Continue independent
authorized work; class/method/file choices remain worker decisions.

## Prepare review and repair

Before review, the current worker finishes contract/coverage mapping, required
final-source checks and lossless evidence capture under the [testing policy](testing.md).
Keep agreed time/context/repair bounds in existing notes. Extra assignments need a
concrete task or required checkpoint; current workers handle local mechanical failures.
Give both reviewers one canonical evidence index. Missing observations need scoped
capture, rather than replay of a passing matrix or another source reviewer.

Collect both original axes before changing assessed source or dispatching repair.
Consolidate blockers by full key, preserving differing judgments and optional suggestions.
Investigate demonstrated failures and related authorized paths before resubmission;
neighboring refactors and exhaustive matrices require their own scope. Complete local
corrections/checks before fresh review; retain the workflow's checkpoint-commit requirement.

If a failure pattern recurs, pause new dispatches while the current worker/orchestrator
diagnoses preparation, contract, capture or incomplete-repair causes. Record rounds,
remaining blocker, next assignment purpose and agreed bounds in existing evidence.
Continue authorized work; human decisions are needed only at existing scope/authority
limits or exhausted agreed bounds. Cost limits cannot satisfy missing checks or blockers.

## Review assignments and scope

Keep the original ticket baseline fixed through repairs. Supply the full ticket
diff, current source, approved behavior/ownership contracts, role guidance/settings,
checks and prior full finding keys/history, including pending revalidation/decisions.
Use fresh separate Spec and Standards assignments with independently configured
settings; preserve each original report before aggregation and exclude sibling
same-round reports from initial assessment context.

- **Spec:** verify acceptance, behavior/ownership, failures and compatibility;
  inspect collaborators needed to establish the promised result.
- **Standards:** follow actual responsibilities through definitions/usages,
  unchanged callers/consumers, every relevant writer, initialization, persistence,
  restoration and invalidation. Apply [codebase design](../../.agents/skills/matt-pocock/codebase-design/SKILL.md)
  and target standards to explain invariant coordination.

A changed-file inventory is not inspection. Record inspected flows, omissions/reasons
and unresolved assumptions. Newly discovered out-of-scope breaches remain visible
for decision without authorizing neighboring refactors.

## Report substantive reasoning

Use the [report envelope](../templates/reviews/report.md). Connect approved contracts
to actual operations/writers/callers/restored state and explain invariant preservation,
including why a clean design is acceptable. Separate that reasoning from the evidence
audit: hashes establish identity and tests establish observed behavior.

Check explicit guarantees against accepted input values and reference aliases.
Narrower assumptions need contract or enforced-validation support; disclosure alone
cannot justify a clean result when accepted inputs break a guarantee. Supply a
counterexample and its consequence under the governing contract.

Findings identify exact source/contract locations, evidence, consequence,
blocking/optional classification and proportionate remedy. Unchanged code may block
when it defeats the approved outcome; length/layout/object preferences alone cannot.
A long cohesive function may be acceptable through a small interface without external
coordination. Keep summaries concise and link details; report caps cannot remove
required scope/evidence/reasoning. Empty findings cover only inspected scope.

## Architecture checkpoints

At ticket start and after implementation, record evidence-backed yes/no for a new
lifecycle, persistence/restoration path, shared mutable state or additional writer,
including prose-created guidance responsibilities. A trigger requires broader affected
workflow assessment before integration; reassess changed repair scope. Routine independent
Spec/Standards still apply; without a trigger, retain those two routine review axes.

Before every required development milestone QA request, create cumulative work in
the feature review index before ready claims or evidence freeze. Use the
[assessment template](../templates/reviews/assessment.md), identifying origin, triggers,
gate, exact source/instructions, full scope/omissions and all unresolved full finding
keys with reports/history/decisions, deferred work and pending revalidation (or none).

Its cumulative baseline is the exact last human-accepted milestone source with QA
decision; for the first milestone, use the exact feature-start revision with Git/planning
provenance. It differs from a ticket baseline. A clean review or repository-first commit
alone establishes neither acceptance nor feature provenance. Missing/ambiguous provenance
holds readiness until the responsible workflow resolves it.

Assign fresh **High Standards** with approved model/guidance/context target, separate
from ticket axes; report unavailable settings. Inspect all `ticket_harness` Python
files in this small repository, including unchanged collaborators; larger targets
inspect the complete affected workflow. Explain actual owners/operations and trace
a plausible change through owners, callers, saved representation, restore, invalidation
and checks. HTML is optional. Reuse prior audit evidence only with exact source,
complete required coverage, retained dispositions and original links. Changed source
needs renewed relevant assessment; preserve originals and explain unchanged evidence.

## Records and identity

Use `.scratch/<feature>/reviews/` for assessments/history/decisions and `evidence/`
for original reports/instruction snapshots/checks. Routine ticket axes share an
assessment; cross-ticket work gets its own, linked to originating tickets/milestone
and the feature review index. Review IDs do not consume/select implementation tickets.

Copy the [assessment](../templates/reviews/assessment.md), [report](../templates/reviews/report.md),
[history](../templates/reviews/history.md) and [decision](../templates/reviews/decision.md)
templates. Complete every field with a value or explicit absence/reason; use relative
links. Preserve original reviewer output verbatim separately if an envelope changes it.
Record actual model/reasoning/context settings or unavailable, and instruction revision/
path plus digest/snapshot. Intended configuration is not proof of delivery.

Identify each exact assessed source separately from checkout HEAD. Where the authorized
workflow permits uncommitted review, retain a source snapshot/manifest; this does not
waive a ticket workflow's committed-diff gate. Save original reports/evidence, including
failed/rejected attempts, at unique paths with report/assignment/source identity and
an external digest manifest. Historical reports keep their scope/format; add no
retroactive attestations. Actor/content attribution supplies provenance.

Review lifecycle is `planned`, `in progress`, or `completed`: completed means required
inspection/reports finished, even with open findings; missing reports mean in progress.
Keep it separate from ticket status, execution, verified completion and QA acceptance.

## Immutable reports and append-only history

A full finding key is `(review ID, report ID, report-local ID)`, displayed with `/`
and IDs without `/`, such as `review-ticket-16/spec-01/F1`. Another report's `F1`
is different. Link reopened/superseding observations to their prior full key.

Append uniquely identified events with full key, disposition, actor/role, reason,
evidence and affected source. Link prior observations, decisions/amendments,
repair ticket/commit, independent verification and milestone assessment; explain
pending/not-applicable links. Correct errors by appending superseding events;
preserve original reports/evidence/events. Refresh only mutable current summaries.

## Dispositions and authority

| Disposition | Required support |
| --- | --- |
| `open` | Concern, evidence/impact and authorized repair or pending decision. |
| `fixed` | Authorized repair/ticket, exact commit and independent verification of that revision/concern; worker claims or mechanical checks alone are insufficient. |
| `deferred to linked ticket` | Follow-up, reason, original classification and authority; blockers need an explicit human decision and required approved amendment. |
| `accepted with reason` | Reason, affected source/risk and authority; consequential risk needs an explicit human review decision. |
| `awaiting human decision` | Concrete question, consequences, options and source/evidence; remains unresolved until decided. |

Retain original severity/blocking classification. Human decisions own consequential
risk acceptance, blocker deferral, changed ownership and expanded scope; preserve the
actual statement, attribution/context and required approved amendment. Missing required
authority/amendment leaves blockers unresolved. Optional suggestions stay optional,
without automatic repairs or approval requests.

Changed source requires a pending-revalidation/reopened event and updated summary before
an old fix is cited as current. Independent revalidation names the exact new source/
concern and appends its result. Preserve earlier fixes; unchanged/irrelevant evidence
retains only its original scope. Renew relevant assessments and QA under the contract.

## Repair, progression and handoff

Fresh repairs receive exact rejected source, original reports/full keys/history and
approved contracts. Explain changed/unchanged ownership, claimed fixes and checks.
Independently verify exact-source fixes, then obtain fresh whole-ticket axes from the
original baseline. Existing required checks and bounded repairs remain in force.

Keep four source-supported observations separate: **assessment complete** (required
inspection/reports finished), **findings resolved/dispositioned** (verified fixes or
valid authority/follow-up), **ready for human QA** (membership, current architecture,
finding and exact-candidate gates pass), and **milestone accepted** (actual human QA
accepts the exact candidate/inputs). Only the authorized QA workflow prepares requests.
Missing/incomplete/stale required review or open in-scope blockers prevent affected
integration/readiness; completed membership alone yields preparation/waiting status.

Clean checkpoints and authorized fixes progress autonomously. Cumulative blockers
outside bounded repair or undecided consequential contracts preserve incomplete work
for human decision; unaffected work follows existing eligibility. A review disposition
cannot resume a stopped run, accept a candidate or authorize promotion; follow
[exact-candidate QA](../adr/0002-human-qa-gates-feature-promotion.md).

Link ticket/milestone → assessment → report/evidence → history/decision → repair →
independent verification → milestone assessment, including return links as needed.
Handoffs carry ownership/affected flows, original and cumulative baselines/current
source, scope, missing reports, unresolved full keys/deferred work, decisions/amendments,
stale evidence and responsible next action. State absences; links imply no unperformed work.

## Active runs and preserved evidence

Outside runs, update tracker/navigation while preserving historical requirements,
reports and frozen QA evidence. During runs write new artifacts only in authorized
harness-owned output outside approved inputs and worker-editable source; preserve
captured identities. Link outputs into tracker history when authoring is permitted.
If the requested destination is an active input, report that blocker and retain the
record in authorized output. Changed source/frozen evidence invalidates relevant
readiness; new proposals remain outside frozen evidence pending renewed review/request.
