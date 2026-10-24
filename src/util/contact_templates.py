"""Contact form templates for testing purposes."""

from faker import Faker

from src.util.models.contact import Contact

faker = Faker()

COMPLETE_CONTACT_FORM = Contact(
    forename=faker.first_name(),
    surname=faker.last_name(),
    email=f"{faker.first_name().lower()}.{faker.last_name().lower()}@example.com",
    telephone=faker.numerify(text="##########"),
    message="This is a test message for John Doe when all fields are filled out.",
)

MANDATORY_CONTACT_FORM = Contact(
    forename=faker.first_name(),
    email=f"{faker.first_name().lower()}.{faker.last_name().lower()}@example.com",
    message="This is another test message for Jane Doe when only mandatory fields are filled out.",
)
