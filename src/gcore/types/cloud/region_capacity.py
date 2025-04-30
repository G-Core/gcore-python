# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .capacity import Capacity
from ..._models import BaseModel

__all__ = ["RegionCapacity"]


class RegionCapacity(BaseModel):
    capacity: List[Capacity]
    """
    '#/components/schemas/RegionCapacityOutSerializerV3/properties/capacity'
    "$.components.schemas.RegionCapacityOutSerializerV3.properties.capacity"
    """

    region_id: int
    """
    '#/components/schemas/RegionCapacityOutSerializerV3/properties/region_id'
    "$.components.schemas.RegionCapacityOutSerializerV3.properties.region_id"
    """
