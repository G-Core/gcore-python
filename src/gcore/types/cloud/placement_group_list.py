# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .placement_group import PlacementGroup

__all__ = ["PlacementGroupList"]


class PlacementGroupList(BaseModel):
    count: int
    """
    '#/components/schemas/ServerGroupSerializerList/properties/count'
    "$.components.schemas.ServerGroupSerializerList.properties.count"
    """

    results: List[PlacementGroup]
    """
    '#/components/schemas/ServerGroupSerializerList/properties/results'
    "$.components.schemas.ServerGroupSerializerList.properties.results"
    """
