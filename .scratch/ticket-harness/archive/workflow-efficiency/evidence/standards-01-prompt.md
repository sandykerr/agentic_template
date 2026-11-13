You are the fresh independent Standards reviewer for this workflow follow-up.
Read and apply `.scratch/workflow-efficiency/evidence/review-brief.md` from the
repository root `/home/ajkerr1/development/agentic_template`.
Report documented-standard breaches with exact standard and source locations,
and separately label judgment calls. Assess actual routing/ownership across
changed and unchanged instructions; distinguish optional improvements from
blocking correctness, reliability or maintenance consequences. Skip checks
already enforced by tooling. Preserve independence from sibling reports. Save
your complete original report to `/tmp/workflow-efficiency-standards-01-original.md`;
return that path and brief result.

Apply this smell baseline as heuristics, with documented repository rules taking
precedence; every smell is a judgment call rather than a hard rule:

- Mysterious Name: a function, variable, or type whose name does not reveal what
  it does or holds. Rename it; if no honest name comes, the design is murky.
- Duplicated Code: the same logic shape appears in more than one hunk or file.
  Extract the shared shape and call it from both.
- Feature Envy: a method reaches into another object's data more than its own.
  Move the method onto the data it envies.
- Data Clumps: the same few fields or params keep traveling together. Bundle
  them into one type and pass that.
- Primitive Obsession: a primitive or string stands in for a domain concept
  deserving its own type. Give the concept its own small type.
- Repeated Switches: the same switch/if cascade on the same type recurs. Use
  polymorphism or one map both sites share.
- Shotgun Surgery: one logical change forces scattered edits across many files.
  Gather what changes together into one module.
- Divergent Change: one file/module is edited for several unrelated reasons.
  Split so each module changes for one reason.
- Speculative Generality: abstractions, parameters or hooks for needs outside
  the spec. Delete them and inline until a real need shows.
- Message Chains: long a.b().c().d() navigation callers should not depend on.
  Hide the walk behind one method on the first object.
- Middle Man: a class/function mostly delegates onward. Cut it and call the
  real target directly.
- Refused Bequest: a subclass/implementer ignores or overrides most inheritance.
  Drop inheritance and use composition.
