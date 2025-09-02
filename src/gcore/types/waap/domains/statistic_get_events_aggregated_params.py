# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["StatisticGetEventsAggregatedParams"]


class StatisticGetEventsAggregatedParams(TypedDict, total=False):
    start: Required[str]
    """Filter data items starting from a specified date in ISO 8601 format"""

    action: Optional[List[Literal["block", "captcha", "handshake", "monitor"]]]
    """A list of action names to filter on."""

    end: Optional[str]
    """Filter data items up to a specified end date in ISO 8601 format.

    If not provided, defaults to the current date and time.
    """

    ip: Optional[SequenceNotStr[str]]
    """A list of IPs to filter event statistics."""

    reference_id: Optional[SequenceNotStr[str]]
    """A list of reference IDs to filter event statistics."""

    result: Optional[List[Literal["passed", "blocked", "monitored", "allowed"]]]
    """A list of results to filter event statistics."""
