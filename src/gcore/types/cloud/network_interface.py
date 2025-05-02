# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .floating_ip import FloatingIP
from .ip_assignment import IPAssignment
from .network_details import NetworkDetails
from .allowed_address_pairs import AllowedAddressPairs

__all__ = ["NetworkInterface", "SubPort"]


class SubPort(BaseModel):
    allowed_address_pairs: List[AllowedAddressPairs]
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/allowed_address_pairs'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.allowed_address_pairs"
    """

    floatingip_details: List[FloatingIP]
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/floatingip_details'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.floatingip_details"
    """

    ip_assignments: List[IPAssignment]
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/ip_assignments'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.ip_assignments"
    """

    network_details: NetworkDetails
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/network_details'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.network_details"
    """

    network_id: str
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/network_id'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.network_id"
    """

    port_id: str
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/port_id'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.port_id"
    """

    port_security_enabled: bool
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/port_security_enabled'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.port_security_enabled"
    """

    segmentation_id: int
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/segmentation_id'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.segmentation_id"
    """

    segmentation_type: str
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/segmentation_type'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.segmentation_type"
    """

    interface_name: Optional[str] = None
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/interface_name/anyOf/0'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.interface_name.anyOf[0]"
    """

    mac_address: Optional[str] = None
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/mac_address/anyOf/0'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.mac_address.anyOf[0]"
    """


class NetworkInterface(BaseModel):
    allowed_address_pairs: List[AllowedAddressPairs]
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/allowed_address_pairs'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.allowed_address_pairs"
    """

    floatingip_details: List[FloatingIP]
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/floatingip_details'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.floatingip_details"
    """

    ip_assignments: List[IPAssignment]
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/ip_assignments'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.ip_assignments"
    """

    network_details: NetworkDetails
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/network_details'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.network_details"
    """

    network_id: str
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/network_id'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.network_id"
    """

    port_id: str
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/port_id'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.port_id"
    """

    port_security_enabled: bool
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/port_security_enabled'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.port_security_enabled"
    """

    sub_ports: List[SubPort]
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/sub_ports'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.sub_ports"
    """

    interface_name: Optional[str] = None
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/interface_name/anyOf/0'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.interface_name.anyOf[0]"
    """

    mac_address: Optional[str] = None
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/mac_address/anyOf/0'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.mac_address.anyOf[0]"
    """
