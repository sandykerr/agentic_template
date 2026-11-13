# Saved checks
Run owns durable gates and verified references. `record` registers successful evidence;
`save` and `restore` preserve JSON keys and later source invalidation semantics.
Verified references resolve to the same canonical gate records used by durable
reporting, so changing a source marks both views invalid. QA reads the verified
view. The caller may invalidate source A after restoring a deliberate stop.
Only Run writes these records; consumer functions are read-only. No concurrency.
