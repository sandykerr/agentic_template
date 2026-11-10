# Report handoff
An attempt's validated human-decision handoff belongs to that attempt even after
a later attempt starts. History preserves all attempts in start order. Report
work may finish after another attempt has been appended. `attach` receives the
attempt ID supplied by the report command; validation ensures handoff content
is valid for that ID. Checking validates and returns report information; it
must not choose or edit an attempt from shared history. Execution locates the
identified owner and asks it to attach the handoff. Consumers read by attempt ID.
Unknown IDs reject without changing any attempt. No durable checkpoint here.
