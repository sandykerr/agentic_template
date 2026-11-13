# Handoff: M1 caller-index repair and final verification

Prepared 2026-11-13 for a fresh agent in this repository. Paths below are relative
to the repository root unless otherwise stated. The human explicitly requested
this workspace destination, overriding the handoff skill's temporary-directory
default. Creating this document did not execute the repair, checks or QA.

## Objective and current authority

Complete the remaining M1 technical work: address the caller-index finding,
renew applicable verification and independent cumulative review, and prepare
the exact tested candidate for the human's final acceptance. Begin with the
existing finding and its evidence; rerunning passing checks alone cannot close
it. Keep implementation within the existing caller-state preservation contract.
Consequential contract changes or risk deferral still need the human's decision.

The human has completed the code/documentation review. Its actual statement and
scope are recorded in [human review completion](../../docs/human_qa/m1_review.md#human-review-completion--2026-11-13)
and the [M1 status and pass conditions](milestones.md#m1-a-complete-qa-controlled-git-cycle).
This does not waive the open blocker or supply candidate-specific approval.
M1 remains unaccepted; M2 tickets 25–29 remain ineligible. Do not reopen completed
ticket 24 merely to represent this cumulative finding or select a later ticket.

## Read first

1. [AGENTS.md](../../AGENTS.md), [glossary](../../GLOSSARY.md), the
   [ADRs](../../docs/adr/0002-human-qa-gates-feature-promotion.md), and conditional
   [environment](../../docs/agents/python-environment.md),
   [testing](../../docs/agents/testing.md) and
   [tracker](../../docs/agents/issue-tracker.md) guidance.
2. [Current M1 assessment](reviews/M1-architecture-01.md), its
   [append-only finding history](reviews/M1-architecture-01-history.md), and the
   [original cumulative report](evidence/m1-qa-01/standards-01-original.md).
3. The [development review contract](../../docs/agents/review-records.md), approved
   [spec](spec.md), [publication authority](approval.md) and relevant
   [M1 requirements](milestones.md#m1-a-complete-qa-controlled-git-cycle).
   Approved authoring inputs are oop-v2 / review-process-1.
4. [Human correction assessment](reviews/M1-human-readability-01.md), its
   [renewed source manifest](evidence/m1-human-review-01/renewed-source.json), and
   [source-specific suite result](evidence/m1-human-review-01/renewed-suite-result.json).
   These explain existing changes and prior verification; do not relabel them as
   checks of your repair.

The root [next_agent_prompt.md](../../next_agent_prompt.md) remains older waiting
context. Use this handoff and the current records for subsequent human-review
completion, evidence retirement and absent temporary environments. Do not follow
its old live-demo paths as if their existence were established.

## Starting state and finding

HEAD was `d02e61ea27de4febd17e337bd51529d07861226b` when this handoff was prepared,
with readability/docstring and observer-test corrections still uncommitted.
During the human's subsequent requested commit preparation, those code/test
changes were committed as `c994d52` without changing their verified bytes. All
26 retained renewed-source hashes still match; this is a source checkpoint,
not an F1 repair, renewed cumulative review or milestone acceptance.

Documentation, evidence/archive and M1-status commits follow that checkpoint.
Inspect current HEAD/status and capture your own starting source/instruction
identity instead of assuming the earlier dirty state or commit IDs are current.
Preserve any remaining unrelated work and all retained originals. Nothing was
pushed as part of this preparation.

The blocking full key is **`review-M1-architecture-01/standards-01/F1`**. An inherited
`GIT_INDEX_FILE` can route harness submission writes into the caller's index;
later integrity rejection prevents integration but does not undo the mutation.
Use the [paired reproduction/control manifest](evidence/m1-qa-01/index-routing-repro-01/manifest.json)
and original report to understand the exact observation and proposed remedies.
The readability correction did not repair it. Events02/03 retain it as open with
current-source revalidation pending; no waiver or independent fixed result exists.

The fixed cumulative baseline is
`1a623bad0b08241367948948b731b9e1f5114671`; its provenance is in the assessment.
It is distinct from the repair's starting snapshot and ticket 24's original
whole-ticket baseline. Preserve those separate identities through verification.

## Execution sequence

1. **Diagnose and repair the bounded cause.** Trace current Git/process owners,
   inherited environment and every relevant repository write. Reproduce through
   the approved public CLI, scripted external processes and real disposable Git
   repositories. Preserve the caller HEAD/index/worktree and intentional isolated
   merge-index overrides. Inspect related routing paths; a fix to one `add` call
   without tracing the cause is insufficient. Keep existing red/control proof and
   capture necessary new observations at a fresh path outside approved inputs.
2. **Verify the final implementation.** Use the reusable environment and exact
   commands in the testing policy. Map existing coverage first, add meaningful
   regression coverage test-first, and run affected caller/fixture checks. Complete
   required final-source full-suite, strict type, lint, format and whitespace gates.
   Packaging/installed checks follow the policy and concrete affected behavior.
   Identify actual source/test revisions and relevant dirty changes for every result.
   Prepare scoped committed review inputs where the selected workflow requires
   them, preserving unrelated work and attributing preexisting edits accurately.
3. **Renew independent review and finding status.** Follow the review contract's
   exact-source repair verification and whole-scope review requirements. Retain
   fresh original Spec and Standards reports separately. Obtain the required
   fresh High cumulative Standards assessment over the complete affected workflow,
   including all package Python files and unchanged collaborators. Retain the
   fixed cumulative baseline, current instructions, inspected/omitted scope and
   prior full finding keys. Append disposition/revalidation events; preserve earlier
   originals. Worker claims or tests alone do not establish `fixed`.
4. **Prepare current candidate QA.** Once findings and required review gates pass,
   follow the [M1 QA requirements](milestones.md#m1-a-complete-qa-controlled-git-cycle).
   Use the [current evidence navigation](evidence/README.md#m1-qa-navigation-after-organization)
   alongside the [historical QA guide](evidence/m1-qa-01/qa-guide.md). Prepare fresh
   candidate/request identities and required behavior observations. The former
   disposable M1 demonstration environment is absent at its recorded `/tmp` path;
   retained requests/checkpoints describe historical observations, not a live
   resumable run or acceptance of repaired source. Do not recreate approval from
   those artifacts or resume a run just to inspect it.
5. **Finish at the human boundary.** Preserve completed code/documentation review
   as such; explain any repair changes requiring additional human inspection.
   Present the exact tested candidate and remaining planned human actions. Only
   actual request-specific human acceptance can close M1 and permit authorized
   promotion/progression under ADR-0002. Update mutable status/navigation from
   verified facts and refresh the next handoff if acceptance remains pending.

The prior 559-pass result applies only to its recorded source. No checks,
independent repair verification or renewed cumulative assessment have been run
for an F1 repair in this conversation. Backend/context telemetry remains
unavailable unless the next session actually observes it.

## Evidence and navigation constraints

The preceding session organized ticket evidence and performed authorized selective,
lossy retirement. Read the [cleanup/organization decision and execution account](evidence-cleanup-and-organization-decisions.md)
and [human C1–C10 choices](evidence/evidence-retention-audit-01/retention-decisions.md).
Ticket READMEs are current navigation; historical originals can still contain
retired paths/hashes. Derived scenario/identity extracts are explicitly not original
captures. Do not rerun historical evidence writers or claim discarded output was
recovered by a new execution. The account also discloses missing original
documentation-audit bundles; do not invent replacement originals.

M1 bundles, caller-index proof, uncommitted correction snapshots, original review
judgments, all five calibration corpora and genuine compatibility examples were
preserved. Ticket 24's separate historical exit-120 capture remains unexplained
and retained; it is not automatically part of this repair's scope. The finite
[G2/C5 evaluation identity and limitations](../../.agents/skills/custom/evaluate-reviewers/SKILL.md#repository-evaluation-history)
do not substitute for current-source review or authorize another calibration campaign.

Record useful results/code identity and necessary observations without rebuilding
every retired raw archive. Respect exact-byte/path dependencies of any actual
active or deliberately continuable run. This one-off archival did not implement
runtime retention, remove compatibility support or amend approved requirements.
No broad reset/staging, history rewrite, publishing or M2 implementation is part
of this handoff.

## Suggested skills

Call these skills through the available skill interface; if none exists, read
their listed `SKILL.md` and follow it directly:

- **diagnosing-bugs** — `.agents/skills/matt-pocock/diagnosing-bugs/SKILL.md`:
  establish the current routing cause and affected paths before repair.
- **tdd** and **test-strategy** — `.agents/skills/matt-pocock/tdd/SKILL.md` and
  `.agents/skills/custom/test-strategy/SKILL.md`: meaningful public-seam regression,
  required checks and deliberate evidence capture.
- **code-review** — `.agents/skills/matt-pocock/code-review/SKILL.md`: fresh separate
  whole-scope axes with the correct committed input and supplied repair baseline.
- **review-architecture** — `.agents/skills/custom/review-architecture/SKILL.md`:
  required current-source cumulative assessment under the development contract;
  an HTML report is optional, not a replacement for substantive source review.
- **create-next-agent-prompt** — `.agents/skills/custom/create-next-agent-prompt/SKILL.md`:
  refresh the eventual QA/status handoff after actual results and eligibility checks.

Development role settings remain GPT-6.1 Sol Medium for implementation/repair,
fresh independent High Spec/Standards and High cumulative Standards, with the
feature's advisory 250K active-context target. The human previously requested
delegated workers with the root as overseer/reviewer. The three Medium archival
workers did not perform the required repair or cumulative source reviews. Report
unavailable configuration honestly rather than claiming delivery/enforcement.
