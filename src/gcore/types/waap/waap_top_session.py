# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["WaapTopSession"]


class WaapTopSession(BaseModel):
    blocked: int
    """The number of blocked requests in the session"""

    duration: float
    """The duration of the session in seconds"""

    requests: int
    """The number of requests in the session"""

    session_id: str
    """The session ID"""

    start_time: datetime
    """The start time of the session as a POSIX timestamp"""
