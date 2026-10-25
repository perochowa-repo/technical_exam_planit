"""Page object for the homepage."""

from playwright.sync_api import Page

from src.pages.cart_page import CartPage


class HomePage:
    """Page object for the homepage."""

    def __init__(self, page: Page):
        self.page = page
        self.cart_page = CartPage(page)

        self.contact_tab_locator = page.get_by_role("link", name="Contact")
        self.shop_tab_locator = page.get_by_role("link", name="Shop", exact=True)

    def navigate_to_home_page(self) -> None:
        """Navigate to the homepage."""
        self.page.goto("/")

    def get_page_title(self) -> str:
        """Get the title of the current page."""
        return self.page.title()

    def navigate_to_tab(self, tab_name: str) -> None:
        """Navigate to a specific tab on the homepage."""
        match tab_name:
            case "Contact":
                self.contact_tab_locator.click()
            case "Shop":
                self.shop_tab_locator.click()
            case "Cart":
                self.cart_page.cart_count.click()
            case _:
                raise ValueError(f"Unknown tab name: {tab_name}")
