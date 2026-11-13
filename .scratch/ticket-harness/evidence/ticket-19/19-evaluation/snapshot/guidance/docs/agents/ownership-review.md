# Ownership and review scope

Use this shared development contract when planning consequential mutable state,
implementing or repairing its operations, assigning Spec/Standards review, or
writing the next-agent handoff. It supplements [review records](review-records.md)
and the approved spec; it defines guidance, not a runtime schema or new gate.
Apply [domain guidance](domain.md), accepted ADRs and the target's own contracts.

## Planning and implementation

Record each consequential state contract in the spec's implementation decisions
(or link its existing authoritative contract). Identify:

| Decision | Required content |
| --- | --- |
| State and owner | The state, responsible module and invariants it owns. |
| Permitted writers | All roles/modules allowed to change it, including initialization and recovery. |
| Operations | The operations through which writers preserve invariants and ordering. |
| Persistence and restoration | Saved representation, reconstruction rules, shared identity/reference requirements and invalidation. State explicitly when no durable representation exists. |
| Failures | Observable rejection/failure behavior, partial-transition handling and who records the outcome. |

Describe responsibilities and operations; internal class, method and file choices
remain worker decisions. Before implementation, locate the approved contract and
record the affected flow: entry callers, owner operations, other writers, readers,
save/restore and invalidation. In implementation/repair evidence, explain changed
ownership and migration of writers, or why existing ownership remains correct.
For prose-only work, explain which guidance responsibility changes and whether
executable ownership is unaffected.

A missing consequential owner, incompatible writer, changed invariant or required
scope expansion goes to the human with source evidence, consequence and options.
Continue independent authorized work, preserving the unresolved decision. Routine
choices within an approved contract and already-authorized repairs can proceed.
A reviewer cannot invent permission by recommending a new owner.

## Assign the whole ticket

Capture the original starting baseline and exact current committed source; keep
the baseline fixed through repairs. Supply the full ticket diff from that baseline,
approved behavior/ownership contracts, role settings/guidance, coverage/check
records and relevant prior finding keys with append-only dispositions. Identify
pending revalidation and human decisions explicitly. Keep separate fresh Spec and
Standards assignments with independently configured settings. Each assesses the
source itself and records its original report before aggregation; sibling reports
from the same review round are excluded from initial assessment context.

- **Spec** checks acceptance requirements and approved behavior/ownership contracts,
  including failures and compatibility. Trace collaborators where needed to decide
  whether the promised behavior actually holds.
- **Standards** follows affected state and responsibilities beyond changed hunks:
  unchanged entry callers and consumers, every relevant writer, initialization,
  persistence/restoration and invalidation. Inspect definitions and usages, then
  follow the actual call/data flow; a changed-file list is a starting inventory.
  Apply [codebase design](../../.agents/skills/matt-pocock/codebase-design/SKILL.md)
  and the target's standards to explain who must coordinate each invariant.

Choose scope by affected responsibilities and concrete risks; record omitted
areas with reasons rather than claiming a whole-codebase review. A newly found
out-of-scope breach stays visible as a concern/decision; it does not authorize a
neighboring refactor. Existing authorized repair bounds, required checks,
architecture checkpoint rules and milestone QA gates remain authoritative.

## Report substantive reasoning

Use the [report envelope](../templates/reviews/report.md). Each original report
names exact baseline/source and assignment/guidance identities, inspected files
and flows (including unchanged collaborators), omitted scope with reasons and
unresolved assumptions. Distinguish:

1. **Substantive assessment:** connect the approved contract to actual operations,
   writers, callers and restored state; explain whether responsibilities preserve
   invariants. A clean report explains why the inspected design is acceptable.
2. **Evidence audit:** report commands, hashes, test observations and their limits.
   A matching hash proves identity; a passing test proves its observed behavior.
   Neither establishes a design conclusion by itself.

For each finding, cite exact code/contract locations, concrete evidence and
consequence, classify blocking versus optional, and give a proportionate remedy.
A documented ownership breach can block even in unchanged code when it defeats
the ticket's approved outcome. A preference for classes, shorter functions or a
particular file layout alone is insufficient. A long cohesive function may be
clean when its callers cross a small interface and it owns its decisions without
external coordination; explain that reasoning for the inspected flow.

Keep the summary concise and link detail as needed. There is no universal short
report cap: preserve all required scope, evidence and reasoning. Empty findings
mean no findings within the recorded inspection, not universal design approval.

For cumulative milestone scope and start/post-implementation risk triggers, apply
[architecture checkpoints](architecture-checkpoints.md). That contract determines
when broader work gates progression; this contract owns its substantive inspection.

## Repair and handoff

Carry the full review/report/local finding keys, original reports, disposition
history, approved contracts and exact rejected source to a fresh repair assignment.
Record its changed/unchanged ownership, claimed fixes and checks. Independently
verify each claimed fix against the exact repaired revision and re-review the
whole implementation from the original baseline using fresh separate axes.
Preserve original reports and append verification/disposition events under the
[record contract](review-records.md#immutable-reports-and-append-only-history).
Source changes require relevant exact-source revalidation; historical clean
reports retain their original scope. Optional suggestions remain optional.

A handoff links current ownership contracts/affected flows, assessment scope,
original baseline/current source, unresolved full keys, missing reports, pending
revalidation and human decisions with the responsible next action. State an
explicit absence when none exists. Preserve active-run inputs, prior evidence,
authorized scope and milestone boundaries. Review completion and risk disposition
remain separate from integration eligibility and human QA acceptance.
