class Attempt:
    def __init__(self, identity, ticket):
        self.record = {"id": identity, "status": "running", "revision": None}
        self.ticket = ticket

    def submit(self, revision):
        if self.record["status"] != "running":
            raise ValueError("not running")
        self.record["revision"] = revision
        self.record["status"] = "submitted"
        self.ticket["attempt"] = self.record["id"]
        self.ticket["revision"] = revision
        self.ticket["status"] = "submitted"
