# Runtime inputs and ticket selection

Use the [harness guide](../ticket-harness.md) to start a run. This reference covers
configuration, accepted Markdown tickets, prerequisite evidence and executable
milestone plans. The [shared planning policy](../../.agents/skills/custom/references/planning.md)
owns authoring approved bundles; those documents need adaptation to the runtime
contracts below. [Milestone QA](qa.md) covers candidates, acceptance and continuation.

## Canonical input contract

[examples/scripted/project.json](../../examples/scripted/project.json) is a minimal example. Configuration is
a JSON object with the following fields. Unknown fields and duplicate keys
(including inside nested objects) are rejected instead of silently ignored.

| Field | Meaning |
| --- | --- |
| `repository` | Git target path, relative to the configuration file or absolute. |
| `base` | Starting commit/ref; must equal the existing integration branch tip. |
| `integration` | Existing local destination branch, not checked out in any worktree. |
| `spec`, `ticket` | Approved Markdown paths, relative to the target or absolute. |
| `tickets` | Optional nonempty array of all Markdown ticket paths in this requirements bundle, including `ticket`. Defaults to `[ticket]`. It provides dependency context, not a multi-ticket execution selection. Paths must be distinct after resolution. |
| `selected_tickets` | Optional nonempty array of ticket paths to execute, relative to the target or absolute. Without `plan`, defaults to `[ticket]`; must include `ticket` and be a subset of `tickets`, with distinct resolved paths. With `plan`, selection must equal the first milestone. Bundle context alone never selects work. |
| `plan` | Optional approved milestone-plan JSON path, relative to the target repository or absolute. Enables the milestone contract below. |
| `completed_runs` | Optional array of earlier harness `run.json` paths, relative to the configuration file or absolute; defaults to `[]`. These provide prerequisite completion evidence, described below. |
| `standards` | Paths for applicable project rules, AGENTS instructions, ADRs, and policy; list them explicitly. |
| `agent` | Argument array for the trusted scripted executable, used freshly for each role. |
| `suite` | Argument array for broader baseline and candidate checks. |
| `checks` | Nonempty mapping of named lightweight checks to argument arrays. |
| `max_repairs` | Optional nonnegative integer; defaults to `2` repairs after the initial assignment. `0` stops on the first rejection. Booleans, floats, strings, and null are invalid. |
| `timeouts` | Optional object overriding [stage allowances](agents.md#stage-timeouts-and-cleanup) in seconds; omitted keys use those defaults. Every supplied value must be a positive finite JSON number no greater than `604800` (one week). Booleans, strings, null, unknown stages, and unsafe numeric ranges are rejected before any worker/check starts. |

All fields except `tickets`, `selected_tickets`, `completed_runs`, `max_repairs`, `timeouts`, and `plan` are required. Paths, refs, and
branch names must be nonempty strings; `standards` is an array of nonempty paths
(it may be empty). Approved files must exist and be readable. `checks` is a
nonempty mapping. Check names match `[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*`.
Every command, including unused named checks, must be a nonempty argument array
of nonempty strings without NUL characters, with an available executable.
Executable availability is checked without invoking it: names resolve on `PATH`;
absolute paths must name executable files. Relative executable paths must name
regular files tracked with executable mode (`100755`) in the approved base tree;
untracked files, caller-only permission changes, symlinks, and paths escaping the
worktree cannot supply a relative executable. Relative executable paths must not
contain `..` segments or end in `/` or `/.`. A bare name resolving through a relative
`PATH` entry is rejected; use an absolute executable path or a tracked `./path`.
Commands execute directly, without a shell, in their assigned detached worktree.
Relative executable/script arguments must also be available at the approved base
revision; preflight does not interpret arbitrary executable arguments or predict
runtime check success. `TICKET_HARNESS_STAGE` identifies the stage for commands.

See [stage timeouts and cleanup](agents.md#stage-timeouts-and-cleanup) for stage
keys and defaults, and [trust and integrity](agents.md#trust-and-integrity) for
command access and evidence protection.

## Markdown tickets

Markdown uses the existing local tracker conventions:

```markdown
# 02: Follow-up

**Status:** ready-for-agent
**Blocked by:** [01: Change value](01-value.md)
**Checks:** ticket

## Acceptance criteria

- [ ] The follow-up has an observable result.
```

- The header has exactly one `# NN: Title`, with a nonempty title and positive
  decimal numeric ID. Leading zeroes normalize to at least two digits (`1`, `01`,
  and `001` all mean `01`). IDs must be unique across the bundle. A numeric
  `NN-` filename prefix must agree with the heading. Optional `ID:` and `Title:`
  metadata must agree too.
- Header metadata precedes the first `##` section. Both `Status: value` and
  `**Status:** value` forms work (likewise other fields). Whitespace around
  values is trimmed. Duplicate fields are rejected, even when repeated values
  agree. Other descriptive header fields such as `Scope:` remain prose.
  YAML front matter is unsupported and rejected; it cannot override the header.
- `Status:` must use a configured local readiness label: `needs-triage`,
  `needs-info`, `ready-for-agent`, `ready-for-human`, or `wontfix`. Every
  selected ticket must be `ready-for-agent`. These are triage labels, never
  execution states or proof of prerequisite completion.
- `Blocked by:` is required. For no dependencies, write `None`, `None.`,
  or the established `None (can start immediately).` form (the final period is
  optional). Otherwise use comma-separated IDs, `NN: Title` references, or
  `[NN: Title](relative-ticket-path.md)` links; a numeric-only link label also
  works. Titles containing commas can be referenced by ID alone. Supplied
  titles and resolved links must agree with the referenced ticket. Every
  dependency must exist in `tickets`; cycles, including self-cycles and cycles
  in unselected work, invalidate the bundle.
- Exactly one `## Acceptance criteria` section must contain at least one
  nonempty `- [ ]`, `- [x]`, or `* [ ]` checklist item (`X` also works). Empty
  checklist items are rejected even beside valid ones. Checked boxes carry
  acceptance text, never harness Done state. Fenced code examples and appended
  `## Comments` history do not supply requirements or metadata.
- Optional `Checks:` lists comma-separated configured check names with no
  duplicates. Omission means all configured checks. Empty or unknown references
  are rejected. Only referenced checks execute and appear in each assignment's
  `required_checks`; the broader `suite` always runs at baseline and candidate.

`run.json.requirements` records the normalized bundle, keyed by canonical ID.
Each entry has `id`, `title`, `readiness`, `dependencies` (canonical IDs),
`acceptance` (checklist text), `checks` (names), and `source` (absolute path).
Original Markdown/configuration bytes remain the approved snapshots.

## Prerequisite completion evidence

Readiness and prerequisite satisfaction are independent. Include every prerequisite
in `tickets`. Select prerequisites for execution in this run or provide their
earlier `run.json` records in `completed_runs`. Each completion record must report
`outcome: "completed"`; every entry in its `tickets` mapping must be `Done`,
with a `done_revision` already ancestral to the configured base. Legacy records
without `tickets` use their single `ticket` entry. Every completed ticket must
exist in the current bundle, and its approved source path and SHA-256 must match
the current prerequisite file. Missing, incomplete, stale, duplicate, or
unintegrated completion evidence rejects the run. A changed prerequisite file
requires fresh completion evidence; checked acceptance boxes alone never suffice.
Completion records are trusted local harness artifacts, not an authenticated
provenance system. Explicitly selected prerequisites must reach Done again in
this run; external evidence cannot unlock their dependents early.

For example, add these fields to select the follow-up above after the earlier
fixture run completed (and use `base: "integration"`):

```json
{
  "ticket": "02-follow-up.md",
  "tickets": ["01-value.md", "02-follow-up.md"],
  "completed_runs": ["../passing-run/run.json"]
}
```

## Approved milestone plans

Supply `"plan": "plan.json"` in project configuration to execute fixed
milestones into `integration`, which serves as the feature branch. Omission retains
the earlier explicit ticket-selection contract. A plan is a separate approved JSON
input, snapshotted and SHA-256 recorded alongside the spec, tickets and configuration.
Starting `run` approves these exact inputs; the `approval` field records the human
bundle-approval reference and never asserts milestone QA acceptance.

This minimal example uses two required tickets and two groups:

```json
{
  "version": "v1",
  "approval": "human approved bundle v1 in planning session",
  "development": "dev",
  "required_tickets": ["01", "02"],
  "milestones": [
    {
      "id": "M1",
      "tickets": ["01"],
      "qa": {
        "setup": "Inspect the disposable target repository",
        "actions": ["Exercise the first capability"],
        "pass_conditions": ["The first capability produces its approved result"]
      }
    },
    {
      "id": "M2",
      "tickets": ["02"],
      "qa": {
        "setup": "Inspect the complete feature",
        "actions": ["Exercise both capabilities together"],
        "pass_conditions": ["All required outcomes satisfy overall feature acceptance"]
      }
    }
  ],
  "final_milestone": "M2",
  "final_coverage": ["01", "02"],
  "roles": {
    "worker": {"model": "approved-worker-model"},
    "spec": {"model": "approved-spec-model"},
    "standards": {"model": "approved-standards-model"}
  },
  "worker_overrides": {
    "02": {"reasoning": "High", "reason": "Approved complexity override"}
  }
}
```

All shown fields except `worker_overrides` are required. Unknown fields and
duplicate JSON keys reject; strings must be nonempty without NUL. Ticket IDs
are numeric strings and normalize like Markdown heading IDs. Each required ticket must exist in
`tickets` and belong to exactly one nonempty milestone. Context-only tickets are
allowed; external prerequisites require verified `completed_runs` evidence.
Dependencies may target the same/earlier milestone, never later ones, including
transitively through context tickets. The final milestone must be last;
`final_coverage` must list every required ticket exactly once, cumulatively including
earlier groups. QA requires nonempty `setup`, `actions` and `pass_conditions`;
the latter two are arrays of nonempty strings.

Each role requires an explicit `model` string. Reasoning defaults independently to worker `Medium`
and Spec/Standards `High`; explicit `Low`, `Medium`, `High` are supported. Optional
`context_limit` is a positive integer active-context target. Worker overrides must
name required tickets, give a nonempty `reason` and at least one of `model`,
`reasoning`, `context_limit`. They apply to implementation and repair; reviewers
keep independent profiles. `run.json` records normalized `plan` and effective
`worker_settings` for every required ticket. These approved profiles do not alter
the scripted command contract or enforce model selection/context occupancy;
live enforcement remains future work.

Optional Markdown headers `Plan version`, `Milestone`, `Worker reasoning` require
plain scalars exactly matching plan version, group ID and effective reasoning
(for example `**Milestone:** M1`). Duplicates, even identical, and links,
explanatory suffixes or inheritance prose reject. The planning authoring template
permits links and inheritance/rationale prose in these headers; runtime adapters
must emit the exact scalars above. Authoring bundles are not automatically
executable input.

`ticket` must identify a member of the first milestone. Omit `selected_tickets`
to select that whole group, or explicitly list exactly its members. Later groups
cannot be selected. Among ready tickets the harness follows the fixed order in
that group's `tickets` array, honoring actual dependencies; each implementation
starts from the latest verified feature revision. All execution gates below remain
mandatory. Validation completes before worktrees, checks, agents or ref changes.
`development` must name an existing local branch distinct from `integration`;
its starting revision is recorded. Every required ticket must be ready-for-agent,
and dependencies outside the plan require verified completed-run evidence, including
for later groups. These checks happen before execution.

## Explicit selection without a milestone plan

To execute a dependency graph in one run, explicitly select its tickets:

```json
{
  "ticket": "02-follow-up.md",
  "tickets": ["01-value.md", "02-follow-up.md", "03-independent.md", "04-human-context.md"],
  "selected_tickets": ["02-follow-up.md", "03-independent.md", "01-value.md"]
}
```

Without `plan`, the harness chooses the lowest **numeric**
canonical ID among Ready selected tickets, independently of configuration order.
Unselected agent-ready and human-ready context never executes automatically.

## Execution gates

In either mode, after preflight validates the entire bundle and all commands,
the broader starting baseline runs once.
A ticket is Pending until all its prerequisites are either externally verified
at the starting base or Done in this run. Integration promotion precedes Done and
unlocking. There is at most one active implementation ticket, including repairs;
its checks, both reviews and exact-candidate broader suite complete before the
next selection. Every new ticket starts at the latest verified integration tip,
including already completed independent changes. Its assignment `base_revision`
is fixed to that tip across its own repairs. Each assignment's `inputs.ticket`
is the active ticket's approved content; other bundle snapshots remain context.
`required_checks` and `check_results` contain that ticket's checks and reports,
plus the shared baseline, without transferring earlier tickets' findings or approvals.
The durable record retains all earlier evidence.

Every selection must reach Done; milestone mode also requires final human QA
acceptance and promotion for run completion. This slice stops the run on the
first blocked ticket or shared environment failure; selected dependents remain
Pending and unrelated selections retain their observed Ready state. Continuing
unrelated work after a block belongs to ticket 29. A shared baseline failure
launches no workers and consumes no repairs; the compatibility `ticket` entry
(the configured primary before execution) becomes Blocked and other selections
retain their pre-baseline states. Integration changes made outside the harness
are never overwritten by candidate promotion.

See [agent execution and records](agents.md#records-and-artifacts) for retained
attempts, bounded repairs, gates and findings. In milestone mode, later groups
wait for [human QA](qa.md).

## Preflight and output placement

A preflight rejection returns nonzero with `outcome: "invalid-input"`, an `inputs` failure
message naming the offending field/ticket, no gates or assignments, and attempt
0. No worker/check processes start, no Git worktrees are added, and integration
references remain unchanged. The new output directory may contain diagnostic
records and snapshots. Git/environment preflight also retains the original
base/integration/ref checks before execution.

The output must be a new directory outside the target repository and separate
from approved input files. Each approved file, including configuration, bundle
tickets, completion records, and standards, is copied verbatim to `inputs/`;
`run.json` stores its SHA-256 and
original path. Agent-editable source lives separately under `worktrees/`.
