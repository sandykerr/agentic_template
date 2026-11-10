from attempt import Attempt

def execute(identity, revision):
    attempt = Attempt(identity)
    attempt.submit(revision)
    attempt.complete()
    return attempt.snapshot()
