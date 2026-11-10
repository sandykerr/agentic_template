class Run:
    def __init__(self):
        self.gates = {"checks": False, "approval": False}

    def record(self, name, passed):
        self.gates[name] = passed

    def revoke(self):
        for name in self.gates:
            self.gates[name] = False
