# Original Standards report: review-ticket-24 / standards-01

| Field | Value |
| --- | --- |
| Assessment | `review-ticket-24`, whole ticket 24, initial independent Standards axis |
| Report / assignment / actor | `standards-01`; `/root/standards24`; fresh review assignment from `/root`, first round; no delegation |
| Configured settings | GPT-6.1 Sol, High; active-context target <=250000 tokens, advisory. Backend instruction delivery/enforcement and measured active-context telemetry unavailable; configuration and digests do not prove those properties. |
| Original baseline | `ed017ae0c2b96769f31c710cfb4ff4708989b446` |
| Assessed source | `65951f6db43fbd2299aa105f3f409eaacd85ec24`, also HEAD during inspection and reproduction |
| Actual commit list | One commit: `65951f6 Own milestone review and checkpoint continuation` |
| Governing plan | `oop-v2` / `review-process-1`; actual ticket 24, scoped spec, publication approval, milestone contract, ADR-0001/0002 |
| Instruction identities | [Dispatch manifest](24-review-round1-instructions.json), shared sources plus Standards additions, and the direct parent assignment. [Independent audit](24-review-standards-01-audit.json) records actual SHA256s for all 25 relevant dispatched paths, all matching dispatch, and dispatch-manifest identity. Development-efficiency/common/axis instructions have their declared working-tree provenance; they are not attributed to the assessed commit. |
| Prior actual findings | None inherited unresolved; no inherited pending relevant revalidation. This report creates its own new key below. Historical fixed/fixture concerns retain their own scopes. |
| Output | This complete original report plus its uniquely named independent audit; root captures report content identity externally after saving. |

Result: **assessment completed, one blocking finding, zero optional suggestions**. The refactor meaningfully localizes review decisions, but an accepted Git reference alias lets ticket integration advance development before human acceptance. That violates the reviewed workflow's authority invariant even though the vulnerable Git/input collaborators are unchanged.

## Instructions and actual scope

Read AGENTS.md, domain guidance, GLOSSARY.md, both ADRs, ownership-review, review-records, architecture-checkpoints, reviewer-evaluation, development-efficiency, testing, python-environment, the report template, actual ticket 24, spec ownership/refactor verification/lifecycle/exact revisions/QA/continuation/review contracts, approval and milestones. Read the common and Standards instructions first, their dispatch manifest, canonical review packet, root mechanical audit, and implementation evidence/coverage map. Applied the code-review skill, Microsoft OOP guidance, codebase-design and test-strategy additions. Repository whole-ticket and substantive reporting rules override the upstream hunk restriction and 400-word cap. No sibling/current-round report or Spec assignment context was read.

Read the actual committed diff with `git diff ed017ae0c2b96769f31c710cfb4ff4708989b446...65951f6db43fbd2299aa105f3f409eaacd85ec24`, including the complete executable changes in qa.py and runner.py and wayfinding change in docs/ticket-harness.md. Read the actual log over that range. The remaining committed changes are ticket-24 evidence artifacts; inspected their canonical packet, implementation/source/check records and relevant checkpoint observations rather than claiming substantive review of every archived byte. Searched for further coding-standards/contribution documents; found no applicable additional root coding standard.

Inspected production definitions and usages throughout all ten `ticket_harness` Python files, with depth chosen by ticket 24's affected workflow:

| Files | Traced responsibilities |
| --- | --- |
| `__main__.py`, `__init__.py` | Run/continue/stop/status dispatch, path resolution, observational status, output and exit behavior; package initializer contains no state logic. |
| `runner.py` | Fresh prepared-input consumption, branch/baseline setup, canonical gate ownership, all check/report/failure paths, ticket scheduling, review construction/outcome, continuation restoration, stopped-marker invalidation and finalization. |
| `qa.py` | Directory ownership lock, stop producer and consumer, request/evidence validation, fresh/restored review initialization, candidate/regression/request preparation, all decision observations and rejection/consumption paths, promotion, persistence/restoration and archive lineage. |
| `inputs.py`, `plans.py` | Accepted configuration and branch names, prepared mappings and aliases, approved source/artifact snapshots, checked plan/membership/role normalization and validation. |
| `tickets.py`, `agents.py` | Initial/current ticket and attempt writers, fixed bases, bounded repairs, ticket feature-ref writer, fresh role/report identities, human-decision authority, canonical run gate consumer and return of a Done candidate. |
| `git.py`, `records.py` | Actual worktree/candidate/source checks, ticket and milestone ref writers, expected-old updates, symbolic-ref semantics relevant to the finding, process/file protection, atomic record writes and cleanup. |

Inspected the four-file coverage map and the concrete CLI fixture, selected approval/rejection, continuation invalidation/identity and repeated-stop tests, milestone preparation/ref/source tests, transaction inventory and real process/Git fixture setup in test_cli.py/test_dependencies.py. Used the existing fixture infrastructure to reproduce a distinct uncertainty through the public CLI; did not invoke private production review methods or create a new test seam.

Omitted independent line-by-line review of every unrelated test/example, all archive payloads, historical reviewer corpora and unrelated preexisting working-tree changes. Reused root's mechanical archive audit rather than replaying it. Did not execute later milestone features, arbitrary crash recovery, runtime review adoption 33/34, real Codex execution, publishing or actual development QA. No assumption that branch names designate independent direct references is justified by validation; the concrete counterexample below defeats that assumption. The report does not claim exhaustive hostile-environment, filesystem-race or Git-configuration coverage.

## Substantive ownership assessment

### Review operations and caller responsibilities

`_Run.execute` now supplies concrete record/config/output/index and derived artifact/worktree paths to `MilestoneReview` (runner.py:155). The review gets the structural `ReviewVerification` interface rather than importing `_Run` or reading its verified registry. Its actual uses are run-owned check, source validation, protected Git operations, persistence, stage observation and checkpoint export. The Protocol describes existing operations; it does not introduce a forwarding checker, a strategy hierarchy or speculative variation. Although the runtime object also has other attributes, the review implementation neither reaches through the interface to scheduling/registry state nor reconstructs the run's decisions.

The owner keeps candidate/source, feature/development inputs, exact request/digest, evidence identities and last raw decision together. `_prepare` contains coherent candidate/regression/readiness work; `_await_decision` owns wait/stop/approval selection. The caller only distinguishes `STOPPED` from `PROMOTED`; it does not have to know a Boolean convention or reorder request-field updates. The run still schedules the next milestone only after promotion, translates stop to exit 2, and distinguishes ticket Done from feature completion. The existing stage-based preparation/promotion failure classification remains in the run (runner.py:171), while QA records the review's observations. This is real depth at the interface, not a class-shape or function-length improvement claim.

The shared durable record/config references are intentional existing persistence representations. QA stores them privately and writes review fields, request/decision/checkpoint identities and successful promotion projections. The run initializes/replaces the current milestone when scheduling, owns baseline/current integration setup and final outcome classification, and persists the shared record. Ticket operations own their ticket/attempt observations and return a candidate to the run. The refactor does not leave a second procedural `qa.review` writer or external collection of ordered review-field patches. These ownership assignments are acceptable except for the actual Git destination alias described in F1: field-level separation alone does not establish branch authority.

### Checks, reference identity and invalidation

Runner.check remains the authority for command execution, protection, timeout/report/finding precedence, canonical gate registration and source invalidation. Agent report parsing returns observations; it does not mutate canonical gates. Ticket human-decision handoffs name the owning attempt rather than selecting one by history position. Review obtains regression evidence through `check` and checkpoint verification references through `export_checks`, with no verified-registry representation knowledge.

In memory, a regression result in the request intentionally aliases its canonical run gate. The serialized request/evidence digests freeze its externally assessed content; a later failed source validation cannot authorize promotion, because validation raises before the ref update. Checkpoint JSON necessarily loses object identity. `_Run.restore_checks` resolves each saved gate back into `record['gates']` (runner.py:197), so `validate_sources` updates the canonical gate and saves it, rather than modifying detached checkpoint copies. Entries carry distinct stage/artifact/source observations in this workflow; I found no normal accepted operation producing ambiguous equal gate records. Rejected ticket checks are removed from the authorization registry, while their durable observations remain. This is separate from the branch-reference identity failure in F1.

### Fresh/restored review, observations and persistence

Fresh preparation runs the candidate regression before writing a consumable request, verifies approved inputs and sources and checks both observed branch tips. Restored preparation reconstructs its request/candidate/development inputs from the already validated checkpoint and joins the same wait/decision/stop operations. Missing/unreadable decisions update status and keep waiting. New raw bytes become an immutable observation artifact; exact JSON decision/request equality and consumed-request checking precede promotion. Nonapprovals do not enter ticket repair machinery or start later milestones. The record projects consumed observations and promoted milestone/ref identities only after the Git transaction returns successfully.

`_persist` retains version 1 and the existing keys and ordering: deliberate stopped record, checkpoint, archived checkpoint bytes, checkpoint digest, run record. Restore validates stopped outcome, checkpoint digest and recorded directory, full record equivalence, archive identity, approved inputs, frozen request/evidence, verified sources and both refs before run restoration. The directory inode lock surrounds start/continuation, not just a removable PID marker. On continuation the run removes stopped-marker authority before resumed work. The restored review adds its prior checkpoint archive to frozen evidence, and a repeated stop collects later observations while preserving prior archives. Rejection diagnostics remain outside prior evidence. These operations preserve the deliberate-checkpoint contract; they promise no arbitrary interruption recovery.

Expected-old commit checks and the two-ref transaction are necessary for ordinary direct branch movement, but do not establish that named refs denote independent destinations. The run, ticket and review writers currently omit that required coordination for accepted symbolic refs. F1 is therefore an ownership/authority finding, not a request for more classes or a stylistic dislike of strings.

### Design heuristics and plausible change

Applied all twelve supplied smell heuristics with repository precedence. The request/candidate/evidence data now travel with the owner; no remaining data clump forces callers to repeat its sequencing. Review names reveal the domain operation. The small direct constructor and explicit outcome earn their interface; no middle-man hierarchy or refused inheritance was added. Pure parsing/Git/process/atomic transformations appropriately stay functions. Some fresh/restored construction necessarily differs, but stop/promotion share `_require_current` and restored requests enter the same wait flow, so I found no actionable duplicate-policy or repeated-switch consequence. A long cohesive preparation method alone is not a violation.

A plausible new decision validation rule would change `_consider_decision` and its behavioral scenarios; run scheduling, check restoration and ticket attempts need not change. A new verification category would change runner-owned category/check logic and its configured policy, with review continuing to ask for verification through the existing operation. A changed checkpoint representation would require review persistence/restore and run's canonical export/restore to agree; this is necessary format coupling, already isolated to the two respective owners. These examples support the refactor's locality. F1 identifies a different actual coordination requirement at Git destinations that the current design does not enforce.

### Independent architecture-trigger reassessment

| Trigger | Ticket start | Final source | Reason |
| --- | --- | --- | --- |
| New lifecycle | No | No | Preparation, wait, deliberate stop/restore and promotion preexist; explicit operations/outcome replace their existing coordination. |
| New persistence/restoration path | No | No | The existing version-1 envelope, archive and canonical gate restoration move under the review without a new format/path or recovery mode. |
| New shared mutable state | No | No | Existing record/config/gate aliases remain; former review locals become private instance state, with no new externally shared store. |
| Additional writer of existing state | No | No | Existing QA procedural writes move to the review; checking/canonical gate writes stay with run. The alias writer defect in F1 already existed and is exposed by whole-workflow inspection, rather than being newly introduced by this refactor. |

Thus these changes do not independently trigger a third broader assessment before integration. F1 still blocks this ticket assessment under the documented whole-ticket ownership rule. The real M1 cumulative all-package assessment, feature-start baseline provenance and actual human QA request/decision/acceptance remain separate unperformed work. Reading relevant package flows here neither performs that milestone assessment nor waives its gates.

## Evidence audit

- Independently resolved both exact revisions and HEAD; inspected the actual single-commit log and fixed-baseline diff. The [independent audit](24-review-standards-01-audit.json) compares all 26 frozen runtime/test/example/config files against committed blobs and working-tree bytes: all match. All 25 applicable dispatch instruction hashes match. These establish identity, not design correctness.
- Reused [final check results](24-final-check-results.json), the actual final logs, [source manifest](24-final-source.json), and [root audit](24-root-final-audit.json). The retained full suite reports **544 passed in 515.90 seconds**; strict mypy, Ruff check/format and both whitespace commands exited 0. No routine full-suite replay was performed. The focused 123-case record supplies development observations rather than a second completion claim.
- Reused [genuine old-checkpoint audit](24-checkpoint/audit.json), producer/stopped/continued records and root provenance comparison: producer's 22 source identities match the fixed pre-refactor baseline, consumer's 22 match the final frozen source; continuation completes with one baseline, preserved earlier attempts/gates, four total attempts and two consumed decisions/promotions. The saved record/checkpoint/archive comparison is finite compatibility evidence. I did not re-run the old producer or independently stream its entire archives.
- Root's retained final archive audit covers 544 scenario observations and 10,446 regular files, including CLI/status/Git/artifact observations; it is reused with that scope. Passing tests and archive hashes do not establish the branch independence invariant. No new private testing seam or implementation-prescriptive tests were introduced.
- Independently ran one scoped public CLI/scripted-process/real-Git reproduction with the documented absolute Python after reading Python/testing guidance. Used `PYTHONPATH=tests:.`, existing `graph.__wrapped__` fixture setup, `configure_plan`, `foreground`, `waiting`, and public stop. The only mutation was a Git symbolic-ref command in the disposable target before run. The CLI run reached QA in roughly two seconds; stop returned 0 and foreground exited 2. No approval was created. The fixture cleaned up. Exact observations and interpreter/recipe are retained in the independent audit and F1 below.

## Findings

### F1 — Blocking, high priority: symbolic branch aliases bypass human ownership of development advancement

**Full key:** `review-ticket-24/standards-01/F1`.

**Documented contract:** ADR-0002 reserves development promotion for exact human QA acceptance. Ticket 24 requires that only an explicit matching, unconsumed approval advances the expected feature/development refs, and retains existing human authority. Spec “State and decision ownership” requires concrete owners/writers to preserve invariants; “Feature-to-development promotion and human QA” separates automatic ticket feature integration from human-approved development advancement. `docs/agents/ownership-review.md` explicitly requires checking accepted aliases and permits a blocking finding in unchanged collaborators when they defeat this ticket's outcome.

**Source and mechanism:** `plans.py:80` rejects only equal feature/development strings. Runner branch setup (`runner.py:97`, `runner.py:111`) checks name syntax and resolves commit IDs, without rejecting/resolving symbolic-ref destination aliases. Ticket integration (`tickets.py:283`, actual `promote(...)` call) invokes `git.py:93`, whose `git update-ref refs/heads/<feature> ...` follows Git symbolic references. Review preparation (`qa.py:192`, `qa.py:232`) and shared stop/restore ref validation (`qa.py:79`) compare resolved commit values and checked-out name strings; they do not establish independent destinations. Thus the QA owner can observe and freeze development only after another nominally feature-only writer has already moved it.

**Concrete accepted input:** With the unchanged existing two-milestone fixture, `configure_plan` supplies feature `integration` and development `dev`. Before public `run`, execute:

```text
git symbolic-ref refs/heads/dev refs/heads/integration
```

The two configured names differ, both refs resolve successfully, neither name is checked out, and no validation rejects the input. Ticket feature integration moves `integration`; `dev` immediately resolves to that new ticket commit too. The public CLI reaches `awaiting_human_qa` normally. Independently observed:

```json
{
  "initial_revision": "fc5569ee494f519d558f379a17becb68dbe06e32",
  "development_alias": "refs/heads/integration",
  "outcome": "awaiting_human_qa",
  "feature_revision": "69cc3e0d548e48987ab8a37bb9322497144aeef8",
  "development_revision": "69cc3e0d548e48987ab8a37bb9322497144aeef8",
  "request_development_revision": "69cc3e0d548e48987ab8a37bb9322497144aeef8",
  "qa_decisions": [],
  "stop_exit": 0,
  "run_exit": 2
}
```

Tickets 01/03 are Done, 02/04 remain Pending. Development has advanced from the initial revision without any human approval. This is observable authority loss before milestone promotion, so a later refusal of the two-ref promotion transaction would not repair it. The reproduction uses ordinary Git-supported refs and the accepted public configuration; it requires no report/checkpoint forgery, target hook, concurrent mutation or private production call. This is not a claim that the refactor newly introduced the defect.

**Consequence:** The named development branch contains unaccepted ticket work before the review exists, contradicting the approved separation of ticket integration and human-owned promotion. Exact candidate/evidence hashes and expected-old commit values do not prevent the alias writer from crossing that authority separation.

**Proportionate remedy:** Enforce independent intended Git destinations before ticket work and preserve that invariant at ref writes and continuation/promotion validation. For example, reject symbolic feature/development refs before starting work and prevent dereferencing/retargeting at updates, rather than treating different branch strings as sufficient proof. Keep this as a focused approved-contract repair, not a neighboring Git abstraction rewrite. Add the distinct public CLI regression demonstrating that accepted alias inputs cannot advance development before approval, and cover relevant stop/continuation validation if the repair changes that path. Renew applicable final-source checks and fresh whole-ticket axes from the original baseline. No ownership-contract amendment is proposed by this report.

## Assessment result

**Completed; not clean. Blocking findings: 1. Optional suggestions: 0.** F1 is open at the exact assessed source. No other blocking or optional finding was established in the recorded inspection; this is not universal architecture approval. The existing mechanical and genuine-checkpoint gates pass with their recorded scope, but do not resolve F1. Root owns aggregation, repair/disposition and exact-source revalidation; this report changes no implementation, ticket status, finding history or handoff. Actual M1 cumulative assessment/provenance and human QA remain unperformed and separate.
