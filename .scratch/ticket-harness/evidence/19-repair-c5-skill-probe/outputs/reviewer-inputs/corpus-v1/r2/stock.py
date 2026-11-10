def reserve(available, requested):
    if requested <= 0:
        raise ValueError("request must be positive")
    return available - requested
