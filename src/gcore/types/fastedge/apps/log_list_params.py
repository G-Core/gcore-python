# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["LogListParams"]


class LogListParams(TypedDict, total=False):
    client_ip: str
    """Search by client IP"""

    edge: str
    """Edge name"""

    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """Reporting period start time, RFC3339 format. Default 1 hour ago."""

    limit: int
    """Limit for pagination"""

    offset: int
    """Offset for pagination"""

    search: str
    """Search string"""

    sort: Literal["desc", "asc"]
    """Sort order (default desc)"""

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Reporting period end time, RFC3339 format. Default current time in UTC."""
