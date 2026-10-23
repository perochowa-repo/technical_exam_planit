"""Page object for the homepage."""

from playwright.sync_api import Page


class HomePage:
    """Page object for the homepage."""

    def __init__(self, page: Page):
        self.page = page

    def navigate_to_home_page(self) -> None:
        """Navigate to the homepage."""
        self.page.goto("/")

    def get_page_title(self) -> str:
        """Get the title of the current page."""
        return self.page.title()
