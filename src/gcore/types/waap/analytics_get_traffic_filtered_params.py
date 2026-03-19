# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AnalyticsGetTrafficFilteredParams"]


class AnalyticsGetTrafficFilteredParams(TypedDict, total=False):
    resolution: Required[Literal["daily", "hourly", "minutely"]]
    """Specifies the granularity of the result data."""

    start: Required[str]
    """Filter data items starting from a specified date in ISO 8601 format"""

    countries: SequenceNotStr[str]
    """
    Filter data by a country code of the originating IP address in ISO 3166-1
    alpha-2 format.
    """

    decision: List[Literal["blocked", "monitored", "allowed", "passed"]]
    """Filter data by decision."""

    domains: Iterable[int]
    """List of domain IDs.

    Empty list means all domains belonging to the current account.
    """

    end: Optional[str]
    """Filter data items up to a specified end date in ISO 8601 format.

    If not provided, defaults to the current date and time.
    """

    http_methods: List[Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]]
    """Filter by HTTP methods"""

    ips: SequenceNotStr[str]
    """Filter traffic data by client IP."""

    optional_action: List[Literal["captcha", "challenge"]]
    """Filter data by optional action."""

    path: Optional[str]
    """Filter by URL path with a glob-like pattern."""

    reference_ids: SequenceNotStr[str]
    """Filter data by reference IDs."""

    request_ids: SequenceNotStr[str]
    """Filter data by request IDs."""

    security_rule_names: SequenceNotStr[str]
    """Filter data by name of a security rule matched the request."""

    session_ids: SequenceNotStr[str]
    """Filter data by session IDs."""

    status_codes: Iterable[int]
    """Filter data by HTTP response status code."""
