"""Contains the ContactService class for contact-related actions."""

from enum import Enum
from logging import Logger

from playwright.sync_api import expect

from src.pages.contact_page import ContactPage
from src.util.models.contact import Contact


class AlertMessages(Enum):
    """Enum for alert messages on the contact page."""

    INITIAL = "We welcome your feedback - tell it how it is."
    ERROR = "We welcome your feedback - but we won't get it unless you complete the form correctly."
    SUCCESS = "Thanks {name}, we appreciate your feedback."

    def format(self, **kwargs) -> str:
        """Format the alert message with the provided values."""
        return self.value.format(**kwargs)


class ContactService:
    """Service class for contact-related actions."""

    def __init__(self, page, logger: Logger):
        self.page = page
        self.logger = logger

        self.contact_page = ContactPage(page)

    def click_button(self, button_name: str) -> None:
        """Click a specific button on the contact page."""
        self.logger.info("Clicking the '%s' button on the contact page.", button_name)
        match button_name:
            case "Submit":
                self.contact_page.click_submit_button()
            case _:
                raise ValueError(f"Unknown button name: {button_name}")

    def verify_mandatory_field_errors(self) -> None:
        """Verify that mandatory field error messages are displayed."""
        self.logger.info("Verifying that mandatory field error messages are displayed.")

        self.verify_alert_message(AlertMessages.ERROR)
        expect(self.contact_page.forename_error).to_be_visible()
        expect(self.contact_page.email_error).to_be_visible()
        expect(self.contact_page.message_error).to_be_visible()

    def verify_alert_message(self, expected_message: AlertMessages | str) -> None:
        """Verify that the alert message matches the expected message."""
        message = expected_message.value if isinstance(expected_message, AlertMessages) else expected_message
        self.logger.info(
            "Verifying that the alert message matches: '%s'",
            message,
        )
        expect(self.contact_page.alert_message_locator).to_have_text(message)

    def populate_contact_fields(self, contact_form: Contact) -> str:
        """Populate all mandatory contact fields and return the first name used."""
        self.logger.info("Populating all mandatory contact fields.")
        self.contact_page.forename_input_locator.fill(contact_form.forename)
        self.contact_page.email_input_locator.fill(contact_form.email)
        self.contact_page.message_textarea_locator.fill(contact_form.message)

        for locator, value in (
            (self.contact_page.surname_input_locator, contact_form.surname),
            (self.contact_page.telephone_input_locator, contact_form.telephone),
        ):
            if value:
                locator.fill(value)

        return contact_form.forename

    def verify_feedback_submission_success(self, forename: str) -> None:
        """Verify that the feedback submission was successful."""
        self.logger.info("Verifying that the feedback submission was successful.")
        self.contact_page.sending_feedback_modal.wait_for(state="hidden", timeout=30000)
        expected_message = AlertMessages.SUCCESS.format(name=forename)
        self.verify_alert_message(expected_message)
