from calculator import calculate_discount


def test_regular_customer():
    assert calculate_discount(100, "regular") == 10


def test_member_customer():
    assert calculate_discount(100, "member") == 20


def test_premium_customer():
    assert calculate_discount(100, "premium") == 30
