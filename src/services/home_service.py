"""Contains the HomeService class for homepage-related actions."""

from logging import Logger

from src.pages.home_page import HomePage


class HomeService:
    """Service class for homepage-related actions."""

    def __init__(self, page, logger: Logger):
        self.page = page
        self.logger = logger

        self.home_page = HomePage(page)

    def navigate_to_home_page(self):
        """Navigate to the homepage."""
        self.logger.info("Navigating to the homepage.")
        self.home_page.navigate_to_home_page()

    def verify_page_title(self, expected_title: str):
        """Verify that the page title contains the expected text."""
        self.logger.info("Verifying that the page title contains: '%s'", expected_title)
        actual_title = self.home_page.get_page_title()
        if expected_title != actual_title:
            raise AssertionError(
                f"Expected title to contain '{expected_title}', but got '{actual_title}'"
            )
