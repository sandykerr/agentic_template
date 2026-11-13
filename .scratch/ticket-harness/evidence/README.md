# Ticket harness evidence

Use a ticket folder for its completion record, original reviews, checks and
supporting captures. Existing specialized subfolders remain together inside it.
Selected historical raw captures were retired under the human's recorded
case decisions. Current ticket READMEs identify retained conclusions and discarded
material. Organization and retirement establish no new test results, resolved
findings or human acceptance.

| Tickets | Current folders |
| --- | --- |
| 01–06 | [01](ticket-01/README.md), [02](ticket-02/README.md), [03](ticket-03/README.md), [04](ticket-04/README.md), [05](ticket-05/README.md), [06](ticket-06/README.md) |
| 07–12 | [07](ticket-07/README.md), [08](ticket-08/README.md), [09](ticket-09/README.md), [10](ticket-10/README.md), [11](ticket-11/README.md), [12](ticket-12/README.md) |
| 13–18 | [13](ticket-13/README.md), [14](ticket-14/README.md), [15](ticket-15/README.md), [16](ticket-16/README.md), [17](ticket-17/README.md), [18](ticket-18/README.md) |
| 19–24 | [19](ticket-19/README.md), [20](ticket-20/README.md), [21](ticket-21/README.md), [22](ticket-22/README.md), [23](ticket-23/README.md), [24](ticket-24/README.md) |

Cross-ticket bundles stay separate:

- [M1 cumulative assessment](../reviews/M1-architecture-01.md) and
  [M1 QA captures](m1-qa-01/): open caller-index finding and demonstration records.
- [M1 human correction](../reviews/M1-human-readability-01.md) and
  [source/check captures](m1-human-review-01/): retained source-specific results.
- [Retention audit](evidence-retention-audit-01/README.md) and
  [human case decisions](evidence-retention-audit-01/retention-decisions.md).
- [Cleanup and organization decisions](../evidence-cleanup-and-organization-decisions.md):
  current direction, exceptions and verified changes.

## Historical paths

On 2026-11-13 ticket artifacts moved without changing their bytes. Original
filenames and complete specialized subtrees were retained. Translate repository
paths using this rule, for tickets 01–24:

```text
.scratch/ticket-harness/evidence/NN-<suffix>
    → .scratch/ticket-harness/evidence/ticket-NN/NN-<suffix>
```

The rule applies to files and directories, including every descendant. For example,
`15-observations/repair1-final-suite/` is now
`ticket-15/15-observations/repair1-final-suite/`, and `19-evaluation-g5/` is now
`ticket-19/19-evaluation-g5/`. The one naming exception is
`ticket16-standards-identities.json`, now in
[ticket-16/](ticket-16/ticket16-standards-identities.json).

Surviving captured reports, completion records, histories, manifests,
source/instruction snapshots, audit reports and scripts remain verbatim. Their embedded paths and
links describe the original layout. For a historical relative link, first resolve
it against the document's original location, then apply the rule above. Same-ticket
basename links and links within whole moved subtrees generally still work; links
to tracker files, other tickets or repository documentation may need this mapping.
Use the new ticket READMEs and maintained tracker links for current navigation.

Basename-relative JSON/manifest fields use the corresponding ticket folder as
their root. Original absolute `/tmp` paths identify past executions and are not
rewritten into promises of a usable run. Archive members and frozen checkpoint
internals retain their original identities and paths.

Historical helper scripts may derive the repository root from their old depth,
write to old paths or require vanished temporary fixtures. Inspect them as captured
tools; adapt a separate copy before any future reuse. Current harness code does
not automatically load these ticket evidence folders.

The [original compressed inventory](evidence-retention-audit-01/worker-inventory-data.json.gz)
still records original paths, hashes and file kinds. Apply the mapping to locate
surviving files; consult ticket retirement notes for deliberately removed material.
The inventory was not rewritten into a new historical observation, and a retained
hash does not make retired bytes available.
This organization introduced no old-path aliases and removed no Git history.

## Retired evidence

The human authorized selective retirement after organization. The
[execution account](../evidence-cleanup-and-organization-decisions.md#retroactive-archival-and-selective-retirement)
records scope, authority, exceptions and actual reductions. Each affected ticket
README has a `Retired evidence` section with its lasting results and limits.

Historical completion/review records describe what was retained when written.
Their references to removed logs, raw trees or captured telemetry are historical;
the current navigation does not promise that those originals remain available.
Rerunning a command would create a new observation. Retained code identities,
result records and summaries do not recreate discarded output or original authority.

## M1 QA navigation after organization

The [original QA guide](m1-qa-01/qa-guide.md) retains its original bytes and scope.
Use these current destinations for its ticket-level inputs:

- Concern-to-repair trace: [first ticket 24 Spec report](ticket-24/24-review-spec-01.md),
  [full finding history](ticket-24/24-finding-history.md),
  [final Spec](ticket-24/24-review-spec-03.md) and
  [final Standards](ticket-24/24-review-standards-03.md).
- Reviewer evaluation: [ticket 19 navigation](ticket-19/README.md),
  [C5 results](ticket-19/19-evaluation-g5/results.md),
  [original Spec judgment](ticket-19/19-evaluation-g5/spec-c5-raw.md) and
  [original Standards judgment](ticket-19/19-evaluation-g5/standards-c5-raw.md).
- Explicitly synthetic decision examples:
  [ticket 16 miniature](ticket-16/16-miniature/README.md).
- Genuine old-code compatibility:
  [producer](ticket-24/24-checkpoint/producer.json),
  [consumer](ticket-24/24-resume-checkpoint/continuation-final.json) and
  [archive audit](ticket-24/24-resume-checkpoint/audit.json).
- Final ticket 24 context: [resumed packet](ticket-24/24-resume-review-packet.md).

M1 remains unaccepted and its caller-index finding remains open. The named
temporary demonstration environment is absent as of the 2026-11-13 check; retained
records and archives describe historical observations, not a live continuation.
