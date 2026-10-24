"""Page object for the Contact page."""

from playwright.sync_api import Page


class ContactPage:
    """Page object for the Contact page."""

    def __init__(self, page: Page):
        self.page = page

        self.forename_input_locator = page.get_by_role("textbox", name="Forename *")
        self.surname_input_locator = page.get_by_role("textbox", name="Surname")
        self.email_input_locator = page.get_by_role("textbox", name="Email *")
        self.telephone_input_locator = page.get_by_role("textbox", name="Telephone")
        self.message_textarea_locator = page.get_by_role("textbox", name="Message *")

        self.submit_button_locator = page.get_by_role("link", name="Submit")
        self.alert_message_locator = page.locator(".alert")

        self.forename_error = page.locator("#forename-err")
        self.email_error = page.locator("#email-err")
        self.message_error = page.locator("#message-err")

        self.sending_feedback_modal = page.get_by_role("heading", name="Sending Feedback")

    def fill_contact_form(self, name: str, email: str, message: str) -> None:
        """Fill out the contact form with the provided details."""
        self.forename_input_locator.fill(name)
        self.email_input_locator.fill(email)
        self.message_textarea_locator.fill(message)

    def click_submit_button(self) -> None:
        """Submit the contact form."""
        self.submit_button_locator.click()

    def get_alert_message(self) -> str:
        """Get the alert message displayed on the contact page."""
        return self.alert_message_locator.inner_text()
