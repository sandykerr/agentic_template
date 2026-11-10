from pathlib import Path
import ast,datetime,hashlib,json,re,subprocess
from urllib.parse import unquote
ROOT=Path('/home/ajkerr1/development/agentic_template');E=ROOT/'.scratch/ticket-harness/evidence';O=Path('/tmp/ticket19-review3'); S=Path('/home/ajkerr1/.codex/sessions/2026/11/10')
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
actors={}
for f in S.glob('rollout-*.jsonl'):
 with f.open() as h:r=json.loads(h.readline())
 p=r.get('payload',{});source=p.get('source',{})
 if isinstance(source,dict):
  a=source.get('subagent',{}).get('thread_spawn',{}).get('agent_path')
  if a:actors[a]=f
results=[]; inv=[]
for stage in ['19-evaluation','19-evaluation-g2','19-evaluation-g3','19-evaluation-g4','19-evaluation-g5']:
 d=E/stage; declaration=load(d/'declaration-capture.json'); rows=load(d/'assignments.json')['assignments']
 for r in rows:
  assert r['settings']=={'fork_turns':'none','model':'gpt-6.1-sol','reasoning_effort':'high'}
  path=actors[r['assignment']];session=[json.loads(s) for s in path.read_text().splitlines()];final=[];tools=[]
  for event in session:
   p=event['payload']
   if event['type']=='turn_context':assert p['model']=='gpt-6.1-sol' and p['effort']=='high'
   if event['type']=='response_item' and p.get('type')=='message' and p.get('role')=='assistant' and p.get('phase')=='final_answer':final.append('\n'.join(c['text'] for c in p['content'] if c.get('type')=='output_text'))
   if event['type']=='response_item' and p.get('type') in ['function_call','custom_tool_call']:
    text=p.get('input',p.get('arguments',''));tools.append({'tool':p.get('name'),'input':text})
  assert final and final[0]==(d/(r['label']+'-raw.md')).read_text(),r['label']
  for p in d.glob(r['label']+'-source-records.json'):
   for event in load(p):
    if event.get('type')=='response_item':assert event in session,(p,event.get('type'))
  results.append({'label':r['label'],'actor':r['assignment'],'session':str(path),'original_sha256':sha(d/(r['label']+'-raw.md')),'final_messages':len(final),'configured_and_observed':'Sol High, configured fork-none','source_record_tools':len(tools)})
  # Retain full inventory locally, print only bounded non-report commands to review.
  inv.append({'label':r['label'],'tools':tools})
probe=E/'19-repair-c5-skill-probe';p=load(probe/'capture.json');session=[json.loads(s) for s in Path(p['session_path']).read_text().splitlines()];final=[];probe_tools=[]
for r in session:
 q=r.get('payload',{})
 if r['type']=='turn_context':assert q['model']=='gpt-6.1-sol' and q['effort']=='medium'
 if r['type']=='response_item' and q.get('type')=='message' and q.get('phase')=='final_answer':final.append('\n'.join(c['text'] for c in q['content'] if c.get('type')=='output_text'))
 if r['type']=='response_item' and q.get('type') in ['function_call','custom_tool_call']:
  assert q.get('name')!='spawn_agent';probe_tools.append(q.get('input',q.get('arguments','')))
assert len(final)==1 and final[0]==(probe/'original-final.md').read_text()
# Independently resolve the retained final checkpoint link list to actual anchors.
check=load(E/'19-repair-c5-check-results-20261110T180103445335Z.json')
def anchors(p):
 seen={};out=set()
 for line in p.read_text().splitlines():
  if not re.match(r'^#{1,6} ',line):continue
  title=re.sub(r'^#{1,6} ','',line).strip(); title=re.sub(r'<[^>]+>','',title); slug=re.sub(r'[^\w\- ]','',title.lower()).replace(' ','-');n=seen.get(slug,0);seen[slug]=n+1;out.add(slug+('-'+str(n) if n else ''))
 return out
for row in check['local_links']:
 src=ROOT/row['from'];name,_,frag=unquote(row['href']).partition('#');name=re.sub(r':\d+$','',name);dest=(src.parent/name).resolve() if name else src
 assert dest.exists(),row
 if frag:assert frag in anchors(dest),(row,frag)
changed=subprocess.check_output(['git','-C',str(ROOT),'diff','--name-only','f2929e7...8e2c826']).decode().splitlines()
for p in changed:
 if p.endswith('.py'):ast.parse((ROOT/p).read_text(),filename=p)
result={'result':'pass','actual_originals':results,'probe_original_final_verified':True,'probe_tools':len(probe_tools),'links':len(check['local_links']),'changed_python_artifacts_parsed':sum(p.endswith('.py') for p in changed),'limits':'Actual sessions/configuration/first raw outputs and selected tool records match; encrypted delivery and backend/context enforcement remain unproven.'}
(O/'standards-provenance.json').write_text(json.dumps(result,indent=2)+'\n');(O/'standards-all-tool-inventory.json').write_text(json.dumps(inv,indent=2)+'\n');(O/'standards-probe-tool-inventory.json').write_text(json.dumps(probe_tools,indent=2)+'\n');print(json.dumps(result,indent=2))
