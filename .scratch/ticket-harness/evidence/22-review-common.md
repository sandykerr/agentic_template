# Ticket 22 independent source review contract

Review only [22: Return clearly prepared inputs](../issues/22-return-clearly-prepared-inputs.md),
approved oop-v2 / review-process-1, M1. Fixed original baseline:
`803c6ff9a4e5e057124aefc5bb96f2c9518162dd`. The dispatch supplies the exact
committed source and canonical worker packet. Resolve both revisions, confirm
the nonempty whole-ticket diff with `git diff <baseline>...<source>`, and inspect
`git log <baseline>..<source> --oneline`. Preserve source throughout assessment.

Read AGENTS.md, GLOSSARY.md, relevant ADRs, the actual seven ticket criteria and
their scoped spec sections. Apply docs/agents/domain.md, python-environment.md,
testing.md, ownership-review.md, review-records.md, architecture-checkpoints.md,
reviewer-evaluation.md and development-efficiency.md. Inspect actual definitions,
usages and unchanged collaborators; summaries, passing tests and hashes do not
establish a substantive design conclusion.

Use evaluated substantive **G2**, final **C5** aggregate
`332ddabe972f596d86cd09eda809bd2f93d1f57602f01d75ed9f39f2b182510d`.
The reviewer-evaluation reference links declaration, manifest, original reports,
results and retained failed trials. Five evolving eight-case corpora and two
guidance versions give finite historical evidence with differing judgments and
misses. Corpus classifications supply no answer pattern for this new source;
there is no general detection, reliability or runtime guarantee.

Trace input entry callers, preparation owner, every writer/consumer, initialization,
snapshot capture, JSON persistence/restoration and invalidation. Explain which
responsibilities changed and why existing owners remain sound. Check explicit
guarantees against accepted inputs and aliases; a narrower input domain requires
contract or enforced validation support. Separate source reasoning from evidence
identity audits. A clean assessment explains invariant preservation.

The preparation interface must return complete validated settings, approved
snapshots, normalized requirements, eligible selection, completion evidence and
applicable worker settings, with explicit filesystem preconditions. Raw settings
stay separate from derived values; run consumes the result without duplicating
preparation rules or externally injecting calculated fields into raw configuration.
All plan consumers, including first-group selection, use validation's returned
checked plan; mutation-free validation is not required. Preserve command validation,
input diagnostics and rejection before processes/refs, legacy/versioned plans,
external prerequisites, primary/explicit selections, readiness/metadata/completion
rules, membership/dependency ordering and worker defaults/overrides. Keep approved
source/config bytes, copied names/hashes, output separation, JSON saved shape,
checkpoint version/status and genuine older checkpoint continuation compatible.
Parsing, graph validation and pure transformations may remain ordinary functions.
Preserve ticket20/21 ownership and the public CLI seam; no configuration framework
or private testing seam. Run lifecycle23, milestone ownership24, blocked-work29,
runtime33/34, orchestration and human QA/promotion are outside this slice.

Inspect genuine pre-edit checkpoint provenance, retained live fixture and final
continuation. Reassess each start/final risk trigger: new lifecycle, persistence or
restoration path, shared mutable state, additional writer. A positive trigger
requires fresh broader affected-workflow assessment before integration. All No
requires no third unconditional reviewer. Real M1 cumulative feature-start
provenance/all-package assessment and human QA remain unperformed and required
before milestone readiness.

No unresolved actual prior finding or relevant pending revalidation is known at
entry. Historical findings retain their original scope. [Eligibility audit](22-root-eligibility.json)
verifies original-to-retained commit mappings from docs/history/2026-11-10-large-file-rewrite.json,
ancestry and runtime/test/config equivalence without editing historical reports.
Use full new finding keys `review-ticket-22/<report-ID>/<local-ID>`.
Consequential ownership, scope and risk decisions remain human-owned; optional
suggestions stay optional.

Assess independently in a fresh context, excluding the current sibling report.
Save your original at the assigned unique path before summarizing; root hashes
and indexes originals unchanged before aggregation. Use docs/templates/reviews/report.md:
exact baseline/source, assignment/report identity, supplied guidance identities,
settings/limits, inspected and omitted scope with reasons, assumptions, substantive
assessment, evidence audit, classified findings with exact source/contract,
counterexample/consequence/remedy and assessment result. Repo whole-ticket scope
and required report fields supersede upstream hunk-only and short-report briefs.
Write only your report and uniquely named audit artifacts. Bookkeeping stays with root.

Requested configuration: fresh GPT-6.1 Sol High independently per axis; advisory
active-context target <=250000. Backend delivery, enforced cap and measured active
context telemetry unavailable unless directly observed. Configuration/digests
alone do not prove delivery/enforcement. Reuse required checks at their exact
source and scope; reproduce focused behavior when useful using the absolute
reusable Python environment. Report actual commands/results and limitations.
