# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .tag import Tag
from ..._models import BaseModel
from .floating_ip_status import FloatingIPStatus

__all__ = ["FloatingIP"]


class FloatingIP(BaseModel):
    id: Optional[str] = None
    """
    '#/components/schemas/FloatingIPSerializer/properties/id/anyOf/0'
    "$.components.schemas.FloatingIPSerializer.properties.id.anyOf[0]"
    """

    created_at: datetime
    """
    '#/components/schemas/FloatingIPSerializer/properties/created_at'
    "$.components.schemas.FloatingIPSerializer.properties.created_at"
    """

    creator_task_id: Optional[str] = None
    """
    '#/components/schemas/FloatingIPSerializer/properties/creator_task_id/anyOf/0'
    "$.components.schemas.FloatingIPSerializer.properties.creator_task_id.anyOf[0]"
    """

    dns_domain: Optional[str] = None
    """
    '#/components/schemas/FloatingIPSerializer/properties/dns_domain/anyOf/0'
    "$.components.schemas.FloatingIPSerializer.properties.dns_domain.anyOf[0]"
    """

    dns_name: Optional[str] = None
    """
    '#/components/schemas/FloatingIPSerializer/properties/dns_name/anyOf/0'
    "$.components.schemas.FloatingIPSerializer.properties.dns_name.anyOf[0]"
    """

    fixed_ip_address: Optional[str] = None
    """
    '#/components/schemas/FloatingIPSerializer/properties/fixed_ip_address/anyOf/0'
    "$.components.schemas.FloatingIPSerializer.properties.fixed_ip_address.anyOf[0]"
    """

    floating_ip_address: Optional[str] = None
    """
    '#/components/schemas/FloatingIPSerializer/properties/floating_ip_address/anyOf/0'
    "$.components.schemas.FloatingIPSerializer.properties.floating_ip_address.anyOf[0]"
    """

    metadata: List[Tag]
    """
    '#/components/schemas/FloatingIPSerializer/properties/metadata'
    "$.components.schemas.FloatingIPSerializer.properties.metadata"
    """

    port_id: Optional[str] = None
    """
    '#/components/schemas/FloatingIPSerializer/properties/port_id/anyOf/0'
    "$.components.schemas.FloatingIPSerializer.properties.port_id.anyOf[0]"
    """

    project_id: int
    """
    '#/components/schemas/FloatingIPSerializer/properties/project_id'
    "$.components.schemas.FloatingIPSerializer.properties.project_id"
    """

    region: str
    """
    '#/components/schemas/FloatingIPSerializer/properties/region'
    "$.components.schemas.FloatingIPSerializer.properties.region"
    """

    region_id: int
    """
    '#/components/schemas/FloatingIPSerializer/properties/region_id'
    "$.components.schemas.FloatingIPSerializer.properties.region_id"
    """

    router_id: Optional[str] = None
    """
    '#/components/schemas/FloatingIPSerializer/properties/router_id/anyOf/0'
    "$.components.schemas.FloatingIPSerializer.properties.router_id.anyOf[0]"
    """

    status: Optional[FloatingIPStatus] = None
    """
    '#/components/schemas/FloatingIPSerializer/properties/status/anyOf/0'
    "$.components.schemas.FloatingIPSerializer.properties.status.anyOf[0]"
    """

    subnet_id: Optional[str] = None
    """
    '#/components/schemas/FloatingIPSerializer/properties/subnet_id/anyOf/0'
    "$.components.schemas.FloatingIPSerializer.properties.subnet_id.anyOf[0]"
    """

    tags: List[Tag]
    """
    '#/components/schemas/FloatingIPSerializer/properties/tags'
    "$.components.schemas.FloatingIPSerializer.properties.tags"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/FloatingIPSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.FloatingIPSerializer.properties.task_id.anyOf[0]"
    """

    updated_at: datetime
    """
    '#/components/schemas/FloatingIPSerializer/properties/updated_at'
    "$.components.schemas.FloatingIPSerializer.properties.updated_at"
    """
