from pathlib import Path
import hashlib
import json

root = Path('/tmp/reviewer-authoring19/outputs')
inputs = Path('/tmp/reviewer-authoring19/inputs')
def write(relative, text):
    (root / relative).write_text(text)
def dump(relative, obj):
    write(relative, json.dumps(obj, indent=2) + '\n')
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
guidance = '''# Proposed Spec guidance v1

Review the complete supplied corpus against each case's own CONTRACT.md. Assess
observable correctness on the accepted input domain and validation explicitly
owned by the function. Explain a concern with a concrete accepted input, expected
behavior, actual source behavior, consequence, and proportionate remedy. Separate
contract violations from optional suggestions. Do not invent caller validation,
external requirements, or requirements for unspecified input domains. Report
supported additional concerns. Do not infer case labels or a desired finding
count. Read-only review: do not edit source or contracts.

For each case, return its identifier, supported contract findings with source
locations and reasoning, and any material uncertainty. If no supported concern
exists, say so. Give optional suggestions separately. Assess only the Spec axis.
'''
write('reviewer-inputs/guidance-v1/spec.md', guidance)
prompt = '''# Proposed full reviewer prompt v1 — held; not dispatched

You are an independent source reviewer assigned only the Spec axis. Review both
cases below. The quoted source and contracts are the complete supplied corpus;
no other repository context is supplied. Apply the following guidance.

''' + guidance
for case, source in [('m4', 'records.py'), ('r2', 'stock.py')]:
    prompt += f'\n## Case {case}\n\n### CONTRACT.md\n\n' + (inputs / 'cases' / case / 'CONTRACT.md').read_text()
    prompt += f'\n### {source}\n\n```python\n' + (inputs / 'cases' / case / source).read_text() + '```\n'
prompt += '''
Return a complete report covering both cases. Include evidence for each supported
finding; do not edit the cases or search for other evaluation artifacts.
'''
write('reviewer-inputs/prompt-v1.md', prompt)
dump('evaluator/key-v1.json', {
    'status': 'proposed evaluator key; verified concerns; packet unready',
    'axis': 'Spec',
    'cases': {
        'm4': {
            'provisional_slot': 'acceptable control',
            'verified_classification': 'invalid control: contract violation',
            'required_concern_if_case_is_retained': 'Standard quoted CSV fields are not parsed; comma splitting breaks embedded commas and leaves escaped quotes undecoded.',
            'source_location': 'records.py:2',
            'rationale': 'CONTRACT.md explicitly includes quoted fields, embedded commas, and doubled quote escaping; all observations use that accepted domain.',
            'counterexamples': ['quoted embedded comma', 'doubled quote escaping'],
            'proportionate_outcome': 'Identify a concrete CSV parsing contract failure; one finding may cover both symptoms. Recommend standard CSV parsing behavior without prescribing a particular implementation.',
            'not_an_overreach': 'A reviewer flagging this defect is correct, even though the proposal called this a control.',
            'status': 'Not eligible to score as an acceptable control; no source repair authorized.'
        },
        'r2': {
            'provisional_slot': 'required concern',
            'verified_classification': 'required concern supported',
            'required_concern': 'Above-stock requests escape as negative stock instead of raising ValueError.',
            'source_location': 'stock.py:4',
            'rationale': 'CONTRACT.md explicitly makes reserve own the availability validation; accepted nonnegative stock and positive request expose the missing check.',
            'counterexamples': ['over-request', 'zero stock positive request'],
            'proportionate_outcome': 'Identify missing availability rejection and negative result; recommend ValueError for above-stock requests before returning a result. One finding covers both symptoms.'
        }
    },
    'adjudication_rules': [
        'Judge substantive contract reasoning, not exact wording or number of findings.',
        'Retain supported extra findings and independently trace them to the supplied contract.',
        'Keep optional suggestions separate; do not count silence about unaccepted input types as a miss.',
        'No current acceptable control exists; false-positive restraint cannot be evaluated with this proposal.',
        'If later source or substantive guidance changes, version them separately and evaluate the entire final declared corpus; do not transfer old results.'
    ],
    'proposed_finite_success_conditions_after_readiness': [
        'Complete authorized final corpus reviewed on Spec with real independent judgments and retained exact originals.',
        'Every final required concern substantively identified; every final supported acceptable control avoids unsupported blocking findings.',
        'Any supported additional findings and disagreements explicitly adjudicated; no unresolved invalid control.'
    ],
    'current_success_claim': 'None: no reviewer judgments and no valid acceptable control.'
})
dump('evaluator/held-declaration.json', {
    'status': 'HELD_UNREADY_PREPARATION_ONLY',
    'source_corpus_version': 'corpus-v1',
    'guidance_version': 'guidance-v1',
    'prompt_version': 'prompt-v1',
    'complete_current_candidate_corpus': ['m4', 'r2'],
    'authorized_stage': 'preparation and bounded preflight only',
    'authorized_dispatches_now': 0,
    'actual_reviewer_assignments': 0,
    'actual_trials': 0,
    'proposed_future_scope_only': {'axes': ['Spec'], 'maximum_trials': 1},
    'future_settings': {
        'reviewer_count': None, 'model': None, 'backend': None,
        'reasoning_effort': None, 'sampling': None, 'resource_limits': None,
        'tool_permissions_and_isolation': None, 'assignment_id': None
    },
    'settings_status': 'Not selected, configured, or authorized; no defaults inferred.',
    'gaps': [
        'm4 is an invalid acceptable control; no valid acceptable control is supplied.',
        'A human scope decision is needed: authorize repair/replacement of the control, or explicitly accept a different concern-only evaluation and its narrower claim.',
        'After any authorized change, final corpus/key and guidance must be versioned and full final corpus preflighted before readiness can be declared.',
        'Future dispatch authorization and actual reviewer configuration, resource/capture arrangements, and independence/isolation must be resolved before assignment.',
        'No reviewer judgments or adjudicated trial results exist.',
        'Backend delivery/enforcement and active-context enforcement telemetry are unavailable.'
    ],
    'repository_example_link': 'Absent from supplied inputs; not consulted; no broader repository/prior-result reads authorized.',
    'permissions': 'Reviewer material is logically separated on disk; isolation is declared only, not enforced.',
    'freeze_status': 'Identity snapshots only, not a readiness freeze or pass.'
})
write('evaluator/capture-plan.md', '''# Held capture plan

This is a proposed retention method, not an executed assignment or backend
configuration. No dispatch helper is supplied. No reviewer result files exist.

If a future trial is expressly authorized after the packet is ready, preserve
all current artifacts and use a new version/trial directory; the proposed maximum
is one trial on Spec. Resolve the actual reviewer count and settings first. Save
each full prompt and settings record before its assignment, and retain provider
assignment identifiers, actual tool/source-access records, errors and outcomes.
Keep each independent reviewer blind to the evaluator directory, builders,
preflight answers, siblings and prior results. Directory separation alone does
not establish that isolation. Verify the actual available isolation mechanism.

Proposed path layout for a later authorized trial is
`trials/trial-01/reviewer-<id>/prompt.raw`, `settings.json`,
`assignment-and-tool-record.raw`, `report.raw`, `report.display.md`, and
`capture-metadata.json`. Do not create plausible reports or completion records
when no assignment happened. Preserve original bytes for every raw stream/report
before decoding or display formatting, including unsuccessful output. Capture
provider-native response records as well when available. Hash the raw bytes and
record byte length, timestamps, encoding and capture mechanism. A display copy is
derived and must never replace raw bytes. If the backend only exposes a text
string, retain the original exposed response and declare the unavailable transport
bytes rather than claiming byte-perfect transport capture. Confirm capture
capability before dispatch. Retain full event/error streams separately from the
final report. Compression is optional and must round-trip byte exactly.

After originals are preserved, adjudicate each concern/control against the final
key and source evidence. Retain misses, supported extra concerns, invalid controls,
unsupported blockers and optional suggestions as distinct outcomes. Append any
correction; never overwrite failed trials/adjudications. Neither a prompt hash nor
a declared setting proves backend instruction delivery or enforcement. Report
unavailable telemetry. Do not claim general reliability, causal wording effects,
whole-ticket acceptance or runtime behavior from this finite evaluation.
''')
files = {}
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name not in ['artifact-manifest.json', 'report.md']:
        files[str(p.relative_to(root))] = {'sha256': sha(p), 'bytes': p.stat().st_size}
dump('evaluator/artifact-manifest.json', {'algorithm': 'SHA-256', 'scope': 'Prepared artifact identities; report excluded to avoid self-reference; no readiness or delivery proof.', 'files': files})
print(json.dumps({'artifacts_hashed': len(files), 'status': 'HELD_UNREADY_PREPARATION_ONLY'}, indent=2))
