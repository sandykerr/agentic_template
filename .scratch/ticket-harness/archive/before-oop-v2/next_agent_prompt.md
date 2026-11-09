> Historical approved-plan snapshot from `152b0c4577269789a419079c6261c69f9a0695fd`. Use the [current feature index](../../README.md) for new work. Original identities and requirement text are retained; relative links are relocated for this archive. Exact pre-publication bytes are preserved in the [source snapshot](source-snapshot.json).

# Awaiting milestone QA — M1 preparation pending

Ticket 15 is fully verified and committed. M1's required implementation work is
complete. **M1 human QA has not been requested or accepted; M2 remains ineligible.**
This is a checkpoint handoff, not an executable ticket 16 assignment. Creating this
handoff launches no implementation, candidate preparation, harness run or QA session.

Follow `AGENTS.md`, [tracker conventions](../../../../docs/agents/issue-tracker.md),
[domain guidance](../../../../docs/agents/domain.md), [GLOSSARY](../../../../GLOSSARY.md), applicable
[ADRs](../../../../docs/adr), and the
[shared milestone/approval policy](../../../../.agents/skills/custom/references/planning.md#milestone-membership).
Preserve the worktree and capture the next session's starting HEAD before any
subsequently authorized work. The unrelated unstaged `docs/agents/issue-tracker.md`
edit remains, SHA-256
`3803de99e541e60d2e9f733d5c98b009a43e60a9584e3819adffc55eae0214ce`.

## Approved checkpoint and verified work

The approved plan is the canonical human-approved milestone-QA realignment in
[spec.md](spec.md),
[ticket-proposal.md](ticket-proposal.md),
[milestones.md](milestones.md), and the
[feature index](README.md). The development documents do not
supply a captured machine-readable runtime plan/version or a request-specific QA
acceptance. Fixture plan version `v1` is synthetic and is not a development run identity.

M1, **A complete QA-controlled Git cycle**, requires exactly tickets **10, 11, 12,
13, 14, 15** in the published order. Their verified completion records are:

- [10: Approved planning inputs](../../evidence/10-completion.md).
- [11: Development checkpoint handoffs](../../evidence/11-completion.md).
- [12: Current milestone execution](../../evidence/12-completion.md).
- [13: Tested feature-to-development candidate](../../evidence/13-completion.md).
- [14: Exact acceptance, promotion and next group](../../evidence/14-completion.md).
- [15: Planned QA stop and continuation](../../evidence/15-completion.md).

Ticket 15 implementation is `36ed3e72c278cf147c84ae9c282cd2899af23ad0`; final repair
and verified source is `d11f0bc60a2c11c40683e58581dffa10e36a91be`. Its completion
bookkeeping is `eb58804f275776f9cce8d3ebd2e3485b7928b0f6`.
The original review baseline was `90255aaf6faf9aedce18f7159093f5dbfde294b7`;
historical baselines are not a substitute for a future session's own starting HEAD.

All five ticket 15 criteria are verified. The renewed final suite passed **544 tests
in 910.17s**; strict mypy, Ruff lint/format, working/staged/committed whitespace,
pinned wheel, isolated install, and installed continuation/invalidation passed.
[Final source identity](../../evidence/15-repair1-final-source-identity.json),
[actual gates](../../evidence/15-repair1-check-results.json),
[123 retained scenarios](../../evidence/15-repair1-fixture-observations.json)
and [root audit](../../evidence/15-repair1-root-audit.json)
confirm current/committed source and retained evidence. Final fresh High
[Spec](../../evidence/15-review-spec.md) and
[Standards](../../evidence/15-review-standards.md) reviews each
found zero blockers and zero optional suggestions. STD15-01 was repaired by a fresh
Medium assignment and every required gate renewed. Initial 543-test results and
initial reviews remain historical. No ticket 15 blocker or unchecked criterion remains.

## Development QA inputs still missing

No development M1 runtime QA artifacts have been created. The following remain
explicitly unavailable:

| Required development QA identity | Current state |
| --- | --- |
| Run identity and separate run-output directory | Not created. |
| Runtime configuration, captured approved plan/version/approval and input snapshots | Not captured for development M1 QA. |
| Assessed source/feature revision and feature branch | Not recorded for QA; verified implementation above is available for preparation. |
| Development branch and expected development base | Not selected or recorded. |
| Exact tested milestone candidate and candidate worktree | Not prepared. |
| Candidate regression command/result/evidence | No development candidate gate executed. Automated implementation checks above remain separate. |
| Request ID, current/archived request paths and identity | No development `qa-request.json` exists. |
| Decision path, human observations and recorded decision | No development decision artifact or acceptance exists. |
| Promotion/continuation/checkpoint for this development assessment | Not executed or recorded. |

Paths and identities under `15-observations/` and the installed proof are
**scripted target-repository fixtures**. Their requests, candidates, gates and
synthetic decisions cannot fill these missing development references or accept M1.
No active development harness run using the approved inputs was identified at
completion. Recheck before any later input mutation; active-run approved inputs
and snapshots must remain immutable.

## Next responsible workflow and human checks

The next step belongs to separately authorized **M1 QA preparation and human
assessment**. Establish the missing development configuration/branches/output,
assessed source, exact tested candidate and request-specific evidence through the
applicable preparation workflow. Preserve candidate preparation, promotion,
continuation, QA-session execution and approval recording as separately authorized
operations. No such operation is authorized merely by this generated status file.

Use M1's [published human QA](milestones.md#m1-a-complete-qa-controlled-git-cycle):

1. Inspect the unified approved spec/proposal flow and this development handoff.
2. In an isolated disposable repository, demonstrate foreground scripted execution
   with two runtime milestones: first-group integration into feature, a tested
   feature-to-current-development candidate, observable indefinite QA waiting and
   later tickets still Pending at attempt zero.
3. Show stale acceptance leaves development unchanged. Stop deliberately at the
   first QA checkpoint using `stop RUN_DIRECTORY`; observe owner exit 2 and
   `stopped_at_qa`. Continue through a new foreground process, preserving Done work,
   baseline/artifacts/history, ownership serialization and stale-state rejection.
4. Record explicit matching acceptance from the human/QA session. Confirm only the
   exact tested candidate promotes and feature aligns before later work begins.
   Preserve consumed-decision history across any further planned stop. Confirm
   final acceptance alone completes the feature.

Setup/contracts are in [the public guide](../../../../docs/ticket-harness.md), including the
canonical runtime plan and exact decision schema. The disposable builders and
scenarios in [test_milestones.py](../../../../tests/test_milestones.py),
[test_qa_promotion.py](../../../../tests/test_qa_promotion.py), and
[test_continuation.py](../../../../tests/test_continuation.py) provide inspected setup examples;
automated execution is not the human's acceptance. Read
[Python environment guidance](../../../../docs/agents/python-environment.md) before Python and
[testing policy](../../../../docs/agents/testing.md) plus
[test-strategy](../../../../.agents/skills/custom/test-strategy/SKILL.md) for any verification work.

Record the actual assessed source/feature/development/candidate revisions,
plan/run/request identities, real gate output, observed human checks, findings and
explicit decision in request-specific evidence. The existing runtime decision
contract remains separate `qa-decision.json` with exactly
`{"decision":"APPROVED","request":<complete current qa-request.json object>}`,
matching JSON fields/types/values and rejecting duplicate/extra/stale/replayed
approval. The human/QA session owns it outside approved requirements and worker
worktrees. A worker cannot author its own acceptance. Changed inputs require
renewed candidate verification and human assessment; corrections need an approved
versioned amendment and renewed acceptance.

## Eligibility and boundaries

M2 tickets **16–20** remain gated by recorded human acceptance of M1. After that
acceptance, select prerequisite-ready work through the approved milestone order;
readiness alone does not satisfy a human checkpoint. QA-session/correction workflows
(16–18), background operation (19), independent progress (20), live Codex, runtime
role-skill capture, OS enforcement and release acceptance remain later slices.
Arbitrary mid-stage crash recovery remains excluded. Ticket completion and plan
approval do not accept M1 or complete the feature before final human QA.

Carry the approved development role settings into any later authorized assignment:
fresh GPT-6.1 Sol Medium implementation/repair, independently configured fresh High
Spec and High Standards; a ticket worker override changes implementation/repair
only. Inherit required project/scoped role guidance from the approved spec, including
custom test strategy/TDD and applicable combined design guidance. Report missing
configuration rather than guessing. Target 250K active context per assignment.
Development settings do not prove runtime profile enforcement or skill capture.
E1 ticket 25 retains its separate priority immediately after verified 24 and never
gates release acceptance. No push is authorized by this handoff.
