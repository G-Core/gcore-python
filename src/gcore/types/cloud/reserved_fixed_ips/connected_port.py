# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..network import Network
from ...._models import BaseModel
from .ip_assignment import IPAssignment

__all__ = ["ConnectedPort"]


class ConnectedPort(BaseModel):
    instance_id: str
    """
    '#/components/schemas/ConnectedDevicesVIPSerializer/properties/instance_id'
    "$.components.schemas.ConnectedDevicesVIPSerializer.properties.instance_id"
    """

    instance_name: str
    """
    '#/components/schemas/ConnectedDevicesVIPSerializer/properties/instance_name'
    "$.components.schemas.ConnectedDevicesVIPSerializer.properties.instance_name"
    """

    ip_assignments: List[IPAssignment]
    """
    '#/components/schemas/ConnectedDevicesVIPSerializer/properties/ip_assignments'
    "$.components.schemas.ConnectedDevicesVIPSerializer.properties.ip_assignments"
    """

    network: Network
    """
    '#/components/schemas/ConnectedDevicesVIPSerializer/properties/network'
    "$.components.schemas.ConnectedDevicesVIPSerializer.properties.network"
    """

    port_id: str
    """
    '#/components/schemas/ConnectedDevicesVIPSerializer/properties/port_id'
    "$.components.schemas.ConnectedDevicesVIPSerializer.properties.port_id"
    """
