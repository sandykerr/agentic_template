from dataclasses import dataclass
from checking import attach

@dataclass
class Attempt:
    id: str
    handoff: dict | None = None

class Execution:
    def __init__(self):
        self.history = []

    def start(self, identity):
        self.history.append(Attempt(identity))

    def receive(self, attempt_id, payload):
        return attach(self.history, attempt_id, payload)

    def decision(self, attempt_id):
        return next(a.handoff for a in self.history if a.id == attempt_id)
