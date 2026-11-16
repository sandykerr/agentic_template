---
name: to-tickets
description: Break a spec, plan, or conversation into approved dependency tickets with shared spec contracts and human QA milestones. Use for ticket breakdown, local publication, or revisions to an existing plan.
---

# To tickets

Read [upstream to-tickets](../../matt-pocock/to-tickets/SKILL.md) for tracer-bullet
slicing, blocking edges, prefactoring and wide-refactor sequencing. Read the
[shared planning reference](../references/planning.md) for project context,
numbering, output ownership, role/testing contracts, milestones and approval.
Perform these procedures directly when no Skill tool is available. Keep upstream
files unchanged; the shared reference governs local staging and publication.

1. Read the supplied source and comments, target-project guidance and existing
   approved inputs. Reuse settled decisions and existing authorization. Resolve
   consequential gaps in scope, dependencies, testing or QA before drafting the
   affected contracts; use [grill-to-tickets](../grill-to-tickets/SKILL.md) when
   the request needs the full design and spec workflow.
2. Draft independently verifiable outcomes with genuine blocking edges. Assign
   IDs in the shared reference's preferred execution order and propose explicit
   milestone membership. Stage complete proposed bodies in the conversation or
   a versioned draft proposal, keeping published inputs unchanged.
3. Present the complete current bundle for review. Revise granularity, edges,
   criteria and affected shared contracts together. Publish when explicit human
   approval covers the material and destination; otherwise retain the draft.
4. Validate and publish using the shared reference's
   [bundle shape](../references/planning.md#complete-bundle-shape) and
   [publication checks](../references/planning.md#approval-validation-and-publication).
   Each issue file contains its own ticket. Shared contracts belong in the spec,
   QA definitions in milestones and navigation/status in the index. Retain the
   reviewed proposal as history, outside the maintained published inputs.

Report published or draft paths, approval scope and remaining prerequisites.
Ticket publication does not start implementation or accept milestone QA.
