# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["WaapAPIPath"]


class WaapAPIPath(BaseModel):
    """Response model for the API path"""

    id: str
    """The path ID"""

    api_groups: List[str]
    """An array of api groups associated with the API path"""

    api_version: str
    """The API version"""

    first_detected: datetime
    """The date and time in ISO 8601 format the API path was first detected."""

    http_scheme: Literal["HTTP", "HTTPS"]
    """The HTTP version of the API path"""

    last_detected: datetime
    """The date and time in ISO 8601 format the API path was last detected."""

    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE", "TRACE", "HEAD", "OPTIONS"]
    """The API RESTful method"""

    path: str
    """
    The API path, locations that are saved for resource IDs will be put in curly
    brackets
    """

    request_count: int
    """The number of requests for this path in the last 24 hours"""

    source: Literal["API_DESCRIPTION_FILE", "TRAFFIC_SCAN", "USER_DEFINED"]
    """The source of the discovered API"""

    status: Literal["CONFIRMED_API", "POTENTIAL_API", "NOT_API", "DELISTED_API"]
    """The status of the discovered API path"""

    tags: List[str]
    """An array of tags associated with the API path"""
