from payments.refund import refund

def test_partial_refund():
    assert refund(1000, 300) == 300

def test_refund_cannot_exceed_charge():
    import pytest
    with pytest.raises(ValueError):
        refund(1000, 1500)
