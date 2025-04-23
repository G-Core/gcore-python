# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .router import Router
from ...._models import BaseModel

__all__ = ["RouterList"]


class RouterList(BaseModel):
    count: int
    """
    '#/components/schemas/RouterSerializerList/properties/count'
    "$.components.schemas.RouterSerializerList.properties.count"
    """

    results: List[Router]
    """
    '#/components/schemas/RouterSerializerList/properties/results'
    "$.components.schemas.RouterSerializerList.properties.results"
    """
