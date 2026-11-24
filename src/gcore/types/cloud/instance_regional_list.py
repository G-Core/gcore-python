# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .instance_regional import InstanceRegional

__all__ = ["InstanceRegionalList"]


class InstanceRegionalList(BaseModel):
    count: int
    """Number of objects"""

    results: List[InstanceRegional]
    """Objects"""
