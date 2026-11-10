"""Preserve actual independent assignment/report records at new paths only."""
from pathlib import Path
import hashlib, json, sys
OUT=Path(__file__).resolve().parent
LOGS=Path('/home/ajkerr1/.codex/sessions/2026/11/10')
OWN=LOGS/'rollout-2026-11-10T12-33-59-01a1c686-1785-7f11-b1b0-fafc5e4158f3.jsonl'
def rows(p):return [json.loads(x) for x in p.read_text().splitlines()]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def create(p,value):
    data=json.dumps(value,indent=2)+'\n'
    if p.exists():assert p.read_text()==data,('immutable artifact differs',str(p))
    else:p.write_text(data)
assignments=[]
for row in rows(OWN):
    p=row['payload']
    if row['type']!='response_item' or p.get('type')!='function_call' or p.get('name')!='spawn_agent':continue
    args=json.loads(p['arguments'])
    if args.get('task_name') not in ['corpus_spec_c5','corpus_standards_c5']:continue
    label=args['task_name'].removeprefix('corpus_').replace('_','-')
    create(OUT/(label+'-dispatch.json'),row)
    prompt=OUT/(label+'-input.txt')
    assignments.append({'label':label,'assignment':'/root/repair19_branch/'+args['task_name'],'timestamp':row['timestamp'],'settings':{k:args[k] for k in ['fork_turns','model','reasoning_effort']},'active_context_target':250000,'dispatch_path':label+'-dispatch.json','dispatch_sha256':sha(OUT/(label+'-dispatch.json')),'known_readable_prompt_path':prompt.name,'known_readable_prompt_sha256':sha(prompt),'prompt_origin':'Exact known author text saved before dispatch, then supplied as spawn message. Opaque serialization is not decrypted-delivery/effectiveness proof.'})
assert len(assignments)==2
create(OUT/'assignments.json',{'assignments':assignments,'limits':'Requested/observed settings and advisory context target; model/delivery/active-context/hard enforcement telemetry unavailable, filesystem isolation advisory.'})
if '--final' in sys.argv:
    provenance={}
    for assignment in assignments:
        label=assignment['label'];target=assignment['assignment'];matches=[]
        for path in LOGS.glob('rollout-*.jsonl'):
            with path.open() as f:first=json.loads(f.readline())
            source=first['payload'].get('source',{})
            if isinstance(source,dict) and source.get('subagent',{}).get('thread_spawn',{}).get('agent_path')==target:matches.append(path)
        assert len(matches)==1,(target,matches)
        path=matches[0];selected=[];final=[]
        for row in rows(path):
            p=row['payload']
            if row['type']=='session_meta':selected.append({'timestamp':row['timestamp'],'type':'session_identity','id':p['id'],'cwd':p['cwd'],'source':p['source'],'model_provider':p.get('model_provider')})
            elif row['type']=='turn_context':selected.append({'timestamp':row['timestamp'],'type':'observed_turn_settings','settings':{k:p[k] for k in ['model','effort','reasoning_effort','model_provider','cwd'] if k in p}})
            elif row['type']=='response_item' and p.get('type') in ['function_call','function_call_output','custom_tool_call','custom_tool_call_output','agent_message']:selected.append(row)
            elif row['type']=='response_item' and p.get('type')=='message' and p.get('role')=='assistant' and p.get('phase')=='final_answer':final.append('\n'.join(x['text'] for x in p.get('content',[]) if x.get('type')=='output_text'))
        assert len(final)==1,(label,'exactly one original required',len(final))
        raw=OUT/(label+'-raw.md')
        if raw.exists():assert raw.read_text()==final[0]
        else:raw.write_text(final[0])
        create(OUT/(label+'-source-records.json'),selected)
        axis=label.removesuffix('-c5');original=Path('/tmp')/f'development-review-19-{axis}-c5-report.md';saved=OUT/(label+'-reviewer-saved.md')
        if saved.exists():assert saved.read_bytes()==original.read_bytes()
        else:saved.write_bytes(original.read_bytes())
        provenance[label]={'session_path':str(path),'original_final_count':1,'raw_report_origin':'Exact first plaintext assistant final_answer from identity-verified independent child session','raw_report_sha256':sha(raw),'reviewer_saved_sha256':sha(saved),'saved_byte_match':raw.read_bytes()==saved.read_bytes(),'saved_match_ignoring_terminal_newline':raw.read_text().rstrip('\n')==saved.read_text().rstrip('\n'),'source_records_sha256':sha(OUT/(label+'-source-records.json')),'known_prompt_origin':'Exact readable author text saved before dispatch, no log decryption/transcription or report-preservation followup','limits':'Opaque received serialization/settings and advisory permission bits are not decrypted-delivery, effectiveness or backend/hard-context enforcement proof.'}
    create(OUT/'capture-provenance.json',provenance)
    names=[p for p in OUT.iterdir() if p.is_file() and (p.name.endswith(('-raw.md','-source-records.json','-dispatch.json','-input.txt','-reviewer-saved.md')) or p.name in ['assignments.json','capture-provenance.json'])]
    create(OUT/'review-capture.json',{'sha256':{p.name:sha(p) for p in sorted(names)},'origin':'Actual identity-verified independent child settings/source/tool/received records, exact original plaintext finals and separate reviewer-saved copies; pre-saved author prompts.'})
print('Captured C5 assignments'+(' and both originals' if '--final' in sys.argv else ''))
