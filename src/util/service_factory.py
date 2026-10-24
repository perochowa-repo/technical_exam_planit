"""Service factory module for creating service instances with caching."""

from collections.abc import Callable
from logging import Logger
from typing import Any, TypeVar, cast

from playwright.sync_api import Page

T = TypeVar("T")


class ServiceFactory:
    """A factory class for creating service instances."""

    def __init__(self, page: Page, logger: Logger) -> None:
        """Initialize the ServiceFactory with a Page and Logger."""
        self._page = page
        self._logger = logger
        self._service_cache: dict[Any, Any] = {}

    def __call__(self, page_class: Callable[[Page, Logger], T]) -> T:
        """Create or retrieve a service instance for the given page class."""
        if page_class not in self._service_cache:
            self._logger.debug("Creating new service instance for %s", page_class.__name__)
            self._service_cache[page_class] = page_class(self._page, self._logger)
        else:
            self._logger.debug("Retrieving cached service instance for %s", page_class.__name__)
        return cast(T, self._service_cache[page_class])
