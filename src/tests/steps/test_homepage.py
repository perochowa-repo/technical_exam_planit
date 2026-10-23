"""Step definitions for the homepage feature."""

import re

from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, scenarios, then

scenarios("../features/homepage.feature")


@given("I navigate to the homepage")
def open_homepage(page: Page) -> None:
    """Open the homepage."""
    page.goto("/")


@then(parsers.parse('I should see that the page title contains "{title}"'))
def verify_homepage_title(page: Page, title: str) -> None:
    """Verify that the page title contains the expected text."""
    expect(page).to_have_title(re.compile(title))
