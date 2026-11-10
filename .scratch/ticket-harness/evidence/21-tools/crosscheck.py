"""Match actual producer baseline and final working source without editing either."""
import hashlib
import json
import subprocess
from pathlib import Path

out = Path('.scratch/ticket-harness/evidence')
base = '8574c6e5fb0a55ea3539e52c7c53044f1c036583'
producer = json.loads((out / '21-checkpoint/producer.json').read_text())
final = json.loads((out / '21-final-source.json').read_text())
for name, digest in producer['source_hashes'].items():
    assert hashlib.sha256(subprocess.check_output(['git', 'show', base + ':' + name])).hexdigest() == digest
for name, digest in final['files'].items():
    assert hashlib.sha256(Path(name).read_bytes()).hexdigest() == digest
changed = [name for name, digest in producer['source_hashes'].items() if final['files'][name] != digest]
assert changed == ['ticket_harness/tickets.py', 'ticket_harness/runner.py'] or set(changed) == {'ticket_harness/tickets.py', 'ticket_harness/runner.py'}
source = {
    'baseline': base,
    'producer_baseline_hashes_matched': len(producer['source_hashes']),
    'final_working_hashes_matched': len(final['files']),
    'changed_producer_files': changed,
    'tests_unchanged': all(final['files'][name] == digest for name, digest in producer['source_hashes'].items() if name.startswith('tests/')),
    'producer_head': producer['producer_head'],
    'final_source_manifest_sha256': hashlib.sha256((out / '21-final-source.json').read_bytes()).hexdigest(),
    'scope': 'Post-continuation crosscheck: same unchanged working runtime was used for continuation and final checks. Producer hashes match exact original baseline Git blobs. Does not claim final source was committed before checks.'
}
(out / '21-source-crosscheck.json').write_text(json.dumps(source, indent=2) + '\n')
print(json.dumps(source))
