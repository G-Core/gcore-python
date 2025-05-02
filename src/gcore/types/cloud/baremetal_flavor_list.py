# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .baremetal_flavor import BaremetalFlavor

__all__ = ["BaremetalFlavorList"]


class BaremetalFlavorList(BaseModel):
    count: int
    """
    '#/components/schemas/BareMetalFlavorExtendedCollectionSerializer/properties/count'
    "$.components.schemas.BareMetalFlavorExtendedCollectionSerializer.properties.count"
    """

    results: List[BaremetalFlavor]
    """
    '#/components/schemas/BareMetalFlavorExtendedCollectionSerializer/properties/results'
    "$.components.schemas.BareMetalFlavorExtendedCollectionSerializer.properties.results"
    """
