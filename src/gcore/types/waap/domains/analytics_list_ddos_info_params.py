# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AnalyticsListDDOSInfoParams"]


class AnalyticsListDDOSInfoParams(TypedDict, total=False):
    group_by: Required[Literal["URL", "User-Agent", "IP"]]
    """The identity of the requests to group by"""

    start: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Filter traffic starting from a specified date in ISO 8601 format"""

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter traffic up to a specified end date in ISO 8601 format.

    If not provided, defaults to the current date and time.
    """

    limit: int
    """Number of items to return"""

    offset: int
    """Number of items to skip"""
