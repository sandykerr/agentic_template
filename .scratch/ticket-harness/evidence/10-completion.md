# Ticket 10 completion evidence

Implemented only [10: Turn one grilling session into an approved plan](../issues/10-produce-approved-harness-inputs-with-planning-skill.md).
Verified implementation: `70a01220dfac353ebea639ae85daac08d5eed8b2`.

## Starting state and scope

- Original fixed review baseline: `42053bd55c925b252e838e8794314ecb1047148e`; initial worktree clean. This baseline was retained through both independent reviews.
- Verified prerequisite 09 through [its completion evidence](09-completion.md), ticket/index reconciliation, and recorded implementation `7f4eac0`, which is an ancestor of the starting HEAD. Its historical 469 tests and reviews establish prerequisite provenance, not checks of this skill.
- Added [grill-to-tickets](../../../.agents/skills/custom/grill-to-tickets/SKILL.md) and [one shared planning reference](../../../.agents/skills/custom/references/planning.md). Upstream skills, runtime, tests, dependencies and packaging are unchanged. Existing custom planning/testing guidance and upstream grilling/domain/synthesis/slicing procedures are reused directly.
- Concurrent numbering guidance appeared in these new implementation files and `docs/agents/issue-tracker.md` during the session. The implementation guidance was retained, revalidated and reviewed. The separate tracker edit remains untouched and unstaged; it is not part of this ticket's commits.
- No active harness run using these approved inputs was found before bookkeeping. Isolated examples used their own synthetic inputs under `/tmp/ticket10-checks/`; no application, run, QA decision or branch promotion was executed.
- The implementation checkpoint preceded `$code-review`. Both reviewers independently assessed the complete original-baseline diff at `70a0122`; neither found a required repair. No implementation changes followed review.

## Criterion evidence and verification scope

The [actual check log](10-checks.log) records commands, exits, source hashes and independent reports. [Raw planning observations](10-planning-observations.json) retain both complete session records, original/revised drafts, published output contents, fixture guidance, helper sources and link observations.

| Criterion | Verified evidence |
| --- | --- |
| One custom user-facing workflow; upstream reuse without edits | The entrypoint reads the single shared reference and routes to local grilling, domain modeling, to-spec, to-tickets and test-strategy instructions, including direct reading when Skill tooling is unavailable. It overrides upstream immediate publication with bundle approval. The baseline diff confirms upstream files unchanged. |
| Grilling, confirmation, joint revision and targeted regrilling | The reference covers QA/milestone decisions, interfaces/invariants, testing seams and roles before confirmed synthesis. In the Taskbox session, feedback changed cutoff ordering; the evaluator requested confirmation using a concrete tie-order example, then updated the spec, ticket 03 criteria, verification coverage and M3 QA together. Both before/after drafts are retained. |
| Explicit coherent-bundle publication approval | Taskbox's explicit declined decision left five approved v1 files byte-identical and published no new issue or version. Reading-list input 3 explicitly approved the displayed spec, all five full ticket bodies, testing/role contracts and milestones at the isolated destination; only then were spec, proposal, five individual issues, milestones and index published. These are synthetic decisions, not approval of this feature's QA. |
| Final QA and capability/every-N milestones | The reference requires final cumulative acceptance, proposes capability checkpoints and validates membership/dependency consistency. Taskbox proposes meaningful dated-creation and filtering checkpoints. Reading-list honors every two tickets with fixed M1=01/02, M2=03/04, final M3=05, cumulative coverage of 01–05 and human acceptance gates. Edges are 01→02/03/04/05 and 03→04; none point to a later milestone. |
| Shared defaults, overrides, seams and QA contracts | The shared reference owns Medium worker/repair, independent High Spec/Standards defaults and explicit model/guidance/test/QA output fields. Reading-list ticket 04 inherits the agreed model but uses High for worker and repair; reviewer settings remain independent. All ticket outputs link the agreed public CLI/temp-file test contract; milestone actions and observable pass conditions are concrete. These documents record choices; runtime profile/skill execution is deferred. |
| Isolated examples and appropriate skill validation | Two fresh GPT-6.1 Sol Medium evaluating agents performed the synthetic sessions in separate temporary workspaces. Final skill validation, 14 source links/anchors, 199 example links/anchors, original-input hashes, complete published output shapes and fresh High reviews passed. No runtime compatibility claim is made; that remains ticket 27. |

Standalone skill/document verification applies under [testing policy](../../../docs/agents/testing.md). Existing CLI/Git tests cover runtime behavior and were not changed or replayed for this prose-only implementation. No tests, new testing seam, artificial red test, runtime schema or runtime capability was introduced.

### Source and example provenance

The examples initially loaded the pre-numbering text. Concurrent numbering additions were retained before checkpoint; both evaluators subsequently reread the entire current skill/reference, recorded their final hashes, and checked their actual artifacts against those numbering rules. These are subsequent conformance audits, not claims that original generation started with the final sources. New IDs/order, historical-ID preservation, dependencies and membership conform. Experiment placement, draft reorder/split renumbering and preserved-ID ordering exceptions were inspected as policy but not separately exercised.

Final committed SHA-256 values match the renewed static manifest:

- Skill: `137522347bce0b00eb94375bbb99dc44555585abb870b73b504eae6cf600a5bb`.
- Shared reference: `02bf9315a0e78afdf9766f689ffd1f7971f1f652d0e085489a6012fb1563aab2`.

## Actual checks

All Python used `/home/ajkerr1/development/agentic_template/.micromamba/envs/dev/bin/python` after reading environment guidance. No dependency installation or environment mutation occurred. Temporary verification helpers and their sources are retained in the observations; they do not become runtime helpers.

| Actual command/check | Result |
| --- | --- |
| `bash /tmp/ticket10-checks/static/run.sh` | Exit 0 for the final implementation: official `quick_validate.py`, 14 file/anchor links, both files' whitespace/conflict checks, empty upstream diff and source hashes. |
| `env PYTHONPATH=/usr/lib/python3/dist-packages` plus reusable Python and the official skill-creator `quick_validate.py .agents/skills/custom/grill-to-tickets` | Exit 0: `Skill is valid!`. The initial invocation lacked PyYAML; the final command uses the already installed system package for this tool only. |
| Reusable Python `/tmp/ticket10-checks/observe_examples.py` | Exit 0: original approved inputs unchanged; both draft documents revised; no new Taskbox issues/version; all five Reading-list issues plus four bundle documents present; new criteria unchecked; 199 local example links/anchors resolve. Complete observed files saved. |
| `sha256sum -c /tmp/ticket10-checks/feedback-before.sha256` | Exit 0: all five original approved Taskbox files unchanged. |
| Approved evaluator's `node .../approved-workspace/.planning-check.cjs` | Exit 0: nine published documents, 96 local references, valid graph/membership, consistent version/roles and unchecked criteria. Helper source and actual session observations retained. |
| `git diff --cached --check` before checkpoint; `git diff --check 42053bd...HEAD` at checkpoint; committed-source hash comparison | Exit 0; both committed files match the final manifest. |

The renewed static run initially exposed a bug in the temporary link checker: a same-file anchor was treated as a directory. Correcting that helper and rerunning the complete static sequence passed without altering implementation sources. Other initial diagnostics and final command provenance are recorded in the check artifacts. No failing required check remains.

## Standards

Fresh independent `/root/review_standards_10`, GPT-6.1 Sol High, reviewed `70a0122` against the original baseline:

> Blocking findings: 0. Optional findings: 0.
>
> No documented-standard violations in either file. The concise discoverable entrypoint routes to upstream procedures and the authoritative reference. The single reference owns detailed policy and output shapes, respects target-project guidance and approved-input boundaries, and separates plan approval from QA acceptance. No actionable Fowler smell was found.

The reviewer read applicable repository/domain/tracker/testing guidance, glossary/ADRs, skill-creator, writing-for-agents/mechanics and relevant upstream procedures. Independently reran the official validator, 14 links/anchors, whitespace, baseline/upstream diff and source checks; all passed. The full retained report is in the check log, including the example provenance limits.

## Spec

Separate fresh `/root/review_spec_10`, GPT-6.1 Sol High, reviewed the same revision and original-baseline diff:

> Findings: zero blockers; zero optional suggestions. No missing/partial scoped requirement, scope creep, or incorrectly implemented behavior found.

The reviewer assessed all six criteria against the assigned ticket, scoped spec sections and R01, inspected raw before/after drafts and published artifacts, and independently passed skill/link/whitespace/upstream checks, the nine-document approved-example check and all five original-input hashes. The report explicitly distinguishes initial pre-numbering execution from subsequent final-source audits and defers runtime proof to ticket 27. Full report retained in the check log.

## Completion reconciliation

All six criteria and required checks/reviews are verified at `70a0122`; no unchecked criterion, blocker, optional suggestion or unresolved required item remains. The ticket retains its declared dependency, records previous readiness `ready-for-agent`, and changes to terminal `completed` with all six criteria checked. The feature index links this evidence. Bookkeeping is committed separately from implementation; the generated next-agent handoff is a third separate commit.

Ticket 11 is the next prerequisite-ready M1 assignment after this bookkeeping. This completion neither accepts M1 nor starts ticket 11. Continue prerequisite-ready M1 tickets 12–15 in approved order; generate a QA handoff/waiting status at the boundary and await human acceptance before M2. The separate E1 priority for 25 immediately after verified 24 remains unchanged. No push occurred.
