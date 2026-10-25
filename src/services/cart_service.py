"""Contains the CartService class cart-related actions."""

from decimal import Decimal
from logging import Logger
from typing import Any

from playwright.sync_api import expect

from src.pages.cart_page import CartPage
from src.util.data.cart_products import PRODUCTS


class CartService:
    """Service class for cart-related actions."""

    def __init__(self, page, logger: Logger):
        self.page = page
        self.logger = logger

        self.cart_page = CartPage(page)

    def add_product_to_cart(self, quantity: int, product: str) -> None:
        """Add a specific product to the cart."""
        self.logger.info("Adding %d pieces of product '%s' to the cart.", quantity, product)
        buy_button = self.cart_page.get_buy_button(product)

        for _ in range(quantity):
            previous_count = self.get_cart_count()
            expected_count = previous_count + 1
            buy_button.click()
            expect(self.cart_page.cart_count).to_have_text(str(expected_count))
            self.logger.info("Cart count increased from %d to %d.", previous_count, expected_count)

    def get_cart_count(self) -> int:
        """Get the current count of items in the cart."""
        count = self.cart_page.get_cart_count()
        self.logger.info("Current cart count is: %d", count)
        return count

    def check_product_name(self, product_name: str) -> None:
        """Check first if the product name is in product catalog before adding to cart."""
        self.logger.info("Checking if product '%s' is in the product catalog.", product_name)
        if product_name not in PRODUCTS:
            raise ValueError(f"Product '{product_name}' is not defined in Product Catalog.")

    def get_expected_cart_details(self, quantity: int, product: str) -> dict[str, float | Decimal]:
        """Calculate the expected cart count after adding a specific quantity of a product."""
        product_price = PRODUCTS[product]
        total_price = product_price * quantity
        return {"quantity": quantity, "price": product_price, "subtotal": total_price}

    def verify_displayed_subtotal(self, cart_data: dict[str, Any]) -> None:
        """Verify the displayed subtotal for each cart item."""
        for product, details in cart_data.items():
            expected_subtotal = f"${details['subtotal']:.2f}"
            displayed_product_subtotal = self.cart_page.get_product_subtotal(product)
            self.logger.info("Verifying product '%s': expected subtotal=%s", product, expected_subtotal)
            expect(displayed_product_subtotal).to_have_text(expected_subtotal)
            self.logger.info("Product '%s' subtotal verified.", product)

    def verify_displayed_price(self, cart_data: dict[str, Any]) -> None:
        """Verify the displayed price for each cart item."""
        for product, details in cart_data.items():
            expected_price = f"${details['price']:.2f}"
            displayed_product_price = self.cart_page.get_product_price(product)
            self.logger.info("Verifying product '%s': expected price=%s", product, expected_price)
            expect(displayed_product_price).to_have_text(expected_price)
            self.logger.info("Product '%s' price verified.", product)

    def verify_cart_total(self, cart_data: dict[str, Any]) -> None:
        """Verify that the cart total is equal to the sum of the subtotals."""
        displayed_subtotals = []
        for product in cart_data:
            subtotal = self.get_subtotal_as_value(product)
            displayed_subtotals.append(subtotal)

        calculated_total = sum(displayed_subtotals, start=Decimal("0.00"))
        displayed_total_text = self.cart_page.cart_total_locator.inner_text()
        displayed_total = Decimal(displayed_total_text.replace("Total:", "").replace("$", "").strip())
        self.logger.info("Sum of displayed subtotals: %s", calculated_total)
        self.logger.info("Displayed cart total: %s", displayed_total)

        assert calculated_total == displayed_total, (
            f"Cart total mismatch: calculated {calculated_total:.2f}, displayed {displayed_total:.2f}"
        )

        self.logger.info("Cart total matches the sum of displayed subtotals.")

    def get_subtotal_as_value(self, product_name: str) -> Decimal:
        """Get Price Displayed as a value."""
        self.logger.info("Retrieving subtotal for %s and parsing as a Decimal", product_name)
        subtotal_text = self.cart_page.get_product_subtotal(product_name).inner_text().strip()
        return Decimal(subtotal_text.replace("$", ""))
