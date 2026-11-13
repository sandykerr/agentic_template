# Approved plan-validation contract
validatePlan is the public pure validation operation. It validates a plan's
nonempty version and tickets, string IDs/titles, the two supported statuses,
nonempty acceptance strings, and string dependency lists. Reject duplicate IDs,
duplicate/unknown/self dependencies and dependency cycles. Return accumulated
errors via {ok:false,errors}; return normalized independent ticket/dependency/
acceptance arrays via {ok:true,value} on success. Preserve raw input unmodified.
All scratch sets/arrays belong to this one call. There is no persistent or shared
mutable state. Optional dependency lists default to empty. A worker may keep
validation together or split helpers; no class/file layout is prescribed.
Scoped request: implement the missing validator behind the existing caller.
