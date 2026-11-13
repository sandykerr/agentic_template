# Review records

Use this development record contract when preparing review assignments, saving
reports, disposing findings or carrying review context into a repair/handoff.
It implements the local [review contract](../../.scratch/ticket-harness/spec.md#review-work-findings-and-decisions)
under the existing [tracker conventions](issue-tracker.md). It defines Markdown
records, not a runtime report schema, scheduler or additional review gate.

Before assigning source reviews or carrying ownership concerns into repairs or
handoffs, apply [ownership and review scope](ownership-review.md). It owns the
substantive cross-module inspection and reporting contract; these records own
identity, preservation and disposition mechanics.

## Location and navigation

Keep records with their feature: `.scratch/<feature>/reviews/` for work items,
histories and decisions; `.scratch/<feature>/evidence/` for immutable reports,
instruction snapshots and check evidence. Link the review index from the feature
index and the originating ticket's history. Routine ticket Spec/Standards reports
share one ticket assessment; a cross-ticket assessment gets its own work item,
linked to every originating ticket and milestone. Use review IDs such as
`review-ticket-16` or `review-M1-architecture-01`, independent of implementation
ticket IDs. These IDs neither consume ticket numbers nor select implementation
work.

Start with the [assessment](../templates/reviews/assessment.md),
[report envelope](../templates/reviews/report.md),
[finding history](../templates/reviews/history.md) and
[human decision](../templates/reviews/decision.md) templates. Replace every
placeholder with a value or an explicit absence/reason; turn path placeholders
into relative Markdown links. Keep the original reviewer output verbatim as an
attachment when adding an envelope would otherwise change it. Existing historical
reports retain their original formats and scope; link them without retroactive
attestations. See the feature's [review index](../../.scratch/ticket-harness/reviews/README.md)
and [isolated worked example](../../.scratch/ticket-harness/evidence/16-miniature/README.md).

The navigable chain is:

`ticket/milestone → assessment → report/finding/evidence → history/decision → repair ticket/commit → independent verification → milestone assessment`.

Use links in both directions where needed to return to the originating scope.
If a repair, decision or eventual milestone assessment does not exist, record
that absence and responsible next action rather than creating evidence of an
assessment or approval that did not happen.

## Assessment identity and lifecycle

An assessment identifies its purpose, originating ticket(s), approved plan and
milestone, fixed original baseline, exact assessed revision(s), reviewer axes,
assignments/model/reasoning/context settings, and instruction identities. Identify
instructions by revision/path plus content digest or retained snapshot, including
the supplied spec/ticket and applicable guidance. Report unavailable settings as
unavailable; intended settings alone are not proof of actual delivery.

Capture inspected files/flows, omitted scope with reasons and unresolved
assumptions, report/evidence links, and a current finding summary keyed as below.
Preserve the original baseline through repairs. Each subsequent report identifies
its own exact assessed revision and assignment; a clean re-review at a new source
does not rewrite the earlier assessment.

Use **Review lifecycle:** `planned`, `in progress`, or `completed`. Completed means
the defined assessment and its reports are finished. Keep unresolved findings,
pending revalidation and integration/milestone eligibility in separate fields.
This lifecycle is independent of ticket triage `Status:`, execution state,
verified ticket completion and human QA acceptance. An assessment can be completed
with outstanding findings. A missing required report leaves it in progress.

## Immutable reports and append-only history

Save each original report/evidence snapshot at a unique path with report ID,
axis/attempt/assignment identity, baseline, assessed source and content identity.
Record a digest in its index or capture manifest; avoid self-referential hashes.
Actor attribution and content identities provide provenance without new signing
infrastructure. Retain failed/rejected attempts as well as successful reports.

A finding key is the tuple `(review ID, report ID, report-local finding ID)`.
For display, join these with `/` and choose IDs without `/`. For example,
`review-ticket-16/spec-01/F1` differs from
`review-ticket-16/standards-01/F1` and `review-ticket-16/spec-02/F1`.
Link a later report's observation to the prior key when it supersedes or reopens
the same concern. Local IDs alone are never sufficient references.

Append numbered or uniquely identified events to the finding history. Each event
records the full key, disposition, actor/role, reason, evidence, affected revision,
and links to the preceding/superseded observation, decision/amendment, repair
ticket, commit, independent verification and milestone assessment as applicable.
Use explicit pending/not-applicable reasons for missing links. Preserve events
even when mistaken: append a correction identifying what it supersedes. Reports,
evidence and previous history events remain unchanged. The assessment's current
summary/index may be refreshed from that history; distinguish this mutable view
from the authoritative observations.

## Dispositions and authority

| Disposition | Required support and next action |
| --- | --- |
| `open` | Original or reopened concern, source/evidence and impact; identify authorized repair or pending decision. |
| `fixed` | Repair ticket/authorized repair, exact commit and independent verification of that exact revision. A worker's assertion or a passing mechanical check alone does not establish independent review of the concern. |
| `deferred to linked ticket` | Follow-up ticket, reason, optional/blocking classification and authority. Optional suggestions may be deferred within approved scope. A blocker needs an explicit human decision and any required approved amendment. |
| `accepted with reason` | Reason, affected source/risk and authority; consequential risk requires an explicit human review decision. |
| `awaiting human decision` | Concrete question, consequence, proposed options, source and evidence; keep the concern unresolved while the decision is absent. |

Keep severity/classification from the original report visible; a disposition
does not silently reclassify a blocker. For a changed source, append a pending
revalidation or reopened event and mark the current summary accordingly before
using an old fix as current evidence. Relevant independent revalidation must name
the new exact revision and concern; append its result, preserving the earlier fix.
Source changes also require renewed applicable assessment/QA under the approved
contract. Unchanged or irrelevant evidence can be cited with its original scope;
it cannot stand in for unperformed revalidation.

Agents may carry out already-authorized repairs and record observations or
proposals. Explicit human decisions own consequential risk acceptance, blocker
deferral, ownership-contract changes and scope expansion. Preserve the actual
human statement and attribution/context; link the approved amendment when the
decision changes an approved contract. Missing amendment means the blocker
remains unresolved under that contract. A review disposition alone cannot
authorize integration, resume a stopped run or grant promotion. Assess eligibility
under the existing approved workflow; keep review decisions separate from
[exact-candidate QA decisions](../adr/0002-human-qa-gates-feature-promotion.md).

## Active runs and preserved evidence

Outside active runs, author review records in the existing feature tracker and
add navigation links without altering historical reports, completed tickets'
original requirements or frozen QA evidence. During a run, write new artifacts
only to harness-owned output outside approved inputs and worker-editable source.
Preserve captured inputs and their identities. After the run, link those outputs
from tracker history without rewriting active approved inputs or frozen evidence.
If the intended authoring files are active inputs, report that blocker and retain
the new record in the authorized output location until authoring is permitted.

For development architecture gating, apply
[architecture checkpoints](architecture-checkpoints.md). Reviewer calibration and
runtime adoption remain tickets 19 and 33; development guidance is not runtime
enforcement. These templates retain their evidence without claiming it exists.
