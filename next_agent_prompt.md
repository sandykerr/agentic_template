Use $implement-with-checkboxes to implement only:

.scratch/ticket-harness/issues/11-stop-development-handoffs-at-qa-milestones.md

# Ticket 11: Stop development handoffs at human checkpoints

The human approved the QA-first plan. Tickets 01–10 are verified complete; implement only ticket 11 within the current M1 milestone. Plan approval and ticket completion do not accept M1. The milestone runtime, promotion, QA-session execution and later release work remain separate tickets.

Read AGENTS.md, .scratch/ticket-harness/README.md, .scratch/ticket-harness/milestones.md, and the assigned ticket. Use these scoped requirements:

- .scratch/ticket-harness/spec.md#planning-and-milestone-contract
- .scratch/ticket-harness/spec.md#agent-contracts-and-access
- .scratch/ticket-harness/ticket-proposal.md#r02-stop-development-handoffs-at-human-checkpoints
- .agents/skills/custom/references/planning.md, the authoritative custom planning reference for membership, defaults, overrides and approval boundaries.
- GLOSSARY.md and relevant ADRs under docs/adr/.

Use GPT-6.1 Sol with Medium worker/repair reasoning unless the ticket explicitly overrides it. Use separate fresh High Spec and Standards review assignments, independently configured. Keep each assignment within the 250K active-context target. These are development assignment settings; do not claim runtime model/profile enforcement or skill capture exists.

Capture your own starting HEAD as the fixed review baseline and inspect the worktree before editing. Ticket 10's implementation is `70a0122`, bookkeeping `fe036e3`; verify its six checked criteria, independent reviews and actual checks from .scratch/ticket-harness/evidence/10-completion.md, .scratch/ticket-harness/evidence/10-checks.log and .scratch/ticket-harness/evidence/10-planning-observations.json. Historical commits are prerequisite evidence, not replacements for your own starting baseline or verification. Its examples initially read pre-numbering text, then received recorded final-source conformance audits; preserve that provenance. Ticket 09's historical 469 tests do not verify new work.

An unrelated concurrent edit to docs/agents/issue-tracker.md was left unstaged when this handoff was generated. Inspect and preserve it, along with any newer unrelated changes. The ticket-10 skill/reference include the current sequential preferred-order numbering guidance and were reviewed at `70a0122`. Stage only your implementation and separately owned bookkeeping.

Implement all six acceptance criteria by updating the two existing development wrappers:

- Preserve evidence-backed checkbox/status reconciliation, the checkpoint commit before review, separate fresh Spec/Standards reviews, and distinct implementation/bookkeeping/handoff commits.
- Select the earliest eligible milestone and genuinely prerequisite-ready work in the approved plan order. An older lower-numbered ticket cannot bypass that order or human QA gates.
- Generate an implementation handoff for eligible work, or a QA handoff/explicit waiting status at a checkpoint. All tickets Done while final QA remains unaccepted is not feature completion.
- Carry Medium worker/repair defaults, explicit ticket overrides and independently configured High reviewer defaults. Include exact QA request, candidate and artifact references when available; report missing references without fabricating them or inventing approvals.
- Reuse testing policy for focused development checks and required completion checks. Keep orchestration, promotion and approval authority outside worker guidance; a generated handoff does not launch work.
- Demonstrate isolated normal-next-ticket, waiting-milestone and awaiting-final-QA handoffs. Retain actual inputs, outputs, commands/exits and source identities.

Use .agents/skills/custom/implement-with-checkboxes/SKILL.md and .agents/skills/custom/create-next-agent-prompt/SKILL.md as the implementation targets. Reuse the shared planning reference for detailed policy rather than copying it into both wrappers. Read writing-for-agents and skill-creator guidance when changing these skills; preserve upstream files and existing completion gates. Read local skill instructions directly when Skill tooling is unavailable.

This ticket is development guidance and handoff behavior. Do not implement runtime milestone scheduling (12), feature-to-dev candidate preparation/promotion (13–14), checkpoint continuation (15), QA-session execution, correction execution, background launch, live Codex, role skill capture, or release completion. In examples distinguish development milestone gates from target-repository runtime QA. Read docs/agents/python-environment.md before Python/dependencies/checks and docs/agents/testing.md before choosing verification. Validate skill frontmatter, local links/anchors, routing, approval boundaries and actual isolated outputs. Preserve appropriate standalone documentation verification without manufacturing runtime changes or a full-suite replay for prose alone. If executable behavior changes, preserve required tests/checks and use the approved public CLI seam with scripted external processes and real temporary Git repositories; agree any new seam before adding tests. Use test-strategy and TDD for actual test/code changes at that seam, with planned evidence capture and the required final full suite.

After appropriate checks pass, checkpoint only your implementation before $code-review so the committed diff is visible. Explicitly supply the original fixed baseline, assigned ticket and scoped requirements. Obtain separate fresh High Spec and Standards reviews; scripted fixture reviewers cannot substitute. Fix blocking findings through fresh Medium repair assignments, rerun affected required checks, commit repairs and re-review the whole implementation against the original baseline. Record optional suggestions separately.

After verified implementation and reviews, follow docs/agents/issue-tracker.md completion bookkeeping: check only proven criteria, set Status: completed only after all gates pass, preserve Blocked by as history, record previous readiness, criterion-specific evidence, actual checks, implementation/review commits and unresolved items. Link evidence from the feature index and commit only ticket 11's bookkeeping separately. Defer approved-input mutations belonging to an active run; preserve snapshots and execution records. Missing verification leaves criteria unchecked and completion pending.

Then follow $create-next-agent-prompt without launching another ticket. Honor the published M1 order: after 11, select prerequisite-ready 12, then 13–15 in order. When all M1 tickets are complete, generate a QA handoff or waiting status; do not assign M2 before recorded human acceptance. Preserve E1's separate priority for 25 immediately after verified 24. Commit the generated handoff separately as the implementation wrapper requires.

Do not push. Report implementation, bookkeeping and handoff commits, actual check results, separate independent review outcomes, unchecked criteria and the next handoff eligibility/path or exact blocker. Completing ticket 11 does not claim milestone or feature acceptance.
