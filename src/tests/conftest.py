"""Pytest configuration file for the test suite."""

import logging
from logging import Logger
from typing import Any

import pytest
from playwright.sync_api import Page

from src.util.service_factory import ServiceFactory

# pylint: disable=redefined-outer-name


@pytest.fixture
def data_cache() -> dict[str, Any]:
    """Provide a data cache for tests."""
    variables: dict[str, Any] = {}
    return variables


@pytest.fixture
def logger() -> Logger:
    """Provide a logger instance for tests."""
    return logging.getLogger("tests")


@pytest.fixture
def service_factory(page: Page, logger: Logger) -> ServiceFactory:
    """Provide a ServiceFactory instance for tests."""
    return ServiceFactory(page, logger)


def pytest_bdd_apply_tag(tag, function):
    """Convert the repeat_5 Gherkin tag into a repetition marker."""
    if tag == "repeat_5":
        pytest.mark.repeat(5)(function)
        return True
    return None
