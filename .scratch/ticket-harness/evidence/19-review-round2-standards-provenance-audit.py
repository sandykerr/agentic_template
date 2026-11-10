from pathlib import Path
import datetime, hashlib, json, re
from urllib.parse import unquote

ROOT=Path('/home/ajkerr1/development/agentic_template')
OUT=Path('/tmp/ticket19-review2')
EV=ROOT/'.scratch/ticket-harness/evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def j(p):return json.loads(p.read_text())
parent_paths=[Path('/home/ajkerr1/.codex/sessions/2026/11/10')/name for name in ['rollout-2026-11-10T11-19-06-01a1c641-8953-7482-bf78-307a87fa5e90.jsonl','rollout-2026-11-10T11-43-32-01a1c657-e8c7-7561-b2e1-72cba6b15731.jsonl']]
parents=[[json.loads(line) for line in p.read_text().splitlines()] for p in parent_paths]
dispatch_matches=[];declaration_operations=[]
for directory,label,rows in [('19-evaluation','g1',parents[0]),('19-evaluation-g2','g2',parents[1]),('19-evaluation-g3','c3',parents[1]),('19-evaluation-g4','c4',parents[1])]:
    case=EV/directory
    for axis in ['spec','standards']:
        if label=='g1':
            dispatch=j(case/f'{axis}-{label}-assignment.json')
            match=[r for r in rows if r['type']=='response_item' and r['payload'].get('call_id')==dispatch['call_id'] and r['payload'].get('type')=='function_call']
            assert len(match)==1
            original=match[0]
            assert original['timestamp']==dispatch['timestamp']
            assert json.loads(original['payload']['arguments'])==dispatch['arguments']
        else:
            dispatch=j(case/f'{axis}-{label}-dispatch.json')
            assert dispatch in rows
        dispatch_matches.append({'corpus':label,'axis':axis,'original_dispatch_match':True})
    for r in rows:
        if r['type']!='response_item' or r['payload'].get('type') not in ['custom_tool_call','function_call']:continue
        p=r['payload'];text=p.get('input',p.get('arguments',''))
        needle={'g1':'build_corpus.py','g2':'build_corpus_g2.py','c3':'19-repair-build-c3.py','c4':'19-repair-build-c4.py'}[label]
        if needle in text:
            declaration_operations.append({'corpus':label,'timestamp':r['timestamp'],'name':p.get('name'),'input':text if len(text)<8000 else 'Large builder authoring input retained in original session; not recopied.'})
followup=j(EV/'19-evaluation-g4/followup-dispatches.json')
for row in followup['original_calls']+followup['original_receipts']:assert row in parents[1]
assert len(followup['original_calls'])==2
assert sha(EV/'19-evaluation-g4'/followup['known_readable_author_text_path'])==followup['known_readable_author_text_sha256']

def anchors(path):
    result=set();counts={};fenced=False
    for line in path.read_text().splitlines():
        if line.startswith('```'):fenced=not fenced
        if fenced:continue
        match=re.match(r'^#{1,6}\s+(.+?)\s*#*\s*$',line)
        if match:
            heading=re.sub(r'[^\w\- ]','',match[1].lower()).replace(' ','-')
            count=counts.get(heading,0);counts[heading]=count+1
            result.add(heading if not count else f'{heading}-{count}')
    return result
checks=j(EV/'19-repair-check-results-20261110T172627119721Z.json')
links=[]
for row in checks['local_links']:
    path=ROOT/row['from'];href=row['href'];name,_,fragment=unquote(href).partition('#')
    name=re.sub(r':\d+$','',name);target=(path.parent/name).resolve() if name else path
    assert target.exists(),row
    if fragment:assert fragment in anchors(target),row
    links.append(row)
initial=j(EV/'19-review-capture.json')
for p,digest in initial['sha256'].items():assert sha(EV/p)==digest
for row in initial['capture_mapping']:assert sha(EV/row['retained_path'])==row['sha256']
root=j(EV/'19-repair-root-path-capture.json')
for row in root['mapping']:assert sha(EV/row['retained_path'])==row['sha256']
result={'dispatch_matches':dispatch_matches,'declaration_builder_operations':declaration_operations,'C4_original_neutral_followups_match':True,'independently_validated_links':len(links),'initial_review_capture_matches':True,'root_observation_capture_matches':True,'limits':'Known prompts/opaque dispatch and advisory read-only permissions do not prove decrypted delivery, backend effectiveness, isolation or context enforcement.'}
(OUT/'standards-provenance-audit.json').write_text(json.dumps(result,indent=2)+'\n')
identities=j(OUT/'standards-identities.json')
identities['supplemental_audit']={'script_sha256':sha(Path(__file__)),'result_sha256':sha(OUT/'standards-provenance-audit.json'),'command':[str(ROOT/'.micromamba/envs/dev/bin/python'),str(Path(__file__))],'exit':0,'source_originals_dispatches':8,'links':len(links)}
identities['instructions_collaborators']['.agents/skills/microsoft/microsoft_oop/SKILL.md']=sha(ROOT/'.agents/skills/microsoft/microsoft_oop/SKILL.md')
(OUT/'standards-identities.json').write_text(json.dumps(identities,indent=2)+'\n')
print(json.dumps({'result':'pass','original_dispatches':len(dispatch_matches),'neutral_followups':2,'links':len(links),'initial_capture':True,'root_capture':True}))
