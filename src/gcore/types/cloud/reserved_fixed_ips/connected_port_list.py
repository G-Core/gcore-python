# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .connected_port import ConnectedPort

__all__ = ["ConnectedPortList"]


class ConnectedPortList(BaseModel):
    count: int
    """
    '#/components/schemas/ConnectedDevicesVIPSerializerList/properties/count'
    "$.components.schemas.ConnectedDevicesVIPSerializerList.properties.count"
    """

    results: List[ConnectedPort]
    """
    '#/components/schemas/ConnectedDevicesVIPSerializerList/properties/results'
    "$.components.schemas.ConnectedDevicesVIPSerializerList.properties.results"
    """
