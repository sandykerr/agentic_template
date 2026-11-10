"""Bounded observations only; never imports with writes or changes supplied inputs."""
from pathlib import Path
import hashlib
import json
import platform
import shutil

base = Path('/tmp/reviewer-authoring19')
inputs, out = base / 'inputs', base / 'outputs'
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
original = {str(p.relative_to(inputs)): digest(p) for p in sorted(inputs.rglob('*')) if p.is_file()}
for relative in original:
    dest = out / 'retention' / 'original-inputs' / relative
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(inputs / relative, dest)
for case, filename in [('m4', 'records.py'), ('r2', 'stock.py')]:
    target = out / 'reviewer-inputs' / 'corpus-v1' / case
    target.mkdir(parents=True, exist_ok=True)
    for name in [filename, 'CONTRACT.md']:
        shutil.copyfile(inputs / 'cases' / case / name, target / name)

def function(case, filename, name):
    namespace = {}
    path = inputs / 'cases' / case / filename
    exec(compile(path.read_bytes(), str(path), 'exec'), namespace)
    return namespace[name]
parse_csv = function('m4', 'records.py', 'parse_csv')
reserve = function('r2', 'stock.py', 'reserve')
observations = []
def observe(case, scenario, args, expectation, expected=None, exception=None):
    fn = parse_csv if case == 'm4' else reserve
    try:
        result = fn(*args)
        actual = {'returned': result, 'python_repr': repr(result), 'type': type(result).__name__}
        conforms = exception is None and result == expected
        if case == 'm4':
            actual['tuple_of_tuple_of_strings'] = isinstance(result, tuple) and all(isinstance(row, tuple) and all(isinstance(x, str) for x in row) for row in result)
    except Exception as error:
        actual = {'exception': type(error).__name__, 'message': str(error)}
        conforms = exception is not None and isinstance(error, exception)
    observations.append({'case': case, 'scenario': scenario, 'arguments': args, 'contract_expectation': expectation, 'observed': actual, 'conforms_for_this_observation': conforms})
observe('m4', 'ordinary rows and order', ['a,b\nc,d'], '((a,b),(c,d)) as tuple of tuple of strings', (('a','b'),('c','d')))
observe('m4', 'quoted embedded comma', ['"alpha,beta",gamma'], "(('alpha,beta', 'gamma'),)", (('alpha,beta','gamma'),))
observe('m4', 'doubled quote escaping', ['"a""b",c'], "(('a\"b', 'c'),)", (('a"b','c'),))
observe('r2', 'satisfiable request', [5, 2], 'return 3', 3)
observe('r2', 'exact exhaustion', [5, 5], 'return 0', 0)
observe('r2', 'over-request', [2, 3], 'raise ValueError; no negative result', exception=ValueError)
observe('r2', 'zero stock positive request', [0, 1], 'raise ValueError; no negative result', exception=ValueError)
identity_after = {str(p.relative_to(inputs)): digest(p) for p in sorted(inputs.rglob('*')) if p.is_file()}
assert original == identity_after, 'Inputs changed'
(out / 'evaluator' / 'input-manifest.json').write_text(json.dumps({'algorithm': 'SHA-256', 'files': original, 'unchanged_after_preflight': original == identity_after}, indent=2) + '\n')
(out / 'evaluator' / 'observations.json').write_text(json.dumps({'interpreter': platform.python_version(), 'method': 'Execute exact supplied source in isolated Python namespaces; call bounded valid-domain examples; compare against literal contract expectations.', 'observations': observations}, indent=2) + '\n')
print(json.dumps({'python': platform.python_version(), 'observations': observations, 'inputs_unchanged': original == identity_after}, indent=2))
