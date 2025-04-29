# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .l7_policy import L7Policy

__all__ = ["L7PolicyList"]


class L7PolicyList(BaseModel):
    count: Optional[int] = None
    """
    '#/components/schemas/L7PolicyListSchema/properties/count'
    "$.components.schemas.L7PolicyListSchema.properties.count"
    """

    results: Optional[List[L7Policy]] = None
    """
    '#/components/schemas/L7PolicyListSchema/properties/results'
    "$.components.schemas.L7PolicyListSchema.properties.results"
    """
