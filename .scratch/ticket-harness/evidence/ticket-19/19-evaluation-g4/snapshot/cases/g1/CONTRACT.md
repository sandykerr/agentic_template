# Prepared input
Preparation owns configuration validation and normalization. Both CLI and resumed
entry paths must return a complete Prepared result: nonempty selected IDs,
normalized unique membership preserving first order, and a positive repair limit
(default 2). Raw configuration is copied, never mutated. Callers may consume the
prepared result directly; they must not finish its initialization in a particular
order or know derived-field rules. Invalid repair limit rejects during preparation,
not later during execution. Result state is in-memory, no checkpoint serialization.
