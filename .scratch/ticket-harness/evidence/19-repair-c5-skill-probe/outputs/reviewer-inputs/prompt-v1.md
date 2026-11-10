# Proposed full reviewer prompt v1 — held; not dispatched

You are an independent source reviewer assigned only the Spec axis. Review both
cases below. The quoted source and contracts are the complete supplied corpus;
no other repository context is supplied. Apply the following guidance.

# Proposed Spec guidance v1

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

## Case m4

### CONTRACT.md

# CSV records
parse_csv(text) accepts ordinary CSV text using comma delimiters and standard
quoted fields, including an embedded comma and doubled quote escaping. It returns
a fresh tuple of tuple-of-string records, preserving row and field order. No
header handling, external state, persistence or mutation of caller data.

### records.py

```python
def parse_csv(text):
    return tuple(tuple(line.split(",")) for line in text.splitlines())
```

## Case r2

### CONTRACT.md

# Stock reservation
reserve(available, requested) accepts nonnegative integer stock and a positive
integer request. It returns remaining stock for a satisfiable request. Requests
above available stock reject with ValueError; no negative stock result may escape.
It owns this validation; the caller should not precheck availability. No mutation,
external state or persistence.

### stock.py

```python
def reserve(available, requested):
    if requested <= 0:
        raise ValueError("request must be positive")
    return available - requested
```

Return a complete report covering both cases. Include evidence for each supported
finding; do not edit the cases or search for other evaluation artifacts.
