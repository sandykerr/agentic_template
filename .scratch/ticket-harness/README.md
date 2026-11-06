# Ticket harness implementation

The [approved spec](spec.md) is implemented by the individual numbered [issues](issues/). This index is the current publication map. The [earlier seven-ticket proposal](ticket-proposal.md) remains planning history; use the numbered issues for execution.

All published issues use the configured ready-for-agent triage label. That label describes readiness; an issue with incomplete prerequisites is not on the executable frontier. Initially, only issue 01 is executable.

**Early experiment priority:** run issue 17 as soon as issue 13 is integrated, before proceeding to the final release walkthrough. Its stable identifier is retained; its dependency is 13, not 16. It can proceed independently of issues 14 and 15 and is separate from first-release completion requirements.

## First-release tickets

Select issues 01–16 for the first usable release. Each issue delivers a bounded observable extension of the existing cycle. The initial tracer bullet crosses the entire path with scripted processes; the complete release also requires real Codex execution and all remaining acceptance gates.

| Issue | Observable behavior | Blocked by |
| --- | --- | --- |
| [01](issues/01-complete-one-scripted-ticket-cycle.md) | Complete one scripted ticket through every gate | None |
| [02](issues/02-reject-invalid-inputs-before-execution.md) | Reject invalid requirements before starting work | 01 |
| [03](issues/03-validate-agent-reports-and-review-evidence.md) | Reject invalid agent reports and review evidence | 01 |
| [04](issues/04-promote-only-the-verified-candidate.md) | Promote only the exact verified candidate | 01 |
| [05](issues/05-repair-rejected-submissions-within-budget.md) | Repair rejected submissions within a bounded allowance | 03, 04 |
| [06](issues/06-surface-human-decisions-without-retrying.md) | Stop for decisions outside approved contracts | 05 |
| [07](issues/07-report-optional-suggestions-without-repair.md) | Report optional review suggestions without rework | 05 |
| [08](issues/08-stop-timed-out-process-trees.md) | Stop stalled assignments and check processes | 05 |
| [09](issues/09-execute-dependencies-sequentially.md) | Execute verified dependencies in a stable order | 02 |
| [10](issues/10-continue-independent-work-after-blocks.md) | Continue unrelated tickets after a blocked prerequisite | 06, 09 |
| [11](issues/11-supply-combined-design-guidance-to-standards-review.md) | Supply combined Python design guidance to Standards review | 03 |
| [12](issues/12-deliver-focused-implementation-and-spec-review-contexts.md) | Deliver focused implementation and Spec-review skills | 11 |
| [13](issues/13-run-a-real-codex-ticket-cycle.md) | Complete one real Codex ticket with configured role profiles | 08, 12 |
| [14](issues/14-verify-role-write-boundaries.md) | Verify implementation and review access boundaries | 13 |
| [15](issues/15-produce-approved-harness-inputs-with-planning-skill.md) | Produce executable Markdown requirements with a planning skill | 09, 11 |
| [16](issues/16-demonstrate-the-first-usable-release.md) | Demonstrate the first usable release from a clean checkout | 07, 10, 14, 15 |

Dependencies express actual required behavior/contracts, not preferred work order. Several implementation branches can become ready together, although the harness's first version still executes target tickets sequentially.

## Agent context policy

- Use GPT-6.1 Sol as requested, with one fresh context for each implementation, review, or repair assignment.
- Target at most **250,000 tokens of active context per agent**, including instructions, relevant source, tool results, reasoning/output retained in context, and room to finish verification and the handoff.
- This is a per-agent context constraint, not a cumulative per-ticket usage budget. Reprocessing cached input across requests can make cumulative usage much larger than the currently occupied context.
- Read the assigned issue and its scoped spec references first. Follow the repository's glossary/ADR instructions, discover the affected source, and pull extra references when necessary. Sibling transcripts and entire upstream skill libraries are not default inputs.
- Keep headroom for debugging and final checks. If the bounded outcome will not fit, preserve useful work and report the evidence and proposed split before expanding the assignment.
- No numerical implementation-usage estimate is claimed before measurements exist. These slices are scoped by observable outcomes and the context required to understand them.
- The current local Codex catalog reports 500,000 nominal tokens and a 95% effective-window setting for gpt-6.1-sol; the inspected session reports a 475,000 effective window. The requested 8M figure was clarified to a 250K agent target after distinguishing cumulative usage from active context.
- The 250K target guides the agents implementing these issues. Configurable runtime context controls and empirical comparison belong to the early live-backend experiment below; this document does not claim that a new hard runtime cap has already been implemented.

## Worker handoff

Start from the latest integrated prerequisite work. Read the current interface and evidence needed for this issue rather than replaying prior development conversations. Work on this issue's acceptance behavior and test at the public CLI/Git/report seam described by the spec.

Return a compact report with the outcome, commit references/changed files, actual check commands and exit results, and remaining decisions or risks. Preserve verbose logs as artifacts and link to them when needed.

During approved harness execution, source specs and tickets remain unchanged and the harness owns execution records. A ready-for-agent label or published ticket alone does not start a run. Concurrency, interrupted-run recovery, and email notification remain deferred.

## Original proposal coverage

| Original proposal | Focused published issues |
| --- | --- |
| 01: Scripted full cycle | 01–04 |
| 02: Bounded repairs | 05–07 |
| 03: Stalled/unreliable stages | 03, 08 |
| 04: Dependency scheduling | 09–10 |
| 05: Live Codex and design/review skills | 11–14 |
| 06: Custom planning | 15 |
| 07: Release demonstration | 16 |

## Early context-budget experiment

[17: Compare configurable 100K–250K agent context limits](issues/17-compare-configurable-agent-context-limits.md) is ready for execution immediately after issue 13 supplies the verified real Codex cycle, configured roles, and usage artifacts. Prioritize it then; it does not require the final release demonstration, multi-ticket scheduling, the planning skill, or the later access-boundary probes. It is a separate early experiment, not an additional first-release completion gate.

The user requested configurable per-agent limits of **100K, 150K, 200K, and 250K**. Compare the same workload, model, role reasoning settings, and acceptance checks at each setting. Record verified results, repair behavior, observed active context, compaction/handoff behavior, elapsed time, and cumulative/cached usage separately.

Use a short control to verify configuration and reporting, plus a task-relevant case that can approach the configured context thresholds. If all runs remain below 100K, they cannot establish the comparative effects of the larger budgets.

Verify whether the installed backend enforces a hard limit, applies a compaction threshold, or only supports advisory guidance. Report that distinction explicitly rather than interpreting cumulative input totals as window occupancy or claiming unsupported enforcement.

## Completion evidence

- [01: Complete one scripted ticket through every gate — completed](evidence/01-completion.md): implementation `b09e324`, final implementation `1666920`; 8 passing tests and passing checks; separate independent Spec and Standards reviews completed. [Actual fixture observations](evidence/01-fixture-observations.json) and the [ticket completion comment](issues/01-complete-one-scripted-ticket-cycle.md#comments) record the passing and rejected runs. Later tickets and first-release completion remain outstanding.

- [02: Reject invalid requirements before starting work — completed](evidence/02-completion.md): checkpoint `855a4c8`, review fixes `dfdb1a6` and final implementation `b11fd20`; 73 passing tests and passing checks; separate fresh Spec and Standards reviews passed. [Actual CLI/Git observations](evidence/02-fixture-observations.json) and the [ticket completion comment](issues/02-reject-invalid-inputs-before-execution.md#comments) provide criterion-specific evidence. Eligibility validation is complete; dependency scheduling and later-ticket features remain outstanding.

- [03: Reject invalid agent reports and review evidence — completed](evidence/03-completion.md): checkpoint `5b04187`, review fixes `2a27565` and final implementation `07094fa`; 256 passing tests and passing documented checks; independent Spec and Standards reviews passed with no remaining findings. [Actual CLI/Git observations](evidence/03-fixture-observations.json) and the [ticket completion comment](issues/03-validate-agent-reports-and-review-evidence.md#comments) verify all six criteria. Report validation is complete; transaction hardening, repairs, broader human-decision handling, and later-ticket features remain outstanding.
