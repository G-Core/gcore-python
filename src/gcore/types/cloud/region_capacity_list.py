# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .region_capacity import RegionCapacity

__all__ = ["RegionCapacityList"]


class RegionCapacityList(BaseModel):
    count: int
    """
    '#/components/schemas/RegionCapacityOutSerializerV3List/properties/count'
    "$.components.schemas.RegionCapacityOutSerializerV3List.properties.count"
    """

    results: List[RegionCapacity]
    """
    '#/components/schemas/RegionCapacityOutSerializerV3List/properties/results'
    "$.components.schemas.RegionCapacityOutSerializerV3List.properties.results"
    """
