Use $implement-with-checkboxes to implement only:

.scratch/ticket-harness/issues/10-produce-approved-harness-inputs-with-planning-skill.md

# Ticket 10: Turn one grilling session into an approved plan

This is current QA-first ticket 10 (formerly QA-first ticket 15); its archived pre-QA definition remains historical. The human approved the plan. Tickets 01–09 are complete; their implementation is the foundation, not work to repeat. The current milestone is M1: prove the scripted Git/QA vertical slice before background operation, real Codex roles, or release completion.

Read AGENTS.md, .scratch/ticket-harness/README.md, .scratch/ticket-harness/milestones.md, and the assigned ticket. Use these scoped requirements:

- .scratch/ticket-harness/spec.md#planning-and-milestone-contract
- .scratch/ticket-harness/spec.md#custom-skills-and-design-policy
- .scratch/ticket-harness/ticket-proposal.md#r01-turn-one-grilling-session-into-an-approved-plan
- GLOSSARY.md and the relevant ADRs under docs/adr/.

Use GPT-6.1 Sol with the ticket's Medium worker default and separate fresh High Spec/Standards review assignments. Keep each agent within the 250K active-context target. Runtime model/profile execution is a later ticket; do not claim this planning skill implements it.

Capture your own starting HEAD as the fixed review baseline and inspect the worktree before editing. Preserve preexisting planning/publication changes and unrelated work; stage only your implementation and separately owned bookkeeping. Read ticket 09's completion evidence and recorded implementation 7f4eac0 to verify the prerequisite. Its historical 469 passing tests do not verify your new work. Do not replace your starting baseline with that historical commit.

Implement the six acceptance criteria in ticket 10:

- One custom user-facing workflow reuses grilling, domain modeling, spec synthesis, and vertical-ticket/dependency principles without editing upstream skills.
- Grilling explicitly covers milestone/QA decisions; confirm shared understanding, draft a spec and proposal, revise both together, and reopen targeted grilling for consequential new decisions.
- Publish individual tickets, spec, milestones and index only after explicit approval of the coherent bundle; unapproved proposals remain unpublished.
- Always include final QA; propose meaningful earlier milestones or honor an every-N request with explicit dependency-consistent membership and a smaller final group.
- Record worker/reviewer defaults, ticket worker overrides, agreed testing seams, QA actions and acceptance conditions through one shared planning reference.
- Validate isolated examples including feedback changing the spec and withheld publication. Generated-bundle runtime/skill-selection proof is ticket 27.

Follow the existing writing-for-agents and skill-creator guidance. Reuse local upstream procedures by reading their instructions when a Skill tool is unavailable. Keep detailed planning policy in one reference. Preserve proposed revisions separately from existing approved inputs until accepted.

The ticket is planning behavior and skill authoring. Read docs/agents/python-environment.md before Python/checks and docs/agents/testing.md before selecting verification. Validate skill frontmatter, links, routing, approval boundaries, complete output shapes, and realistic isolated planning examples. Use the approved public CLI/scripted-process/real-Git seam if executable runtime behavior changes; new seams require the established agreement. Do not manufacture runtime changes or a full-suite replay for prose alone. Preserve any required checks justified by actual executable changes. Record actual commands, exits, sources and artifacts rather than claiming intended examples ran.

Do not implement milestone scheduling, branch promotion, approval watching, safe restart, QA execution, background launch, role skill capture, or live Codex. Those remain owning tickets within the published plan.

After appropriate checks pass, create a checkpoint commit containing only your implementation before $code-review. Supply the original fixed baseline, ticket and scoped requirements explicitly. Obtain separate fresh Spec and Standards reviews; scripted fixture reviews do not substitute. Fix blocking findings, rerun affected required checks, commit fixes, and re-review changed code. Record optional suggestions separately.

After verified implementation and reviews, follow docs/agents/issue-tracker.md completion bookkeeping: check only verified criteria, set Status: completed only when all gates pass, preserve Blocked by as history, record previous readiness, per-criterion evidence, actual checks, implementation/review commits, review outcomes and unresolved items. Link evidence from the feature index and commit only this ticket's bookkeeping separately.

Then follow $create-next-agent-prompt without launching another ticket. Honor the explicit milestone order in the feature index: after 10, prefer ready M1 ticket 11, then the remaining prerequisite-ready M1 tickets 12–15 in order. After all M1 work completes, generate a QA handoff/waiting status; do not assign M2 before human acceptance. Preserve the explicit early priority of 25 immediately after verified 24 under its separate E1 plan. Commit the generated handoff separately as the implementation wrapper requires.

Do not push or modify approved inputs belonging to an active run. Report implementation/bookkeeping/handoff commits, actual checks and independent review outcomes, unchecked criteria, and next handoff eligibility. Do not claim feature or milestone acceptance from completion of this ticket.
