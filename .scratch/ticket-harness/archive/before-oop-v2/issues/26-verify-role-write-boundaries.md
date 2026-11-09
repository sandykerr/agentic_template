> Historical approved-plan snapshot from `152b0c4577269789a419079c6261c69f9a0695fd`. Use the [current feature index](../../../README.md) for new work. Original identities and requirement text are retained; relative links are relocated for this archive. Exact pre-publication bytes are preserved in the [source snapshot](../source-snapshot.json).

# 26: Verify runtime write and approval boundaries

**What to build:** Retain pre-QA ticket 14's real sandbox probes and add QA decisions, dev, and feature refs to the protected authority checks. Implementers may edit assigned source; reviewers remain read-only; implementation/repair cannot authorize promotion. Do not silently widen permissions or treat a prompt instruction as proof of enforcement.

**Blocked by:** [16: Guide a human through milestone QA](16-guide-and-record-human-milestone-qa.md); [24: Complete the workflow with real Codex roles](24-run-a-real-codex-ticket-cycle.md).

**Status:** ready-for-agent

**Milestone:** M4. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R17](../ticket-proposal.md#r17-verify-runtime-write-and-approval-boundaries).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [agent contracts and access](../spec.md#agent-contracts-and-access); [feature to development promotion and human qa](../spec.md#feature-to-development-promotion-and-human-qa).

## Acceptance criteria

- [ ] Verify an implementer can edit only assigned source while reviewers have read-only source sufficient to produce their reports.
- [ ] Probe disposable sentinels for sibling source, approved inputs, authoritative records, QA decisions, and feature/development refs; refuse or detect out-of-scope effects before acceptance.
- [ ] Keep submission capture, both integration destinations, QA decision consumption and execution state under harness authority; implementation/repair cannot authorize acceptance.
- [ ] Reject assignments when required access/instruction guarantees cannot be established; do not silently widen permissions or substitute prompt claims for probes.
- [ ] Record actual backend/sandbox/file/ref observations while preserving caller work and approved inputs.

## Verification

Existing disposable sentinel probes plus QA/ref targets provide concrete access evidence without touching caller work. A failed access guarantee leaves verification incomplete.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.

## Comments

### QA realignment

Reconciled with approved slice R17; the [previous definition](../../issues-before-milestone-qa/14-verify-role-write-boundaries.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.
