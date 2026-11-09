# OOP amendment numbering and publication map

**Draft — unapproved. Plan version:** oop-v1.

The human explicitly requested that new OOP work be inserted as 16–18 and existing published open tickets shift to keep execution order sequential. Completed 01–15 and historical evidence keep their IDs. Existing stable R01–R19 slice identifiers stay unchanged; O01–O03 identify only the added refactor slices.

| Previous published ID | Proposed ID | Slice | Title |
| --- | --- | --- | --- |
| New | 16 | O01 | [16: Own implementation-attempt transitions](ticket-proposal.md#16-own-implementation-attempt-transitions) |
| New | 17 | O02 | [17: Own ticket execution and bounded repairs](ticket-proposal.md#17-own-ticket-execution-and-bounded-repairs) |
| New | 18 | O03 | [18: Own milestone review and checkpoint continuation](ticket-proposal.md#18-own-milestone-review-and-checkpoint-continuation) |
| 16 | 19 | R07 | [19: Guide a human through milestone QA](ticket-proposal.md#19-guide-a-human-through-milestone-qa) |
| 17 | 20 | R08 | [20: Propose a versioned correction plan](ticket-proposal.md#20-propose-a-versioned-correction-plan) |
| 18 | 21 | R09 | [21: Execute approved QA corrections](ticket-proposal.md#21-execute-approved-qa-corrections) |
| 19 | 22 | R10 | [22: Operate the orchestrator in the background](ticket-proposal.md#22-operate-the-orchestrator-in-the-background) |
| 20 | 23 | R11 | [23: Continue independent work inside the current milestone](ticket-proposal.md#23-continue-independent-work-inside-the-current-milestone) |
| 21 | 24 | R12 | [24: Supply coherent design guidance to Standards review](ticket-proposal.md#24-supply-coherent-design-guidance-to-standards-review) |
| 22 | 25 | R13 | [25: Capture and deliver selected local skills](ticket-proposal.md#25-capture-and-deliver-selected-local-skills) |
| 23 | 26 | R14 | [26: Deliver focused implementation and Spec contexts](ticket-proposal.md#26-deliver-focused-implementation-and-spec-contexts) |
| 24 | 27 | R15 | [27: Complete the workflow with real Codex roles](ticket-proposal.md#27-complete-the-workflow-with-real-codex-roles) |
| 25 | 28 | R16 | [28: Run the early context-budget comparison](ticket-proposal.md#28-run-the-early-context-budget-comparison) |
| 26 | 29 | R17 | [29: Verify runtime write and approval boundaries](ticket-proposal.md#29-verify-runtime-write-and-approval-boundaries) |
| 27 | 30 | R18 | [30: Run a generated approved plan through the runtime](ticket-proposal.md#30-run-a-generated-approved-plan-through-the-runtime) |
| 28 | 31 | R19 | [31: Demonstrate the revised first usable release](ticket-proposal.md#31-demonstrate-the-revised-first-usable-release) |

## Publication scope

After approval of the complete bundle, publish the revised spec, proposal, milestones and feature index, three new issues, renamed 13 open issues and their synchronized current references. Preserve the prior canonical documents and 13 open issue bodies under `archive/before-oop-v1/` with their original identities and a provenance note for source revision `152b0c4577269789a419079c6261c69f9a0695fd`. Add this numbering map without overwriting the previous numbering-history record. Update current owner pointers in historical navigation only; leave historical requirement text, completed-ticket bodies, evidence logs, captured run inputs and previous decisions unchanged.

Current references outside the feature's live authoring files, including a current execution handoff, must be checked at publication. Replace stale scheduling guidance with the new M1 scope or an explicit historical pointer. Do not rewrite historical or runtime identity claims merely because their numbers collide with new tickets.

The prior development plan had no explicit version identifier. `oop-v1` names this proposed amendment; it is not a retrospective version for old run inputs. The publication approval record must identify this exact draft bundle. Scope confirmation in this conversation is not approval of unseen ticket criteria.
