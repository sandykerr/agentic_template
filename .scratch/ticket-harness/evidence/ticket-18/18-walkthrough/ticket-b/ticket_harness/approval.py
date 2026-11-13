def candidate_ready(run):
    return run.gates["checks"] and run.gates["approval"]
