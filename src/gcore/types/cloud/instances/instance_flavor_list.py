# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .instance_flavor import InstanceFlavor

__all__ = ["InstanceFlavorList"]


class InstanceFlavorList(BaseModel):
    count: int
    """
    '#/components/schemas/InstanceFlavorExtendedCollectionSerializer/properties/count'
    "$.components.schemas.InstanceFlavorExtendedCollectionSerializer.properties.count"
    """

    results: List[InstanceFlavor]
    """
    '#/components/schemas/InstanceFlavorExtendedCollectionSerializer/properties/results'
    "$.components.schemas.InstanceFlavorExtendedCollectionSerializer.properties.results"
    """
