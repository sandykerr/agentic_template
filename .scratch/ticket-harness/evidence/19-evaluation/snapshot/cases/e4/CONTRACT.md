# Submission observations
Attempt owns submission and the mirrored current-ticket observation. Both normal
worker and repair entry paths preserve the same transition invariant: only a
running attempt may submit, its revision and status change together, and the
current-ticket fields reflect that attempt. Changes to submission policy must
have one owning operation; entry callers delegate rather than reproduce record
edits. State is in-memory and deliberately exposes records to read-only reporting.
Only the owner may write those records. No concurrent calls or persistence here.
