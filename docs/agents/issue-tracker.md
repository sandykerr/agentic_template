# Issue tracker: Local Markdown

## Conventions

- Features live in `.scratch/<feature>/`, with `spec.md` and `issues/<NN>-<slug>.md`.
  Publishing means writing local Markdown; fetch by referenced path or ticket ID.
- Follow [ticket numbering](../../.agents/skills/custom/references/planning.md#ticket-numbering).
  Dependencies, milestone gates and approved priorities determine eligibility;
  declare prerequisites by number/title in `Blocked by:`. Readiness proves no completion.
- Put `Status:` near the top of open implementation tickets; append history under
  `## Comments`. Keep harness execution status separate from authoring readiness.
- Approved specs/tickets stay unchanged during active harness runs. Record execution
  separately; defer ticket/index bookkeeping until the run ends and preserve snapshots.
- For assignments, reports, findings, repairs, integration/readiness and handoffs,
  apply the [review contract](review-records.md). Review completion does not accept QA.

## Triage readiness

| Status | Meaning |
| --- | --- |
| `needs-triage` | Maintainer evaluation required. |
| `needs-info` | More information required. |
| `ready-for-agent` | Specified for unattended agent implementation. |
| `ready-for-human` | Human implementation required. |
| `wontfix` | Declined. |

`completed` is terminal completion bookkeeping, not readiness or harness state.

## Completion bookkeeping

Outside active runs, mark acceptance criteria `[x]` only with current-source evidence,
required passing checks and relevant independent reviews. Preserve criterion wording,
scope, dependencies and `Blocked by:`; change checkbox markers only in acceptance criteria.
Leave unverified criteria `[ ]` and explain gaps.

When every criterion and required gate passes, set `**Status:** completed`; otherwise
retain readiness. Append a completion comment recording previous readiness,
implementation commits, criterion evidence, actual check results, separate Spec and
Standards outcomes and unresolved items. Link longer evidence; link completion evidence
from the feature index when present. Before claiming completion, reconcile acceptance markers, status,
comment and index. This bookkeeping replaces no harness execution records.

## Wayfinding operations

For `wayfinder`, use `.scratch/<effort>/map.md` and `issues/<NN>-<slug>.md`.
Set child `Type:` to `research`, `prototype`, `grilling` or `task`; name prerequisites
in `Blocked by:`. Select the lowest-numbered open, unclaimed child whose prerequisites
are resolved. Claim by saving `Status: claimed` before work. Resolve by appending
`## Answer`, setting `Status: resolved` and linking a concise answer pointer from
map Decisions-so-far. These planning operations do not authorize changing approved run inputs.
