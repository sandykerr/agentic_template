---
name: grill-to-tickets
description: Turn a feature idea or planning conversation into a jointly revised spec, dependency tickets, and human QA milestones, then publish the coherent bundle after explicit approval. Use for planning and plan revisions, not implementation or milestone QA execution.
---

# Grill to tickets

Use [the shared planning reference](../references/planning.md) for every session:
it owns the decision checklist, output shapes, milestone rules, and approval
boundary. Read it before interviewing or drafting. This is one user-facing
workflow; perform its internal stages without asking the user to invoke other
commands.

Read the applicable upstream instructions at each stage. Where no Skill tool is
available, read the linked files and perform their procedures directly. Apply
the shared reference's staging and approval boundary to their publication steps.

1. Read target-project guidance and existing approved inputs, then use
   [grilling](../../matt-pocock/grilling/SKILL.md) to settle the design tree and
   [domain modeling](../../matt-pocock/domain-modeling/SKILL.md) when terms or
   decisions need sharpening. Finish with the user's confirmation of shared
   understanding.
2. Use [spec synthesis](../../matt-pocock/to-spec/SKILL.md) and
   [test strategy](../test-strategy/SKILL.md) to draft the agreed behavior and
   testing contracts. Use [vertical tickets](../../matt-pocock/to-tickets/SKILL.md)
   to propose bounded outcomes, blocking edges, and milestone membership. Assign
   sequential IDs using the shared reference's [ticket numbering rules](../references/planning.md#ticket-numbering)
   before presenting the proposal.
3. Present the spec and proposal together. Revise both through feedback; reopen
   targeted grilling when feedback introduces consequential decisions. Finish
   with an explicit decision on the current coherent bundle.
4. On approval, validate and publish the bundle using the shared reference's
   output shapes. Otherwise retain a clearly marked draft and report that
   publication is withheld.

Report the draft or published locations, plan version and approval scope, and
remaining decisions. Planning output does not start a run or record QA acceptance.
