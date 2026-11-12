"""Validate final repair evidence, then optionally bind frozen bytes to an exact commit."""
import hashlib,json,re,subprocess,sys
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence')
frozen=json.loads((out/'24-repair1-final-source.json').read_text())
for name,digest in frozen['source_hashes'].items():
 assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==digest,name
results=json.loads((out/'24-repair1-final-check-results.json').read_text())
assert len(results)==6 and all(r['exit']==0 for r in results)
assert '556 passed' in Path(results[0]['log']).read_text()
capture=json.loads((out/'24-review-round1-capture.json').read_text())
for name,digest in capture['artifacts'].items():assert hashlib.sha256((out/name).read_bytes()).hexdigest()==digest
producer=json.loads((out/'24-checkpoint/producer.json').read_text())
consumer=json.loads((out/'24-repair1-checkpoint/continuation-final.json').read_text())
for name,digest in producer['source_hashes'].items():
 assert hashlib.sha256(subprocess.check_output(['git','show',frozen['baseline']+':'+name])).hexdigest()==digest
 assert consumer['consumer_hashes'][name]==frozen['source_hashes'][name]
assert consumer['final']['outcome']=='completed'
archive=json.loads((out/'24-repair1-capture-audit.json').read_text())
assert archive['scenarios']==556
for doc in ('24-repair1-report.md','24-repair1-review-packet.md'):
 for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',(out/doc).read_text()):
  if not target.startswith(('http:','https:','#')):
   path=out/target.split('#')[0]
   if path.name=='24-repair1-committed-source.json':continue
   assert path.exists(),(doc,target)
tool_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((out/'24-repair1-tools').glob('*.py'))}
(out/'24-repair1-tool-identities.json').write_text(json.dumps(tool_hashes,indent=2)+'\n')
summary=dict(frozen_identities=len(frozen['source_hashes']),final_commands=len(results),all_exit_zero=True,original_reports_unchanged=True,genuine_old_producer_and_final_consumer_match=True,links_resolve_except_pending_postcommit_audit=True,raw_capture_scenarios=archive['scenarios'])
if len(sys.argv)>1:
 commit=subprocess.check_output(['git','rev-parse',sys.argv[1]],text=True).strip()
 rows=[]
 for name,digest in frozen['source_hashes'].items():
  raw=subprocess.check_output(['git','show',commit+':'+name]);actual=hashlib.sha256(raw).hexdigest();assert actual==digest,name
  rows.append(dict(path=name,sha256=digest,committed_blob=subprocess.check_output(['git','rev-parse',commit+':'+name],text=True).strip(),matches_frozen_and_worktree=True))
 (out/'24-repair1-committed-source.json').write_text(json.dumps(dict(commit=commit,baseline=frozen['baseline'],identities=rows,checks='24-repair1-final-check-results.json',audit=summary),indent=2)+'\n')
 summary['commit']=commit
 summary['links_resolve_including_postcommit_audit']=True
print(json.dumps(summary))
