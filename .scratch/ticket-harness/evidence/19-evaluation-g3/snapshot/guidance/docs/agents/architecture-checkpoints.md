# Development architecture checkpoints

Use this contract when implementing tickets, preparing integration, or writing a
milestone QA handoff. It implements the approved
[cumulative checkpoint contract](../../.scratch/ticket-harness/spec.md#cumulative-architecture-checkpoints)
through repo-owned guidance and tracker records. Automated runtime enforcement
belongs to ticket 33. Apply [ownership and review scope](ownership-review.md) for
substantive assessment and [review records](review-records.md) for identities,
immutable reports, finding history and human authority.

## Decide when review is required

At **ticket start and after implementation**, record yes/no with source evidence
for each trigger: a new lifecycle, persistence/restoration path, shared mutable
state, or additional writer of existing state. Include guidance state when a
prose change introduces one of these responsibilities. Explain unchanged owners
and affected entry callers, writers, consumers, restore and invalidation paths.
A trigger requires a broader assessment of that affected workflow **before ticket
integration**. Missing or incomplete required work remains an explicit blocker;
ordinary ticket Spec/Standards reviews still run independently. A no-trigger
result needs no third unconditional reviewer. Reassess after repairs when their
scope changes the trigger result.

Before **each required development milestone QA request**, create a cumulative
review work item in the feature's review index. Do this before presenting a
candidate as ready or freezing its assessment evidence. Planning may create the
item early with lifecycle `planned`; missing reports stay visible. Required
membership completion alone produces a preparation/waiting handoff until the
checkpoint and other candidate gates are satisfied.

## Pin the cumulative work

Use the [assessment template](../templates/reviews/assessment.md). Record:

- Purpose and originating milestone/tickets; the trigger assessment at start and
  after implementation, and whether the checkpoint gates integration or QA.
- **Cumulative baseline:** exact last human-accepted milestone source, linked to
  its actual QA decision. For the first milestone, use the feature starting
  revision with Git/planning provenance. This is distinct from a ticket's newly
  captured fixed review baseline. Never infer acceptance from clean reviews or
  choose the repository's first commit without feature provenance. If the
  starting revision or acceptance evidence is missing/ambiguous, expose that gap
  and hold readiness while the responsible workflow establishes it.
- Exact assessed source commit plus source/instruction identities; complete file
  and workflow inventory, with omitted scope and reasons. For this repository's
  small package, inspect **all `ticket_harness` Python files**, including unchanged
  collaborators. Larger targets inventory the complete affected workflow and its
  collaborators. A list of files alone does not establish inspection.
- All prior unresolved full finding keys, original reports, disposition/decision/
  amendment/verification links, and pending exact-source revalidation. Record an
  explicit absence when there are none; retain optional/deferred observations.

Use a **fresh High Standards assignment**, with the approved model, role guidance
and active-context target. Keep it distinct from routine ticket attempts and
preserve their independent Spec/Standards axes. Report unavailable settings.
Architecture review guidance can inform the assessment; an HTML report is not
required for a checkpoint. The original report must explain actual owners,
operations, unchanged writers/consumers and restored/invalidation behavior. Trace
the concrete edits for a plausible change (for example another review stage or
repair-policy adjustment): which owner, callers, saved representation, restore,
invalidation and checks would change, and why. Hashes and passing tests support
identity/behavior, not the design conclusion.

An existing audit can satisfy this work only when its **exact source, complete
required coverage and retained dispositions** match the present checkpoint. Link
that proof and the original audit. A changed source requires renewed relevant
review; record scope and why any unchanged evidence remains applicable. Until
that review names the current source, prior readiness is stale. Do not edit old
reports to make them appear current.

## Findings and progression

Apply the [disposition and authority rules](review-records.md#dispositions-and-authority):
fixed needs independent verification of the exact repair revision; deferral needs
a linked ticket and reason; consequential risk acceptance, blocker deferral,
changed ownership or scope requires an actual human decision and applicable
approved amendment. Keep awaiting decisions and missing amendments unresolved.
Preserve original classification and append history; never obtain authority by
relabeling a blocker. Optional suggestions remain optional and cause no automatic
repair or approval request.

Record four separate observations, supported by source-specific evidence:

| Observation | Meaning and next action |
| --- | --- |
| Assessment completed | Required reports and inspection finished; findings can remain open. Missing reports mean in progress. |
| Findings resolved/dispositioned | Exact fixes independently verified or valid authority and linked follow-up retained. Open in-scope blockers still prevent affected integration/readiness. |
| Candidate ready for human QA | Required membership, current architecture work, finding gates and all existing exact-candidate checks are satisfied. Only the authorized QA workflow prepares the actual request. |
| Milestone accepted | Actual human QA decision accepts the exact candidate/inputs. Only this permits the subsequent milestone/promotion under the approved workflow. |

A clean checkpoint progresses autonomously within approved scope; it supplies no
human acceptance. Authorized in-scope blockers use existing bounded repairs.
A cumulative blocker outside those bounds or a consequential undecided contract
preserves work and produces an incomplete human-decision handoff; independent
unaffected work may continue only under the existing eligibility rules. A review
decision cannot resume a stopped run or accept a candidate.

## Tracker and handoff

Link the assessment from every originating ticket, the milestone and feature
review index. Carry baseline/current source, complete scope, lifecycle, missing
reports, unresolved full keys, deferred ticket links, human decisions/amendments,
stale evidence and the next responsible action into implementation and QA/waiting
handoffs. Distinguish an absent checkpoint from a clean one. Refresh the current
summary while preserving reports and append-only history.

Preserve approved active-run inputs and frozen QA snapshots. During a run, new
artifacts belong only in authorized harness output, with authoring links added
later. If the requested authoring path is an active input, report that exact
blocker. Changed assessed source or frozen evidence invalidates relevant readiness;
new proposals may remain outside frozen evidence pending renewed review/request.

The [ticket 18 walkthrough](../../.scratch/ticket-harness/evidence/18-walkthrough/README.md)
retains finite isolated observations. Its example human statements are synthetic;
its reviews do not assess or accept the real development milestone.
