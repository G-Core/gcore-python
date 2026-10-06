# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WaapIPInfoCountsV2"]


class WaapIPInfoCountsV2(BaseModel):
    attack_types: int
    """The number of distinct attack types (rules) that blocked requests from this IP"""

    blocked_requests: int
    """The number of requests from the IP address that were blocked"""

    domains: int
    """The number of distinct domains accessed by this IP"""

    paths: int
    """The number of distinct paths (URLs) accessed by this IP"""

    total_requests: int
    """The total number of requests made by the IP address"""

    unique_sessions: int
    """The number of unique sessions from the IP address"""

    user_agents: int
    """The number of distinct user agents used by this IP"""
