"""Declare complete final C4 corpus under unchanged G2 guidance; evaluator-only."""
from pathlib import Path
import datetime
import hashlib
import json
import shutil

ROOT=Path(__file__).resolve().parents[3]
EV=ROOT/'.scratch/ticket-harness/evidence'
OLD=EV/'19-evaluation-g3'
OUT=EV/'19-evaluation-g4'
CANDIDATE=Path('/tmp/development-review-19-c4-candidate')
assert not OUT.exists()
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def files(directory):
    return {str(p.relative_to(directory)):sha(p) for p in sorted(directory.rglob('*')) if p.is_file()}
preserved=EV/'19-repair-c3-preservation.json'
assert not preserved.exists()
preserved.write_text(json.dumps({'corpus':'C3','guidance':'G2','sha256':files(OLD),'purpose':'All frozen failed-trial source/reports/results/history before C4 declaration; no mutations permitted.'},indent=2)+'\n')
manifest=files(CANDIDATE)
audit=json.loads((EV/'19-repair-path-preflight-results.json').read_text())
assert manifest==audit['candidate_sources']
old=json.loads((OLD/'source-manifest.json').read_text())
delta={name:{'C3':old[name],'C4':digest} for name,digest in manifest.items() if digest!=old[name]}
assert set(delta)=={'cases/b7/caller.py'}
OUT.mkdir()
shutil.copytree(CANDIDATE,OUT/'snapshot')
identity=hashlib.sha256(json.dumps(manifest,sort_keys=True).encode()).hexdigest()
(OUT/'source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(OUT/'corpus-identity.txt').write_text(identity+'\n')
(OUT/'revision-delta.json').write_text(json.dumps({'guidance_version':'G2 unchanged since C2','previous_corpus':(OLD/'corpus-identity.txt').read_text().strip(),'final_corpus':identity,'changed_files':delta,'all_contracts_guidance_concerns_and_other_controls_unchanged':True,'preflight_identity_sha256':sha(EV/'19-repair-path-preflight-results.json')},indent=2)+'\n')
prior=(OLD/'declaration.md').read_text()
table=prior[prior.index('| Case |'):prior.index('Required pass:')]
table=table.replace('root/ref decoding preserves path characters.','root/ref terminator decoding and explicit filesystem text decoding preserve path characters, CR and non-UTF8 filesystem bytes.')
(OUT/'declaration.md').write_text(f'''# C4 declared complete final corpus — evaluator only

Guidance: **G2 unchanged since C2**. Corpus: **C4**, independent version identity.
Fixed whole-ticket baseline `f2929e79cfd5a68f670862775053ae85ba9582b5`; rejected source
`e90abb64ab95c5b15cdb0949b03c6a948365339b`. Declared before any C4 reviewer assignment.
36-file mapping SHA-256 `{identity}`; [manifest](source-manifest.json),
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

{table}Required pass: two actual fresh independent Spec/Standards assignments each assess
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
''')
for axis in ['spec','standards']:
    prompt=(OLD/f'{axis}-c3-input.txt').read_text()
    prompt=prompt.replace('/tmp/development-review-19-c3','/tmp/development-review-19-c4')
    prompt=prompt.replace((OLD/'corpus-identity.txt').read_text().strip(),identity)
    prompt=prompt.replace(f'/tmp/development-review-19-{axis}-c3-report.md',f'/tmp/development-review-19-{axis}-c4-report.md')
    (OUT/f'{axis}-c4-input.txt').write_text(prompt)
(OUT/'declaration-capture.json').write_text(json.dumps({'declared_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'guidance_version':'G2','corpus_version':'C4','declaration_sha256':sha(OUT/'declaration.md'),'source_manifest_sha256':sha(OUT/'source-manifest.json'),'corpus_sha256':identity,'known_prompt_sha256':{axis:sha(OUT/f'{axis}-c4-input.txt') for axis in ['spec','standards']},'C3_preservation_sha256':sha(preserved)},indent=2)+'\n')
TEMP=Path('/tmp/development-review-19-c4')
assert not TEMP.exists()
shutil.copytree(OUT/'snapshot',TEMP)
for path in TEMP.rglob('*'):
    path.chmod(0o555 if path.is_dir() else 0o444)
TEMP.chmod(0o555)
print(json.dumps({'corpus':'C4','guidance':'G2 unchanged','corpus_sha256':identity,'files':len(manifest),'changed_files':list(delta),'declaration_sha256':sha(OUT/'declaration.md')},indent=2))
