import pytest
from products import Product


def test_creating_prod():
    """Test that a normal product is created correctly."""
    product = Product("MacBook Air M2", price=1450, quantity=100)

    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() is True


def test_creating_prod_invalid_details():
    """Test that invalid product data raises ValueError."""
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)   # empty name

    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)   # negative price


def test_prod_becomes_inactive():
    """Test that a product becomes inactive when quantity is set to 0."""
    product = Product("MacBook Air M2", price=1450, quantity=100)

    product.set_quantity(0)

    assert product.get_quantity() == 0
    assert product.is_active() is False


def test_buy_modifies_quantity():
    """Test that buying a product reduces stock and returns correct total price."""
    product = Product("Google Pixel 7", price=500, quantity=10)

    total_price = product.buy(2)

    assert total_price == 1000
    assert product.get_quantity() == 8
    assert product.is_active() is True


def test_buy_too_much():
    """Test that buying more than available stock raises ValueError."""
    product = Product("Bose QuietComfort Earbuds", price=250, quantity=5)

    with pytest.raises(ValueError):
        product.buy(10)
