# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .l7_policy import L7Policy

__all__ = ["L7PolicyList"]


class L7PolicyList(BaseModel):
    count: Optional[int] = None
    """Number of objects"""

    results: Optional[List[L7Policy]] = None
    """Objects"""
