# Fresh bounded repair: ticket25 round1

Rejected source3b0c1ab7ec41929d3febab44269f791e55897e70; original baseline remains
2c01fe9fe04c78fa10a2dac11e94826876467562. Original Spec/Standards and broader
reports/probes are retained in their separately allocated capture directories;
25-review-round1-digests.sha256 identifies originals. 25-finding-history.md records
all five distinct full keys. They consolidate to two owner-local defects:

1. Optional shared/milestone names must be validated whenever supplied, including
empty strings, before output writes. Use a consistent None-versus-present meaning
for validation/routing/linking; never allow an empty supplied value to poison a
reserved ticket or unscoped shared folder. Cover empty shared and empty milestone
at the existing invalid-scope public CLI seam, checking no allocated output.
2. Validate all registered original file identities before an identical-retry
success. Preserve no-overwrite, metadata mismatch rejection and healthy idempotence.
Add the A/B-register, mutate B, retry A regression and unchanged-artifact assertion
at the public CLI seam. No schema/owner/refactor expansion is required.

Read AGENTS/domain/ADRs, current review/testing/environment/tracker contracts,
test-strategy and TDD before edits. Keep coverage map and report actual red/green
commands/results. Parent owns retained Forest203 session10089; send exact scoped
commands/scripts to parent for serial execution rather than opening another SSH
connection or writing competing terminal commands. Do not run tests on login.
Write failing tests, request red execution and await actual results before fixing.
After local fix, request focused green/type/static checks; parent will run required
final full/static/installed gates and create the repair checkpoint before reviews.

Only edit ticket_harness/evidence.py and tests/test_evidence.py, plus your own repair
report/evidence notes as needed. Preserve all existing reports, probes, observations,
planning edits and frozen metadata. Do not mark findings fixed or ticket complete;
fresh reviewers must independently verify exact-source fixes. Current owner/lock/
JSON namespaces and the four trigger assessments remain correct and unchanged.
No neighboring refactor, cleanup/deletion policy, runtime adoption or QA approval.
Requested fresh GPT-6.1 Sol Medium <=250000 active-context target; enforcement/
measured telemetry unavailable. Report requested versus available settings honestly.
