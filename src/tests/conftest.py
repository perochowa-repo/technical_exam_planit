"""Pytest configuration file for the test suite."""

import logging
from collections.abc import Generator
from logging import Logger
from typing import Any

import pytest
from playwright.sync_api import Page

from src.util.service_factory import ServiceFactory


@pytest.fixture
def data_cache() -> dict[str, Any]:
    """Provide a data cache for tests."""
    variables: dict[str, Any] = {}
    return variables


@pytest.fixture
def test_logger() -> Logger:
    """Provide a logger instance for tests."""
    return logging.getLogger("tests")


@pytest.fixture
def service_factory(
    page: Page,
    test_logger: Logger,
) -> Generator[ServiceFactory, Any, None]:
    """Provide a ServiceFactory instance for tests."""
    yield ServiceFactory(page, test_logger)


def pytest_bdd_apply_tag(tag, function):
    """Convert the repeat_5 Gherkin tag into a repetition marker."""

    if tag == "repeat_5":
        pytest.mark.repeat(5)(function)
        return True

    return None
