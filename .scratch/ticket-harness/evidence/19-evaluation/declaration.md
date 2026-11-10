# Declared corpus — evaluator only

Declared before any corpus reviewer assignment on 2026-11-10. Exact creation time
and command output are retained in declaration-capture.json. This document and
build_corpus.py are excluded from reviewer input. No evaluation has yet occurred.
Fixed ticket baseline: `f2929e79cfd5a68f670862775053ae85ba9582b5` (clean worktree).
Corpus SHA-256 over canonical sorted path/digest mapping:
`ebf72b6255ad6c2c6365990f4479c11ddfc52113d13b57f02a4c584119401c23`.
[All 36 file identities](source-manifest.json); [source snapshot](snapshot/REVIEW.md).

| Case | Declared kind / required axis | Expected observation and rationale |
| --- | --- | --- |
| a3 | Required concern / Spec | JSON restoration detaches verified dictionaries from durable gates. `Run.invalidate` updates gates while QA still sees valid copies. Block incorrect restored eligibility; restore canonical references while preserving schema. Standards may also detect ownership breach. |
| b7 | Acceptable control / both | Cohesive Git validation hides command/error/branch/dirty/ancestor decisions behind one operation; the caller supplies policies and a real process adapter. Nested helper/functions do not justify a blocker. Contract intentionally excludes Git mutations and richer failure diagnostics. |
| c2 | Required concern / Spec | `checking.attach` selects history[-1], ignoring validated attempt ID. Late reports and unknown IDs mutate the wrong attempt. Block correctness/ownership breach; return validation to execution and attach through explicit identified owner. |
| d9 | Acceptable control / both | Pure parser returns immutable values, validates dependencies/cycles and preserves order. Local recursion/state are implementation details, not domain lifecycle ownership. No class/framework requirement. |
| e4 | Required concern / Standards | `repair.receive_repair` duplicates `Attempt.submit` edits into both attempt and current-ticket state; an extra writer owns ordering/policy outside approved owner. Present matching behavior does not satisfy one owning transition operation. Block explicit ownership breach with concrete propagation risk; delegate to existing submit operation, not broader refactor. |
| f6 | Acceptable control / both | Atomic replacement and captured subprocess primitives own filesystem/process mechanics, with documented failure/timeout contracts. No domain state to encapsulate; speculative class, fsync, metadata, or custom runner demands are unsupported blockers. |
| g1 | Required concern / Standards | Prepared returns incomplete None fields; CLI completes/normalizes/validates externally, resume returns incomplete result and accepts invalid limits. Block broken preparation ownership/completeness; preparation returns fully checked result to both callers. Spec may also detect direct behavior violation. |
| h8 | Acceptable control / both | Attempt owns mirrored state and legal transitions, validates before mutation, returns copies; caller delegates. Small object has actual invariant responsibility. No general state-machine requirement. |

Both fresh axes assess all eight independent cases once under the same final
guidance. Required pass: relevant axis detects each required concern with exact
source evidence, proportionate blocking classification/remedy; no unsupported
blocking findings on any control. Cross-axis concerns supplement, never replace a
miss on its declared relevant axis. Optional suggestions are evaluated on their
own evidence and do not fail merely by existing. Findings outside the key require
independent substantive adjudication; counts alone cannot score judgment.

Each report must reason about clean cases too. Preserve full raw output, settings,
provided instructions, source identities and every failed trial. Any required miss
or false blocker requires guidance correction or explicit unresolved limitation;
a correction needs fresh full-corpus trials of final guidance, retaining earlier
versions. No case-source repair may silently replace this declared corpus.

Guidance G1 is the exact supplied snapshot from baseline f2929e7: existing shared
ownership, record, checkpoint, test strategy and design contracts. No substantive
review guidance correction precedes this first trial. REVIEW.md supplies corpus
routing/report scope, not expected classifications. Model requested independently
for each axis: fresh gpt-6.1-sol High, fork_turns none, <=250000 active-context target.
Settings/tool acceptance are observed assignment configuration; backend telemetry,
hard context enforcement and filesystem sandbox isolation between assignments are
not established. Supplied snapshots are read-only and reviewers must stay within
them; the shared workspace remains technically accessible. Check source hashes
before and after. No harness run or production testing seam is involved.

Finite claim: eight short synthetic development cases, two independent full-corpus
reports per trial. They do not assess actual ticket_harness architecture or later
refactors, guarantee future detection, or demonstrate runtime delivery. Human
risk/design/QA authority and authorized autonomous repair remain unchanged.
