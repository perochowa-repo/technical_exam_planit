"""Pytest configuration file for the test suite."""

import logging
from collections.abc import Generator
from logging import Logger
from typing import Any

import pytest
from playwright.sync_api import Page

from src.util.service_factory import ServiceFactory


@pytest.fixture
def test_logger() -> Logger:
    """Provide a logger instance for tests."""
    return logging.getLogger("tests")


@pytest.fixture
def service_factory(
    page: Page,
    logger: Logger,
) -> Generator[ServiceFactory, Any, None]:
    """Provide a ServiceFactory instance for tests."""
    yield ServiceFactory(page, logger)
