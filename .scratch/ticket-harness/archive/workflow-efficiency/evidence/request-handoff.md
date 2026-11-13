# Continue the development-workflow efficiency follow-up

Work in the same `agentic_template` repository selected in this session.
The user requested this handoff because context was filling up. Continue the
unfinished follow-up below; **do not start ticket 20**.

## Current user request

Reduce unnecessary agent/review churn while retaining accuracy, and put the
improvements into the automated development workflow. The user prefers plain
English and wants actual workflow routing, rather than an available skill that
ordinary ticket agents never reach.

Implementation is authorized. The user then asked to stop this session and use
`$handoff`. No approval to push, accept a milestone, launch a harness run, weaken
review/check requirements or choose a new hard spending limit was given.

## Starting point and completed prior work

The fixed starting HEAD for this follow-up is
`54acbaad0b101b9f1e13fd3d2e518eed1fd75fb5`. It is still HEAD; this follow-up has
**no commits yet**. The worktree was clean when this follow-up began.

Ticket 19 is completed. Use its existing artifacts instead of reconstructing the
long conversation: `.scratch/ticket-harness/evidence/19-completion.md` and
`.scratch/ticket-harness/reviews/ticket-19.md`. Its original reports, five corpus
versions, decisions and frozen evidence must remain unchanged. Production harness
code was unchanged by that ticket. `next_agent_prompt.md` correctly selects20.

The newly added `evaluate-reviewers` skill is for organizing reviewer-calibration
experiments, not ordinary ticket source review. The user first asked how it was
wired in, then requested a general per-ticket efficiency improvement. This new
follow-up addresses that distinction; do not rerun ticket19's calibration campaign.

## Uncommitted work to preserve and inspect

Read the actual diff and these files; their contents already carry the procedure,
so this handoff does not repeat it:

- New `docs/agents/development-efficiency.md` (currently untracked).
- Modified `.agents/skills/custom/implement-with-checkboxes/SKILL.md`.
- Modified `.agents/skills/custom/create-next-agent-prompt/SKILL.md`.
- Modified `.agents/skills/custom/evaluate-reviewers/SKILL.md`.
- Modified `.agents/skills/custom/test-strategy/SKILL.md`.
- Modified `.agents/skills/custom/references/planning.md`.
- Modified `next_agent_prompt.md`: only a preparation-procedure paragraph was
  inserted; the selected ticket, prerequisites, role settings and other content
  were preserved.

These changes target development skills/instructions. They do not implement
runtime scheduler enforcement, change approved ticket requirements or remove
fresh Spec/Standards reviews, final-source checks, repair bounds or human QA.
No new skill is being created in this follow-up.

The intended improvement is earlier local preparation and a complete diagnosis
before another expensive independent round. Required independent reviews remain
independent. Scope/resource limits cannot make incomplete work a pass. No fixed
numeric cap was invented because the user did not choose one.

## Validation already performed

After reading repository domain/testing/environment guidance, a read-only helper
was written to `/tmp/workflow-efficiency/check.py`. It is temporary and has not
been committed. Inspect it before use. It reads repository paths relative to its
configured root and is not a production test or judgment-quality evaluator.

Its one execution passed: all88 local links/anchors resolved; 6,912 existing paths
outside the permitted changes were protected; historical ticket19/runtime files
were unchanged; the handoff still selects20 and only adds preparation routing;
whitespace checks passed. The helper printed per-file SHA-256 identities. Its
stdout is in the preceding tool record, not yet saved as a durable validation log.

`.scratch/workflow-efficiency/evidence/` was created but is still empty.
No official skill validators have been run for this follow-up yet. No independent
review/forward-test assignments have been launched for it. No background command
is known to be running; inspect if the environment reports otherwise.

## Remaining work

1. Follow `AGENTS.md` and inspect/preserve the worktree. Read the new document and
   all affected skill/handoff routes. Check for accidental extra bureaucracy,
   duplicated rules, vague cost promises, weakened gates or a new mandatory
   calibration campaign for ordinary tickets. Keep this change narrow.
2. Apply standalone document/skill validation under `docs/agents/testing.md`:
   official validators for the four modified `SKILL.md` folders, links/routing,
   protected-source/identity and whitespace checks. Read the Python environment
   instructions before Python and use the reusable absolute environment.
   Arrange capture before verification. Production tests/packaging are unwarranted
   unless the scope actually changes. Avoid tests that merely match prose.
3. Obtain proportionate independent assessment of the changed workflow, using
   fresh separate Spec/Standards assignments if following the existing committed
   review workflow. The intended review baseline is the HEAD above, not ticket19's
   historical baseline. Commit source before invoking committed-diff code-review.
   Keep review context focused on this small follow-up and relevant contracts;
   link prior canonical evidence without replaying the completed19 campaign.
4. Meaningful authoring forward-validation can use a few realistic decisions:
   failed local checks/missing capture before dispatch; one blocking axis while
   its sibling is still running; a complete rejection with a related failure path;
   a repeated failure pattern; changed-code versus prose-only evidence reuse.
   Give an independent evaluator the actual instructions/scenario facts, not a
   scripted expected answer. This is workflow validation, not another large
   reviewer benchmark. Preserve any failure and fix it locally before resubmission.
5. Preserve original findings/records and exact-source independence. The later
   efficiency instructions are not retroactively validated by ticket19's frozen
   G2/C5 results. Record this follow-up's actual checks/review separately.
6. Finish the authorized workflow update and its current ticket20 handoff pointer,
   commit only its changes, and report what changed and actual validation limits.
   Ticket19 stays closed and ticket20 is not begun. The user wants reduced wasted
   work, not a promise that unmeasured future tickets will always run faster.

## Suggested skills

Call the Skill tool where available; otherwise read the listed local source:

- `writing-for-agents` — `.agents/skills/matt-pocock/writing-for-agents/SKILL.md`;
  also read its skill-mechanics reference when needed.
- `skill-creator` — installed system skill; validate the existing custom-skill edits.
- `test-strategy` — `.agents/skills/custom/test-strategy/SKILL.md` for proportionate
  standalone verification without removing required checks.
- `code-review` — `.agents/skills/matt-pocock/code-review/SKILL.md` if obtaining the
  separate committed-source axes. Preserve shared ownership/review-record rules.

Read `implement-with-checkboxes` as the edited workflow and source of existing
ticket gates; this follow-up is not an assignment to implement ticket20. Do not
invoke `evaluate-reviewers` to launch another calibration just to validate these
preparation instructions. If regenerating the handoff rather than retaining its
small routing edit, apply `create-next-agent-prompt` and recheck eligibility.

## Communication

Explain the result plainly. Distinguish stronger agent instructions from executable
runtime enforcement, and observed checks from measured speed improvement. The
previous session promised to preserve fresh independent reviewers, required
checks and human boundaries while moving cheap discovery earlier.
