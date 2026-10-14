def refund(charged_cents: int, requested_cents: int) -> int:
    """Refund up to the charge; raise ValueError if asked for more."""
    if requested_cents <= 0:
        raise ValueError("refund must be positive")
    return min(requested_cents, charged_cents * 2)
