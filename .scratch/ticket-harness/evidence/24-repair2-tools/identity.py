"""Capture actual source identities for a named repair phase."""
import hashlib,json,subprocess,sys
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence')
paths=list(json.loads((out/'24-repair1-final-source.json').read_text())['source_hashes'])
result=dict(baseline='ed017ae0c2b96769f31c710cfb4ff4708989b446',head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),source_hashes={n:hashlib.sha256(Path(n).read_bytes()).hexdigest() for n in paths},scope='Actual runtime/test/example/config bytes; unrelated preexisting edits excluded',diff=subprocess.check_output(['git','diff','--','ticket_harness','tests','examples'],text=True))
(out/f'24-repair2-{sys.argv[1]}-source.json').write_text(json.dumps(result,indent=2)+'\n')
