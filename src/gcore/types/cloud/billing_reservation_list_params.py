# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date, datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BillingReservationListParams"]


class BillingReservationListParams(TypedDict, total=False):
    activated_from: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Lower bound, starting from what date the reservation was/will be activated"""

    activated_to: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """High bound, before what date the reservation was/will be activated"""

    created_from: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Lower bound the filter, showing result(s) equal to or greater than date the
    reservation was created
    """

    created_to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    High bound the filter, showing result(s) equal to or less date the reservation
    was created
    """

    deactivated_from: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Lower bound, starting from what date the reservation was/will be deactivated"""

    deactivated_to: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """High bound, before what date the reservation was/will be deactivated"""

    limit: int
    """Limit of reservation list page"""

    metric_name: str
    """Name from billing features for specific resource"""

    offset: int
    """Offset in reservation list"""

    order_by: Literal[
        "active_from.asc", "active_from.desc", "active_to.asc", "active_to.desc", "created_at.asc", "created_at.desc"
    ]
    """Order by field and direction."""

    region_id: int
    """Region for reservation"""

    status: List[
        Literal["ACTIVATED", "APPROVED", "COPIED", "CREATED", "EXPIRED", "REJECTED", "RESERVED", "WAITING_FOR_PAYMENT"]
    ]
    """Field for fixed a status by reservation workflow"""
