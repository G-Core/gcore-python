# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AuditLogListParams"]


class AuditLogListParams(TypedDict, total=False):
    client_id: int
    """Client ID."""

    limit: int
    """Maximum number of items in response."""

    max_requested_at: str
    """End of the requested time period (ISO 8601/RFC 3339 format, UTC.)

    You can specify a date with a time separated by a space, or just a date.

    Examples:

    - &`max_requested_at`=2021-05-05 12:00:00
    - &`max_requested_at`=2021-05-05
    """

    method: str
    """HTTP method type of requests.

    Use upper case only.

    Example:

    - ?method=DELETE
    """

    min_requested_at: str
    """Beginning of the requested time period (ISO 8601/RFC 3339 format, UTC.)

    You can specify a date with a time separated by a space, or just a date.

    Examples:

    - &`min_requested_at`=2021-05-05 12:00:00
    - &`min_requested_at`=2021-05-05
    """

    offset: int
    """Offset relative to the beginning of activity logs."""

    path: str
    """Exact URL path."""

    remote_ip_address: str
    """Exact IP address from which requests are sent."""

    status_code: int
    """Status code returned in the response.

    Specify the first numbers of a status code to get requests for a group of status
    codes.

    To filter the activity logs by 4xx codes, use:

    - &`status_code`=4 -
    """

    token_id: int
    """Permanent API token ID. Requests made with this token should be displayed."""

    user_id: int
    """User ID."""
