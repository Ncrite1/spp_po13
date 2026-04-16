import requests

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.items.append({"name": name, "price": price})

    def total(self):
        return sum(item["price"] for item in self.items)

    def apply_discount(self, percentage):
        if not (0 <= percentage <= 100):
            raise ValueError("Invalid discount percentage")
        for item in self.items:
            item["price"] *= (1 - percentage / 100)

def log_purchase(item):
    """Логирование покупки с обработкой исключений."""
    try:
        response = requests.post("https://example.com/log", json=item, timeout=5)
        return response.status_code
    except requests.exceptions.RequestException:
        return 500

def apply_coupon(cart, coupon_code):
    coupons = {"SAVE10": 10, "HALF": 50}
    if coupon_code in coupons:
        cart.apply_discount(coupons[coupon_code])
    else:
        raise ValueError("Invalid coupon")
