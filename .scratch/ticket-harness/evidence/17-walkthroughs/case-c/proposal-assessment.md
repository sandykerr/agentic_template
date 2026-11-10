# Case C — supplemental privacy-proposal classification

**Classification: evidence-supported optional design suggestion.** Making Attempt's lifecycle storage private and exposing read-only observations could enforce the already-approved permitted-writer rule. It is **not required** for the scoped outcome, is not an additional blocking finding, and is not authorized for implementation by this assessment-only request.

## Identity and preserved original finding

- Assignment: `/root/implement_17/walkthrough_c`, supplemental proposal-classification request on the same reviewer assignment.
- Settings: parent confirmed actual spawn arguments `fork_turns=none`, `model=gpt-6.1-sol`, `reasoning_effort=high`. This records parent-observed configuration; provider/backend delivery telemetry remains unavailable. Active-context target remains at most 250,000 tokens; measured active context is unavailable.
- Fixed original baseline: `2ffaf5b8e05a02b448cdbe9bb7c13f371c3a80e7`.
- Exact assessed candidate and re-observed HEAD: `2e70734df5cd491e7f0b7c8363f25679ae7570a5` in `/tmp/ticket17-walkthroughs/case-c`.
- Original report: [case-c-report.md](case-c-report.md), review/report `review-walkthrough-case-c/standards-01`.
- Original full finding key: `review-walkthrough-case-c/standards-01/F1`.
- Original report SHA-256 before this supplement: `b65638e387a4306f433ff841a26ca70dea57cd7653bb0fc678da757d3409cd16`.

F1 remains **blocking and open** at the assessed candidate. `execution.js:4` directly sets `a.status = 'complete'`, violating `CONTRACT.md:2-4`, which assigns lifecycle writes to Attempt's constructor, submit, and complete operations and requires a matching event in the same owner operation. `attempt.js:4` already provides the correct completion operation. On the ordinary fresh-Attempt path, `execution.js:3-5` produces status `'complete'` with events `['starting', 'submitted']`; `report.js:1` copies that incomplete history. This consequence is established by static source tracing, not a runtime test. Replacing the direct assignment with `a.complete()` is the proportionate required correction. This supplement neither downgrades that finding nor records it as fixed.

## Proposal and substantive assessment

The supplied alternative is to make `Attempt.status` and `Attempt.events` private and provide read-only observations, **in addition to** correcting the caller. The proposal is supported as optional because it targets the specific mechanism demonstrated by F1: a caller currently has writable access to the owner's lifecycle storage and in fact uses it to bypass the owner. Enforcing the existing writer rule at the module's interface could prevent this kind of accidental bypass and keep lifecycle coordination local to Attempt. This is a concrete connection to the inspected source and approved ownership rule, rather than a preference for classes or file layout.

Nevertheless, the approved contract does not demand language-enforced privacy. `CONTRACT.md:8-9` leaves internal naming/class layout to the worker. Calling the existing nonthrowing completion operation already restores the full requested submit/complete/summary flow and its paired events. The small owner interface already has useful depth: each lifecycle operation coordinates state and history behind a single call. Privacy would strengthen enforcement of that interface, not supply behavior missing from the approved owner operations. It must not become a new acceptance condition or a reason to withhold approval after the actual bypass is correctly repaired and independently revalidated.

The proposal's two storage fields also have different observation risks. Status is a primitive string, while events is a mutable array. Merely hiding an events field and returning that same array from a getter would still let callers mutate owner history; a genuinely read-only observation would need a defensive copy or an equivalent mechanism. `report.js:1` currently copies the events it receives and never mutates the Attempt, so this reader supplies no observed second writer or additional defect. There is no evidence here of other callers corrupting history or a broader encapsulation failure. The optional suggestion therefore rests on enforcing the documented rule against the demonstrated caller-bypass mechanism; it does not assert unobserved failures.

The original report's statement that public mutable properties alone do not justify a separate encapsulation refactor remains applicable. This assessment explicitly classifies a newly supplied proposal, using the actual bypass and the existing owner rule as evidence. It does not add an optional finding retrospectively, change the original finding count, or claim privacy is necessary. The evidence supports considering a compatible enforcement improvement, not requiring a refactor simply because the properties are public.

## Authorization, compatibility, and scope limits

The supplied contract permits internal implementation choices within its existing ownership and reader responsibilities. An authorized implementer could consider private storage with compatible read-only observations as such a choice if it preserves the existing operations, returned values, and reader behavior. That does not require inventing a new owner or new lifecycle state. The current supplemental request authorizes assessment only, so no implementation has been performed.

The concrete design has not been supplied. Replacing the current public observations without adapting `report.js:1` would break the summary reader. Getters preserving `a.status` and `a.events`, or another explicitly compatible design, could avoid that problem. There is no supplied runtime/toolchain compatibility requirement establishing which private-field mechanism is available, and no unseen consumer compatibility can be certified. These are limits on endorsing a particular implementation, not new blockers on the existing minimal remedy.

No neighboring refactor, new lifecycle states, persistence, reconstruction, exception handling, or broader writer-role changes are justified. Those additions are outside the request. A later proposal that actually changes the approved ownership contract or requires scope expansion would need the source-backed human decision required by the supplied ownership guidance. This report invents neither such a change nor a human approval. Optional privacy work can be declined without accepting F1's present violation; F1 still needs its required correction.

## Guidance identities and mechanical audit

This assessment uses the same three frozen guidance texts and approved contract as the original report; their contents remain in this assignment's context. They were not replaced with other-case or parent-repository material. Rechecked identities:

| Path | SHA-256 |
| --- | --- |
| `/tmp/ticket17-walkthroughs/guidance/1-ownership-review.md` | `9b76eb5e2b89a4bc6fb5ec07e091321158ff8a628ec70dac257229a8d6098f4d` |
| `/tmp/ticket17-walkthroughs/guidance/2-review-records.md` | `71eff72da027b67a9dc0652bac589d56539678b8405ea48c6435e03229cf480c` |
| `/tmp/ticket17-walkthroughs/guidance/3-SKILL.md` | `2c20617f87ec8af6a434859f381b2f061a69b530444e74eb39e78bb016a6d1e2` |
| `/tmp/ticket17-walkthroughs/case-c/CONTRACT.md` | `2058b00ee1e33f424af7707e5e3dec4c839e7b07d75a99299120d7fb4b8dc35b` |

The supplemental inspection re-read all four supplied tracked files, rechecked HEAD and working-tree status, and hashed the original report and guidance/contract. `git status --short` returned no entries. The original report contains the complete candidate source identities, baseline diff scope, and original inspection record. The flows assessed here are unchanged initialization, submit, complete, new caller completion, and summary observations. Persistence/restoration are expressly absent in `CONTRACT.md:5-6`.

No runtime tests, source edits, original-report edits, other-case reads, parent-repository reads, or new human decisions were performed. No implementation of the privacy proposal exists to validate. The optional classification is a substantive design judgment tied to the supplied evidence; hashes and a clean working tree establish identity, not that judgment's truth.
