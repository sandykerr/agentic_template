"""Scoped public-CLI retry-integrity probe; no assessed source writes."""
import hashlib
import json
import os
import socket
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path('/panfs/ccds02/nobackup/people/ajkerr1/agentic_template/agentic_template')
observations = []

def call(argv, cwd=ROOT):
    result = subprocess.run(argv, cwd=cwd, text=True, capture_output=True)
    observations.append({'argv': [str(value) for value in argv], 'cwd': str(cwd),
                         'exit': result.returncode, 'stdout': result.stdout,
                         'stderr': result.stderr})
    return result

with tempfile.TemporaryDirectory(prefix='ticket25-spec-retry-', dir='/dev/shm') as temporary:
    repo = Path(temporary)
    result = call(['git', 'init', '-q', str(repo)])
    assert result.returncode == 0
    feature = repo / '.scratch' / 'probe'
    (feature / 'issues').mkdir(parents=True)
    (feature / 'issues' / '25-probe.md').write_text('# 25: Probe\n')
    base = [str(ROOT / '.venv/bin/python'), '-m', 'ticket_harness.evidence',
            '--feature', str(feature)]
    allocations = []
    for label in ('A', 'B'):
        result = call(base + ['allocate', '--ticket', '25', '--purpose', 'retry integrity probe',
                             '--producer', 'spec-probe'])
        assert result.returncode == 0
        allocation = json.loads(result.stdout)
        (Path(allocation['destination']) / 'payload.txt').write_text(label + ' original\n')
        allocations.append(allocation)
    def register(allocation):
        return call(base + ['register', '--allocation', allocation['allocation'],
                            '--file', 'payload.txt', '--source-version', 'probe',
                            '--activity', 'retry integrity probe', '--result', 'observed'])
    for allocation in allocations:
        assert register(allocation).returncode == 0
    artifact = Path(allocations[0]['review_artifact'])
    before = artifact.read_bytes()
    b_payload = Path(allocations[1]['destination']) / 'payload.txt'
    b_payload.write_text('B changed after registration\n')
    retry_a = register(allocations[0])
    retry_b = register(allocations[1])
    result = {'host': socket.gethostname(), 'architecture': os.uname().machine,
              'checkout': str(ROOT), 'source': call(['git', 'rev-parse', 'HEAD']).stdout.strip(),
              'probe_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'observations': observations,
              'retry_A_exit': retry_a.returncode, 'retry_B_control_exit': retry_b.returncode,
              'artifact_unchanged': artifact.read_bytes() == before,
              'registered_B_sha256': json.loads(before)['captures'][1]['files'][0]['sha256'],
              'actual_B_sha256': hashlib.sha256(b_payload.read_bytes()).hexdigest(),
              'artifact_before': json.loads(before), 'artifact_after': json.loads(artifact.read_text())}
    print(json.dumps(result, indent=2))
