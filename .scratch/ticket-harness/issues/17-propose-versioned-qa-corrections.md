# 17: Propose a versioned correction plan

**What to build:** Extend the unified planning flow for QA feedback: propose focused correction tickets and affected spec/milestone changes, show the changes from the approved version, and obtain targeted approval. Unchanged requirements retain their approval; prior versions and completed-ticket history remain intact.

**Blocked by:** [10: Turn one grilling session into an approved plan](10-produce-approved-harness-inputs-with-planning-skill.md); [16: Guide a human through milestone QA](16-guide-and-record-human-milestone-qa.md).

**Status:** ready-for-agent

**Milestone:** M2. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R08](../ticket-proposal.md#r08-propose-a-versioned-correction-plan).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [planning and milestone contract](../spec.md#planning-and-milestone-contract); [corrections and safe continuation](../spec.md#corrections-and-safe-continuation).

## Acceptance criteria

- [ ] Use the unified planning workflow to turn QA findings into focused correction-ticket and affected spec/milestone proposals.
- [ ] Show changes from the approved version, retain approval of unchanged requirements, and reopen targeted grilling for substantive unresolved decisions.
- [ ] Keep unapproved changes staged; publish only explicitly accepted amendments with a new plan version and stable IDs/history.
- [ ] Preserve prior snapshots, completed-ticket evidence, decisions, and the current milestone's gate on later work.
- [ ] Demonstrate feedback updating both the proposal and staged spec consistently. Runtime execution of amendments belongs to ticket 18.

## Verification

A QA feedback example produces a revised proposal, updates the staged spec consistently, leaves unapproved changes unpublished, and publishes only the accepted amendment. Runtime execution belongs to ticket 18.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.
