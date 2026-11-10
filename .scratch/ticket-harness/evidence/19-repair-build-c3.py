"""Declare complete corpus C3 under unchanged guidance G2; evaluator-only."""
from pathlib import Path
import datetime
import hashlib
import json
import shutil

ROOT=Path(__file__).resolve().parents[3]
EV=ROOT/'.scratch/ticket-harness/evidence'
OLD=EV/'19-evaluation-g2'
OUT=EV/'19-evaluation-g3'
CANDIDATE=Path('/tmp/development-review-19-c3-candidate')
assert not OUT.exists()
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def files(directory):
    return {str(p.relative_to(directory)):sha(p) for p in sorted(directory.rglob('*')) if p.is_file()}
preserved=EV/'19-repair-c2-preservation.json'
assert not preserved.exists()
preserved.write_text(json.dumps({'corpus':'C2','guidance':'G2','sha256':files(OLD),'purpose':'All frozen failed-trial files before C3 declaration; future checks prohibit any mutation.'},indent=2)+'\n')
manifest=files(CANDIDATE)
audit=json.loads((EV/'19-repair-control-preflight-results.json').read_text())
assert manifest==audit['sources'],'Candidate differs from substantively audited source'
old=json.loads((OLD/'source-manifest.json').read_text())
delta={name:{'C2':old[name],'C3':digest} for name,digest in manifest.items() if digest != old[name]}
assert set(delta)=={'cases/b7/git_ops.py','cases/d9/plan.py','cases/f6/io_ops.py'}
assert all(manifest[name]==old[name] for name in manifest if name.startswith('guidance/'))
OUT.mkdir()
shutil.copytree(CANDIDATE,OUT/'snapshot')
identity=hashlib.sha256(json.dumps(manifest,sort_keys=True).encode()).hexdigest()
(OUT/'source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(OUT/'corpus-identity.txt').write_text(identity+'\n')
(OUT/'revision-delta.json').write_text(json.dumps({'guidance_version':'G2 unchanged from C2','previous_corpus':(OLD/'corpus-identity.txt').read_text().strip(),'final_corpus':identity,'changed_files':delta,'all_contracts_and_guidance_unchanged':True,'preflight_identity_sha256':sha(EV/'19-repair-control-preflight-results.json')},indent=2)+'\n')
(OUT/'declaration.md').write_text(f'''# C3 declared complete corpus — evaluator only

Guidance: **G2 unchanged**. Corpus: **C3**, distinct from its guidance version.
Fixed whole-ticket baseline `f2929e79cfd5a68f670862775053ae85ba9582b5`; rejected source
`e90abb64ab95c5b15cdb0949b03c6a948365339b`. Declared before C3 reviewer assignments.
36-file mapping SHA-256 `{identity}`; [manifest](source-manifest.json),
[neutral source snapshot](snapshot/REVIEW.md), [delta](revision-delta.json).

[G1/C1](../19-evaluation/declaration.md) and [G2/C2](../19-evaluation-g2/declaration.md)
remain intact, including failed source/contracts, reports, classifications and
results. C1 failed invalid-control/adjudication; C2 correctly exposed more invalid
controls despite all four required seeds detected. [C2 per-case adjudication](../19-evaluation-g2/results.md)
preserves valid new b7/d9/f6 findings and differing d9/f6 reviewer interpretations.
No valid blocker is relabeled false or removed by narrowing a contract.

C3 preserves every original contract and seeded-concern source. Relative to C2,
only b7/git_ops.py, d9/plan.py and f6/io_ops.py change: command-specific root/ref
record-terminator decoding preserves path whitespace; parser rejects missing
dependency operands and uses an explicit local DFS stack without recursion depth
restriction; invocation validates finite timeout before process creation, without
positive-only policy. Corrected h8 and every guidance byte remain exactly C2.
[Evaluator preflight](../19-repair-control-preflight-results.json) substantively
assesses all four controls and records bounded ordinary observations before this
declaration. The extra 1200-node recursion failure is evaluator preflight, not a
G2 reviewer finding. [Full C2 preservation](../19-repair-c2-preservation.json)
pins every failed-trial artifact before C3 dispatch.

| Case | Kind / required axis | Expected observation and rationale |
| --- | --- | --- |
| a3 | Required concern / Spec | JSON restoration detaches verified references from canonical gates; invalidation leaves QA stale. Block and rebuild canonical references preserving saved keys/repeated records. |
| b7 | Acceptable control / both | Cohesive function owns Git failures, branch/dirty/base/ancestry checks; root/ref decoding preserves path characters. No class/framework/richer diagnostic requirement. |
| c2 | Required concern / Spec | Checking chooses history[-1] despite supplied ID; delayed/unknown handoffs mutate wrong owner. Block and return validation to execution/identified Attempt attachment. |
| d9 | Acceptable control / both | Pure immutable parser preserves order, rejects missing IDs/references/cycles, validates nonempty dependency tokens, iterates graph locally without interpreter recursion-depth bound. No object/lifecycle framework. |
| e4 | Required concern / Standards | Repair duplicates owning submission guard and mirrored edits; block extra writer/policy propagation and delegate to submit. |
| f6 | Acceptable control / both | Atomic file replacement/cleanup and captured argv process primitive own mechanics; finite timeout checked, nonzero results and TimeoutExpired preserved. No domain state/fsync/metadata requirement. |
| g1 | Required concern / Standards | Preparation returns incomplete fields; CLI finishes privately, resume incomplete/unvalidated. Block hidden caller initialization and complete checked result in preparation. |
| h8 | Acceptable control / both | One owner guards mirrored transitions and deep-copies ordinary mutable inputs/observations; caller delegates under unchanged isolation promise. No assumed scalar restriction/framework. |

Required pass: actual fresh independent Spec and Standards each assess all eight
cases once, both supplied exact final G2 guidance. Declared relevant axis detects
each required seed with concrete source/contract evidence, blocking classification
and proportionate remedy. Controls receive no unsupported blocker; a valid new
contract breach is another invalid-control failure requiring correction, not an
unsupported reviewer finding. Optional suggestions adjudicated by evidence, not
count. Explain all matches/mismatches. Retain every trial/source/report/version.
Any correction needs a fresh complete declaration and final-source evaluation.

Known readable axis prompts and hashes are retained before dispatch. Reviewers
receive only read-only neutral snapshot/contracts/guidance and axis assignment;
no key, builder, evaluator audit, old result, repair/ticket19/spec material or sibling
output. Preserve actual settings/calls/outputs/original finals and pre/post hashes.
Use fresh fork-none GPT-6.1 Sol High, <=250000 active-context advisory target;
backend/enforcement/usage telemetry unavailable. Filesystem isolation advisory.
No harness run, production test, future refactor, human design/risk waiver or QA.

Finite history if C3 is assessed: **three complete eight-case corpora, two guidance
versions, three original reports per axis**. C3 adds no guidance correction. C1 to
C2 changed source and guidance together; C2 to C3 corrects controls under same G2.
No causal wording-effect, future-detection, general reliability or runtime delivery
claim follows. C3's clean corrected controls cannot show original-flaw detection.
Actual later refactors, M1 cumulative review and human QA remain separate.
''')
for axis in ['spec','standards']:
    prompt=(OLD/f'{axis}-g2-input.txt').read_text()
    prompt=prompt.replace('/tmp/development-review-19-g2','/tmp/development-review-19-c3')
    prompt=prompt.replace((OLD/'corpus-identity.txt').read_text().strip(),identity)
    prompt=prompt.replace(f'/tmp/development-review-19-{axis}-g2-report.md',f'/tmp/development-review-19-{axis}-c3-report.md')
    (OUT/f'{axis}-c3-input.txt').write_text(prompt)
(OUT/'declaration-capture.json').write_text(json.dumps({'declared_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'guidance_version':'G2','corpus_version':'C3','declaration_sha256':sha(OUT/'declaration.md'),'source_manifest_sha256':sha(OUT/'source-manifest.json'),'corpus_sha256':identity,'known_prompt_sha256':{axis:sha(OUT/f'{axis}-c3-input.txt') for axis in ['spec','standards']},'C2_preservation_sha256':sha(preserved)},indent=2)+'\n')
TEMP=Path('/tmp/development-review-19-c3')
assert not TEMP.exists()
shutil.copytree(OUT/'snapshot',TEMP)
for path in TEMP.rglob('*'):
    path.chmod(0o555 if path.is_dir() else 0o444)
TEMP.chmod(0o555)
print(json.dumps({'corpus':'C3','guidance':'G2 unchanged','corpus_sha256':identity,'files':len(manifest),'changed_files':list(delta),'declaration_sha256':sha(OUT/'declaration.md')},indent=2))
