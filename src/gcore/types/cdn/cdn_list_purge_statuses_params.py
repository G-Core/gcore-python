# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CdnListPurgeStatusesParams"]


class CdnListPurgeStatusesParams(TypedDict, total=False):
    cname: str
    """Purges associated with a specific resource CNAME.

    Example:

    - &cname=example.com
    """

    from_created: str
    """
    Start date and time of the requested time period (ISO 8601/RFC 3339 format,
    UTC.)

    Examples:

    - &`from_created`=2021-06-14T00:00:00Z
    - &`from_created`=2021-06-14T00:00:00.000Z
    """

    limit: int
    """Maximum number of purges in the response."""

    offset: int
    """
    Number of purge requests in the response to skip starting from the beginning of
    the requested period.
    """

    purge_type: str
    """Purge requests with a certain purge type.

    Possible values:

    - **`purge_by_pattern`** - Purge by Pattern.
    - **`purge_by_url`** - Purge by URL.
    - **`purge_all`** - Purge All.
    """

    status: str
    """Purge with a certain status.

    Possible values:

    - **In progress**
    - **Successful**
    - **Failed**
    - **Status report disabled**
    """

    to_created: str
    """End date and time of the requested time period (ISO 8601/RFC 3339 format, UTC.)

    Examples:

    - &`to_created`=2021-06-15T00:00:00Z
    - &`to_created`=2021-06-15T00:00:00.000Z
    """
