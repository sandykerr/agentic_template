# Approved gate contract
Gates owns durable gate records and alone writes validity. A verified reference
must be the same canonical object as its gate record, including after checkpoint
restoration. Source changes invalidate all gates from another source and every
verified consumer must observe that invalidation. Checkpoint stores records and
verified IDs, preserving the existing JSON shape. Invalid/missing gate IDs must
reject restoration rather than establish readiness.
Scoped request: add replaceSource, invalidating prior-source evidence through the
existing Gates owner. Preserve checkpoint compatibility and readiness behavior.
