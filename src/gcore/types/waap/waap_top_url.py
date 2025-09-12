# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WaapTopURL"]


class WaapTopURL(BaseModel):
    count: int
    """The number of attacks to the URL"""

    url: str
    """The URL that was attacked"""
