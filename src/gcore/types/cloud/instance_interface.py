# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .floating_ip import FloatingIP
from .ip_assignment import IPAssignment
from .network_details import NetworkDetails
from .allowed_address_pairs import AllowedAddressPairs

__all__ = ["InstanceInterface"]


class InstanceInterface(BaseModel):
    allowed_address_pairs: List[AllowedAddressPairs]
    """
    '#/components/schemas/InstanceInterfaceSerializer/properties/allowed_address_pairs'
    "$.components.schemas.InstanceInterfaceSerializer.properties.allowed_address_pairs"
    """

    floatingip_details: List[FloatingIP]
    """
    '#/components/schemas/InstanceInterfaceSerializer/properties/floatingip_details'
    "$.components.schemas.InstanceInterfaceSerializer.properties.floatingip_details"
    """

    ip_assignments: List[IPAssignment]
    """
    '#/components/schemas/InstanceInterfaceSerializer/properties/ip_assignments'
    "$.components.schemas.InstanceInterfaceSerializer.properties.ip_assignments"
    """

    network_details: NetworkDetails
    """
    '#/components/schemas/InstanceInterfaceSerializer/properties/network_details'
    "$.components.schemas.InstanceInterfaceSerializer.properties.network_details"
    """

    network_id: str
    """
    '#/components/schemas/InstanceInterfaceSerializer/properties/network_id'
    "$.components.schemas.InstanceInterfaceSerializer.properties.network_id"
    """

    port_id: str
    """
    '#/components/schemas/InstanceInterfaceSerializer/properties/port_id'
    "$.components.schemas.InstanceInterfaceSerializer.properties.port_id"
    """

    port_security_enabled: bool
    """
    '#/components/schemas/InstanceInterfaceSerializer/properties/port_security_enabled'
    "$.components.schemas.InstanceInterfaceSerializer.properties.port_security_enabled"
    """

    interface_name: Optional[str] = None
    """
    '#/components/schemas/InstanceInterfaceSerializer/properties/interface_name/anyOf/0'
    "$.components.schemas.InstanceInterfaceSerializer.properties.interface_name.anyOf[0]"
    """

    mac_address: Optional[str] = None
    """
    '#/components/schemas/InstanceInterfaceSerializer/properties/mac_address/anyOf/0'
    "$.components.schemas.InstanceInterfaceSerializer.properties.mac_address.anyOf[0]"
    """
