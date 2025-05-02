# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .l7_rule import L7Rule
from ..._models import BaseModel

__all__ = ["L7RuleList"]


class L7RuleList(BaseModel):
    count: Optional[int] = None
    """Number of objects"""

    results: Optional[List[L7Rule]] = None
    """Objects"""
