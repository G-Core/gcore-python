# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["APIPathListParams"]


class APIPathListParams(TypedDict, total=False):
    api_group: Optional[str]
    """Filter by the API group associated with the API path"""

    api_version: Optional[str]
    """Filter by the API version"""

    http_scheme: Optional[Literal["HTTP", "HTTPS"]]
    """The different HTTP schemes an API path can have"""

    ids: Optional[List[str]]
    """Filter by the path ID"""

    limit: int
    """Number of items to return"""

    method: Optional[Literal["GET", "POST", "PUT", "PATCH", "DELETE", "TRACE", "HEAD", "OPTIONS"]]
    """The different methods an API path can have"""

    offset: int
    """Number of items to skip"""

    ordering: Literal[
        "id",
        "path",
        "method",
        "api_version",
        "http_scheme",
        "first_detected",
        "last_detected",
        "status",
        "source",
        "-id",
        "-path",
        "-method",
        "-api_version",
        "-http_scheme",
        "-first_detected",
        "-last_detected",
        "-status",
        "-source",
    ]
    """Sort the response by given field."""

    path: Optional[str]
    """Filter by the path. Supports '\\**' as a wildcard character"""

    source: Optional[Literal["API_DESCRIPTION_FILE", "TRAFFIC_SCAN", "USER_DEFINED"]]
    """The different sources an API path can have"""

    status: Optional[List[Literal["CONFIRMED_API", "POTENTIAL_API", "NOT_API", "DELISTED_API"]]]
    """Filter by the status of the discovered API path"""
