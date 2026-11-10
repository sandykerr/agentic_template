from pathlib import Path
import ast, datetime, difflib, gzip, hashlib, json, os, re, subprocess, sys, tempfile, types
ROOT=Path('/home/ajkerr1/development/agentic_template'); EV=ROOT/'.scratch/ticket-harness/evidence'; OUT=Path('/tmp/ticket19-review3')
BASE='f2929e79cfd5a68f670862775053ae85ba9582b5'; HEAD='8e2c82679a2314e31ebff69accab3743f55f996d'; PREV='ce4e57d77be6dfd695f0ecb15284c5e9d5792b93'
def run(*args,**kw): return subprocess.run(args,capture_output=True,**kw)
def git(*args): return subprocess.check_output(['git','-C',str(ROOT),*args]).decode().strip()
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text())
def mapping(p): return {str(f.relative_to(p)):sha(f) for f in sorted(p.rglob('*')) if f.is_file()}
assert git('rev-parse','HEAD')==HEAD and git('merge-base',BASE,HEAD)==BASE and not git('status','--porcelain')
changed=git('diff','--name-only',BASE+'...'+HEAD).splitlines(); assert all(p.startswith(('.scratch/ticket-harness/','.agents/skills/custom/','docs/agents/')) for p in changed)
corpus=[]; stages=[EV/('19-evaluation'+s) for s in ['', '-g2','-g3','-g4','-g5']]
for stage in stages:
 m=load(stage/'source-manifest.json'); assert m==mapping(stage/'snapshot'); digest=hashlib.sha256(json.dumps(m,sort_keys=True).encode()).hexdigest(); assert digest==(stage/'corpus-identity.txt').read_text().strip()
 for name,h in load(stage/'review-capture.json')['sha256'].items(): assert sha(stage/name)==h,(stage,name)
 corpus.append({'stage':stage.name,'aggregate':digest,'files':len(m)})
for i in range(1,5):
 a,b=load(stages[i-1]/'source-manifest.json'),load(stages[i]/'source-manifest.json')
 delta=[p for p in a if a[p]!=b[p]]; corpus[i]['delta']=delta
 if i>1: assert all(a[p]==b[p] for p in a if p.startswith('guidance/'))
 assert all(a[p]==b[p] for p in a if p.endswith('/CONTRACT.md') or p.startswith(('cases/a3/','cases/c2/','cases/e4/','cases/g1/')))
for c in [2,3,4]:
 p=EV/f'19-repair-c{c}-preservation.json'; assert load(p)['sha256']==mapping(stages[c-1])
for p in ['19-review-capture.json','19-review-round2-capture.json']:
 for f,h in load(EV/p)['sha256'].items(): assert sha(EV/f)==h,(p,f)
protected=set(git('ls-tree','-r','--name-only',PREV).splitlines())-{'docs/agents/reviewer-evaluation.md','.scratch/ticket-harness/reviews/ticket-19.md','.scratch/ticket-harness/evidence/19-finding-history.md'}
assert not protected.intersection(git('diff','--name-only',PREV,HEAD).splitlines())
current=load(EV/'19-repair-c5-check-results-20261110T180103445335Z.json')
for key in ['checked_document_sha256','current_evidence_sha256']:
 for p,h in current[key].items(): assert sha(ROOT/p)==h,(key,p)
assert len(current['local_links'])==182 and current['protected_previous_paths']==len(protected)==6742
# Actual C5 raw finals, session identity/settings, source/tool records and parent calls.
provenance=load(stages[-1]/'capture-provenance.json'); inventory=[]
for label,p in provenance.items():
 rows=[json.loads(x) for x in Path(p['session_path']).read_text().splitlines()]
 finals=[]; tools=[]
 for r in rows:
  q=r.get('payload',{})
  if r['type']=='session_meta': assert q['source']['subagent']['thread_spawn']['agent_path']=='/root/repair19_branch/corpus_'+label.replace('-','_')
  if r['type']=='turn_context': assert q['model']=='gpt-6.1-sol' and q['effort']=='high'
  if r['type']=='response_item' and q.get('type')=='message' and q.get('role')=='assistant' and q.get('phase')=='final_answer': finals.append('\n'.join(v['text'] for v in q['content'] if v.get('type')=='output_text'))
  if r['type']=='response_item' and q.get('type') in ['function_call','custom_tool_call']: tools.append(q)
 assert len(finals)==1 and finals[0]==(stages[-1]/(label+'-raw.md')).read_text()
 retained=load(stages[-1]/(label+'-source-records.json'))
 for r in retained:
  if r.get('type')=='response_item': assert r in rows
 inventory.append({'label':label,'tools':tools})
# Probe capture is lossless, inputs immutable, decision held; exact tested/final delta.
probe=EV/'19-repair-c5-skill-probe'; cap=load(probe/'capture.json')
for p,h in cap['sha256'].items(): assert sha(probe/p)==h,p
raw=gzip.decompress((probe/cap['lossless_record_capture']['path']).read_bytes()); assert hashlib.sha256(raw).hexdigest()==cap['lossless_record_capture']['uncompressed_sha256']
delta=load(EV/'19-repair-c5-skill-final-delta.json'); tested=probe/'inputs/SKILL.md'; final=ROOT/'.agents/skills/custom/evaluate-reviewers/SKILL.md'
assert sha(tested)==delta['tested_skill_snapshot_sha256'] and sha(final)==delta['final_skill_sha256']
assert ''.join(difflib.unified_diff(tested.read_text().splitlines(True),final.read_text().splitlines(True),fromfile='probe-supplied-skill',tofile='final-authored-skill'))==delta['exact_diff']
held=load(probe/'outputs/evaluator/held-declaration.json'); assert held['actual_reviewer_assignments']==held['actual_trials']==0
# Narrow exact-path whitespace authorization, with full failure retained.
exception='.scratch/ticket-harness/evidence/19-evaluation-g3/spec-c3-reviewer-saved.md'; p=ROOT/exception
assert sha(p)=='75dbfbdde31879ceeb2f35bb50fb6fe0a318f09cfbb6d15fb6fb76502a40f84d' and len(p.read_bytes())-len(p.read_bytes().rstrip(b'\n'))==2
ws=[]
for args,expected in [(['diff','--check',BASE+'...'+HEAD],2),(['diff','--check',BASE+'...'+HEAD,'--','.',':(exclude)'+exception],0),(['-c','core.whitespace=-blank-at-eof','diff','--check',BASE+'...'+HEAD,'--',exception],0)]:
 r=run('git','-C',str(ROOT),*args,text=True); assert r.returncode==expected; ws.append({'args':args,'exit':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
# Compile fixture modules from exact committed blobs without repository imports/bytecode.
def module(stage,case,name):
 path=f'.scratch/ticket-harness/evidence/{stage}/snapshot/cases/{case}/{name}.py'; code=subprocess.check_output(['git','-C',str(ROOT),'show',HEAD+':'+path]); m=types.ModuleType('audit_'+case+'_'+name);sys.modules[m.__name__]=m;exec(compile(code,path,'exec'),m.__dict__);return m
m=module('19-evaluation-g5','h8','attempt'); ident={'nested':[1]}; a=m.Attempt(ident); ident['nested'].append(2); assert a.snapshot()[0]['id']=={'nested':[1]}
def rejects(fn):
 try: fn()
 except ValueError:return
 raise AssertionError('expected rejection')
before=a.snapshot();rejects(a.complete);rejects(lambda:a.submit({}));assert a.snapshot()==before
rev={'nested':[3]};a.submit(rev);rev['nested'].append(4);snap=a.snapshot();snap[0]['revision']['nested'].append(5);snap[1]['id']['nested'].append(6);assert a.snapshot()[0]['revision']=={'nested':[3]};assert a.snapshot()[0]['id']=={'nested':[1]}
before=a.snapshot();rejects(lambda:a.submit('again'));assert a.snapshot()==before;a.complete();before=a.snapshot();rejects(a.complete);assert a.snapshot()==before
old=module('19-evaluation','h8','attempt'); ident={'nested':[1]}; a=old.Attempt(ident);ident['nested'].append(2);assert a.snapshot()[0]['id']['nested']==[1,2]
plan=module('19-evaluation-g5','d9','plan'); parsed=plan.parse('b:a+a,a:');assert [t.id for t in parsed]==['b','a'] and parsed[0].dependencies==('a','a')
for text in ['a:+','a:b+,b:','a:a','a:b','a:,a:']:rejects(lambda text=text:plan.parse(text))
assert len(plan.parse(','.join(f'{i}:{i+1}' for i in range(1500))+',1500:'))==1501
io=module('19-evaluation-g5','f6','io_ops');
for timeout in [None,float('inf'),float('nan')]:rejects(lambda timeout=timeout:io.invoke([sys.executable,'-c','pass'],OUT,timeout))
with tempfile.TemporaryDirectory(prefix='standards-exact-',dir=OUT) as td:
 td=Path(td); p=td/'destination';p.write_text('old')
 try:io.atomic_write(p,'\udcff')
 except UnicodeEncodeError:pass
 else:raise AssertionError('expected encoding error')
 assert p.read_text()=='old' and list(td.iterdir())==[p];io.atomic_write(p,'new');assert p.read_text()=='new'
 r=io.invoke([sys.executable,'-c','import sys; print("ok");sys.exit(7)'],td,2);assert r.returncode==7 and r.stdout=='ok\n'
 # Real Git old/current branch and environment routing, filesystem byte transport.
 def make(repo):
  repo.mkdir();subprocess.check_call(['git','init','-q','-b','main',str(repo)]);subprocess.check_call(['git','-C',str(repo),'-c','user.name=a','-c','user.email=a@b','commit','-q','--allow-empty','-m','init']);return subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD']).decode().strip()
 repo=td/'repo';base=make(repo);subprocess.check_call(['git','-C',str(repo),'tag','main'])
 g=module('19-evaluation-g5','b7','git_ops');sys.modules['git_ops']=g;caller=module('19-evaluation-g5','b7','caller');assert caller.preflight(repo,'main',base)==(repo.resolve(),'main')
 oldg=module('19-evaluation-g4','b7','git_ops');sys.modules['git_ops']=oldg;oldcaller=module('19-evaluation-g4','b7','caller');rejects(lambda:oldcaller.preflight(repo,'main',base))
 foreign=td/'foreign';make(foreign);original=os.environ.copy();os.environ['GIT_DIR']=str(foreign/'.git');os.environ['GIT_WORK_TREE']=str(foreign)
 try:assert caller.preflight(repo,'main',base)==(repo.resolve(),'main')
 finally:os.environ.clear();os.environ.update(original)
 paths=[]
 for suffix in ['space ','cr\r','lf\n',os.fsdecode(b'nonutf8-\xff')]:
  rp=td/suffix;b=make(rp);assert caller.preflight(rp,'main',b)==(rp.resolve(),'main');paths.append(repr(suffix))
result={'result':'pass','baseline':BASE,'source':HEAD,'commits':git('log','--oneline',BASE+'..'+HEAD).splitlines(),'changed_files':len(changed),'protected_previous_paths':len(protected),'corpora':corpus,'whitespace':ws,'C5_report_session_verified':list(provenance),'authoring_tested_skill':sha(tested),'authoring_final_skill':sha(final),'behavior':['old h8 alias reproduced; current nested ingress/output isolation and invalid transition checks pass','old C4 branch/tag false rejection reproduced; C5 requested branch/tag accepted','ambient foreign routing cleared','space/CR/LF/nonUTF8 Git roots retained','d9 missing operands/errors/order/repeated dependencies/1501 forward chain','f6 nonfinite guard/encoding cleanup/complete replacement/nonzero capture'],'limits':'Bounded exact-fixture observations, no production tests or comprehensive OS/backend proof'}
(OUT/'standards-audit.json').write_text(json.dumps(result,indent=2)+'\n');(OUT/'standards-c5-tool-inventory.json').write_text(json.dumps(inventory,indent=2)+'\n');print(json.dumps(result,indent=2))
