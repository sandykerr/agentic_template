from pathlib import Path
from urllib.parse import unquote
import datetime,hashlib,json,re,gzip
R=Path('/home/ajkerr1/development/agentic_template');E=R/'.scratch/ticket-harness/evidence';O=Path('/tmp/ticket19-review3')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def finals(rows):return ['\n'.join(x['text'] for x in row['payload'].get('content',[]) if x.get('type')=='output_text') for row in rows if row['type']=='response_item' and row['payload'].get('type')=='message' and row['payload'].get('role')=='assistant' and row['payload'].get('phase')=='final_answer']
records=[];timing=[]
for folder in ['19-evaluation','19-evaluation-g2','19-evaluation-g3','19-evaluation-g4','19-evaluation-g5']:
 p=E/folder;d=json.loads((p/'declaration-capture.json').read_text());assert sha(p/'declaration.md')==d['declaration_sha256'];assert sha(p/'source-manifest.json')==d['source_manifest_sha256']
 assignments=json.loads((p/'assignments.json').read_text())['assignments'];assert len(assignments)==2
 for row in assignments:
  assert datetime.datetime.fromisoformat(d['declared_at_utc'])<datetime.datetime.fromisoformat(row['timestamp'].replace('Z','+00:00'));assert row['settings']=={'fork_turns':'none','model':'gpt-6.1-sol','reasoning_effort':'high'},row
  label=row.get('label',row.get('axis'));timing.append({'folder':folder,'assignment':row})
# G1's capture provenance omits session path; resolve through its retained session identity.
for axis in ['spec','standards']:
 retained=json.loads((E/f'19-evaluation/{axis}-g1-tool-evidence.json').read_text());identity=next(r for r in retained if r['type']=='session_identity');sid=identity['id'];matches=list(Path('/home/ajkerr1/.codex/sessions/2026/11/10').glob('*'+sid+'.jsonl'));assert len(matches)==1
 rows=[json.loads(l) for l in matches[0].read_text().splitlines()];allfinal=finals(rows);raw=E/f'19-evaluation/{axis}-g1-raw.md';assert raw.read_text()==allfinal[0]
 records.append({'label':axis+'-g1','session':str(matches[0]),'original_report_sha256':sha(raw),'all_final_count_including_preservation_followup':len(allfinal),'first_original_match':True})
probe=E/'19-repair-c5-skill-probe';cap=json.loads((probe/'capture.json').read_text());lines=Path(cap['session_path']).read_bytes().splitlines(keepends=True);selected=[];rows=[json.loads(l) for l in lines]
for line,row in zip(lines,rows):
 p=row['payload']
 if row['type']=='response_item' and (p.get('type') in ['function_call','function_call_output','custom_tool_call','custom_tool_call_output','agent_message'] or (p.get('type')=='message' and p.get('role')=='assistant' and p.get('phase')=='final_answer')):selected.append(line)
assert b''.join(selected)==gzip.decompress((probe/'original-tool-and-final-records.jsonl.gz').read_bytes());assert (probe/'original-final.md').read_text()==finals(rows)[0]
# Validate every current recorded link target and anchor directly, separate from old checker.
check=json.loads((E/'19-repair-c5-check-results-20261110T180103445335Z.json').read_text());links=[]
def anchors(path):
 out=[];counts={}
 for line in path.read_text().splitlines():
  m=re.match(r'^#{1,6}\s+(.*)',line)
  if not m:continue
  name=re.sub(r'[^\w\- ]','',m.group(1).lower()).replace(' ','-');i=counts.get(name,0);counts[name]=i+1;out.append(name+('-'+str(i) if i else ''))
 return out
for row in check['local_links']:
 p=R/row['from'];name,_,fragment=unquote(row['href']).partition('#');name=re.sub(r':\d+$','',name);target=(p.parent/name).resolve() if name else p;assert target.exists(),row
 if fragment:assert fragment in anchors(target),(row,anchors(target))
 links.append(row)
summary={'G1_original_finals':records,'all_declaration_settings':timing,'probe_raw_original_line_match':True,'probe_actual_final_match':True,'probe_saved_display_equivalent':False,'probe_saved_display_delta':'Two displayed quote-escaping representations plus terminal newline; original final and actual observations independently retained. Not relabeled as byte-identical.','current_links_verified':len(links),'limits':'Plaintext original session finals and selected original records verified. Opaque task messages/configuration do not prove decrypted delivery, effectiveness, backend enforcement, measured context or technical isolation.'}
(O/'spec-provenance.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({'G1_original_matches':2,'declarations':5,'fresh_configured_axes':len(timing),'probe_lossless_actual_match':True,'links':len(links)}))
