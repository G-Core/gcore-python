# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .detailed_lb_pool import DetailedLbPool

__all__ = ["DetailedLbPoolList"]


class DetailedLbPoolList(BaseModel):
    count: int
    """
    '#/components/schemas/DetailedLbPoolSerializerList/properties/count'
    "$.components.schemas.DetailedLbPoolSerializerList.properties.count"
    """

    results: List[DetailedLbPool]
    """
    '#/components/schemas/DetailedLbPoolSerializerList/properties/results'
    "$.components.schemas.DetailedLbPoolSerializerList.properties.results"
    """
