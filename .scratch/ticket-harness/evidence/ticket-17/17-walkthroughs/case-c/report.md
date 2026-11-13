# Case C — original Standards review

Result: **one blocking finding**, no optional findings. The new entry operation bypasses the approved lifecycle owner and returns completion status without its required completion event. This is a scoped guidance walkthrough; the harness implementation is outside this assessment.

## Assignment and source identity

- Review ID: `review-walkthrough-case-c`.
- Report ID: `standards-01`; assignment: `/root/implement_17/walkthrough_c`.
- Axis: fresh independent Standards development review, including substantive ownership assessment of the entire supplied ticket.
- Original fixed baseline: `2ffaf5b8e05a02b448cdbe9bb7c13f371c3a80e7`.
- Exact assessed candidate and observed HEAD: `2e70734df5cd491e7f0b7c8363f25679ae7570a5`.
- Baseline tree: `2e94a420c3e47e2108888de7e28227975d5b7ee5`; candidate tree: `f6d3146d6b83bdd4e47369295483785ff7bf6d97`.
- Repository: `/tmp/ticket17-walkthroughs/case-c`; report is outside that repository.
- Reviewer model/reasoning: parent confirmed the actual spawn arguments `fork_turns=none`, `model=gpt-6.1-sol`, `reasoning_effort=high`. This is parent-observed assignment configuration; provider/backend telemetry and independent confirmation of backend delivery are unavailable.
- Context target: at most 250,000 active context tokens. The supplied material is small, but actual active-context telemetry is unavailable; this is a target, not a measured attestation.
- This Standards report is completed. Integration eligibility, milestone assessment, Spec review, human QA acceptance, repair, and independent repair verification are not assessed or claimed. No prior reports or finding dispositions were supplied or consulted.

## Guidance and approved contract identities

The following supplied frozen files were read in full. Their linked resources were not required by this assignment and were not opened. The third file supplies the codebase-design vocabulary applied below.

| Instruction/contract path | SHA-256 |
| --- | --- |
| `/tmp/ticket17-walkthroughs/guidance/1-ownership-review.md` | `9b76eb5e2b89a4bc6fb5ec07e091321158ff8a628ec70dac257229a8d6098f4d` |
| `/tmp/ticket17-walkthroughs/guidance/2-review-records.md` | `71eff72da027b67a9dc0652bac589d56539678b8405ea48c6435e03229cf480c` |
| `/tmp/ticket17-walkthroughs/guidance/3-SKILL.md` | `2c20617f87ec8af6a434859f381b2f061a69b530444e74eb39e78bb016a6d1e2` |
| `/tmp/ticket17-walkthroughs/case-c/CONTRACT.md` | `2058b00ee1e33f424af7707e5e3dec4c839e7b07d75a99299120d7fb4b8dc35b` |

The approved request is in `CONTRACT.md:7-9`: add `runTicket` to submit and complete an attempt and return a summary while preserving owner invariants. `CONTRACT.md:2-4` assigns status and event history to Attempt, requires a matching event in the same owner operation for each transition, permits only constructor/submit/complete to write them, and directs callers to those operations. `CONTRACT.md:4-6` makes reports read-only, excludes persistence/reconstruction, and guarantees submit/complete cannot throw in this fixture.

The ambient user instructions identify domain/testing/Python/issue-tracker documents in the parent workspace. They were not accessed: this assignment explicitly forbids parent-repository access and supplies the isolated source and three frozen texts as context. No Python, dependency installation, tests, issue operations, or parent code exploration was performed. No additional isolated `AGENTS.md` or local standards document appears in the repository inventory.

## Inspected scope and assumptions

All four tracked files were inspected in full at the candidate; the complete baseline-to-candidate diff and baseline contract/owner/reader were also inspected. Only `execution.js` changes in this ticket.

| File/flow | Assessment scope |
| --- | --- |
| `CONTRACT.md:1-9` | Scoped behavior, approved owner/writers, event invariant, failure and restoration limits. |
| `execution.js:1-6` | New entry caller, submit/completion ordering, direct state write, call into summary. |
| `attempt.js:1-5` (unchanged) | Constructor initialization; all owner status/history operations and their paired writes. |
| `report.js:1` (unchanged) | Summary consumer, returned status and copied history; absence of source mutation. |

Actual flow followed: `new Attempt()` initializes `starting` and its event; `runTicket(a)` calls `submit()`, writes status itself, then calls `summary(a)`; the summary returns current status and a copied event array. A repository-wide search across the four source/contract files found every supplied lifecycle reference. There is no supplied caller above exported `runTicket`, no other supplied writer/reader, and no persistence/restoration/invalidation operation to follow. Those absences delimit this fixture; they are not claims about unseen applications.

Assumptions: `a` is a valid Attempt under the supplied contract. Behavior for arbitrary duck-typed objects, concurrency, malicious external property mutation, repeat invocation rules, new lifecycle states, and thrown submission/completion failures are not requested. No such requirements are invented here. Parent repository, other cases, sibling reports/discussions, linked snapshots, runtime harness, and external integrations were omitted by explicit assignment scope. There is no unresolved ownership decision needed for the remedy below: the approved owner already exposes completion.

## Original substantive assessment and review rationale

The owner operations already provide a small interface with useful depth: callers request submission or completion while Attempt coordinates both status and history. Initialization also pairs initial state and initial event. This places knowledge of the lifecycle invariant in one module and gives callers locality without requiring any new class, property visibility rule, or adapter.

The candidate correctly uses that interface for submission, but completion crosses the seam by assigning the owner's storage directly. The entry caller therefore assumes responsibility for part of an invariant it is expressly forbidden to own. Calling the existing completion operation would preserve both ordering and the two state updates. No additional abstraction or neighboring refactor is justified.

The unchanged summary reader complies with its responsibility: it reads status and copies history. That behavior makes the breach visible to consumers, since the copied history accurately lacks the event which the entry caller failed to record. Making the report invent that event would relocate lifecycle responsibility to another unauthorized module and would leave the source attempt inconsistent. The issue belongs at the new entry caller.

### F1 — completion bypasses the lifecycle owner (blocking)

Full finding key: `review-walkthrough-case-c/standards-01/F1`.

- **Contract evidence:** `CONTRACT.md:2-4` requires every transition's event to be appended in the same owner operation and allows only constructor, submit, and complete to write status/history. `CONTRACT.md:7-8` explicitly requires the new operation to preserve those invariants.
- **Code evidence:** `execution.js:3` invokes `a.submit()`, but `execution.js:4` assigns `a.status = 'complete'` directly. The unused existing `Attempt.complete()` at `attempt.js:4` both changes status and appends `'complete'`. `report.js:1`, invoked at `execution.js:5`, copies the current events without repairing them.
- **Concrete consequence:** for a freshly constructed Attempt, static evaluation of the supplied operations yields `{ status: 'complete', events: ['starting', 'submitted'] }`. The required completion event is absent in both the Attempt and returned summary. Status and history disagree about completion; the approved ownership contract and scoped outcome are defeated on the ordinary success path.
- **Classification:** blocking, because this violates an explicit approved invariant and permitted-writer rule. The missing event and forbidden writer are two aspects of the same bypass, recorded as one finding.
- **Proportionate remedy:** replace the direct assignment at `execution.js:4` with `a.complete()`. The existing nonthrowing owner operation already supplies the required behavior. Preserve submission-before-completion and summary-after-completion ordering. No ownership-contract change or human risk-acceptance decision is needed to propose this repair.
- **Disposition:** open. No source was modified, no repair commit exists in this assessment, and independent verification is pending any repair. The responsible next action is for the assigning agent/authorized implementer to repair and commission exact-revision revalidation from the fixed original baseline. This review does not invent a human decision or disposition accepting the breach.

No optional findings are raised. In particular, public mutable properties alone do not justify a separate encapsulation refactor in this tiny contract: the demonstrated problem is the concrete unauthorized write in the new caller, and the existing owner operation provides its remedy.

## Mechanical evidence audit and observation limits

The following observations establish identity and inspection coverage; they do not independently prove the design conclusion above.

- `git status --short` returned no entries at inspection time.
- `git rev-parse HEAD <baseline>^{tree} <candidate>^{tree}` produced the candidate and tree identities recorded above.
- `git ls-tree -r <candidate>` enumerated exactly `CONTRACT.md`, `attempt.js`, `execution.js`, and `report.js`.
- `git diff <baseline> <candidate> --` showed the entire ticket change: the placeholder in `execution.js` became the six-line entry operation. The owner, reader, and contract were unchanged.
- `git show <baseline>:attempt.js`, `:report.js`, and `:CONTRACT.md` confirmed their baseline content; full candidate reads and `rg -n 'status|events|submit|complete|runTicket|summary' CONTRACT.md attempt.js execution.js report.js` supplied code locations and writer/reader references.
- `git diff --check <baseline> <candidate> --` exited successfully with no output. This is a whitespace check, not validation of owner invariants.
- No tests or runtime execution were performed. The concrete output in F1 is a static trace of the complete supplied source, not an observed test result. No test configuration or testing guidance is supplied inside the isolated fixture; inaccessible parent testing instructions were not substituted with invented checks.

Candidate working-file SHA-256 identities:

| File | SHA-256 |
| --- | --- |
| `attempt.js` | `a93b3291e1cb3f92083e869947d3d86d5e08a5782b5bf0f57d3e71473bc5a3c6` |
| `execution.js` | `39056da921ada5f9308f75adb21680b02136d0c302452cdfc3fcfad52f9b0aa9` |
| `report.js` | `d57b1437a0813ffe3030d599722fb5cde98d86b6c70a9d04665c35a6b6dc4f49` |

This file preserves this review's original substantive assessment and evidence record. It makes no claim of universal design approval, raw backend telemetry, a test pass, repair verification, or human acceptance. No source, approved input, sibling report, or historical disposition was changed.
