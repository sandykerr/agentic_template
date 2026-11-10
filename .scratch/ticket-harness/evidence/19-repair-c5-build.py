"""Declare full C5/G2 corpus; source/guidance identities precede both assignments."""
from pathlib import Path
import datetime, hashlib, json, shutil
ROOT=Path('/home/ajkerr1/development/agentic_template')
EV=ROOT/'.scratch/ticket-harness/evidence'
OLD=EV/'19-evaluation-g4';OUT=EV/'19-evaluation-g5';CANDIDATE=Path('/tmp/development-review-19-c5-candidate')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def files(directory):return {str(p.relative_to(directory)):sha(p) for p in sorted(directory.rglob('*')) if p.is_file()}
assert not OUT.exists()
preservation=EV/'19-repair-c4-preservation.json';assert not preservation.exists()
preservation.write_text(json.dumps({'corpus':'C4','guidance':'G2','sha256':files(OLD),'purpose':'All original C4 sources/reports/results/declarations/history/checks preserved before C5; later invalid-control adjudication uses new paths only.'},indent=2)+'\n')
manifest=files(CANDIDATE)
for name in ['19-repair-c5-branch-preflight-results.json','19-repair-c5-adapter-preflight-results.json']:
    assert json.loads((EV/name).read_text())['candidate_sources']==manifest
old=json.loads((OLD/'source-manifest.json').read_text())
delta={name:{'C4':old[name],'C5':digest} for name,digest in manifest.items() if old[name]!=digest}
assert set(delta)=={'cases/b7/git_ops.py','cases/b7/caller.py'}
OUT.mkdir();shutil.copytree(CANDIDATE,OUT/'snapshot')
identity=hashlib.sha256(json.dumps(manifest,sort_keys=True).encode()).hexdigest()
(OUT/'source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');(OUT/'corpus-identity.txt').write_text(identity+'\n')
(OUT/'revision-delta.json').write_text(json.dumps({'guidance_version':'G2 unchanged since C2','previous_corpus':(OLD/'corpus-identity.txt').read_text().strip(),'final_corpus':identity,'changed_files':delta,'all_contracts_guidance_concerns_and_other_controls_unchanged':True,'preflight_sha256':{name:sha(EV/name) for name in ['19-repair-c5-branch-preflight-results.json','19-repair-c5-adapter-preflight-results.json']}},indent=2)+'\n')
prior=(OLD/'declaration.md').read_text();table=prior[prior.index('| Case |'):prior.index('Required pass:')]
table=table.replace('root/ref terminator decoding and explicit filesystem text decoding preserve path characters, CR and non-UTF8 filesystem bytes.','full local symbolic-ref identity handles namespace collisions; exact filesystem decoding preserves root characters; adapter clears Git local-routing environment and disables optional locks for requested-checkout read-only commands.')
(OUT/'declaration.md').write_text(f'''# C5 complete pre-assignment declaration — evaluator only

Guidance **G2 unchanged since C2**; independent corpus version **C5**. Fixed
whole-ticket baseline `f2929e79cfd5a68f670862775053ae85ba9582b5`; latest rejected
implementation source `ce4e57d77be6dfd695f0ecb15284c5e9d5792b93`. Declaration predates
both C5 assignments. Exact 36-file aggregate `{identity}`; [manifest](source-manifest.json),
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

{table}Required pass: fresh independent Spec and Standards each inspect all eight cases
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
''')
for axis in ['spec','standards']:
    prompt=(OLD/f'{axis}-c4-input.txt').read_text().replace('/tmp/development-review-19-c4','/tmp/development-review-19-c5').replace('/tmp/development-review-19-'+axis+'-c4-report.md','/tmp/development-review-19-'+axis+'-c5-report.md').replace((OLD/'corpus-identity.txt').read_text().strip(),identity)
    prompt+=' Identity audit includes all regular files, including hidden guidance/.agents files; compute the aggregate with sorted path/digest mapping and default json.dumps(sort_keys=True) comma-space/colon-space separators. Identity verification remains separate from substantive source assessment.\n'
    (OUT/f'{axis}-c5-input.txt').write_text(prompt)
(OUT/'declaration-capture.json').write_text(json.dumps({'declared_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'guidance_version':'G2','corpus_version':'C5','declaration_sha256':sha(OUT/'declaration.md'),'source_manifest_sha256':sha(OUT/'source-manifest.json'),'corpus_sha256':identity,'known_prompt_sha256':{axis:sha(OUT/f'{axis}-c5-input.txt') for axis in ['spec','standards']},'C4_preservation_sha256':sha(preservation)},indent=2)+'\n')
TEMP=Path('/tmp/development-review-19-c5');assert not TEMP.exists();shutil.copytree(OUT/'snapshot',TEMP)
for path in TEMP.rglob('*'):path.chmod(0o555 if path.is_dir() else 0o444)
TEMP.chmod(0o555)
print(json.dumps({'corpus':'C5','guidance':'G2 unchanged','corpus_sha256':identity,'files':len(manifest),'changed_files':list(delta),'declaration_sha256':sha(OUT/'declaration.md')},indent=2))
