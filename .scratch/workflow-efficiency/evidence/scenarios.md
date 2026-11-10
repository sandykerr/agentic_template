# Preparation decision exercise

Use the repository's current implementation, development-efficiency, testing and
review contracts to decide the next actions in these independent hypothetical
states. Explain what can proceed now, what must wait, required verification and
which evidence remains applicable. This is preparation-only: do not implement a
ticket, dispatch reviewers/repairs, run a harness, or change repository files.

1. An ordinary CLI implementation worker has a failing formatting check and a
   passing behavior run whose required Git observation was not captured. Neither
   source reviewer has been assigned. The worker proposes sending two reviewers
   immediately and reconstructing the Git evidence from a remembered result.
2. Spec has returned a blocker against committed revision A; Standards is still
   inspecting A. The orchestrator can edit A now and wants to start a repair using
   the Spec summary. There is also an optional naming suggestion.
3. Both original reports against A are saved. One blocker demonstrates a retained
   input alias in a state-copy operation; the relevant contract also covers saved,
   restored and returned state. These operations are all in the approved ticket
   scope. The second report is clean. The proposed repair changes only the exact
   line in the counterexample and then requests review of that patch from A.
4. A later complete review round finds another instance of the same alias failure
   pattern. No numerical time/spending cap was agreed, and authorized repair scope
   remains. The orchestrator proposes a new full reviewer round immediately with
   a summary saying the previous review was too strict.
5. A verified implementation's subsequent changes are (a) a completion-note link
   and handoff paragraph, or, in a separate branch, (b) a shared parser's accepted
   input handling. Earlier checks and reviews passed on the previous revision.
   Decide how their evidence applies to each branch, including required final
   implementation checks and source review.
