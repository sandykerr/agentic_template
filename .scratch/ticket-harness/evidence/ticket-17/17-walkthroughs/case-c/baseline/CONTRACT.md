# Approved attempt contract
Attempt owns lifecycle status and event history. Every status transition has a
matching event appended in the same owner operation. Only constructor, submit,
and complete write status/history. Callers invoke these operations. Reports read
status/history without mutation. Persistence is absent; reconstruction is outside
this small program. Submission and completion cannot throw in this fixture.
Scoped request: add runTicket to submit and complete an attempt and return a
summary. Preserve owner invariants. Internal naming/class layout is a worker
choice. No additional lifecycle states are requested.
