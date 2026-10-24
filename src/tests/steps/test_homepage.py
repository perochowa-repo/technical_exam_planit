from pytest_bdd import parsers, scenarios, then

from src.services.home_service import HomeService
from src.util.service_factory import ServiceFactory

scenarios("../features/homepage.feature")


@then(parsers.parse('I should see that the page title contains "{title}"'))
def verify_homepage_title(service_factory: ServiceFactory, title: str) -> None:
    """Verify that the page title contains the expected text."""
    home_service = service_factory(HomeService)
    home_service.verify_page_title(title)
