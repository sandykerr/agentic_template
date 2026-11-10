"""Retain independent preparation-only authoring test; never generate its judgment."""
from pathlib import Path
import gzip,hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[3];EV=ROOT/'.scratch/ticket-harness/evidence'
OUT=EV/'19-repair-c5-skill-probe';RAW=Path('/tmp/reviewer-authoring19')
LOGS=Path('/home/ajkerr1/.codex/sessions/2026/11/10');OWN=LOGS/'rollout-2026-11-10T12-33-59-01a1c686-1785-7f11-b1b0-fafc5e4158f3.jsonl'
TARGET='/root/repair19_branch/authoring_skill_probe'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,data):
    if p.exists():assert p.read_bytes()==data,('preserved original differs',p)
    else:p.write_bytes(data)
assert not OUT.exists();OUT.mkdir()
declared=json.loads((EV/'19-repair-c5-skill-preflight-declaration.json').read_text())
for name,digest in declared['input_sha256'].items():assert sha(RAW/name)==digest,name
assert set(declared['input_sha256'])=={str(p.relative_to(RAW)) for p in (RAW/'inputs').rglob('*') if p.is_file()}|{'request.txt'}
shutil.copytree(RAW/'inputs',OUT/'inputs');shutil.copytree(RAW/'outputs',OUT/'outputs');shutil.copy2(RAW/'request.txt',OUT/'request.txt')
dispatch=[]
for line in OWN.read_text().splitlines():
    row=json.loads(line);p=row['payload']
    if row['type']=='response_item' and p.get('type')=='function_call' and p.get('name')=='spawn_agent':
        args=json.loads(p['arguments'])
        if args.get('task_name')=='authoring_skill_probe':dispatch.append(row)
assert len(dispatch)==1
write(OUT/'dispatch.json',(json.dumps(dispatch[0],indent=2)+'\n').encode())
args=json.loads(dispatch[0]['payload']['arguments']);assert {k:args[k] for k in ['fork_turns','model','reasoning_effort']}==declared['requested_settings']
paths=[]
for path in LOGS.glob('rollout-*.jsonl'):
    with path.open() as f:first=json.loads(f.readline())
    source=first['payload'].get('source',{})
    if isinstance(source,dict) and source.get('subagent',{}).get('thread_spawn',{}).get('agent_path')==TARGET:paths.append(path)
assert len(paths)==1;path=paths[0];selected=[];raw_lines=[];final=[]
for line in path.read_bytes().splitlines(keepends=True):
    row=json.loads(line);p=row['payload']
    if row['type']=='session_meta':selected.append({'timestamp':row['timestamp'],'type':'session_identity','id':p['id'],'cwd':p['cwd'],'source':p['source'],'model_provider':p.get('model_provider')})
    elif row['type']=='turn_context':selected.append({'timestamp':row['timestamp'],'type':'observed_turn_settings','settings':{k:p[k] for k in ['model','effort','reasoning_effort','model_provider','cwd'] if k in p}})
    elif row['type']=='response_item' and p.get('type') in ['function_call','function_call_output','custom_tool_call','custom_tool_call_output','agent_message']:
        selected.append(row);raw_lines.append(line)
    elif row['type']=='response_item' and p.get('type')=='message' and p.get('role')=='assistant' and p.get('phase')=='final_answer':
        final.append('\n'.join(x['text'] for x in p.get('content',[]) if x.get('type')=='output_text'));raw_lines.append(line)
assert len(final)==1
write(OUT/'original-final.md',final[0].encode());write(OUT/'source-records.json',(json.dumps(selected,indent=2)+'\n').encode())
raw=b''.join(raw_lines);compressed=gzip.compress(raw,mtime=0);write(OUT/'original-tool-and-final-records.jsonl.gz',compressed);assert gzip.decompress(compressed)==raw
manifest={str(p.relative_to(OUT)):sha(p) for p in sorted(OUT.rglob('*')) if p.is_file()}
write(OUT/'capture.json',(json.dumps({'assignment':TARGET,'session_path':str(path),'requested_settings':declared['requested_settings'],'original_final_count':1,'sha256':manifest,'lossless_record_capture':{'path':'original-tool-and-final-records.jsonl.gz','uncompressed_sha256':hashlib.sha256(raw).hexdigest(),'compression':'gzip mtime=0, original selected JSONL line bytes; readable source records separate'},'raw_final_origin':'Exact first plaintext final_answer from identity-verified authoring tester; no reviewer dispatch/calibration authorized','saved_copy_terminal_newline_equivalent':(OUT/'outputs/report.md').read_text().rstrip('\n')==final[0].rstrip('\n'),'limits':'One preparation-only authoring observation on declared earlier skill bytes; final skill has separately identified role-count/reflow correction. No general effectiveness or backend/isolation enforcement proof.'},indent=2)+'\n').encode())
print(json.dumps({'captured':str(OUT.relative_to(ROOT)),'files':len(manifest),'status':'original authoring observation captured; substantive adjudication separate'},indent=2))
