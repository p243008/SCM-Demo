def calculate_discount(price, customer_type):
    if customer_type == "premium":
        return price * 0.03

    if customer_type == "member":
        return price * 0.20

    return price * 0.10
