import json

class Run:
    def __init__(self):
        self.gates = []
        self.verified = []

    def record(self, source):
        gate = {"source": source, "passed": True, "valid": True}
        self.gates.append(gate)
        self.verified.append(gate)

    def invalidate(self, source):
        for gate in self.gates:
            if gate["source"] == source:
                gate["valid"] = False

    def save(self):
        return json.dumps({"gates": self.gates, "verified": self.verified})

    @classmethod
    def restore(cls, saved):
        value = json.loads(saved)
        run = cls()
        run.gates = value["gates"]
        run.verified = value["verified"]
        return run
