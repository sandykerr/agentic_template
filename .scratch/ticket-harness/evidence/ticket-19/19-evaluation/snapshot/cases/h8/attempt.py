class Attempt:
    def __init__(self, identity):
        self._record = {"id": identity, "status": "running", "revision": None}
        self._current = dict(self._record)

    def submit(self, revision):
        if self._record["status"] != "running" or not revision:
            raise ValueError("invalid submission")
        self._transition("submitted", revision)

    def complete(self):
        if self._record["status"] != "submitted":
            raise ValueError("invalid completion")
        self._transition("completed", self._record["revision"])

    def _transition(self, status, revision):
        updated = {**self._record, "status": status, "revision": revision}
        self._record = updated
        self._current = dict(updated)

    def snapshot(self):
        return dict(self._record), dict(self._current)
