# 18: Execute approved QA corrections

**What to build:** Accept an approved amendment at the QA boundary without editing captured prior inputs. Run its corrections through existing ticket gates inside the current milestone, retain version/evidence lineage, prepare a fresh candidate, and require renewed QA. Later groups remain gated.

**Blocked by:** [15: Continue after a deliberate QA stop](15-continue-from-a-planned-qa-checkpoint.md); [17: Propose a versioned correction plan](17-propose-versioned-qa-corrections.md).

**Status:** ready-for-agent

**Milestone:** M2. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R09](../ticket-proposal.md#r09-execute-approved-qa-corrections).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [corrections and safe continuation](../spec.md#corrections-and-safe-continuation); [independent checks and exact revisions](../spec.md#independent-checks-and-exact-revisions).

## Acceptance criteria

- [ ] Accept an explicitly approved versioned amendment at the current QA boundary without editing captured prior inputs or executing unapproved corrections.
- [ ] Execute correction tickets through fresh implementation/repair assignments, independent checks, both reviews, and exact feature-candidate gates.
- [ ] Retain plan-version lineage, prior Done history, rejected evidence, and the distinction between QA corrections and bounded in-assignment repairs.
- [ ] Prepare a fresh dev candidate and require renewed human acceptance; old approval cannot accept changed source and later groups remain gated.
- [ ] Demonstrate QA rejection, targeted amendment approval, correction, renewed QA, and continuation through the scripted public seam.

## Verification

A scripted QA rejection leads to an approved correction, a new candidate and decision, then continuation. Old approval cannot accept the corrected revision; an unapproved amendment cannot run.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.
