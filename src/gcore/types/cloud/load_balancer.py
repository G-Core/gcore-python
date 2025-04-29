# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .tag import Tag
from ..._models import BaseModel
from .floating_ip import FloatingIP
from .ddos_profile import DDOSProfile
from .interface_ip_family import InterfaceIPFamily
from .provisioning_status import ProvisioningStatus
from .load_balancer_statistics import LoadBalancerStatistics
from .load_balancer_instance_role import LoadBalancerInstanceRole
from .load_balancer_operating_status import LoadBalancerOperatingStatus
from .load_balancer_member_connectivity import LoadBalancerMemberConnectivity

__all__ = ["LoadBalancer", "AdditionalVip", "Flavor", "Listener", "Logging", "LoggingRetentionPolicy", "VrrpIP"]


class AdditionalVip(BaseModel):
    ip_address: str
    """
    '#/components/schemas/NetworkPortFixedIp/properties/ip_address'
    "$.components.schemas.NetworkPortFixedIp.properties.ip_address"
    """

    subnet_id: str
    """
    '#/components/schemas/NetworkPortFixedIp/properties/subnet_id'
    "$.components.schemas.NetworkPortFixedIp.properties.subnet_id"
    """


class Flavor(BaseModel):
    flavor_id: str
    """
    '#/components/schemas/LbFlavorSerializer/properties/flavor_id'
    "$.components.schemas.LbFlavorSerializer.properties.flavor_id"
    """

    flavor_name: str
    """
    '#/components/schemas/LbFlavorSerializer/properties/flavor_name'
    "$.components.schemas.LbFlavorSerializer.properties.flavor_name"
    """

    ram: int
    """
    '#/components/schemas/LbFlavorSerializer/properties/ram'
    "$.components.schemas.LbFlavorSerializer.properties.ram"
    """

    vcpus: int
    """
    '#/components/schemas/LbFlavorSerializer/properties/vcpus'
    "$.components.schemas.LbFlavorSerializer.properties.vcpus"
    """


class Listener(BaseModel):
    id: str
    """
    '#/components/schemas/ListenerSerializer/properties/id'
    "$.components.schemas.ListenerSerializer.properties.id"
    """


class LoggingRetentionPolicy(BaseModel):
    period: Optional[int] = None
    """
    '#/components/schemas/LaasIndexRetentionPolicyPydanticSerializer/properties/period/anyOf/0'
    "$.components.schemas.LaasIndexRetentionPolicyPydanticSerializer.properties.period.anyOf[0]"
    """


class Logging(BaseModel):
    destination_region_id: Optional[int] = None
    """
    '#/components/schemas/LoggingOutSerializer/properties/destination_region_id/anyOf/0'
    "$.components.schemas.LoggingOutSerializer.properties.destination_region_id.anyOf[0]"
    """

    enabled: bool
    """
    '#/components/schemas/LoggingOutSerializer/properties/enabled'
    "$.components.schemas.LoggingOutSerializer.properties.enabled"
    """

    topic_name: Optional[str] = None
    """
    '#/components/schemas/LoggingOutSerializer/properties/topic_name/anyOf/0'
    "$.components.schemas.LoggingOutSerializer.properties.topic_name.anyOf[0]"
    """

    retention_policy: Optional[LoggingRetentionPolicy] = None
    """
    '#/components/schemas/LoggingOutSerializer/properties/retention_policy/anyOf/0'
    "$.components.schemas.LoggingOutSerializer.properties.retention_policy.anyOf[0]"
    """


class VrrpIP(BaseModel):
    ip_address: str
    """
    '#/components/schemas/VRRPIP/properties/ip_address'
    "$.components.schemas.VRRPIP.properties.ip_address"
    """

    role: LoadBalancerInstanceRole
    """
    '#/components/schemas/VRRPIP/properties/role'
    "$.components.schemas.VRRPIP.properties.role"
    """

    subnet_id: str
    """
    '#/components/schemas/VRRPIP/properties/subnet_id'
    "$.components.schemas.VRRPIP.properties.subnet_id"
    """


class LoadBalancer(BaseModel):
    id: str
    """
    '#/components/schemas/LoadbalancerSerializer/properties/id'
    "$.components.schemas.LoadbalancerSerializer.properties.id"
    """

    created_at: datetime
    """
    '#/components/schemas/LoadbalancerSerializer/properties/created_at'
    "$.components.schemas.LoadbalancerSerializer.properties.created_at"
    """

    name: str
    """
    '#/components/schemas/LoadbalancerSerializer/properties/name'
    "$.components.schemas.LoadbalancerSerializer.properties.name"
    """

    operating_status: LoadBalancerOperatingStatus
    """
    '#/components/schemas/LoadbalancerSerializer/properties/operating_status'
    "$.components.schemas.LoadbalancerSerializer.properties.operating_status"
    """

    project_id: int
    """
    '#/components/schemas/LoadbalancerSerializer/properties/project_id'
    "$.components.schemas.LoadbalancerSerializer.properties.project_id"
    """

    provisioning_status: ProvisioningStatus
    """
    '#/components/schemas/LoadbalancerSerializer/properties/provisioning_status'
    "$.components.schemas.LoadbalancerSerializer.properties.provisioning_status"
    """

    region: str
    """
    '#/components/schemas/LoadbalancerSerializer/properties/region'
    "$.components.schemas.LoadbalancerSerializer.properties.region"
    """

    region_id: int
    """
    '#/components/schemas/LoadbalancerSerializer/properties/region_id'
    "$.components.schemas.LoadbalancerSerializer.properties.region_id"
    """

    additional_vips: Optional[List[AdditionalVip]] = None
    """
    '#/components/schemas/LoadbalancerSerializer/properties/additional_vips'
    "$.components.schemas.LoadbalancerSerializer.properties.additional_vips"
    """

    creator_task_id: Optional[str] = None
    """
    '#/components/schemas/LoadbalancerSerializer/properties/creator_task_id/anyOf/0'
    "$.components.schemas.LoadbalancerSerializer.properties.creator_task_id.anyOf[0]"
    """

    ddos_profile: Optional[DDOSProfile] = None
    """
    '#/components/schemas/LoadbalancerSerializer/properties/ddos_profile/anyOf/0'
    "$.components.schemas.LoadbalancerSerializer.properties.ddos_profile.anyOf[0]"
    """

    flavor: Optional[Flavor] = None
    """
    '#/components/schemas/LoadbalancerSerializer/properties/flavor/anyOf/0'
    "$.components.schemas.LoadbalancerSerializer.properties.flavor.anyOf[0]"
    """

    floating_ips: Optional[List[FloatingIP]] = None
    """
    '#/components/schemas/LoadbalancerSerializer/properties/floating_ips'
    "$.components.schemas.LoadbalancerSerializer.properties.floating_ips"
    """

    listeners: Optional[List[Listener]] = None
    """
    '#/components/schemas/LoadbalancerSerializer/properties/listeners'
    "$.components.schemas.LoadbalancerSerializer.properties.listeners"
    """

    logging: Optional[Logging] = None
    """
    '#/components/schemas/LoadbalancerSerializer/properties/logging/anyOf/0'
    "$.components.schemas.LoadbalancerSerializer.properties.logging.anyOf[0]"
    """

    metadata: Optional[List[Tag]] = None
    """
    '#/components/schemas/LoadbalancerSerializer/properties/metadata'
    "$.components.schemas.LoadbalancerSerializer.properties.metadata"
    """

    preferred_connectivity: Optional[LoadBalancerMemberConnectivity] = None
    """
    '#/components/schemas/LoadbalancerSerializer/properties/preferred_connectivity'
    "$.components.schemas.LoadbalancerSerializer.properties.preferred_connectivity"
    """

    stats: Optional[LoadBalancerStatistics] = None
    """
    '#/components/schemas/LoadbalancerSerializer/properties/stats/anyOf/0'
    "$.components.schemas.LoadbalancerSerializer.properties.stats.anyOf[0]"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/LoadbalancerSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.LoadbalancerSerializer.properties.task_id.anyOf[0]"
    """

    updated_at: Optional[datetime] = None
    """
    '#/components/schemas/LoadbalancerSerializer/properties/updated_at/anyOf/0'
    "$.components.schemas.LoadbalancerSerializer.properties.updated_at.anyOf[0]"
    """

    vip_address: Optional[str] = None
    """
    '#/components/schemas/LoadbalancerSerializer/properties/vip_address/anyOf/0'
    "$.components.schemas.LoadbalancerSerializer.properties.vip_address.anyOf[0]"
    """

    vip_ip_family: Optional[InterfaceIPFamily] = None
    """
    '#/components/schemas/LoadbalancerSerializer/properties/vip_ip_family/anyOf/0'
    "$.components.schemas.LoadbalancerSerializer.properties.vip_ip_family.anyOf[0]"
    """

    vip_port_id: Optional[str] = None
    """
    '#/components/schemas/LoadbalancerSerializer/properties/vip_port_id/anyOf/0'
    "$.components.schemas.LoadbalancerSerializer.properties.vip_port_id.anyOf[0]"
    """

    vrrp_ips: Optional[List[VrrpIP]] = None
    """
    '#/components/schemas/LoadbalancerSerializer/properties/vrrp_ips'
    "$.components.schemas.LoadbalancerSerializer.properties.vrrp_ips"
    """
