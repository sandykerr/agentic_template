"""Retain repair instruction/report identities and immutable-original audit."""
import hashlib,json,subprocess
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence')
capture=json.loads((out/'24-review-round1-capture.json').read_text())
for name,digest in capture['artifacts'].items():
 assert hashlib.sha256((out/name).read_bytes()).hexdigest()==digest
paths=['next_agent_prompt.md','AGENTS.md','GLOSSARY.md','.scratch/ticket-harness/spec.md','.scratch/ticket-harness/issues/24-own-milestone-review-and-checkpoint-continuation.md']
paths += [str(p) for p in Path('docs/agents').glob('*.md')]
paths += [str(p) for p in Path('docs/adr').glob('*.md')]
paths += ['.agents/skills/'+p+'/SKILL.md' for p in ('custom/implement-with-checkboxes','custom/test-strategy','matt-pocock/tdd','matt-pocock/codebase-design','microsoft/microsoft_oop')]
paths += [str(out/n) for n in capture['artifacts']]
paths += [str(out/'24-review-round1-capture.json'),str(out/'24-finding-history.md')]
result=dict(actor='/root/repair24_1',settings=dict(configured_model='GPT-6.1 Sol',reasoning='Medium',active_context_target='<=250000 advisory',backend_delivery_enforcement_and_telemetry='unavailable'),baseline=capture['original_baseline'],rejected_source=capture['assessed_source'],head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),originals_unchanged=True,instruction_and_context_identities={p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in paths},worktree_at_capture=subprocess.check_output(['git','status','--short'],text=True))
(out/'24-repair1-start.json').write_text(json.dumps(result,indent=2)+'\n')
