# C4 declared complete final corpus — evaluator only

Guidance: **G2 unchanged since C2**. Corpus: **C4**, independent version identity.
Fixed whole-ticket baseline `f2929e79cfd5a68f670862775053ae85ba9582b5`; rejected source
`e90abb64ab95c5b15cdb0949b03c6a948365339b`. Declared before any C4 reviewer assignment.
36-file mapping SHA-256 `bb544f58260e57309be8ffbfb9a2752994b65d8186c899fd7f8ce7e91c33a197`; [manifest](source-manifest.json),
[neutral snapshot](snapshot/REVIEW.md), [explicit delta](revision-delta.json).

Preserved failed trials: [G1/C1](../19-evaluation/declaration.md),
[G2/C2](../19-evaluation-g2/results.md), [G2/C3](../19-evaluation-g3/results.md).
All their sources/contracts/reports/classifications/results/history/checks remain
intact. The first invalid h8 clean adjudication and later b7/d9/f6 breaches stay
visible. All four seeded required concerns were detected in each earlier trial;
no historical complete-corpus pass stands. Extra defects are not retroactively
inserted into the original seeded key. C2 reviewer disagreements and C3 clean b7
judgments remain original, with later evaluator counterexamples distinguished.

C4 changes only b7/caller.py relative to C3: capture process bytes, then explicitly
os.fsdecode stdout/stderr into text CompletedProcess values, preserving CR and
filesystem bytes without universal-newline translation. os.fspath preserves the
checkout's filesystem representation. Argument vectors, no shell, text results,
check=False and validate's sole policy ownership remain. All eight original
contracts, seeded concerns, other controls and guidance bytes are unchanged.
No root-path input restriction is introduced. [Actual exact-caller preflight](../19-repair-path-preflight-results.json)
precedes declaration and observes old/new behavior for trailing space, CR, trailing
newline, Unicode and non-UTF8 filesystem paths in real temporary Git repositories.
C3 corrupts CR and raises on non-UTF8; all C4 candidate roots equal the actual roots.
The [earlier all-control audit](../19-repair-control-preflight-results.json) remains
exact for unchanged d9/f6/h8. These observations support source validity, not reviewer
judgment or exhaustive behavior. [Full C3 preservation](../19-repair-c3-preservation.json)
pins every failed-trial file before C4. The root's original output-translation
preflight is separately retained, not a blind report or full-validate observation.

| Case | Kind / required axis | Expected observation and rationale |
| --- | --- | --- |
| a3 | Required concern / Spec | JSON restoration detaches verified references from canonical gates; invalidation leaves QA stale. Block and rebuild canonical references preserving saved keys/repeated records. |
| b7 | Acceptable control / both | Cohesive function owns Git failures, branch/dirty/base/ancestry checks; root/ref terminator decoding and explicit filesystem text decoding preserve path characters, CR and non-UTF8 filesystem bytes. No class/framework/richer diagnostic requirement. |
| c2 | Required concern / Spec | Checking chooses history[-1] despite supplied ID; delayed/unknown handoffs mutate wrong owner. Block and return validation to execution/identified Attempt attachment. |
| d9 | Acceptable control / both | Pure immutable parser preserves order, rejects missing IDs/references/cycles, validates nonempty dependency tokens, iterates graph locally without interpreter recursion-depth bound. No object/lifecycle framework. |
| e4 | Required concern / Standards | Repair duplicates owning submission guard and mirrored edits; block extra writer/policy propagation and delegate to submit. |
| f6 | Acceptable control / both | Atomic file replacement/cleanup and captured argv process primitive own mechanics; finite timeout checked, nonzero results and TimeoutExpired preserved. No domain state/fsync/metadata requirement. |
| g1 | Required concern / Standards | Preparation returns incomplete fields; CLI finishes privately, resume incomplete/unvalidated. Block hidden caller initialization and complete checked result in preparation. |
| h8 | Acceptable control / both | One owner guards mirrored transitions and deep-copies ordinary mutable inputs/observations; caller delegates under unchanged isolation promise. No assumed scalar restriction/framework. |

Required pass: two actual fresh independent Spec/Standards assignments each assess
all eight cases under exact final G2 guidance. Each required seed is detected by
its declared relevant axis with source-specific evidence, justified blocking
classification and proportionate remedy. Controls receive no unsupported blocker;
a valid new contract breach is another invalid-control failure, not a false blocker.
Adjudicate optional suggestions and every match/mismatch substantively, not by count.
Preserve all failures/versions. Any later source/guidance correction requires a
new complete declaration/final-source trial; no current result is silently reused.

Known readable full axis prompts and hashes are saved before dispatch. Reviewers
receive only a read-only neutral snapshot/contracts/guidance and their respective
assignment. No key, builder, old outcomes, evaluator audit, repair/ticket19/spec,
root preflight or sibling output. Preserve actual settings/source reads/tool outputs
and exact original finals, independently from command/hash audits. Requested roles:
fresh fork-none GPT-6.1 Sol High, <=250000 active-context advisory target. Backend
selection/delivery/enforcement, measured usage/hard context enforcement unavailable;
filesystem isolation advisory. No production tests, harness/backend/refactor/QA.

Finite declared history: **four complete eight-case corpora, two guidance versions,
one report per axis per corpus** if this final trial is performed. G1/C1, G2/C2,
G2/C3 and G2/C4 use evolving source; this is not four identical-corpus reliability
repetitions. C1 to C2 changed source and guidance together; C3/C4 are source-only
corrections under G2. No causal wording-effect, general quality/detection guarantee,
retrospective clean attestation or runtime effectiveness claim follows. Corrected
controls do not demonstrate new detection of their original defects. Later refactor
reviews, real M1 cumulative assessment and explicit human QA remain separate.
