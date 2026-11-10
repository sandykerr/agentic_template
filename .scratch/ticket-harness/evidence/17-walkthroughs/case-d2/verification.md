# Case d2 — supplemental exact-fix verification

Result: **verified fixed** at `45e518804a7b4011861940065d07237287454e14` for prior blocking finding `walkthrough-case-d/standards-01/F1`. This is an independent reviewer observation of the fixture preparer's claimed repair, not human approval, integration eligibility or milestone QA acceptance.

## Identity and independence

- Supplemental review/report identity: `walkthrough-case-d2/standards-verification-01`, assignment `/root/implement_17/walkthrough_d2`.
- Fixed original baseline: `49ae60016d513a35c22f7139994da144929cdf88`.
- Prior rejected source: `8647da4cd28a01ea060027df087554df3bf73161`.
- Exact repaired source and observed HEAD: `45e518804a7b4011861940065d07237287454e14`.
- Prior report: `/tmp/ticket17-walkthroughs/case-d-report.md`, review/report `walkthrough-case-d/standards-01`, SHA256 `05d5d9b7a0cc53bf1d00bd694370834b174dcd6c8d83abbedaf49b592b0f8517`.
- Initial independent report: `/tmp/ticket17-walkthroughs/case-d2-report.md`, review/report `walkthrough-case-d2/standards-01`, SHA256 `581ea5d8005569ea8fc713741f3dc3c1ad172bdc94da857d71889a3713134c6d`.
- The initial report was finished and hashed before the prior report/finding was supplied. That prior report was first read for this separate supplemental assignment; it was absent from the initial assessment context. This supplement does not retroactively claim that the initial reviewer checked the sparse-input reproduction.
- Parent-configured fresh assignment settings remain `fork_turns=none`, `model=gpt-6.1-sol`, `reasoning_effort=high`. Provider/backend configuration and active context telemetry remain unavailable. Target remains <=250000 active context tokens.

## Specific concern and source assessment

The original blocking concern is narrow: a sparse acceptance array such as `Array(1)` passes `ticket.acceptance.some(...)` because that operation skips holes, then the successful normalized array materializes the hole as `undefined`. This violates nonempty acceptance strings required by the unchanged `CONTRACT.md:4`, and unchanged `cli.js:3-5` trusts the validator and returns success.

I inspected the prior implementation from this repository's Git history and the complete prior-to-repaired diff. The only repair is `validator.js:42`: `ticket.acceptance.some(...)` becomes `Array.from(ticket.acceptance).some(...)`. Contract and caller have no differences between these exact commits. I also reread the complete repaired validator, caller and contract while tracing the affected acceptance-validation, normalization and publication flow.

For ordinary arrays, `Array.from` creates a dense local array, so a hole is presented as `undefined` to the existing string/nonblank predicate. The owner records its acceptance error at `validator.js:43`. Although normalization still makes a local ticket, `validator.js:74` prevents that partial state from being published as success. `cli.js:4` exposes the rejection as exit 2. No new caller coordination, writer, persistent state, ownership change or contract amendment is required. Valid string arrays continue through the unchanged independent-copy construction at `validator.js:45-50`. The remedy is proportionate to the original finding.

Disposition observation: the specific F1 concern is **verified fixed**, rather than unresolved or reopened, at the exact repaired source above. Its historical blocking classification and original open observation remain intact in the prior report. There is no new finding, human decision or risk-acceptance statement in this supplement. The assigning parent owns any later append-only tracker disposition; no tracker files were accessed or changed here.

## Observed checks and mechanical audit

Read-only verification was performed in `/tmp/ticket17-walkthroughs/case-d2` using Git revision/diff/status commands, full source reads, SHA256 checks and Node `v24.22.0`. The initial attempted probe used Node's `execFileSync` to read the old Git blob; it failed with `spawnSync git EPERM` before executing assertions. No permission escalation was requested. The corrected probe read the exact old blob through shell `git show`, passed its text to Node via a quoted environment value, and imported it as a data URL; the repaired validator and caller were imported directly from the exact candidate worktree. No temporary source or test file was created.

The successful `node --input-type=module` probe used built-in `node:assert/strict` and exited 0, printing:

```text
PASS: prior commit independently reproduces F1 sparse-input acceptance and materialized undefined
PASS: four sparse acceptance shapes reject at repaired validator and caller, with raw holes preserved
PASS: both statuses, dependency success, independent normalized output, defaults, dense acceptance and graph rejection, mixed-error accumulation, repeated calls
```

Assertions established:

- The prior exact validator accepts `Array(1)`, returns an `undefined` acceptance value, and owns that returned index. This independently reproduces the reported defect rather than merely trusting the prior prose.
- Repaired validation rejects `Array(1)`, `['done', ,]`, `[, 'done']`, and `['a', , 'b']` with the acceptance error and no `value`; `prepare` returns exit 2. Deeply frozen input containers remain valid inputs for rejection, and their hole ownership patterns stay unchanged.
- A valid two-ticket plan with both supported statuses and an inter-ticket dependency succeeds through validation and `prepare`. Returned tickets/dependency/acceptance arrays are distinct from raw containers. Mutating returned arrays preserves raw data. Optional dependencies still default to an empty array.
- Empty, blank, nonstring and null acceptance inputs reject. Duplicate IDs, unknown/self/duplicate dependencies and a two-ticket cycle reject. A mixed-invalid plan accumulates version, title, status, acceptance and unknown-dependency errors. Repeated validation produces equal results.

Source identities remain:

| File | SHA256 |
| --- | --- |
| repaired `CONTRACT.md` | `a3eaf6f98273016ec553632ebbc6842c95a275e80eec49b95424717e4ea3fb59` |
| repaired `cli.js` | `0433e43678cd9b88e030f67f2c52201d86c0643d9383a908c143340f09e45bf0` |
| repaired `validator.js` | `45cd312dd8f9cd7d1816b3d78890cdabf955a0f47ef28fc501eb3d53f9c855ed` |
| prior `validator.js` | `0f9a4407567f042990dd0a0ae80ab844f269a09b26bb93539b07d5352b5351b6` |

Applicable frozen instructions were already read for the initial assessment and retain these SHA256 identities:

| Path | SHA256 |
| --- | --- |
| `/tmp/ticket17-walkthroughs/guidance/1-ownership-review.md` | `9b76eb5e2b89a4bc6fb5ec07e091321158ff8a628ec70dac257229a8d6098f4d` |
| `/tmp/ticket17-walkthroughs/guidance/2-review-records.md` | `71eff72da027b67a9dc0652bac589d56539678b8405ea48c6435e03229cf480c` |
| `/tmp/ticket17-walkthroughs/guidance/3-SKILL.md` | `2c20617f87ec8af6a434859f381b2f061a69b530444e74eb39e78bb016a6d1e2` |

The initial report and the newly supplied prior report were hashed before and after the checks and retained identical contents. The source worktree remained clean. No initial output, prior report, source, guidance, contract or other case was modified. This supplemental report is the only new output of this follow-up.

## Limits

This supplement verifies the named concern plus its affected caller and ordinary validation behavior; it is not another fresh full-ticket assignment. The separately preserved initial report records that broader source assessment. No parent repository, other case source, sibling report beyond the one newly authorized prior report, linked guidance resource, harness implementation, external suite, benchmark or human QA was inspected. Inputs with hostile getters/proxies, overridden iterators and unbounded graph depth remain outside these checks. No JSON-only or dense-array restriction is assumed: the sparse arrays here use the supplied public JavaScript operation directly. Hashes establish identity, and probes establish observed cases; the fixed conclusion also rests on the actual validation/copy/publication flow described above.
