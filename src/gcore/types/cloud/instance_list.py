# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .instance import Instance
from ..._models import BaseModel

__all__ = ["InstanceList"]


class InstanceList(BaseModel):
    count: int
    """Number of objects"""

    results: List[Instance]
    """Objects"""
