"""Discount calculation for the SCM demo."""

PREMIUM_DISCOUNT = 0.30
MEMBER_DISCOUNT = 0.20
REGULAR_DISCOUNT = 0.10


def calculate_discount(price, customer_type):
    """Return the discount amount for a price and customer type."""
    if customer_type == "premium":
        return price * PREMIUM_DISCOUNT

    if customer_type == "member":
        return price * MEMBER_DISCOUNT

    return price * REGULAR_DISCOUNT
