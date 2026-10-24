"""Data models for the contact form."""

from dataclasses import dataclass


@dataclass
class Contact:
    """Data class representing a contact form submission."""

    forename: str
    email: str
    message: str
    surname: str | None = None
    telephone: str | None = None
