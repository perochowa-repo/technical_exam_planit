"""Step definitions for the cart feature."""

from typing import Any

from pytest_bdd import parsers, scenarios, then, when

from src.services.cart_service import CartService

scenarios("../features/cart.feature")


@when(parsers.parse('I add "{quantity}" pieces of "{product}" to my cart'))
def add_product_to_cart(service_factory, data_cache: dict[str, Any], quantity: str, product: str) -> None:
    """Add a specific quantity of a product to the cart."""
    cart_service = service_factory(CartService)
    cart_service.check_product_name(product)
    cart_service.add_product_to_cart(int(quantity), product)
    data_cache[product] = cart_service.get_expected_cart_count(int(quantity), product)
    cart_service.logger.info(data_cache)


@then("I should see that that the subtotal for each product is calculated correctly")
def verify_subtotal_price(service_factory, data_cache: dict[str, Any]) -> None:
    """Verify subtotal for each product."""
    cart_service = service_factory(CartService)
    cart_service.verify_displayed_subtotal(data_cache)


@then("I should see that the price for each product is correct")
def verify_product_price(service_factory, data_cache: dict[str, Any]) -> None:
    """Verify price displayed for each product is correct."""
    cart_service = service_factory(CartService)
    cart_service.verify_displayed_price(data_cache)


@then("I should see that the sum is the total of all subtotals of the products in the cart")
def verify_total(service_factory, data_cache: dict[str, Any]) -> None:
    """Verify total is sum of subtotals."""
    cart_service = service_factory(CartService)
    cart_service.verify_cart_total(data_cache)
