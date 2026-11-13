"""Prepare a persistent public-CLI QA target; stop cleanly for human inspection."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
HOME = Path(tempfile.mkdtemp(prefix='ticket-harness-m1-human-qa-'))
TARGET, RUN = HOME / 'target', HOME / 'run'
PYTHON = sys.executable
EVENTS = []

def command(args, cwd=ROOT):
    result = subprocess.run(list(map(str, args)), cwd=cwd, capture_output=True, text=True)
    EVENTS.append(dict(command=list(map(str,args)), cwd=str(cwd), exit=result.returncode,
                       stdout=result.stdout, stderr=result.stderr))
    if result.returncode:
        raise RuntimeError(result.stderr or result.stdout)
    return result.stdout.strip()

def git(*args):
    return command(['git', '-C', TARGET, *args])

def snapshot(name):
    record = json.loads((RUN / 'run.json').read_text())
    (OUT / (name + '-record.json')).write_text(json.dumps(record, indent=2) + '\n')
    request = json.loads((RUN / 'qa-request.json').read_text())
    (OUT / (name + '-request.json')).write_text(json.dumps(request, indent=2) + '\n')
    return record, request

def wait_for(process, predicate):
    deadline = time.monotonic() + 60
    while time.monotonic() < deadline:
        if (RUN / 'run.json').exists():
            record = json.loads((RUN / 'run.json').read_text())
            if predicate(record):
                return record
        if process.poll() is not None:
            raise RuntimeError(f'CLI exited {process.returncode}; inspect {HOME}')
        time.sleep(.05)
    raise TimeoutError(f'CLI did not reach expected state; inspect {HOME}')

def launch(operation):
    args = [PYTHON, '-m', 'ticket_harness', operation]
    args += ['--config', str(HOME / 'project.json'), '--output', str(RUN)] if operation == 'run' else [str(RUN)]
    with (HOME / (operation + '.stdout')).open('w') as stdout, (HOME / (operation + '.stderr')).open('w') as stderr:
        process = subprocess.Popen(args, cwd=ROOT, stdout=stdout, stderr=stderr, start_new_session=True)
    EVENTS.append(dict(command=args, cwd=str(ROOT), pid=process.pid, stdout=str(HOME / (operation + '.stdout')), stderr=str(HOME / (operation + '.stderr'))))
    return process

def stop(process):
    command([PYTHON, '-m', 'ticket_harness', 'stop', RUN])
    process.wait(timeout=20)
    assert process.returncode == 2, process.returncode
    EVENTS.append(dict(operation='foreground-exit', pid=process.pid, exit=process.returncode))

shutil.copytree(ROOT / 'examples/scripted', TARGET)
(TARGET / '02-more.md').write_text('# 02: Deliver second work\n\nStatus: ready-for-agent\nBlocked by: 01\nChecks: ticket\n\n## Acceptance criteria\n\n- [ ] Deliver work 02.\n')
plan = dict(version='v1', approval='User requested M1 QA preparation; disposable demonstration inputs, not development acceptance', development='dev', required_tickets=['01','02'], final_milestone='M2', final_coverage=['01','02'], milestones=[
    dict(id='M1', tickets=['01'], qa=dict(setup='Inspect the disposable candidate worktree', actions=['Read value.txt and work-01; confirm work-02 is absent'], pass_conditions=['value.txt is 2, work-01 delivered, dev unchanged, ticket02 unstarted'])),
    dict(id='M2', tickets=['02'], qa=dict(setup='Inspect complete disposable feature after explicit M1 approval', actions=['Read work-01 and work-02'], pass_conditions=['Both work files exist; final acceptance alone marks feature complete']))],
    roles=dict(worker=dict(model='scripted-fixture'), spec=dict(model='scripted-spec'), standards=dict(model='scripted-standards')))
(TARGET / 'plan.json').write_text(json.dumps(plan, indent=2) + '\n')
agent = HOME / 'agent.py'
agent.write_text('''import json, os, sys\nfrom pathlib import Path\na=json.load(sys.stdin)\nr={k:a[k] for k in ('role','ticket','attempt','base_revision','revision')}\nr['pid']=os.getpid()\nwith Path(''' + repr(str(HOME / 'launches.jsonl')) + ''').open('a') as out:\n    out.write(json.dumps(dict(ticket=a['ticket'],role=a['role'],attempt=a['attempt'],pid=os.getpid()))+'\\n')\nif a['role']=='implementation':\n    Path('value.txt').write_text('2\\n')\n    Path('work-'+a['ticket']).write_text('delivered '+a['ticket']+'\\n')\n    r.update(result='submitted',summary='Delivered '+a['ticket'],changed_files=['value.txt','work-'+a['ticket']],checks=[],acceptance_evidence=['Delivered requested work'],unresolved_questions=[])\nelse:\n    r['findings']=[]\nprint(json.dumps(r))\n''')
check = HOME / 'check.py'
check.write_text('''import os, subprocess\nfrom pathlib import Path\nstage=os.environ['TICKET_HARNESS_STAGE']\nprint(stage, subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip())\nassert Path('value.txt').read_text()==('1\\n' if stage=='baseline' else '2\\n')\nif stage!='baseline':\n    assert Path('work-01').read_text()=='delivered 01\\n'\nif Path('work-02').exists():\n    assert Path('work-02').read_text()=='delivered 02\\n'\n''')
git('init', '-b', 'main')
git('config', 'user.name', 'QA Fixture')
git('config', 'user.email', 'qa@example.invalid')
git('add', '.')
git('commit', '-m', 'Approved disposable two-milestone QA input')
base = git('rev-parse', 'HEAD')
git('branch', 'integration')
git('branch', 'dev')
config = dict(repository=str(TARGET), base='main', integration='integration', spec='spec.md', ticket='01-value.md', tickets=['01-value.md','02-more.md'], standards=['STANDARDS.md'], agent=[PYTHON,str(agent)], suite=[PYTHON,str(check)], checks=dict(ticket=[PYTHON,str(check)]), max_repairs=0, plan='plan.json')
(HOME / 'project.json').write_text(json.dumps(config, indent=2) + '\n')
location = dict(home=str(HOME),target=str(TARGET),run=str(RUN),base=base,source=command(['git','rev-parse','HEAD']),scripted_roles=True,human_acceptance=False)
(OUT / 'demo-location.json').write_text(json.dumps(location, indent=2) + '\n')
process = launch('run')
try:
    wait_for(process, lambda r:r['outcome']=='awaiting_human_qa')
    first, request = snapshot('first-wait')
    assert first['tickets']['01']['state']=='Done' and first['tickets']['02']['attempt']==0
    assert first['feature_complete'] is False
    assert git('rev-parse','dev')==base
    assert git('rev-parse','integration')==request['feature_revision']
    decision=dict(decision='APPROVED', request=dict(request,candidate_revision=base))
    temporary=RUN / 'qa-decision.new'
    temporary.write_text(json.dumps(decision))
    temporary.replace(RUN / 'qa-decision.json')
    rejected=wait_for(process,lambda r:r.get('qa_decision_status')=='rejected')
    snapshot('stale-rejected')
    assert rejected['attempts']==first['attempts'] and git('rev-parse','dev')==base
    stop(process)
    stopped,_=snapshot('first-stop')
    assert stopped['outcome']=='stopped_at_qa'
    old_events=(HOME / 'launches.jsonl').read_bytes()
    process=launch('continue')
    restored=wait_for(process,lambda r:r['outcome']=='awaiting_human_qa')
    assert restored['attempts']==first['attempts']
    assert (HOME / 'launches.jsonl').read_bytes()==old_events
    assert sum(g['stage']=='baseline' for g in restored['gates'])==1
    snapshot('restored-wait')
    stop(process)
    final, final_request=snapshot('human-checkpoint')
    assert final['outcome']=='stopped_at_qa'
    assert final_request==request
    assert not final.get('qa_decisions')
    location.update(candidate=final_request['candidate_revision'], feature=final_request['feature_revision'], development=final_request['development_revision'], request_id=final_request['request_id'], candidate_worktree=final_request['candidate_worktree'], checkpoint=final['checkpoint_id'], observation='stale decision rejected; clean stop/continue/second stop; baseline and assignments not replayed; awaiting real human fixture approval')
    (OUT / 'demo-location.json').write_text(json.dumps(location,indent=2)+'\n')
    command([PYTHON,'-m','ticket_harness','status',RUN])
    print(json.dumps(location,indent=2))
finally:
    (OUT / 'demo-commands.json').write_text(json.dumps(EVENTS,indent=2)+'\n')
    if process.poll() is None:
        try:
            stop(process)
        except Exception:
            process.terminate()
            process.wait(timeout=10)
    # Archive outside live evidence: live paths remain usable for the next process.
    shutil.make_archive(str(OUT / 'demo-initial-checkpoint'), 'gztar', root_dir=HOME)
    archive=OUT / 'demo-initial-checkpoint.tar.gz'
    (OUT / 'demo-archive.json').write_text(json.dumps(dict(archive=archive.name,sha256=hashlib.sha256(archive.read_bytes()).hexdigest()),indent=2)+'\n')
