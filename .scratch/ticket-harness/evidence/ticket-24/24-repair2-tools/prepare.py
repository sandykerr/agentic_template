"""Version existing evidence tooling; retain original records unchanged."""
import hashlib,json,subprocess
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence')
source=out/'24-repair1-tools'; target=out/'24-repair2-tools'
for name in ['identity.py','checks.py','capture24repair1.py','archive.py','continue-old.py','archive-checkpoint.py','validate.py']:
 text=(source/name).read_text().replace('repair1','repair2').replace('REPAIR1','REPAIR2').replace('556','559')
 if name=='identity.py': text=text.replace("+['docs/ticket-harness.md']",'')
 (target/name.replace('repair1','repair2')).write_text(text)
captures=[json.loads((out/f'24-review-round{n}-capture.json').read_text()) for n in (1,2)]
for c in captures:
 for n,d in c['artifacts'].items():assert hashlib.sha256((out/n).read_bytes()).hexdigest()==d
paths=['AGENTS.md','GLOSSARY.md','.scratch/ticket-harness/spec.md','.scratch/ticket-harness/issues/24-own-milestone-review-and-checkpoint-continuation.md']
paths += [str(p) for p in Path('docs/agents').glob('*.md')]+[str(p) for p in Path('docs/adr').glob('*.md')]
paths += ['.agents/skills/'+p+'/SKILL.md' for p in ('custom/implement-with-checkboxes','custom/test-strategy','matt-pocock/tdd','matt-pocock/codebase-design','microsoft/microsoft_oop')]
paths += [str(out/n) for c in captures for n in c['artifacts']]
paths += [str(out/n) for n in ['24-finding-history.md','24-diagnosis2.md','24-diagnosis2-atomic-probe.py','24-diagnosis2-atomic-probe.json']]
r=dict(actor='/root/repair24_2',settings=dict(model='GPT-6.1 Sol',reasoning='Medium',context='<=250000 advisory',backend_delivery_and_telemetry='unavailable'),baseline=captures[0]['original_baseline'],rejected_source=captures[1]['assessed_source'],head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),originals_match_both_captures=True,identities={n:hashlib.sha256(Path(n).read_bytes()).hexdigest() for n in paths},capture_timing='During local repair; not a pre-edit source snapshot',status=subprocess.check_output(['git','status','--short'],text=True))
(out/'24-repair2-start.json').write_text(json.dumps(r,indent=2)+'\n')
