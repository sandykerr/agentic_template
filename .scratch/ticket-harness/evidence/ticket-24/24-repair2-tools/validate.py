"""Validate final repair evidence, then optionally bind frozen bytes to an exact commit."""
import hashlib,json,re,subprocess,sys
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence')
frozen=json.loads((out/'24-repair2-final-source.json').read_text())
for name,digest in frozen['source_hashes'].items():
 assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==digest,name
results=json.loads((out/'24-repair2-final-check-results.json').read_text())
assert len(results)==6 and all(r['exit']==0 for r in results)
assert '559 passed' in Path(results[0]['log']).read_text()
for round_number in (1,2):
 capture=json.loads((out/f'24-review-round{round_number}-capture.json').read_text())
 for name,digest in capture['artifacts'].items():assert hashlib.sha256((out/name).read_bytes()).hexdigest()==digest
producer=json.loads((out/'24-checkpoint/producer.json').read_text())
consumer=json.loads((out/'24-repair2-checkpoint/continuation-final.json').read_text())
for name,digest in producer['source_hashes'].items():
 assert hashlib.sha256(subprocess.check_output(['git','show',frozen['baseline']+':'+name])).hexdigest()==digest
 assert consumer['consumer_hashes'][name]==frozen['source_hashes'][name]
assert consumer['final']['outcome']=='completed'
archive=json.loads((out/'24-repair2-capture-audit.json').read_text())
assert archive['scenarios']==559
optional=json.loads((out/'24-repair2-focused-raw-audit.json').read_text())
assert optional['exit']==130 and not optional['completed'] and not optional['passing_gate']
assert json.loads((out/'24-repair2-red-captured.json').read_text())['exit']==1
assert json.loads((out/'24-repair2-green-captured.json').read_text())['exit']==0
for doc in ('24-repair2-report.md','24-repair2-review-packet.md'):
 for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',(out/doc).read_text()):
  if not target.startswith(('http:','https:','#')):
   path=out/target.split('#')[0]
   if path.name=='24-repair2-committed-source.json':continue
   assert path.exists(),(doc,target)
tool_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((out/'24-repair2-tools').glob('*.py'))}
(out/'24-repair2-tool-identities.json').write_text(json.dumps(tool_hashes,indent=2)+'\n')
summary=dict(frozen_identities=len(frozen['source_hashes']),final_commands=len(results),all_exit_zero=True,original_reports_unchanged=True,genuine_old_producer_and_final_consumer_match=True,links_resolve_except_pending_postcommit_audit=True,raw_capture_scenarios=archive['scenarios'])
if len(sys.argv)>1:
 commit=subprocess.check_output(['git','rev-parse',sys.argv[1]],text=True).strip()
 rows=[]
 for name,digest in frozen['source_hashes'].items():
  raw=subprocess.check_output(['git','show',commit+':'+name]);actual=hashlib.sha256(raw).hexdigest();assert actual==digest,name
  rows.append(dict(path=name,sha256=digest,committed_blob=subprocess.check_output(['git','rev-parse',commit+':'+name],text=True).strip(),matches_frozen_and_worktree=True))
 (out/'24-repair2-committed-source.json').write_text(json.dumps(dict(commit=commit,baseline=frozen['baseline'],identities=rows,checks='24-repair2-final-check-results.json',audit=summary),indent=2)+'\n')
 summary['commit']=commit
 summary['links_resolve_including_postcommit_audit']=True
print(json.dumps(summary))
