# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .l7_rule import L7Rule
from ..._models import BaseModel

__all__ = ["L7RuleList"]


class L7RuleList(BaseModel):
    count: Optional[int] = None
    """
    '#/components/schemas/L7RuleListSchema/properties/count'
    "$.components.schemas.L7RuleListSchema.properties.count"
    """

    results: Optional[List[L7Rule]] = None
    """
    '#/components/schemas/L7RuleListSchema/properties/results'
    "$.components.schemas.L7RuleListSchema.properties.results"
    """
