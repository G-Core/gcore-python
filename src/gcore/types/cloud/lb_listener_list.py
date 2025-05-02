# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .lb_listener import LbListener

__all__ = ["LbListenerList"]


class LbListenerList(BaseModel):
    count: int
    """Number of objects"""

    results: List[LbListener]
    """Objects"""
