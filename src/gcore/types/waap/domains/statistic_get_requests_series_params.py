# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["StatisticGetRequestsSeriesParams"]


class StatisticGetRequestsSeriesParams(TypedDict, total=False):
    start: Required[str]
    """Filter data items starting from a specified date in ISO 8601 format"""

    actions: List[Literal["allow", "block", "captcha", "handshake"]]
    """Filter the response by actions."""

    countries: SequenceNotStr[str]
    """Filter the response by country codes in ISO 3166-1 alpha-2 format."""

    end: Optional[str]
    """Filter data items up to a specified end date in ISO 8601 format.

    If not provided, defaults to the current date and time.
    """

    ip: str
    """Filter the response by IP."""

    limit: int
    """Number of items to return"""

    offset: int
    """Number of items to skip"""

    ordering: str
    """Sort the response by given field."""

    reference_id: str
    """Filter the response by reference ID."""

    security_rule_name: str
    """Filter the response by security rule name."""

    status_code: int
    """Filter the response by response code."""

    traffic_types: List[
        Literal[
            "policy_allowed",
            "policy_blocked",
            "custom_rule_allowed",
            "custom_blocked",
            "legit_requests",
            "sanctioned",
            "dynamic",
            "api",
            "static",
            "ajax",
            "redirects",
            "monitor",
            "err_40x",
            "err_50x",
            "passed_to_origin",
            "timeout",
            "other",
            "ddos",
            "legit",
            "monitored",
        ]
    ]
    """Filter the response by traffic types."""
