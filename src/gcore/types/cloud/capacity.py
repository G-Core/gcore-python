# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Capacity"]


class Capacity(BaseModel):
    capacity: int
    """
    '#/components/schemas/CapacityDetailsSerializer/properties/capacity'
    "$.components.schemas.CapacityDetailsSerializer.properties.capacity"
    """

    flavor_name: str
    """
    '#/components/schemas/CapacityDetailsSerializer/properties/flavor_name'
    "$.components.schemas.CapacityDetailsSerializer.properties.flavor_name"
    """
