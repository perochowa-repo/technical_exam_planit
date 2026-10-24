"""Step definitions for the contact page feature."""

from typing import Any

from pytest_bdd import parsers, scenarios, then, when

from src.services.contact_service import ContactService
from src.util.contact_templates import MANDATORY_CONTACT_FORM
from src.util.service_factory import ServiceFactory

scenarios("../features/contact_page.feature")


@when(parsers.parse('I click the "{button_name}" button'))
def click_button(service_factory: ServiceFactory, button_name: str) -> None:
    """Click a specific button."""
    contact_service = service_factory(ContactService)
    contact_service.click_button(button_name)


@then("I should see that mandatory field error messages should be displayed")
def verify_mandatory_field_errors_are_displayed(service_factory: ServiceFactory) -> None:
    """Verify that mandatory field error messages are displayed."""
    contact_service = service_factory(ContactService)
    contact_service.verify_mandatory_field_errors()


@when("I populate all mandatory contact fields")
def populate_mandatory_contact_fields(service_factory: ServiceFactory, data_cache: dict[str, Any]) -> None:
    """Populate all mandatory contact fields."""
    contact_service = service_factory(ContactService)
    data_cache["forename"] = contact_service.populate_contact_fields(MANDATORY_CONTACT_FORM)


@then("I should see the my feedback has been submitted successfully")
def verify_feedback_submission_success(service_factory: ServiceFactory, data_cache: dict[str, Any]) -> None:
    """Verify that the feedback submission was successful."""
    contact_service = service_factory(ContactService)
    forename = data_cache["forename"]
    contact_service.verify_feedback_submission_success(forename)
