def validate_handoff(attempt_id, payload):
    if payload.get("attempt") != attempt_id or not payload.get("decision"):
        raise ValueError("invalid handoff")
    return dict(payload)

def attach(history, attempt_id, payload):
    handoff = validate_handoff(attempt_id, payload)
    history[-1].handoff = handoff
    return handoff
