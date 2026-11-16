# Testing policy

For harness development, use [test-strategy](../../.agents/skills/custom/test-strategy/SKILL.md)
for coverage selection, evidence, existing Spec/Standards review and suite audits;
use [TDD](../../.agents/skills/matt-pocock/tdd/SKILL.md) for implementation.
Read [environment guidance](python-environment.md) before Python or checks.
Use the [commands below](#check-commands) for project checks and tool setup.

The approved seam is the public CLI with scripted external processes, real
temporary Git repositories and observable Git/report outcomes. A public module
seam requires a design decision with the human. Cover meaningful role, attempt,
failure-policy differences and interactions through behavior rather than internal mocks.

## Required verification

| Change or stage | Verification |
| --- | --- |
| Development iteration | Focused behavioral and affected caller/fixture tests plus relevant static checks; expand when shared impact is uncertain. |
| Implementation ticket checkpoint | Full suite and required strict type, lint, format, and whitespace checks on the final implementation, plus explicit ticket checks. |
| Further code, test, configuration, or dependency changes | Rerun affected checks and renew full-suite completion for the final implementation. |
| Packaging or entry-point changes | Wheel/install and installed CLI checks; other installed scenarios when explicitly required or resolving concrete uncertainty. |
| Standalone documentation or skill changes | Validate documents/skills, links, routing, and relevant workflow decisions; runtime tests when executable examples or behavior are affected. |
| Bookkeeping or handoff after verified implementation | Validate records, links, and consistency; preserve implementation check provenance. Prose-only bookkeeping needs no suite replay. |

Focused passes do not replace the full-suite gate or explicit checks. Missing or
failing required checks leave verification incomplete. Evidence identifies actual
source/test revisions and relevant uncommitted changes and retains required
CLI/Git observations from that execution; apply test-strategy's capture/reuse rules.

Before producing development check evidence, use
[capture-evidence](../../.agents/skills/custom/capture-evidence/SKILL.md) to allocate
the destination and register actual provenance. Capture preserves originals for
required checks/reviews; subsequent retirement follows the separately approved
evidence workflow and cannot change frozen-input or exact-candidate gates.

Every configured harness baseline, lightweight, review and exact-candidate gate
remains required. Source changes invalidate approvals under existing rules;
development test selection or a prior passing tree cannot authorize skipping gates
or reusing approval for another candidate.

## Check commands

Use the current checkout's `.venv/bin/python`. Follow the
[environment setup and synchronization instructions](python-environment.md)
before checks; the frozen requirements include the project's pinned `dev` tools.

```bash
.venv/bin/python -m pytest
.venv/bin/python -m mypy
.venv/bin/python -m ruff check ticket_harness tests examples
.venv/bin/python -m ruff format --check ticket_harness tests examples
git diff --check
```

For retained CLI fixture observations, set `TICKET_HARNESS_TEST_OBSERVATIONS` to
an output directory before running the tests that support it.
