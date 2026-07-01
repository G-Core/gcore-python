# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BillingReservationListParams"]


class BillingReservationListParams(TypedDict, total=False):
    metric_name: str
    """Metric name for the resource (e.g., 'bm1-hf-medium_min')"""

    order_by: Literal["active_from.asc", "active_from.desc", "active_to.asc", "active_to.desc"]
    """Order by field and direction."""

    region_id: int
    """Region for reservation"""

    show_inactive: bool
    """Include inactive commits in the response.

    Only applies when no period is given; ignored when 'time_from'/'time_to' are
    supplied, since the period defines the window.
    """

    time_from: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start of the reservation period (ISO 8601).

    Must be supplied together with 'time_to'. When both are given, period-matched
    monthly pricing is returned and the period must be at most one month (31 days).
    When both are omitted, current pricing is returned.
    """

    time_to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End of the reservation period (ISO 8601).

    Must be supplied together with 'time_from'. When both are given, period-matched
    monthly pricing is returned and the period must be at most one month (31 days).
    When both are omitted, current pricing is returned.
    """
