class Prepared:
    def __init__(self, raw):
        self.raw = dict(raw)
        self.selected = None
        self.repair_limit = None

def prepare(raw):
    if not raw.get("selected"):
        raise ValueError("empty selection")
    return Prepared(raw)
