# Ticket 16 implementation evidence

Implementation assignment: fresh GPT-6.1 Sol Medium, context target 250K, fixed
starting baseline `eae64ae6bce4f96aa0e2e7a3d5f63e8aba93da87`, initially clean
worktree. Implements only the development record contract/templates/navigation
for [ticket 16](../issues/16-record-review-work-findings-and-decisions.md).
This report is implementation evidence, not completion bookkeeping, an independent
implementation review or human QA acceptance.

## Outcome and scope

The authoritative [record contract](../../../docs/agents/review-records.md) and
four linked templates define assessment identity, immutable reports, compound
finding keys, append-only dispositions, human decisions and source revalidation.
Existing implementation/handoff wrappers, feature index and tracker/harness documentation route
to it. The [feature review index](../reviews/README.md) provides a home for actual
future assessments without inventing one. No upstream skill, runtime, report wire
format, tests, dependency or approved requirement changes are included.

Prerequisites 10/11 retain their [completion evidence](10-completion.md) and
[completion evidence](11-completion.md), original checks and independent reviews.
Their implementation/bookkeeping commits are ancestors of the starting baseline.
Their historical checks establish prerequisites, not verification of this change.
The older handoff's uncommitted-publication warning is historical: starting
`git status --short` was empty. No active run was launched or active captured input
was edited. The helper checks preserved issue/archive hashes and runtime/upstream
diffs against the baseline.

## Coverage map and verification choice

The [testing policy](../../../docs/agents/testing.md) standalone documentation/skill
row and test-strategy apply. Existing runtime tests cover runtime behavior, not
this authoring contract; replaying them would not validate the new Markdown
records. Prior ticket 10/11 document/workflow checks supply the method, not new
check results. No runtime behavior tests or new testing seam were added.

| Criterion | Final-source validation and distinct failure detected |
| --- | --- |
| 1: one identified assessment, ticket/cross-ticket scopes | Contract/assessment template; miniature ticket-01 combines Spec/Standards, architecture-MX is separately planned. Scope, exact source, assignments/instructions, reports and omitted work are present. Prevents review IDs becoming implementation tickets/readiness or cross-ticket work being hidden in a ticket report. |
| 2: immutable snapshots, compound keys, append-only history | Saved report/source/verification manifest; before/after snapshot hashes; prefix checks on every appended history event. Spec-01/F1, Standards-01/F1 and Standards-02/F1 retain distinct keys; later report links its prior concern. Detects snapshot rewriting, lost history and ID collisions. |
| 3: all dispositions and exact independent verification | E01/E02 open; E03/E04 fixed B using a separate synthetic verifier process; E05 relevant independent revalidation at C; E06 deferred; E07 awaiting; E08 accepted; E09 reopened blocking concern at C. Completed assessment still carries blocker/deferred work. Detects worker-only fix assertions, stale B verification applied to C, and completed-review labels hiding findings. |
| 4: human authority and separate QA | Human decision template and synthetic risk decision expose attribution, reason, scope and amendment necessity; E07/E08 keep proposal and decision distinct. Contract preserves blocker classification/required amendment, ownership/scope decisions and separate exact-candidate QA. MX remains unrequested/unaccepted. Detects agent risk acceptance or disposition becoming integration/promotion authority. |
| 5: navigable six histories | Miniature README's six-case table links originating ticket/milestone → concern/evidence → event/decision → repair/follow-up → actual disposable Git commit/snapshot → exact verification → pending MX assessment. All saved Markdown links/anchors resolve. Detects orphan evidence, broken return paths and fabricated eventual assessment results. |
| 6: tracker context and lifecycle/input preservation | Feature review index, tracker and wrapper routing; fixture ticket readiness is unchanged by completed/planned review lifecycles; original reports remain immutable. Contract routes during-run artifacts to harness-owned output and post-run links outside active input immutability. Protected source hashes/HEAD and unchanged runtime/upstream checks support the isolated execution. |

## Retained execution evidence

- [Runner](16-run-checks.sh) and [helper source](16-check.py): documented reusable
  Python environment; official skill-creator validation of both modified skills,
  actual source identities, local file/anchor traversal, whitespace/conflict checks,
  isolated Git fixture and preserved reports/history. Runner appends exact commands,
  exits and raw output to [check log](16-checks.log), including any failed attempts.
- [Build results](16-build-results.json): actual temporary Git commands/results,
  full source revisions, before/after immutable hashes, append event observations,
  final guidance hashes and saved-file identities.
- [Saved-artifact final check](16-check-results.json): independently rereads saved
  documents/records, validates identities and navigation against actual final
  guidance/helper/report sources. This is mechanical verification, not a second
  reviewer assignment.
- [Miniature tracker](16-miniature/README.md): actual Markdown outputs and external
  [report/source digest manifest](16-miniature/manifest.json). The synthetic source
  has real disposable Git commits retained with command output and source snapshots.

The fixture's reviewer reports and human risk statement are explicitly synthetic.
Independent mechanical verifier subprocesses establish the demo's exact-source
observation only; they cannot establish actual reviewer independence, judgment,
model delivery or calibration. No real human risk, milestone acceptance, runtime
enforcement, candidate preparation or promotion is claimed. Required independent
Spec/Standards reviews of the implementation remain with the parent workflow.

## Workflow observations

Source inspection confirms implementation review preparation reads the contract
before saving reports/handling repairs, and handoff context carries full finding
keys, decisions and pending revalidation. Report/history templates link directly
to that same contract rather than copying its authority rules into every skill.
Placeholders in templates are intentional authoring instructions, rendered as
text rather than live broken links; only the completed miniature records assert
example identities. The actual evidence chain explicitly records absent cumulative
assessment/QA instead of fabricating acceptance.

Record maintenance does not enforce runtime gates. Tickets 17–19 own broader
review scope, architecture gating and actual reviewer evaluation; 33 owns runtime
adoption. Parent bookkeeping will link actual fresh implementation reviews using
these templates after the implementation checkpoint; it must retain the original
baseline and preserve any unresolved findings. Ticket 16's acceptance/status and
the generated next-agent handoff are deliberately untouched by this implementation.

## Validation iterations

The first helper attempts exposed its own navigation-audit limitations: it
treated fenced and inline illustrative Markdown in existing harness guidance as
real links, then reached the check-result link before creating that result file.
The final checker excludes code examples and creates an explicitly in-progress
result destination before validating links. Adding the feature-index audit also
exposed valid directory navigation, which the checker now accepts alongside file
links while requiring fragment destinations to be files. Raw failure commands/exits remain in
the append-only check log. The [initial fixture archive](16-initial-fixture.tar.gz)
preserves the first discarded generated tracker; the
[pre-final fixture archive](16-pre-final-fixture.tar.gz) preserves the subsequent
saved-artifact validation example before final feature-index navigation was added.
These archives are historical attempts, not the final example or current source.
The [directory-link audit fixture](16-link-audit-fixture.tar.gz) retains that
last generated example before the checker accepted valid directory destinations.
The final build and saved-artifact checks use the retained current helper and
current guidance, with identities in their respective result files. No old
passing result is relabelled as a check of changed source.

The initial staged whitespace check caught trailing spaces in the runner's
command-label formatting. The runner now prints arguments without trailing
spaces. The displayed check log normalizes only those trailing blanks; its
[original bytes](16-original-command-log.gz) and the
[initial whitespace diagnostics](16-initial-staged-whitespace.log.gz) remain
retained as compressed raw evidence. Subsequent checks use the final runner.
