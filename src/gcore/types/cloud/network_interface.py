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
    """Group of subnet masks and/or IP addresses that share the current IP as VIP"""

    floatingip_details: List[FloatingIP]
    """Bodies of floating IPs that are NAT-ing IPs of this port"""

    ip_assignments: List[IPAssignment]
    """IP addresses assigned to this port"""

    network_details: NetworkDetails
    """Body of the network this port is attached to"""

    network_id: str
    """ID of the network the port is attached to"""

    port_id: str
    """ID of virtual ethernet port object"""

    port_security_enabled: bool
    """Port security status"""

    segmentation_id: int
    """id of network segment"""

    segmentation_type: str
    """type of network segment"""

    interface_name: Optional[str] = None
    """Interface name"""

    mac_address: Optional[str] = None
    """MAC address of the virtual port"""


class NetworkInterface(BaseModel):
    allowed_address_pairs: List[AllowedAddressPairs]
    """Group of subnet masks and/or IP addresses that share the current IP as VIP"""

    floatingip_details: List[FloatingIP]
    """Bodies of floating IPs that are NAT-ing IPs of this port"""

    ip_assignments: List[IPAssignment]
    """IP addresses assigned to this port"""

    network_details: NetworkDetails
    """Body of the network this port is attached to"""

    network_id: str
    """ID of the network the port is attached to"""

    port_id: str
    """ID of virtual ethernet port object"""

    port_security_enabled: bool
    """Port security status"""

    sub_ports: List[SubPort]
    """body of ports that are included into trunk port"""

    interface_name: Optional[str] = None
    """Interface name"""

    mac_address: Optional[str] = None
    """MAC address of the virtual port"""
