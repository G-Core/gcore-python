# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AnalyticsGetFiltersParams"]


class AnalyticsGetFiltersParams(TypedDict, total=False):
    start: Required[str]
    """Filter data items starting from a specified date in ISO 8601 format"""

    domains: Iterable[int]
    """List of domain IDs.

    Empty list means all domains belonging to the current account.
    """

    end: Optional[str]
    """Filter data items up to a specified end date in ISO 8601 format.

    If not provided, defaults to the current date and time.
    """

    limit: int
    """Number of items to return"""

    name: Optional[str]
    """
    Case-insensitive partial autocomplete pattern matched against the value name by
    the value provider. Must be between 2 and 100 characters; empty or omitted
    returns the available suggestions for the current account and time range.
    """

    offset: int
    """Number of items to skip"""

    ordering: Literal["count", "value"]
    """Suggestion ordering.

    `count` sorts by observed occurrence count descending (most frequent first) with
    value as a tie breaker; `value` sorts alphabetically by value ascending with
    count as a tie breaker.
    """
