"""Page object for the Cart page."""

from playwright.sync_api import Locator, Page


class CartPage:
    """Page object for the Cart page."""

    def __init__(self, page: Page):
        self.page = page

        self.cart_count = page.locator(".cart-count")
        self.cart_items = page.locator("tr.cart-item")
        self.cart_total_locator = self.page.locator("strong.total")

    def get_buy_button(self, product_name: str) -> Locator:
        """Return the Buy button for the specified product."""
        product = self.page.locator("li.product").filter(
            has=self.page.get_by_role("heading", name=product_name, exact=True)
        )
        return product.get_by_role("link", name="Buy", exact=True)

    def get_cart_count(self) -> int:
        """Return the current count of items in the cart."""
        count_text = self.cart_count.inner_text()
        return int(count_text) if count_text.isdigit() else 0

    def get_product_row(self, product_name: str) -> Locator:
        """Get the cart row for a specific product."""
        return self.cart_items.filter(has=self.page.get_by_role("cell").filter(has_text=product_name))

    def get_product_price(self, product_name: str) -> Locator:
        """Get the unit price for a specific product."""
        return self.get_product_row(product_name).locator("td").nth(1)

    def get_product_subtotal(self, product_name: str) -> Locator:
        """Get the subtotal for a specific product."""
        return self.get_product_row(product_name).locator("td").nth(3)
