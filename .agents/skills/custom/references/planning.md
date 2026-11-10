# Shared planning reference

This is the authoritative planning policy for custom planning workflows and
their generated bundles. Upstream skills supply interview, domain, synthesis,
and slicing procedures; this reference augments their outputs and governs when
publication is allowed. It defines planning documents, not a runtime schema.

## Context and draft boundary

Read the target repository's `AGENTS.md`, domain glossary and relevant ADRs,
tracker and triage conventions, testing policy, and existing feature inputs.
Use project requirements and accepted architecture decisions over general design
heuristics. Reuse existing custom guidance before proposing another policy.
Resolve environment facts by inspection; decisions belong to the human.

For consequential mutable state, apply the repo-owned
[ownership and review-scope contract](../../../../docs/agents/ownership-review.md#planning-and-implementation)
when grilling decisions and drafting implementation contracts. Carry the owner,
permitted writers, invariant-preserving operations, persistence/restoration and
failure rules into the spec; resolve consequential gaps before approval.

For this repository, read [domain guidance](../../../../docs/agents/domain.md),
[tracker conventions](../../../../docs/agents/issue-tracker.md),
[triage vocabulary](../../../../docs/agents/triage-labels.md), and
[testing policy](../../../../docs/agents/testing.md) before the corresponding work.
For another target, use that project's equivalents; ask only for missing
decisions that cannot be inferred from its guidance or the conversation.

For this repository's ownership refactors 20–24, carry the
[evaluated development-review guidance and corpus](../../../../docs/agents/reviewer-evaluation.md)
into the implementation/review context. Preserve its exact guidance identity,
finite observations and unresolved limits; later refactor evidence and M1 QA
remain separate required work.

Keep proposals in the conversation or an explicitly marked draft location,
separate from published inputs. A suitable local staging location is
`.scratch/<feature>/drafts/<version>/`; mark each document **Draft — unapproved**.
Before approval, keep proposed individual ticket bodies inside `ticket-proposal.md`
rather than publishing files under `issues/`. Existing approved spec, tickets,
milestones and index stay unchanged. Proposed glossary/ADR changes affecting an
approved contract belong with the draft until accepted; ordinary resolved domain
terms can be captured using the project's domain-modeling procedure.

For an existing plan, identify the approved version and its immutable inputs.
Draft the proposed version separately, with an explicit change summary and
unchanged requirements carried forward. Preserve completed-ticket identities,
historical evidence, and prior versions. Active-run inputs stay immutable;
approval of a revision permits a separate new version, not an in-place edit of
the active version. External publication requires its own authorization.

## Grilling decisions and shared understanding

Use grilling's frontier rounds: ask only decisions whose prerequisites are
settled, give recommendations, and wait for answers. Use domain modeling to
resolve overloaded terms and test domain relationships with concrete scenarios.
Consult [deep-module guidance](../../matt-pocock/codebase-design/SKILL.md) when
interfaces or ownership need design work. Record these decisions:

- User problem, intended outcomes, actors, scope, and explicit exclusions.
- Important interfaces, ownership of invariants, external dependencies, and
  observable failure behavior. Leave internal implementation choices to workers.
- Agreed behavioral testing seams, existing prior art, required check commands
  or named gates, and evidence needed to establish success. Prefer existing
  public seams; explicitly agree any new seam with the human using
  [test strategy](../test-strategy/SKILL.md).
- Required work versus independent experiments or optional follow-ups; genuine
  prerequisite edges; ticket size and any prefactoring necessary for green slices.
- Meaningful earlier capabilities for human QA, plus final acceptance; or the
  user's every-N-ticket cadence. Set explicit membership, concrete human checks,
  observable pass conditions, and how earlier gates constrain later work.
- Worker/repair and separate Spec/Standards settings, ticket overrides, and
  applicable role guidance. Resolve ambiguous settings before approval.

Summarize settled decisions, proposed scope, testing seams, defaults and QA
strategy. The frontier must be empty for the proposed scope, and the user must
confirm shared understanding before synthesis. Confirmation authorizes drafting;
it is distinct from approval to publish the eventual bundle.

## Synthesis and joint revision

Use to-spec's problem/solution/stories/decisions/testing structure and to-tickets'
vertical slices and blocking edges. Each ticket delivers an independently
verifiable outcome small enough for one fresh context. Mechanical wide refactors
use upstream expand–migrate–contract guidance when vertical slicing cannot land
green. Specify contracts rather than prescribing internal classes or file layouts.

Present the spec and ticket/milestone proposal as one draft version. Include each
proposed ticket's complete body, not only its title; the user must be able to
approve the acceptance criteria, dependencies and exceptions before publication.
Ask whether granularity and blocking edges are correct, which slices need merging
or splitting, and whether the QA actions demonstrate the intended capabilities.

Apply feedback to the spec and proposal together. A changed outcome must update
the spec, affected ticket criteria/dependencies, milestone membership/QA, and any
testing or role settings it changes. Record the changes so the next approval
identifies the revised bundle. Pure clarification can be edited directly;
consequential new scope, interface, invariant, testing seam, dependency, or QA
decisions reopen only the affected grilling frontier and its dependent questions.
Confirm the resulting shared understanding before synthesizing the new version.

## Milestone membership

Always include a final milestone covering completion of every required ticket
and overall feature acceptance. Its required membership can be only the final
group; explicitly state cumulative coverage of earlier accepted groups. A single
milestone is reasonable for a small feature, but still propose earlier meaningful
capability checkpoints and explain when no useful earlier boundary exists.

By default group tickets into demonstrable capabilities. For an explicit every-N
request, fix a topological ticket order using genuine dependencies and agreed
priority, then partition it into groups of N with a smaller final group when
needed. For example seven tickets at N=3 produce groups 01–03, 04–06, and 07.
Record the actual IDs, not a dynamic rule such as "whichever three finish next".
If a requested order conflicts with dependencies, propose a valid order or ask
the human to resolve the conflict; do not quietly change N or invent edges.

Assign every required ticket to exactly one required milestone. Dependencies may
point within its group or to an earlier group, never a later group. Milestone IDs
remain stable across accepted versions; record any approved membership change.
An independent experiment can have a separate selection and final acceptance;
declare its priority without making it a release prerequisite accidentally.

For each milestone give QA setup, actions the human can perform, expected
observable results, and acceptance evidence. Distinguish ticket Done, milestone
accepted/promoted, and feature complete. Later groups wait for human acceptance
of the previous group; all tickets Done still requires final QA. Plan approval
does not accept a candidate. Actual request identities, candidates, decisions,
execution, promotion and continuation are owned by later runtime/QA workflows.

Before required milestone QA readiness, apply
[development architecture checkpoints](../../../../docs/agents/architecture-checkpoints.md).
Plan cumulative work with the prior accepted milestone or feature starting revision,
complete workflow inventory and carried findings. Assess lifecycle, restoration,
shared-state and writer risks at ticket start and after implementation; triggered
work requires broader assessment before integration. Keep review completion,
finding dispositions, candidate readiness and human acceptance separate.

## Ticket numbering

By default, number a new local ticket bundle consecutively in its preferred
execution order, with blockers before dependents and required milestones in
their planned order. Start at 01 for a fresh feature; continue after any existing
IDs when adding tickets. Within a milestone, use agreed priority to order
independent tickets. Numbering expresses a readable preferred sequence; retain
genuine dependency edges so independent work can still run in parallel.

Place an independent experiment at its intended scheduling point in that
sequence while keeping its separate membership and acceptance. For example,
if an experiment follows the backend slice, give it the next number before
later release work; numbering alone must not make it a release prerequisite.
Human QA gates still determine when later milestones become eligible.

Settle the draft order before assigning final IDs. When feedback reorders,
splits or adds draft tickets, refresh their numbers, filenames, dependency
links, milestone membership, proposal and index together before approval.
Present the numbered proposal in ascending order so the human can inspect
the intended sequence without a separate reordering request.

For revisions, preserve already published IDs, completed-ticket evidence and
captured run inputs. If preserving published IDs prevents sequential order,
show the exception explicitly. Renumber published open tickets only when the
human requests it; retain an old-to-new mapping and update live references
without rewriting historical identities or active-run inputs.

## Role and testing contracts

Use [efficient ticket development](../../../../docs/agents/development-efficiency.md)
to plan required assignments, check reuse and review preparation. Record agreed
resource/repair bounds without substituting them for accuracy or acceptance gates.

Record these defaults in the bundle unless the human chooses explicit alternatives:

| Role | Reasoning | Configuration |
| --- | --- | --- |
| Implementation and repair | Medium | One worker setting; a ticket worker override applies to both roles. |
| Spec reviewer | High | Independently configured from worker and Standards. |
| Standards reviewer | High | Independently configured from worker and Spec. |

Record the agreed model for each role; do not silently guess model availability.
Use fresh assignments, and record any agreed active-context target. For each
ticket, state its worker override and reason or explicitly inherit the default.
A worker override never changes reviewer settings. Record local source references
for required guidance, project defaults by role, and ticket additions by role.
Additions supplement defaults and preserve required role/output/access contracts.
Unselected installed skills are not automatically run inputs. Runtime skill
resolution/capture and model-profile execution remain separate work.

Preserve agreed interfaces, invariants and testing seams in the spec, with each
ticket linking its relevant contracts and checks. State behavioral coverage and
required gates without duplicating implementation details. QA actions complement
automated gates; neither replaces the other. A new testing seam or changed check
requirement is a planning decision, not an internal worker convenience.

## Complete bundle shape

For the local Markdown tracker, publish the following under `.scratch/<feature>/`
(or the target's configured versioned destination). Use actual values throughout;
the fields below are a checklist, not executable metadata. Link relative paths
and section anchors so a fresh worker can find the approved contracts.

### `spec.md`

- Title, plan version, approval record/reference, and relationship to any prior version.
- **Problem Statement**, **Solution**, and numbered **User Stories** covering the
  agreed behavior, failures and actors.
- **Implementation Decisions**: agreed interfaces, invariants, ownership and
  constraints; applicable domain/design references; deferred internal choices.
- **Testing Decisions**: agreed seams, prior art, behavioral coverage, required
  commands or named gate references, and expected evidence.
- **Role Configuration**: model/reasoning defaults for worker/repair, Spec and
  Standards independently; context targets and required/default guidance sources.
- **Milestone Contract**: link to explicit membership, QA and final coverage.
- **Out of Scope** and **Further Notes**, including unresolved matters if still
  a draft. Required decisions must be resolved before approval/publication.

### `ticket-proposal.md`

- Draft/approved state and version matching the spec; summary of changes from
  the prior proposal and any approved version.
- Each ticket's full proposed body using the individual-ticket shape below.
- Dependency graph or edge list, preferred topological order, milestone table
  with actual ticket IDs, and the role/testing exceptions being proposed.
- Questions/feedback and their resolution; approval scope and decision reference
  once accepted. After publication link the individual ticket files.

### `issues/<NN>-<slug>.md` (one per approved ticket)

```markdown
# <NN>: <Outcome title>

**What to build:** <complete bounded end-to-end behavior>
**Blocked by:** <numbers, titles and links, or None (can start immediately)>
**Status:** <target triage label; ready-for-agent only when sufficiently specified>
**Plan version:** <approved version; link to spec>
**Milestone:** <stable ID; link to membership and QA>
**Worker reasoning:** <inherit Medium, or explicit override and rationale; applies to repair>
**Role guidance:** <inherit project defaults; additions by role with local source references>
**Context:** <scoped spec contracts, domain/design references, agreed seam and check references>

## Acceptance criteria

- [ ] <observable requirement and evidence that verifies it>
- [ ] <failure/constraint requirement where applicable>

## Verification

<agreed behavioral seam, required checks and evidence; link shared requirements>
```

Apply [ticket numbering](#ticket-numbering). Readiness is separate from satisfied
dependencies or execution state. New acceptance markers remain unchecked. Include
a model/context override here if agreed; absent overrides inherit the spec defaults.

### `milestones.md`

- Version and approval reference, stable ordered IDs, named capabilities, fixed
  required ticket membership and gate into each next group.
- For each group: QA setup/actions, expected results and observable acceptance
  conditions, required evidence, and initial state **not yet requested/accepted**.
- Final checkpoint identified explicitly, with cumulative coverage of all
  required work and overall feature acceptance.
- Separate optional/experiment membership and priority where applicable.

### `README.md` (feature index)

- Version, approval scope/reference, links to spec, proposal and milestones.
- Every ticket's ID/title/link, declared dependencies, readiness and milestone;
  preferred execution order and current eligible group without claiming execution.
- Final QA requirement and distinction between plan approval and QA acceptance.
- Link prior versions/change summary for revisions; preserve existing completion
  evidence. A published plan alone does not claim any ticket or milestone complete.

## Approval, validation and publication

Before requesting publication approval, show the complete current spec and
proposal, including the ticket bodies, milestone definitions, defaults/overrides
and testing contracts. Identify version and intended destination. Explain that
the decision covers the coherent bundle; approval of scope, one ticket, or shared
understanding alone does not approve publication of unseen material.

Use an explicit human approval that identifies this current bundle. Existing
authorization suffices when it clearly covers the material being published;
do not ask again merely because a stage changed. If approval is declined,
withheld, ambiguous, or only partial, retain the draft and report the unresolved
scope. No individual tickets, canonical spec, milestones or index are published
until coherent-bundle approval is established. Silence is not approval.

Validate the approved draft before publication:

- Every agreed outcome maps to spec behavior and verifiable ticket criteria;
  spec/proposal/ticket defaults, overrides, testing contracts and QA agree.
- IDs and dependencies exist and are unique; graph is acyclic, and declared
  external prerequisites have explicit completion requirements.
- New ticket numbers follow the preferred execution sequence and milestone
  order, with blockers before dependents and experiments at their agreed
  scheduling points. Any preserved-ID exception is explicit; proposal order,
  filenames, headings, dependency links, milestones and index agree.
- Every required ticket has exactly one membership, dependencies respect group
  ordering, cadence matches the request, and final cumulative coverage is complete.
- Every milestone has actionable QA and acceptance conditions; no contradictory
  settings, unresolved required decisions, or fabricated acceptance remain.
- References resolve, ticket bodies match those approved, and the destination
  preserves existing approved inputs and unrelated work.

If validation requires a substantive change, revise the draft and obtain approval
for that changed scope. Publish all files of the validated bundle, then check
their cross-links, version, membership and criteria agree and record the human's
approval reference without inventing a decision or timestamp. Report paths and
any remaining execution prerequisites. This workflow authors approved inputs;
it does not implement scheduling, branch promotion, approval watching, restart,
QA execution, background launch, or runtime skill selection. Generated-bundle
runtime and skill-metadata proof remains ticket 37 in the harness project.
