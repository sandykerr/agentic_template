# Review report: review-M1-index-repair-01 / standards-01

**Completed: zero blocking findings and zero optional suggestions.** Independent
source inspection and retained same-source behavioral evidence support the repair
of `review-M1-architecture-01/standards-01/F1` at the assessed revision. This
report does not record its disposition, replace cumulative review, accept M1 or
authorize M2.

| Field | Value |
| --- | --- |
| Assessment | `review-M1-index-repair-01`; [repair work item](../../reviews/M1-index-repair-01.md) |
| Report identity | `standards-01`, Standards axis, first fresh repair-review assignment in this round; actor `/root/m1_standards`, assigned by `/root`; no further delegation |
| Actual settings | Assignment requested GPT-6.1 Sol, High, advisory 250K active-context target. Backend model/reasoning delivery, hard context enforcement and measured active-context telemetry are unavailable. |
| Original baseline | Fixed repair baseline `e2b0a260fa192a7b51edc5f4cc5692c6340444c2`. Original cumulative baseline remains `1a623bad0b08241367948948b731b9e1f5114671`; it is not the repair diff baseline. |
| Assessed source | HEAD `88e4cd8aabc78e76e66efc02983fec3900ab0a23`, containing repair checkpoint `e06eeaf7ae961a927e13b8d330b1675646afe4e2`. Tracked executable/test inputs match these assessed HEAD blobs; current environment/instruction inputs are separately captured. |
| Supplied instructions | Current AGENTS, GLOSSARY, ADR-0001/0002, environment/testing/tracker/review-records policies, approved oop-v2 / review-process-1 spec/approval/M1, handoff, code-review full smell baseline, codebase-design, Microsoft OOP and test-strategy. Exact path/digest inventory: [canonical manifest](source-and-instructions.json), SHA-256 `f0253bb01a37928566a4806499f5c2a58364fb4ffc2a75a1bdb7ae8685507dc3`; [instruction snapshot](instruction-snapshot.tar.gz). Also read [review brief](../m1-index-repair-01/review-brief.md), SHA-256 `8869820daeafde6eb971d802ceecbf1a311c93a2b857745645b5ab8091208b8a`, and report template SHA-256 `9164c2267b27fd6ee89d09bb9d056b07bf07a682d0dc556e3e6b6f62c9bb3afc`. These identify local bytes; backend delivery attestation is unavailable. |
| Original output/evidence | This unique original; [canonical index](README.md), [retained check aggregate](../m1-index-repair-01/verification-completion-result.json), [worker coverage/ownership map](../m1-index-repair-01/worker-notes.md), [routing observations](../m1-index-repair-01/routing-observations/summary.json). Root owns the external report digest/capture and subsequent aggregation. |
| Inspected scope | Whole three-file repair from `git diff e2b0a260fa192a7b51edc5f4cc5692c6340444c2...HEAD`, and the callers, writers, initialization, persistence, restoration and invalidation flows detailed below. |
| Omitted scope | `adapt_agent_guidance_step5_options.md`, the unrelated guidance-options document added by later commit `88e4cd8`, is excluded from this bounded executable repair review as assigned. No full cumulative all-file attestation, calibration rerun, live backend, exhaustive environment/platform matrix, old-checkpoint campaign replay, installed-wheel campaign or current candidate QA execution. No sibling same-round report was read. No unresolved assumption is used to exclude the original accepted inherited-index input. |
| Prior observations | Original blocking key [review-M1-architecture-01/standards-01/F1](../m1-qa-01/standards-01-original.md#f1--blocking-inherited-git-index-routing-writes-into-the-callers-index); [append-only history Events01–05](../../reviews/M1-architecture-01-history.md); [human readability correction assessment](../../reviews/M1-human-readability-01.md). Historical ticket19/ticket24 keys are discussed below. No prior report is rewritten or superseded by editing its contents. |

## Substantive assessment

The governing preservation requirement is the approved spec's **Independent
checks and exact revisions** and **Testing Decisions**: submission capture belongs
to the harness, while unrelated caller work remains untouched. The current agent
reference explicitly includes caller HEAD, index and working files. The handoff
authorizes resolving routing within existing Git/process owners, including related
routes and the isolated merge override. Neither validation nor this repair assumes
that an inherited `GIT_INDEX_FILE` is absent. ADR-0001 permits the bounded local
repair; ADR-0002 still reserves exact-candidate milestone acceptance to the human.

I read all of `git.py`, `records.py`, `tickets.py`, `runner.py` and `qa.py`, then
followed their actual definitions/usages. I also inspected public CLI dispatch and
package initialization; input command validation, preparation, saved configuration,
approved-input checks and completion ancestry; plan settings/validation; assignment
construction and report-result handling; the scripted agent/check; the transaction
test file and its `TicketFixture`/`ReportFixture` collaborators; and relevant
continuation, clean-merge and concurrent-ref test flows. Unrelated parsing helpers
and every historical test/corpus were not inspected line by line. A package search
for subprocess/environment operations identified exactly the four launch sites
below, with no separate launcher in inputs, plans, agents, tickets, QA or the CLI.

### Routing owner and every affected writer

`records.worktree_environment` (`records.py:22–46`) owns the ordinary launch
environment transformation. It creates a fresh dictionary per call, removing
repository-local Git routing/configuration keys. It never edits `os.environ`,
caches mutable state or asks ticket/run callers to save and restore ambient keys.
The Git module already depended on records for failure handling; the helper adds
no dependency cycle. Removing it would distribute this policy across three actual
launch sites, so its small interface earns its place. A function is appropriate
for this stateless transformation under the spec and both design skills.

| Launch and actual callers | Relevant operations and invariant reasoning |
| --- | --- |
| `git.git`, `git.py:14–28` | Input validation (`ls-tree`, completion ancestry), run branch/base establishment, baseline and ticket/review worktree creation, source checks, submission capture, candidate creation, QA validation and promotion helpers all use the same copied environment before Git starts. Target selection via `-C` can no longer be overridden by inherited local index/repository/worktree/object/configuration routing. `worktree` owns creation and Git's per-worktree index initialization; `capture` stages and commits only its selected source. Repair copying explicitly excludes `.git`. Hook-capable checkout/commit/merge descendants inherit the selected launch environment. |
| `_update_direct_branches`, `git.py:157–214` | Both ticket `promote` and QA `promote_milestone` reach the direct interactive `Popen`, now using the same transformation. Ref commands retain no-dereference expected-old updates, prepared destination locks, topology validation while locked, commit/abort cleanup and disabled final ref hooks. Filtering also reaches the ordinary adapter used for the topology observations, keeping those observations and writes in the same selected repository. |
| `records.execute`, `records.py:114–182` | Its only package caller is `_Run.check`; baseline, lightweight checks, implementation/repair, both review roles, ticket candidate and milestone regression all pass their assigned source cwd through it. The copied filtered environment gains `TICKET_HARNESS_STAGE` immediately before launch. Thus a configured agent or check invoking its own ordinary Git process cannot inherit the caller's index route independently of harness Git. Assignment persistence, output collection, timeout/cleanup and protected-evidence handling remain in the existing process owner. |
| `require_clean_milestone_candidate`, `git.py:217–273` | Its direct `subprocess.run` remains intentionally different: remove all inherited `GIT_*`, then set the target object store and explicit empty global/system/attribute settings for an isolated bare merge comparison. The preceding tree write, object-store discovery and bare initialization now use the filtered normal adapter. The direct comparison retains its explicit `--git-dir` and selected object store; its candidate tree/parent/source checks still reject source-changing resolutions. Applying the ordinary helper after these explicit overrides would break this operation, and the repair correctly does not do so. |

The caller index remains caller-owned, with no new writer, snapshot or compensating
rollback. Each detached source's index remains Git-owned. Prevention occurs before
even status/source-check operations can refresh an inherited caller index, and
before submission `add --all`, commit, merge or ref writes. This addresses the
original failure's timing: later invalidation previously detected damage after the
caller index had already changed. It now remains a source-approval mechanism,
while launch policy prevents that unrelated write.

The filter has no value-dependent branch: absolute, relative, empty or aliased
values of a removed key are omitted alike. Removing `GIT_CONFIG_COUNT` makes its
numbered configuration entries inactive; `GIT_CONFIG_PARAMETERS` is removed too.
Nonlocal identity, PATH and tracing are retained as documented. This does not
claim protection against a trusted command deliberately specifying a new Git
route, changing its own environment, or directly writing other filesystem paths;
the existing trusted-command contract grants those capabilities. `GIT_NAMESPACE`
remains inherited, with only a finite retained current-workflow observation.

### Initialization, durable identity, restore and failure

`inputs.load` validates commands without executing configured workers, resolves
the selected target and creates `PreparedInputs`; its Git lookups already use the
fixed adapter. `_Run.execute` owns fresh configuration, branch/base setup, baseline
worktree and scheduling. `_TicketExecution` retains a fixed approved base while
creating new worktrees for repaired attempts; `_Attempt` owns paired attempt/ticket
observations. No caller must temporarily modify global environment before these
operations or coordinate an extra restore step afterward.

Environment dictionaries live only for one process launch and are not added to
run/config/checkpoint schemas. `MilestoneReview._persist` still saves config,
record, evidence and run-exported verification references in version 1. On
continuation, `restore_checkpoint` checks saved source/input/ref/evidence identities
using the fixed Git adapter before `_Run` resumes. `_Run.restore_checks` reconnects
saved verification entries to canonical gates; subsequent `validate_sources`
updates the durable gate and saves before raising. Future work admitted by the
continued run reaches the same `check`/`execute` path. Completed assignments and
baseline are not replayed. The repair changes neither saved aliases nor the
source-invalidation registry.

Git failures still raise `GateFailure`; process OS/cleanup errors still become
failed gate evidence and the runner's environment outcome. Run/attempt owners
retain partial work, diagnostics and rejected history. The changed code introduces
no new lifecycle, persistence/restoration path, shared mutable state or writer.
The worker's four No/No trigger conclusions are supported by this trace. Mandatory
M1 cumulative review remains required independently.

### Coverage value and design heuristics

The added test uses the approved public CLI, scripted external processes and a
real disposable Git repository. The fixture owns its repository, scripts and
cleanup. `monkeypatch.context` scopes the one environment delta to the CLI launch;
fixture Git setup precedes it, and the immediate byte assertion precedes all
observer Git commands. The setup deliberately distinguishes staged, unstaged and
untracked caller content, then checks HEAD and integration behavior as well.

The four cases have meaningful differences: ordinary harness writes on success;
ordinary writes followed by Standards rejection; an implementation process doing
its own `git add`; and a candidate check doing its own `git add`. The latter two
detect omission of `execute`'s filter even when harness Git is repaired. The worker
retained an intermediate red execution demonstrating that distinction. A full
writer-by-rejection Cartesian matrix adds no demonstrated policy branch; the
selected rejection happens before a candidate check could run. Existing normal
preservation, repair, clean-merge/ref-lock and restored-invalidation scenarios
remain useful and are not replaced by this regression.

I applied all twelve smell heuristics as judgments, with repository rules taking
precedence and tooling-covered concerns excluded. I found no consequential
mysterious naming, duplicated routing policy, feature envy, data clump, primitive
obsession, repeated switch, shotgun surgery, divergent change, speculative
generality, message chain, middle man or refused bequest in the repair. The
separate isolated-merge environment is different policy with an actual purpose,
not duplicate ordinary routing logic. String keys mirror Git's external contract;
no new class hierarchy or environment registry is justified. The test's fixture
reuse and four representative cases have no concrete reliability or maintenance
defect warranting a preference-based finding.

## Evidence audit

I independently resolved the fixed baseline and HEAD, inspected the committed
repair diff and commit list (`e06eeaf`, followed by unrelated `88e4cd8`), and checked
working status. A read-only `.venv/bin/python` audit matched all **28** canonical
source hashes and **50** instruction hashes to current bytes and the frozen
implementation manifest. All available assessed HEAD source blobs matched too;
`requirements-uv.in` and `requirements-uv.txt` are untracked environment inputs,
identified by hashes rather than misattributed to the repair commit. Dirty
instruction/environment/navigation work is not represented as committed source.

Installed Git is 2.43.7. Its local `git rev-parse --local-env-vars` output exactly
matches the helper's fifteen-key set. This is installed-version evidence, not
universal future Git coverage. Scoped committed whitespace checking passed.

I reused [verification-completion-result.json](../m1-index-repair-01/verification-completion-result.json),
SHA-256 `ef5911ca9a3430d4ef8bf00f8de396fb88d9b9e1420f9c579d4eb18b2d3cc79e`:
the retained full-suite log/JUnit report **563 passed**, zero failures/errors/skips,
2878.13 seconds, and strict mypy, Ruff lint/format and whitespace checks exited 0.
Its source manifests bind the tested dirty implementation bytes; the old HEAD
field alone would not. The independent hash comparison above establishes the
current source correspondence. I did not rerun these passing checks.

The retained final four-case regression passed. I read the fresh routing recipe,
summary and caller-index observation, then independently checked all eight saved
observations for successful completion, equal caller/foreign index hashes and
unchanged caller/foreign HEADs; retained caller index binaries match their before/
after hashes. All 24 source entries captured for those observations match current
canonical source. The eight cases cover control, original clean caller-index
pattern, foreign directory/worktree/common-dir/object routing, counted core.worktree
configuration and namespace. These are retained executions, not newly executed
CLI cases in this assignment. The caller-index case completed with indexed/working
value 1 and integration value 2, preserving the immediate index hash
`2fd48c857d8eee3386403dfbba5692cc9f1d3fe44e29d9d7f056636b5ef36273`.

Historical failing `/tmp` hook checks, interrupted full runs and capture-helper
path-alias failure remain separate from the successful executable-TMPDIR repeat.
They are not relabeled as passing checks. No packaging/entry-point change or
concrete installed behavior uncertainty calls for a new wheel campaign here.
Source hashes and passing observations establish identity/behavior; the ownership
conclusion above comes from following the actual operations and callers.

## Findings

No new blocking findings or optional suggestions in the inspected bounded scope.

For **`review-M1-architecture-01/standards-01/F1`**, the original counterexample is
addressed at `88e4cd8aabc78e76e66efc02983fec3900ab0a23`: local routing is removed
before every ordinary relevant launch, including external writers; the intentional
isolated override remains owned by its operation. The retained same-source original
pattern and stronger dirty-caller regression corroborate prevention rather than
late rejection or rollback. This supplies independent exact-source verification
support for a fixed disposition. Root must preserve the original blocking
classification and append the disposition with repair and verification links.

Historical `review-ticket-24/spec-01/F1`, `review-ticket-24/standards-01/F1` and
`review-ticket-24/spec-02/F1` remain separate keys: current QA still catches deep
decision `RecursionError`, and ticket/QA promotion still checks direct topology
under prepared locks, including development verification beside ticket feature
updates. The repair changes their process environment without removing their
mechanisms. Their earlier differing judgments remain preserved. I do not relabel
old reports as reviews of this revision.

Historical `review-ticket-19/spec-01/F1` and `review-ticket-19/spec-02/F1` concern
the h8 alias and b7 branch/tag controls, not this production route. Their final
G2/C5 result remains finite concern/control evidence at its recorded identity;
earlier misses/invalid controls remain failures. No new calibration, general
detection/reliability claim, runtime delivery attestation or hard-context evidence
is supplied. Historical optional/synthetic fixture observations remain at those
original scopes.

## Assessment result

The independent Standards repair assessment is **complete and clean** for the
recorded scope. The original caller-index concern is independently verified as
repaired on the exact assessed source; no remaining bounded blocker or unresolved
accepted-input counterexample was found. Source/instruction identity, test results,
ownership reasoning and authority limits remain separate observations.

Finding disposition, the separate Spec axis, mandatory cumulative High Standards
renewal, current candidate/request preparation and actual human QA acceptance are
owned by their respective workflows. This report alone establishes none of those
later gates and authorizes no development promotion or M2 work.
