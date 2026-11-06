# Issue tracker: Local Markdown

Specs and tickets for this repository live in `.scratch/`.

## Conventions

- One feature per directory: `.scratch/<feature-slug>/`.
- The spec is `.scratch/<feature-slug>/spec.md`.
- Implementation tickets are one file each: `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, numbered from `01` in dependency order.
- Record triage readiness in a `Status:` line near the top of each open implementation ticket, using the vocabulary in `triage-labels.md`. Verified completion changes this line to `Status: completed` under the completion bookkeeping rules below.
- Declare dependencies in a `Blocked by:` line using ticket numbers and titles. A ticket's readiness label does not imply its dependencies are complete.
- Append comments and conversation history under a `## Comments` heading.

## Publishing and fetching

When a skill says to publish to the issue tracker, create the appropriate local Markdown file. When fetching a ticket, read its referenced path or locate its numbered file within the feature.

## Harness execution

Approved specs and tickets remain unchanged during a harness run. The harness records execution statuses, attempts, and outcomes separately. The authoring-time triage `Status:` is separate from the harness's execution state.

## Completion bookkeeping

Outside an active harness run, reconcile implementation tickets with their verified outcomes:

- Mark an acceptance criterion `[x]` only when evidence for the current implementation demonstrates it and the required checks and relevant independent reviews are satisfied. Leave unverified criteria `[ ]` and explain the gaps.
- Preserve criterion wording, scope, and declared dependencies, including the `Blocked by:` line. Update checkbox markers only in the acceptance criteria section.
- When every acceptance criterion and required gate is satisfied, set the ticket's header to `**Status:** completed` and record the previous readiness label in the completion comment. `completed` is a terminal bookkeeping status, not a triage readiness label or a replacement for harness-owned execution records. Retain the existing readiness status while completion remains unverified.
- Append a completion comment under `## Comments` with implementation commit references, evidence for each criterion, actual check results, separate Spec and Standards review outcomes, and any unresolved items. Link longer evidence rather than copying logs into the ticket.
- Link the completion evidence from the feature index when one exists. Verify that the acceptance markers, header status, completion comment, and feature index agree before declaring the ticket complete.
- If the ticket is an approved input to an active harness run, defer all ticket/index bookkeeping until the run has ended; keep the run's immutable snapshots and execution records intact.

## Wayfinding operations

For `wayfinder`, the map is `.scratch/<effort>/map.md`, with one child per ticket under `.scratch/<effort>/issues/`.

- Child tickets have a `Type:` of `research`, `prototype`, `grilling`, or `task`.
- A `Blocked by:` line names prerequisite child tickets.
- A child is available when it is open, unclaimed, and every prerequisite is resolved; choose the lowest number first.
- Claim a child by setting `Status: claimed`.
- Resolve it by appending an `## Answer`, setting `Status: resolved`, and adding a concise pointer to the map's Decisions-so-far.
- These operations manage planning work before harness execution; they do not authorize mutations to approved run inputs.
