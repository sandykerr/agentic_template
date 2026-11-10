from copy import deepcopy


class Attempt:
    def __init__(self, identity):
        self._record = {"id": deepcopy(identity), "status": "running", "revision": None}
        self._current = deepcopy(self._record)

    def submit(self, revision):
        if self._record["status"] != "running" or not revision:
            raise ValueError("invalid submission")
        self._transition("submitted", revision)

    def complete(self):
        if self._record["status"] != "submitted":
            raise ValueError("invalid completion")
        self._transition("completed", self._record["revision"])

    def _transition(self, status, revision):
        updated = deepcopy({**self._record, "status": status, "revision": revision})
        current = deepcopy(updated)
        self._record = updated
        self._current = current

    def snapshot(self):
        return deepcopy(self._record), deepcopy(self._current)
