# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AnalyticsGetEventStatisticsParams"]


class AnalyticsGetEventStatisticsParams(TypedDict, total=False):
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

    ips: SequenceNotStr[str]
    """Filter statistics by client IP addresses (max 10)."""

    security_rule_names: SequenceNotStr[str]
    """Filter data by name of a security rule matched the request."""
