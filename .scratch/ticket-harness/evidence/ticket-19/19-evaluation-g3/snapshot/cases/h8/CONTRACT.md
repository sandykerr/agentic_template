# Attempt operations
Attempt owns running -> submitted -> completed transitions and mirrored current
observations. Construction sets both views consistently. Submission requires a
running attempt and nonempty revision; completion requires a submitted attempt.
Invalid operations leave both views untouched. Consumers receive copied snapshots;
caller-owned input dictionaries cannot mutate state. No persistence or concurrency.
Caller asks for operations; it does not edit the record. A small class is permitted
because these operations own a real invariant. No general state-machine framework.
