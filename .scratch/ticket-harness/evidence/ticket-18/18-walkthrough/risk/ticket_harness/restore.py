from types import SimpleNamespace


def restore(data):
    run = SimpleNamespace(gates=dict(data["gates"]))
    review = SimpleNamespace(gates=dict(run.gates))
    return run, review
