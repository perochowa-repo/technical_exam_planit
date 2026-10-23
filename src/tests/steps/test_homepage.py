"""Step definitions for the homepage feature."""

from pytest_bdd import given, parsers, scenarios, then

from src.services.home_service import HomeService
from src.util.service_factory import ServiceFactory

scenarios("../features/homepage.feature")


@given("I navigate to the homepage")
def navigate_to_home_page(service_factory: ServiceFactory) -> None:
    """Navigate to the homepage"""
    home_service = service_factory(HomeService)
    home_service.navigate_to_home_page()


@then(parsers.parse('I should see that the page title contains "{title}"'))
def verify_homepage_title(service_factory: ServiceFactory, title: str) -> None:
    """Verify that the page title contains the expected text."""
    home_service = service_factory(HomeService)
    home_service.verify_page_title(title)
