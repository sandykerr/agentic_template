"""Mechanical evidence/link/frozen identity validation, separate from source reviews."""
import hashlib,json,re,subprocess
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence')
frozen=json.loads((out/'24-final-source.json').read_text())
for name,digest in frozen['source_hashes'].items():
 assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==digest,name
 if name.startswith(('tests/','examples/')) or name in ('pyproject.toml','environment.yml'):
  assert hashlib.sha256(subprocess.check_output(['git','show',frozen['baseline']+':'+name])).hexdigest()==digest,name
for name,digest in json.loads((out/'24-tool-identities.json').read_text()).items():
 assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==digest,name
for doc in ('24-implementation-report.md','24-review-packet.md'):
 p=out/doc
 for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',p.read_text()):
  if not target.startswith(('http:','https:','#')):
   assert (p.parent/target.split('#')[0]).exists(),(doc,target)
results=json.loads((out/'24-final-check-results.json').read_text())
assert len(results)==6 and all(r['exit']==0 for r in results)
assert json.loads((out/'24-focused-check-results.json').read_text())[0]['exit']==0
print(json.dumps(dict(frozen_identities=len(frozen['source_hashes']),source_matches=True,tests_examples_packaging_unchanged=True,final_commands=len(results),all_exit_zero=True,report_links_resolve=True,tool_identities_match=True)))
