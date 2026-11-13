# Human QA gates feature promotion

After plan approval, the harness may automatically implement, verify, review, and integrate individual tickets into a feature branch, but promotion into the development branch requires human acceptance of an exact tested milestone candidate. This refines [ADR-0001](0001-reusable-harness-and-local-integration.md), separating continuous verified ticket integration from the human's acceptance of a meaningful increment instead of postponing all integration until the feature is finished.

Each plan has a final QA milestone and may have earlier ones; the next milestone bounds ticket execution. QA decisions identify the approved plan version and candidate inputs, remain separate from immutable approved requirements, and become stale when those inputs change. Planned QA checkpoints permit deliberate stop and continuation; recovery from arbitrary interruptions remains deferred, as do hosted PR approval and publishing.
