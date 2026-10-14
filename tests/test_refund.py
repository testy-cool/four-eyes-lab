from payments.refund import refund

def test_partial_refund():
    assert refund(1000, 300) == 300
