# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BillingReservationListParams"]


class BillingReservationListParams(TypedDict, total=False):
    time_from: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start of the reservation period (ISO 8601).

    The period must not exceed 31 days. The API returns monthly pricing for this
    period.
    """

    time_to: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End of the reservation period (ISO 8601).

    The period must not exceed 31 days. The API returns monthly pricing for this
    period.
    """

    metric_name: str
    """Metric name for the resource (e.g., 'bm1-hf-medium_min')"""

    order_by: Literal["active_from.asc", "active_from.desc", "active_to.asc", "active_to.desc"]
    """Order by field and direction."""

    region_id: int
    """Region for reservation"""
