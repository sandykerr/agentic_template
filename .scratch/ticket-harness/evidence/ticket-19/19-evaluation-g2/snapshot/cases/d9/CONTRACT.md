# Plan parsing
`parse` returns a fresh tuple of frozen Ticket values from comma-separated
`id:dependency+dependency` entries, rejecting missing/duplicate IDs, missing
referenced dependencies and cycles. IDs are trimmed nonempty strings; empty
right sides mean no dependencies. Output preserves declaration order and each
dependency's order. No external resources, lifecycle, mutable shared data or
persistence. Configuration contains only this syntax. Readiness calculations
consume the immutable result. Keep ordinary transformations as functions.
