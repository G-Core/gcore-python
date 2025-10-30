# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StatisticGetLogsUsageSeriesParams"]


class StatisticGetLogsUsageSeriesParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Beginning of the requested time period (ISO 8601/RFC 3339 format, UTC.)"""

    to: Required[str]
    """End of the requested time period (ISO 8601/RFC 3339 format, UTC.)"""

    resource: int
    """CDN resources IDs by that statistics data is grouped.

    To request multiple values, use:

    - &resource=1&resource=2

    If CDN resource ID is not specified, data related to all CDN resources is
    returned.
    """
