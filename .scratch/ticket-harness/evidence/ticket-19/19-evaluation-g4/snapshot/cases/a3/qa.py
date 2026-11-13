def eligible(run, source):
    return any(g["source"] == source and g["passed"] and g["valid"]
               for g in run.verified)

def report(run):
    return [dict(gate) for gate in run.gates]
