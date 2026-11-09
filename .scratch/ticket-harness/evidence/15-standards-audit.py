import hashlib,json,subprocess
from pathlib import Path
root=Path.cwd(); evidence=root/'.scratch/ticket-harness/evidence'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda n:json.loads((evidence/n).read_text())
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
identity=read('15-final-suite-source.json')['sha256']
assert len(identity)==23
for name,expected in identity.items():
    assert sha(root/name)==expected,name
    assert hashlib.sha256(subprocess.check_output(['git','show',f'{head}:{name}'])).hexdigest()==expected,name
checks=read('15-check-results.json')['checks']
for name,result in checks.items():
    assert result['exit_code']==0,name
    assert read(result['source_identity'])['sha256']==identity,name
observations=read('15-fixture-observations.json')['observations']
for row in observations:
    p=evidence/row['raw_file'];assert sha(p)==row['raw_sha256'],p
    raw=json.loads(p.read_text());assert row['scenario']==raw['scenario']
    assert row['outcome']==raw['record']['outcome']
assert len(observations)==122
manifest=read('15-package-manifest.json')
for name,expected in manifest['installed_source_sha256'].items():
    assert sha(root/'ticket_harness'/name)==expected
    assert sha(Path('/tmp/ticket15-installed/ticket_harness')/name)==expected
for name,expected in manifest['wheel_and_backend_sha256'].items():assert sha(Path(name))==expected
originals=read('15-log-originals.json')
for name,data in originals.items():assert hashlib.sha256(data['original'].encode()).hexdigest()==data['sha256']
archives=0
for row in observations:
    if row['scenario'] not in ('test_clean_qa_stop_continues_in_new_process_without_replaying_done_work','test_repeated_stops_retain_previous_decisions_and_checkpoint_lineage'):continue
    retained=evidence/row['retained_run_files']
    raw=json.loads((evidence/row['raw_file']).read_text());record=raw['record'];out=Path(record['artifacts']).parent
    for p in (retained/'checkpoints').glob('*.json'):
        cp=json.loads(p.read_text());assert p.stem==cp['record']['checkpoint_id']
        for name,expected in cp['evidence'].items():assert sha(retained/Path(name).relative_to(out))==expected,(p,name)
        assert any(sha(q)==cp['request_sha256'] for q in (retained/'artifacts').glob('*qa-request.json'))
        archives+=1
    for decision in record['qa_decisions']:
        assert sha(retained/Path(decision['artifact']).relative_to(out))==decision['sha256']
    assert sum(g['stage']=='baseline' for g in record['gates'])==1
    assert sum(l['role']=='implementation' and l['event']=='start' for l in raw['launches'])==4
    assert raw['integration']==raw['development']==record['integration_revision']
tracker=sha(root/'docs/agents/issue-tracker.md');assert tracker=='3803de99e541e60d2e9f733d5c98b009a43e60a9584e3819adffc55eae0214ce'
repro=evidence/'15-standards-restored-evidence-repro.json';data=json.loads(repro.read_text())
data['provenance']={'head':head,'baseline':'90255aaf6faf9aedce18f7159093f5dbfde294b7','command':['/home/ajkerr1/development/agentic_template/.micromamba/envs/dev/bin/python','/tmp/ticket15-standards-repro.py'],'script_sha256':sha(Path('/tmp/ticket15-standards-repro.py')),'source_sha256':identity,'seam':'Public CLI subprocesses using existing isolated real-Git fixture builders; no internal mocks; fixture repositories removed by owned cleanup.'}
repro.write_text(json.dumps(data,indent=2)+'\n')
(evidence/'15-standards-restored-evidence-repro.py').write_bytes(Path('/tmp/ticket15-standards-repro.py').read_bytes())
report={'baseline':'90255aaf6faf9aedce18f7159093f5dbfde294b7','head':head,'source_and_committed_hashes_verified':len(identity),'final_gate_maps_and_exits_verified':len(checks),'raw_final_observation_hashes_and_outcomes_verified':len(observations),'successful_checkpoint_archives_verified':archives,'installed_source_hashes_verified':len(manifest['installed_source_sha256']),'package_and_backend_hashes_verified':len(manifest['wheel_and_backend_sha256']),'original_historical_log_hashes_verified':len(originals),'unrelated_tracker_sha256':tracker,'reproduction_evidence_sha256':sha(repro),'audit_script':'15-standards-audit.py','full_suite_repeated':False}
(evidence/'15-standards-audit.json').write_text(json.dumps(report,indent=2)+'\n')
(evidence/'15-standards-audit.py').write_bytes(Path('/tmp/ticket15-standards-audit.py').read_bytes())
print(json.dumps(report,indent=2))
