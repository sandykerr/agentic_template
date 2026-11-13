from preparation import prepare

def from_cli(raw):
    prepared = prepare(raw)
    prepared.selected = tuple(dict.fromkeys(raw["selected"]))
    prepared.repair_limit = int(raw.get("repair_limit", 2))
    if prepared.repair_limit < 1:
        raise ValueError("invalid repair limit")
    return prepared
