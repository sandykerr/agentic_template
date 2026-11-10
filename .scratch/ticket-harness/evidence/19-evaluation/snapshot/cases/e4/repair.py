def receive_repair(attempt, revision):
    if attempt.record["status"] != "running":
        raise ValueError("not running")
    attempt.record["revision"] = revision
    attempt.record["status"] = "submitted"
    attempt.ticket["attempt"] = attempt.record["id"]
    attempt.ticket["revision"] = revision
    attempt.ticket["status"] = "submitted"
