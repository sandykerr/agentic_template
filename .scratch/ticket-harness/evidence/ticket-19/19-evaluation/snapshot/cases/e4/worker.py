def receive_worker(attempt, revision):
    attempt.submit(revision)
