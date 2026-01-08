# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from .connected_port import ConnectedPort

__all__ = ["ConnectedPortListResponse"]


class ConnectedPortListResponse(BaseModel):
    count: int
    """Number of objects"""

    results: List[ConnectedPort]
    """Objects"""
