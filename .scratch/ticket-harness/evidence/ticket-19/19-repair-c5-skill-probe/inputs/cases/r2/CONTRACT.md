# Stock reservation
reserve(available, requested) accepts nonnegative integer stock and a positive
integer request. It returns remaining stock for a satisfiable request. Requests
above available stock reject with ValueError; no negative stock result may escape.
It owns this validation; the caller should not precheck availability. No mutation,
external state or persistence.
