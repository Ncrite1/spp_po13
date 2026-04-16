import pytest
from unittest.mock import patch
from shopping import Cart, log_purchase, apply_coupon

@pytest.fixture
def empty_cart():
    return Cart()

def test_add_item(empty_cart):
    empty_cart.add_item("Apple", 10.0)
    assert len(empty_cart.items) == 1
    assert empty_cart.items[0]["name"] == "Apple"

def test_negative_price(empty_cart):
    with pytest.raises(ValueError, match="Price cannot be negative"):
        empty_cart.add_item("Banana", -5.0)

def test_total(empty_cart):
    empty_cart.add_item("Apple", 10.0)
    empty_cart.add_item("Juice", 20.0)
    assert empty_cart.total() == 30.0

@pytest.mark.parametrize("discount, expected_total", [
    (0, 100.0),
    (50, 50.0),
    (100, 0.0),
])
def test_apply_discount_valid(empty_cart, discount, expected_total):
    empty_cart.add_item("Gadget", 100.0)
    empty_cart.apply_discount(discount)
    assert empty_cart.total() == expected_total

@pytest.mark.parametrize("discount", [-10, 110])
def test_apply_discount_invalid(empty_cart, discount):
    empty_cart.add_item("Gadget", 100.0)
    with pytest.raises(ValueError):
        empty_cart.apply_discount(discount)

def test_log_purchase_mock():
    with patch('requests.post') as mocked_post:
        item = {"name": "Apple", "price": 10.0}
        log_purchase(item)

        mocked_post.assert_called_once_with("https://example.com/log", json=item)

def test_apply_coupon_success(empty_cart):
    empty_cart.add_item("Laptop", 1000.0)
    apply_coupon(empty_cart, "SAVE10")
    assert empty_cart.total() == 900.0

def test_apply_coupon_mocked(empty_cart, monkeypatch):
    fake_coupons = {"TEST": 90}
    with pytest.raises(ValueError):
        apply_coupon(empty_cart, "NON_EXISTENT")