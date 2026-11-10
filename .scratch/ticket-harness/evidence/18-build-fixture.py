from pathlib import Path
import subprocess,json,hashlib,shutil
root=Path.cwd(); out=root/'.scratch/ticket-harness/evidence/18-walkthrough'; repo=Path('/tmp/ticket18-fixture')
assert not out.exists() and not repo.exists()
out.mkdir(); repo.mkdir()
def git(*args): return subprocess.check_output(['git',*args],cwd=repo,text=True).strip()
def write(path,text):
 p=repo/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
def commit(msg):
 git('add','.');git('commit','-m',msg);return git('rev-parse','HEAD')
def snap(name,rev):
 dest=out/name;dest.mkdir()
 for p in sorted(repo.rglob('*')):
  if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts:
   q=dest/p.relative_to(repo);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
 return {'source':rev,'files':{str(p.relative_to(dest)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(dest.rglob('*')) if p.is_file()}}
git('init','-b','feature');git('config','user.name','Isolated fixture');git('config','user.email','fixture@example.invalid')
write('ticket_harness/__init__.py','')
write('ticket_harness/run.py','''class Run:
    def __init__(self):
        self.gates = {"checks": False, "approval": False}

    def record(self, name, passed):
        self.gates[name] = passed

    def revoke(self):
        for name in self.gates:
            self.gates[name] = False
''')
write('CONTRACT.md','''# Isolated development fixture
This miniature is not the real harness. Run owns canonical gate truth. Consumers
must observe later revocation; all readiness requires current checks and approval.
Before candidate readiness, restore must preserve that property. Human QA remains
separate and no automated result accepts a milestone. This feature starts at the
initial fixture commit; there is no prior accepted milestone.
''')
base=commit('Fixture feature starting revision'); sources={'baseline':snap('baseline',base)}
write('ticket_harness/checks.py','''def checks_ready(run):
    return run.gates["checks"]
''')
write('ticket-A.md','''# A: expose check status
Return the current check status of a Run, including after revocation. No saved
representation or new writer. Use the existing Run owner and dictionary contract.
''')
write('observe.py','''from ticket_harness.run import Run
from ticket_harness.checks import checks_ready
r = Run()
assert not checks_ready(r)
r.record("checks", True)
assert checks_ready(r)
r.revoke()
assert not checks_ready(r)
print("A check status and revocation: PASS")
''')
a=commit('Ticket A check consumer');sources['ticket-a']=snap('ticket-a',a)
write('ticket_harness/approval.py','''def candidate_ready(run):
    return run.gates["checks"] and run.gates["approval"]
''')
write('ticket-B.md','''# B: expose candidate readiness
Return true only when current checks and approval pass. Preserve revocation.
No persistence path or new writer. Human QA acceptance is separate from readiness.
''')
with (repo/'observe.py').open('a') as f:f.write('''from ticket_harness.approval import candidate_ready
r.record("checks", True)
assert not candidate_ready(r)
r.record("approval", True)
assert candidate_ready(r)
r.revoke()
assert not candidate_ready(r)
print("B checks plus approval and revocation: PASS")
''')
b=commit('Ticket B approval consumer');sources['ticket-b']=snap('ticket-b',b)
write('ticket_harness/restore.py','''from types import SimpleNamespace


def restore(data):
    run = SimpleNamespace(gates=dict(data["gates"]))
    review = SimpleNamespace(gates=dict(run.gates))
    return run, review
''')
write('ticket-C.md','''# C: restore run and review state
Restore one authoritative gates mapping shared by run and review consumers.
New persistence/restoration and shared state trigger cumulative assessment before
integration. Consumer checks and candidate readiness must reflect later revocation.
''')
c=commit('Unintegrated ticket C risk candidate');sources['risk']=snap('risk',c)
git('branch','integration',b)
write('observe-risk.py','''from ticket_harness.run import Run
from ticket_harness.restore import restore
from ticket_harness.checks import checks_ready
from ticket_harness.approval import candidate_ready
run, review = restore({"gates": {"checks": True, "approval": True}})
assert candidate_ready(review)
Run.revoke(run)
print({"canonical": run.gates, "review": review.gates,
       "checks_ready_after_revoke": checks_ready(review),
       "candidate_ready_after_revoke": candidate_ready(review)})
assert not candidate_ready(review), "restored review readiness survives canonical revocation"
''')
# observation-only script remains outside source snapshot until archived below
shutil.copy2(repo/'observe-risk.py',out/'observe-risk.py');(repo/'observe-risk.py').unlink()
write('ticket_harness/restore.py','''from ticket_harness.run import Run


def restore(data):
    run = Run()
    for name in run.gates:
        run.record(name, data["gates"][name])
    return run, run
''')
fixed=commit('Authorized isolated C repair restore canonical owner');sources['clean']=snap('clean',fixed)
bundle=out/'source.bundle';git('bundle','create',str(bundle),'--all')
(out/'sources.json').write_text(json.dumps(sources,indent=2)+'\n')
print(json.dumps({k:v['source'] for k,v in sources.items()},indent=2))
