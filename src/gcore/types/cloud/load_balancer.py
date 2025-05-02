# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .tag import Tag
from .logging import Logging
from ..._models import BaseModel
from .floating_ip import FloatingIP
from .ddos_profile import DDOSProfile
from .interface_ip_family import InterfaceIPFamily
from .provisioning_status import ProvisioningStatus
from .load_balancer_statistics import LoadBalancerStatistics
from .load_balancer_instance_role import LoadBalancerInstanceRole
from .load_balancer_operating_status import LoadBalancerOperatingStatus
from .load_balancer_member_connectivity import LoadBalancerMemberConnectivity

__all__ = ["LoadBalancer", "AdditionalVip", "Flavor", "Listener", "VrrpIP"]


class AdditionalVip(BaseModel):
    ip_address: str
    """IP address"""

    subnet_id: str
    """Subnet UUID"""


class Flavor(BaseModel):
    flavor_id: str
    """Flavor ID is the same as name"""

    flavor_name: str
    """Flavor name"""

    ram: int
    """RAM size in MiB"""

    vcpus: int
    """Virtual CPU count. For bare metal flavors, it's a physical CPU count"""


class Listener(BaseModel):
    id: str
    """Listener ID"""


class VrrpIP(BaseModel):
    ip_address: str
    """IP address"""

    role: LoadBalancerInstanceRole
    """LoadBalancer instance role to which VRRP IP belong"""

    subnet_id: str
    """Subnet UUID"""


class LoadBalancer(BaseModel):
    id: str
    """Load balancer ID"""

    created_at: datetime
    """Datetime when the load balancer was created"""

    name: str
    """Load balancer name"""

    operating_status: LoadBalancerOperatingStatus
    """Load balancer operating status"""

    project_id: int
    """Project ID"""

    provisioning_status: ProvisioningStatus
    """Load balancer lifecycle status"""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    tags_v2: List[Tag]
    """List of key-value tags associated with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    additional_vips: Optional[List[AdditionalVip]] = None
    """List of additional IP addresses"""

    creator_task_id: Optional[str] = None
    """Task that created this entity"""

    ddos_profile: Optional[DDOSProfile] = None
    """Loadbalancer advanced DDoS protection profile."""

    flavor: Optional[Flavor] = None
    """Load balancer flavor (if not default)"""

    floating_ips: Optional[List[FloatingIP]] = None
    """List of assigned floating IPs"""

    listeners: Optional[List[Listener]] = None
    """Load balancer listeners"""

    logging: Optional[Logging] = None
    """Logging configuration"""

    preferred_connectivity: Optional[LoadBalancerMemberConnectivity] = None
    """
    Preferred option to establish connectivity between load balancer and its pools
    members
    """

    stats: Optional[LoadBalancerStatistics] = None
    """Statistics of load balancer."""

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """

    updated_at: Optional[datetime] = None
    """Datetime when the load balancer was last updated"""

    vip_address: Optional[str] = None
    """Load balancer IP address"""

    vip_ip_family: Optional[InterfaceIPFamily] = None
    """Load balancer IP family"""

    vip_port_id: Optional[str] = None
    """The ID of the Virtual IP (VIP) port."""

    vrrp_ips: Optional[List[VrrpIP]] = None
    """List of VRRP IP addresses"""
