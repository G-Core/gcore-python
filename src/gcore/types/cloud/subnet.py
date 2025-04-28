# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .tag import Tag
from ..._models import BaseModel
from .ip_version import IPVersion
from .neutron_route import NeutronRoute

__all__ = ["Subnet"]


class Subnet(BaseModel):
    cidr: str
    """
    '#/components/schemas/SubnetSerializer/properties/cidr'
    "$.components.schemas.SubnetSerializer.properties.cidr"
    """

    created_at: datetime
    """
    '#/components/schemas/SubnetSerializer/properties/created_at'
    "$.components.schemas.SubnetSerializer.properties.created_at"
    """

    enable_dhcp: bool
    """
    '#/components/schemas/SubnetSerializer/properties/enable_dhcp'
    "$.components.schemas.SubnetSerializer.properties.enable_dhcp"
    """

    ip_version: IPVersion
    """
    '#/components/schemas/SubnetSerializer/properties/ip_version'
    "$.components.schemas.SubnetSerializer.properties.ip_version"
    """

    name: str
    """
    '#/components/schemas/SubnetSerializer/properties/name'
    "$.components.schemas.SubnetSerializer.properties.name"
    """

    network_id: str
    """
    '#/components/schemas/SubnetSerializer/properties/network_id'
    "$.components.schemas.SubnetSerializer.properties.network_id"
    """

    project_id: int
    """
    '#/components/schemas/SubnetSerializer/properties/project_id'
    "$.components.schemas.SubnetSerializer.properties.project_id"
    """

    region: str
    """
    '#/components/schemas/SubnetSerializer/properties/region'
    "$.components.schemas.SubnetSerializer.properties.region"
    """

    region_id: int
    """
    '#/components/schemas/SubnetSerializer/properties/region_id'
    "$.components.schemas.SubnetSerializer.properties.region_id"
    """

    tags: List[Tag]
    """
    '#/components/schemas/SubnetSerializer/properties/tags'
    "$.components.schemas.SubnetSerializer.properties.tags"
    """

    updated_at: datetime
    """
    '#/components/schemas/SubnetSerializer/properties/updated_at'
    "$.components.schemas.SubnetSerializer.properties.updated_at"
    """

    id: Optional[str] = None
    """
    '#/components/schemas/SubnetSerializer/properties/id/anyOf/0'
    "$.components.schemas.SubnetSerializer.properties.id.anyOf[0]"
    """

    available_ips: Optional[int] = None
    """
    '#/components/schemas/SubnetSerializer/properties/available_ips/anyOf/0'
    "$.components.schemas.SubnetSerializer.properties.available_ips.anyOf[0]"
    """

    creator_task_id: Optional[str] = None
    """
    '#/components/schemas/SubnetSerializer/properties/creator_task_id/anyOf/0'
    "$.components.schemas.SubnetSerializer.properties.creator_task_id.anyOf[0]"
    """

    dns_nameservers: Optional[List[str]] = None
    """
    '#/components/schemas/SubnetSerializer/properties/dns_nameservers/anyOf/0'
    "$.components.schemas.SubnetSerializer.properties.dns_nameservers.anyOf[0]"
    """

    gateway_ip: Optional[str] = None
    """
    '#/components/schemas/SubnetSerializer/properties/gateway_ip/anyOf/0'
    "$.components.schemas.SubnetSerializer.properties.gateway_ip.anyOf[0]"
    """

    has_router: Optional[bool] = None
    """
    '#/components/schemas/SubnetSerializer/properties/has_router'
    "$.components.schemas.SubnetSerializer.properties.has_router"
    """

    host_routes: Optional[List[NeutronRoute]] = None
    """
    '#/components/schemas/SubnetSerializer/properties/host_routes/anyOf/0'
    "$.components.schemas.SubnetSerializer.properties.host_routes.anyOf[0]"
    """

    metadata: Optional[List[Tag]] = None
    """
    '#/components/schemas/SubnetSerializer/properties/metadata'
    "$.components.schemas.SubnetSerializer.properties.metadata"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/SubnetSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.SubnetSerializer.properties.task_id.anyOf[0]"
    """

    total_ips: Optional[int] = None
    """
    '#/components/schemas/SubnetSerializer/properties/total_ips/anyOf/0'
    "$.components.schemas.SubnetSerializer.properties.total_ips.anyOf[0]"
    """
