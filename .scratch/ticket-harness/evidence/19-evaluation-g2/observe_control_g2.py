"""Disposable dictionary-isolation observation, not production regression coverage."""
from copy import deepcopy
from pathlib import Path
import hashlib
import json

OUT = Path(__file__).resolve().parent
result = {}
for version,path in [('G1',OUT.parent/'19-evaluation/snapshot/cases/h8/attempt.py'),('G2',OUT/'snapshot/cases/h8/attempt.py')]:
    namespace = {}
    exec(compile(path.read_text(),str(path),'exec'),namespace)
    identity,revision = {'value':['A']},{'value':['r1']}
    attempt = namespace['Attempt'](identity)
    attempt.submit(revision)
    attempt.complete()
    initial = deepcopy(attempt.snapshot())
    identity['value'].append('external')
    revision['value'].append('external')
    after_input = deepcopy(attempt.snapshot())
    observed,current = attempt.snapshot()
    observed['id']['value'].append('snapshot')
    current['revision']['value'].append('snapshot')
    after_snapshot = deepcopy(attempt.snapshot())
    before_invalid = deepcopy(attempt.snapshot())
    errors = []
    for operation in [lambda:attempt.submit({'value':['r2']}),attempt.complete]:
        try:
            operation()
        except ValueError as error:
            errors.append(str(error))
    after_invalid = deepcopy(attempt.snapshot())
    result[version] = {'source_path':str(path),'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'initial':initial,'after_input_mutation':after_input,'after_snapshot_mutation':after_snapshot,
        'input_isolated':initial == after_input,'snapshot_isolated':after_input == after_snapshot,
        'invalid_operations':errors,'invalid_operations_unchanged':before_invalid == after_invalid,
        'mirrored_observations_equal':after_invalid[0] == after_invalid[1]}
assert result['G1']['input_isolated'] is False
assert result['G1']['snapshot_isolated'] is False
assert result['G2']['input_isolated'] is True
assert result['G2']['snapshot_isolated'] is True
assert result['G2']['invalid_operations_unchanged'] is True
assert result['G2']['mirrored_observations_equal'] is True
result['limits'] = 'One dictionary/list example and invalid terminal transitions; observable fixture evidence, not reviewer judgment, exhaustive input validation, production coverage or a reliability rate.'
path = OUT/'control-observation.json'
assert not path.exists(), 'Never overwrite a retained observation'
path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'observation':str(path),'G1_input_isolated':False,'G2_input_isolated':True,'G2_snapshot_isolated':True,'invalid_operations_unchanged':True},indent=2))
