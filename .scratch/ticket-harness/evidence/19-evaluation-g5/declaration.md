# C5 complete pre-assignment declaration — evaluator only

Guidance **G2 unchanged since C2**; independent corpus version **C5**. Fixed
whole-ticket baseline `f2929e79cfd5a68f670862775053ae85ba9582b5`; latest rejected
implementation source `ce4e57d77be6dfd695f0ecb15284c5e9d5792b93`. Declaration predates
both C5 assignments. Exact 36-file aggregate `332ddabe972f596d86cd09eda809bd2f93d1f57602f01d75ed9f39f2b182510d`; [manifest](source-manifest.json),
[neutral snapshot](snapshot/REVIEW.md), [source-only delta](revision-delta.json).

All four prior full trials, original sources/contracts/reports/declarations/results,
checks and histories remain unchanged: [C1](../19-evaluation/README.md),
[C2](../19-evaluation-g2/results.md), [C3](../19-evaluation-g3/results.md),
[C4](../19-evaluation-g4/results.md). [Complete C4 preservation](../19-repair-c4-preservation.json)
pins every old file. Original h8 isolation adjudication, b7 path/caller defects,
d9 grammar/depth and f6 timeout failures retain their original observations.
A later actual whole-ticket Spec review exposes C4 b7's branch/tag collision:
short symbolic-ref returns heads/main for the valid branch main when a tag also
has that name. Both C4 corpus clean b7 judgments and its then-current passing
adjudication remain originals, now superseded at new paths. No historical
complete-corpus pass is claimed. Additional pre-declaration evaluator audit
reproduces foreign Git environment routing and optional status index mutation.
Those are evaluator observations, not new blind reviewer findings or extra seeds.

C5 changes only b7/git_ops.py and b7/caller.py. The owner reads full symbolic HEAD,
checks refs/heads/ and extracts the exact local branch suffix before comparing the
expected branch. The caller uses Git's own local-environment-name discovery to
clear foreign repository routing in a copied environment, disables optional locks
for requested-checkout commands, retains byte capture/os.fsdecode/os.fspath and
delegates all repository policies to validate. Original contracts, required
concern sources, other controls and every G2 guidance byte are unchanged.
No scalar/path/branch/environment input restriction or semantic policy escapes
into the caller. [Branch/path/policy audit](../19-repair-c5-branch-preflight-results.json)
and [exact-caller routing/read-only audit](../19-repair-c5-adapter-preflight-results.json)
precede declaration. They establish bounded observed behavior, not reviewer judgment
or exhaustive Git/platform correctness. Existing exact earlier observations apply
only to their original source identities; unchanged d9/f6/h8 preflight remains
applicable by identical source bytes.

| Case | Kind / required axis | Expected observation and rationale |
| --- | --- | --- |
| a3 | Required concern / Spec | JSON restoration detaches verified references from canonical gates; invalidation leaves QA stale. Block and rebuild canonical references preserving saved keys/repeated records. |
| b7 | Acceptable control / both | Cohesive function owns Git failures, branch/dirty/base/ancestry checks; full local symbolic-ref identity handles namespace collisions; exact filesystem decoding preserves root characters; adapter clears Git local-routing environment and disables optional locks for requested-checkout read-only commands. No class/framework/richer diagnostic requirement. |
| c2 | Required concern / Spec | Checking chooses history[-1] despite supplied ID; delayed/unknown handoffs mutate wrong owner. Block and return validation to execution/identified Attempt attachment. |
| d9 | Acceptable control / both | Pure immutable parser preserves order, rejects missing IDs/references/cycles, validates nonempty dependency tokens, iterates graph locally without interpreter recursion-depth bound. No object/lifecycle framework. |
| e4 | Required concern / Standards | Repair duplicates owning submission guard and mirrored edits; block extra writer/policy propagation and delegate to submit. |
| f6 | Acceptable control / both | Atomic file replacement/cleanup and captured argv process primitive own mechanics; finite timeout checked, nonzero results and TimeoutExpired preserved. No domain state/fsync/metadata requirement. |
| g1 | Required concern / Standards | Preparation returns incomplete fields; CLI finishes privately, resume incomplete/unvalidated. Block hidden caller initialization and complete checked result in preparation. |
| h8 | Acceptable control / both | One owner guards mirrored transitions and deep-copies ordinary mutable inputs/observations; caller delegates under unchanged isolation promise. No assumed scalar restriction/framework. |

Required pass: fresh independent Spec and Standards each inspect all eight cases
under exact G2 source/guidance. Every required seed is detected by its relevant
axis with source-specific evidence, justified blocking classification and
proportionate remedy. Controls receive no unsupported blocker. A supported new
control breach invalidates that control rather than becoming a false blocker.
Adjudicate all match/mismatch/optional observations substantively. Preserve failures;
any source/guidance correction after declaration needs a new full version/trial.

Save known readable complete prompts/hashes before dispatch. Supply only the
read-only neutral source/contracts/G2 guidance snapshot and each axis assignment,
without this declaration/key, old results, evaluator audits/builders, repair/ticket
material or sibling reports. Requested settings: fresh fork-none GPT-6.1 Sol High
for each axis; <=250000 active-context advisory. Retain actual assignment/session
settings, tool/source/received records and exact plaintext original final reports.
Configured settings and permission bits do not prove backend delivery/effectiveness,
filesystem isolation, model or hard context enforcement. Telemetry/measured active
context unavailable. No production tests/runtime schema, harness, refactor20–24,
M1 acceptance, backend runtime33/34, promotion or push.

Finite history after this trial: five complete eight-case corpora, two guidance
versions, one independent original report per axis per corpus. Sources evolve;
these are not five identical-corpus reliability repetitions. C1–C2 changes source
and guidance together; C3–C5 are source-only under G2. Corrected controls do not
establish detection of unchanged original flaws. No causal wording-effect, general
detection rate, guaranteed future correctness, large-package attention or runtime
effectiveness follows. Actual whole-ticket reviews, future refactor reviews,
feature-start/all-package M1 cumulative assessment and human QA remain separate.
