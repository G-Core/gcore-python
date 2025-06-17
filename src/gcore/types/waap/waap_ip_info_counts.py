# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WaapIPInfoCounts"]


class WaapIPInfoCounts(BaseModel):
    blocked_requests: int
    """The number of requests from the IP address that were blocked"""

    total_requests: int
    """The total number of requests made by the IP address"""

    unique_sessions: int
    """The number of unique sessions from the IP address"""
