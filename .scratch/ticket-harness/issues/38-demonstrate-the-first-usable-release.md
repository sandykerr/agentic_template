# 38: Demonstrate the revised first usable release

**What to build:** Expand pre-QA ticket 16's clean-checkout acceptance to planning, background operation, two QA milestones, corrections, safe checkpoint continuation, exact local promotions, blocked/waiting work, optional findings, selected guidance, and actual Codex/access evidence. Clearly document deferred concurrency, arbitrary crash recovery, hosted PRs/GitHub checks, and email.

**Blocked by:** [11: Stop development handoffs at human checkpoints](11-stop-development-handoffs-at-qa-milestones.md); [28: Operate the orchestrator in the background](28-operate-the-harness-in-the-background.md); [29: Continue independent work inside the current milestone](29-continue-independent-work-after-blocks.md); [36: Verify runtime write and approval boundaries](36-verify-role-write-boundaries.md); [37: Run a generated approved plan through the runtime](37-run-a-generated-plan-through-the-runtime.md); [07: Report optional review suggestions without rework](07-report-optional-suggestions-without-repair.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](../spec.md).

**Milestone:** M4. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R19](../ticket-proposal.md#r19-demonstrate-the-revised-first-usable-release).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](../spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [testing decisions](../spec.md#testing-decisions); [out of scope](../spec.md#out-of-scope).

**Review amendment:** Inherit [review records](../spec.md#review-work-findings-and-decisions), [runtime adoption](../spec.md#runtime-review-adoption) and [architecture checkpoints](../spec.md#cumulative-architecture-checkpoints).

## Acceptance criteria

- [ ] Document installation, actual CLI/background/foreground/status/log/stop/continue interfaces, role settings, limits, requirements, skill selections and artifact/decision inspection.
- [ ] Provide a clean-checkout disposable example covering two milestones, planned QA waits, explicit approval, correction-plan amendment, safe continuation and exact feature-to-dev promotion.
- [ ] Retain repaired/blocked/dependent/unrelated/optional-finding examples and final feature acceptance without bypassing any QA boundary.
- [ ] Run the complete deterministic suite and required static/packaging/installed CLI checks without routine model credentials or network access.
- [ ] Retain actual small Codex/skill/access evidence or report its blocker; show immutable approved inputs and exact candidate-bound branch advancement.
- [ ] Clearly separate sequential operation and planned-QA continuation from deferred concurrency, arbitrary crash recovery, hosted PR/GitHub checks, and email. Context experiment 35 is prioritized separately, not a release gate.

- [ ] The final walkthrough includes navigable review work, immutable reports, a concern-to-human-decision-to-change-to-verification history, cumulative architecture assessment and unresolved-finding visibility across stop/continue; human final acceptance remains separate.

## Verification

Run the existing required complete suite and packaging/installed CLI checks, follow the documented disposable-repository walkthrough, and retain actual live evidence or its explicit blocker. Ticket 35 is scheduled early but is not a prerequisite for release acceptance.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.

## Comments

### QA realignment

Reconciled with approved slice R19; the [previous definition](../archive/issues-before-milestone-qa/16-demonstrate-the-first-usable-release.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.
