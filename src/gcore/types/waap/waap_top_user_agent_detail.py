# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["WaapTopUserAgentDetail"]


class WaapTopUserAgentDetail(BaseModel):
    attacks: Optional[int] = None
    """Total number of detected attacks."""

    blocked: Optional[int] = None
    """Number of blocked attacks."""

    domains: Optional[int] = None
    """Number of distinct domains."""

    paths: Optional[int] = None
    """Number of distinct URL paths excluding query strings."""

    requests: Optional[int] = None
    """Total number of requests."""

    sessions: Optional[int] = None
    """Number of distinct sessions."""

    user_agent: Optional[str] = None
    """The user agent string; missing values are represented as ""."""
