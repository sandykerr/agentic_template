# Local IO
`atomic_write` replaces a local UTF-8 file with complete text using a temporary
file on the same filesystem. Existing content survives an exception before replace;
temporary files are cleaned on failure. Caller supplies a directory that exists.
No crash durability/fsync or metadata preservation guarantee. `invoke` runs an
argument vector without a shell, in a supplied cwd with text capture and finite
timeout, returning nonzero exits for the caller's domain policy; TimeoutExpired
propagates. These primitives own no run/attempt/review state and perform no domain
record mutations. No persistence beyond the explicitly written file.
