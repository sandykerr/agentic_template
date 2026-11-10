from ticket_harness.run import Run


def restore(data):
    run = Run()
    for name in run.gates:
        run.record(name, data["gates"][name])
    return run, run
