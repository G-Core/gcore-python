# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ZoneGetStatisticsParams"]


class ZoneGetStatisticsParams(TypedDict, total=False):
    from_: Annotated[int, PropertyInfo(alias="from")]
    """Beginning of the requested time period (Unix Timestamp, UTC.)

    In a query string: &from=1709068637
    """

    granularity: str
    """
    Granularity parameter string is a sequence of decimal numbers, each with
    optional fraction and a unit suffix, such as "300ms", "1.5h" or "2h45m".

    Valid time units are "s", "m", "h".
    """

    record_type: str
    """DNS record type.

    Possible values:

    - A
    - AAAA
    - NS
    - CNAME
    - MX
    - TXT
    - SVCB
    - HTTPS
    """

    to: int
    """End of the requested time period (Unix Timestamp, UTC.)

    In a query string: &to=1709673437
    """
