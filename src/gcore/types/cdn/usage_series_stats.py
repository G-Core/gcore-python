# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["UsageSeriesStats", "UsageSeriesStatItem"]


class UsageSeriesStatItem(BaseModel):
    active_from: Optional[str] = None
    """Date and time when paid feature was enabled (ISO 8601/RFC 3339 format, UTC.)"""

    active_to: Optional[str] = None
    """Date and time when paid feature was disabled (ISO 8601/RFC 3339 format, UTC.)

    It returns **null** if the paid feature is enabled.
    """

    client_id: Optional[int] = None
    """Client ID."""

    cname: Optional[str] = None
    """CDN resource CNAME."""

    resource_id: Optional[int] = None
    """CDN resource ID."""


UsageSeriesStats: TypeAlias = List[UsageSeriesStatItem]
