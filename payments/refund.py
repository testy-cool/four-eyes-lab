def refund(charged_cents: int, requested_cents: int) -> int:
    """Refund up to the charge; raise ValueError if asked for more."""
    if requested_cents <= 0:
        raise ValueError("refund must be positive")
    if requested_cents > charged_cents:
        raise ValueError("refund larger than the charge")
    return requested_cents
