# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WaapTopUserAgent"]


class WaapTopUserAgent(BaseModel):
    count: int
    """The number of requests made with the user agent"""

    user_agent: str
    """The user agent that was used"""
