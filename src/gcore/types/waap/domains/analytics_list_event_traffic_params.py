# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..waap_resolution import WaapResolution

__all__ = ["AnalyticsListEventTrafficParams"]


class AnalyticsListEventTrafficParams(TypedDict, total=False):
    resolution: Required[WaapResolution]
    """Specifies the granularity of the result data."""

    start: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Filter traffic starting from a specified date in ISO 8601 format"""

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter traffic up to a specified end date in ISO 8601 format.

    If not provided, defaults to the current date and time.
    """
