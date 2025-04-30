# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .network_interface import NetworkInterface

__all__ = ["NetworkInterfaceList"]


class NetworkInterfaceList(BaseModel):
    count: int
    """
    '#/components/schemas/InstanceInterfaceTrunkCollectionSerializer/properties/count'
    "$.components.schemas.InstanceInterfaceTrunkCollectionSerializer.properties.count"
    """

    results: List[NetworkInterface]
    """
    '#/components/schemas/InstanceInterfaceTrunkCollectionSerializer/properties/results'
    "$.components.schemas.InstanceInterfaceTrunkCollectionSerializer.properties.results"
    """
