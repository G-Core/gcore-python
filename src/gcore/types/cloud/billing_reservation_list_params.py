# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BillingReservationListParams"]


class BillingReservationListParams(TypedDict, total=False):
    metric_name: str
    """Metric name for the resource (e.g., 'bm1-hf-`medium_min`')"""

    order_by: Literal["active_from.asc", "active_from.desc", "active_to.asc", "active_to.desc"]
    """Order by field and direction."""

    region_id: int
    """Region for reservation"""

    show_inactive: bool
    """Include inactive commits in the response"""
