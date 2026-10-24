"""Common step definitions for the test scenarios."""

from pytest_bdd import given, parsers, when

from src.services.home_service import HomePageTabs, HomeService
from src.util.service_factory import ServiceFactory


@given("I navigate to the home page")
def navigate_to_home_page(service_factory: ServiceFactory) -> None:
    """Navigate to the homepage"""
    home_service = service_factory(HomeService)
    home_service.navigate_to_home_page()


@when(parsers.parse('I navigate to the "{page_name}" page'))
def navigate_to_page(service_factory: ServiceFactory, page_name: str) -> None:
    """Navigate to a specific page based on the page name."""
    home_service = service_factory(HomeService)
    page_name_enum = HomePageTabs(page_name)
    home_service.navigate_to_tab(page_name_enum)
