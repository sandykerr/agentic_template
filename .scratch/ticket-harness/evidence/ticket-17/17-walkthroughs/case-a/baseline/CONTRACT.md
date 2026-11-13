# Approved capacity contract
Capacity owns available units. Remaining capacity must never become negative.
Only Capacity.reserve may write remaining after construction. It atomically
validates positive integer units and sufficient capacity; invalid reservations
return false without mutation. All submission modes respect this contract.
There is no durable representation or restoration path in this service.
Scoped request: add cancellation so reserved units can be returned, preserving
existing submit behavior and reservation invariants. Capacity.cancel is a new
permitted writer; it rejects nonpositive/noninteger amounts without mutation.
