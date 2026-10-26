"""Contains the HomeService class for homepage-related actions."""

import re
from enum import Enum
from logging import Logger

from playwright.sync_api import expect

from src.pages.home_page import HomePage


class HomePageTabs(Enum):
    """Enum for the tabs on the homepage."""

    HOME = "Home"
    CONTACT = "Contact"
    SHOP = "Shop"
    CART = "Cart"


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
        expect(self.home_page.page).to_have_title(re.compile(re.escape(expected_title)))

    def navigate_to_tab(self, tab_name: HomePageTabs):
        """Navigate to a specific tab on the homepage."""
        self.logger.info("Navigating to the '%s' tab.", tab_name.value)
        self.home_page.navigate_to_tab(tab_name.value)
