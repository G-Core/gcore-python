# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .network import Network
from ..._models import BaseModel
from .allowed_address_pairs import AllowedAddressPairs

__all__ = ["ReservedFixedIP", "Attachment", "Reservation"]


class Attachment(BaseModel):
    resource_id: Optional[str] = None
    """
    '#/components/schemas/AttachmentSerializer/properties/resource_id/anyOf/0'
    "$.components.schemas.AttachmentSerializer.properties.resource_id.anyOf[0]"
    """

    resource_type: Optional[str] = None
    """
    '#/components/schemas/AttachmentSerializer/properties/resource_type/anyOf/0'
    "$.components.schemas.AttachmentSerializer.properties.resource_type.anyOf[0]"
    """


class Reservation(BaseModel):
    resource_id: Optional[str] = None
    """
    '#/components/schemas/ReservationSerializer/properties/resource_id/anyOf/0'
    "$.components.schemas.ReservationSerializer.properties.resource_id.anyOf[0]"
    """

    resource_type: Optional[str] = None
    """
    '#/components/schemas/ReservationSerializer/properties/resource_type/anyOf/0'
    "$.components.schemas.ReservationSerializer.properties.resource_type.anyOf[0]"
    """

    status: Optional[str] = None
    """
    '#/components/schemas/ReservationSerializer/properties/status/anyOf/0'
    "$.components.schemas.ReservationSerializer.properties.status.anyOf[0]"
    """


class ReservedFixedIP(BaseModel):
    allowed_address_pairs: List[AllowedAddressPairs]
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/allowed_address_pairs'
    "$.components.schemas.ReservedFixedIPSerializer.properties.allowed_address_pairs"
    """

    attachments: List[Attachment]
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/attachments'
    "$.components.schemas.ReservedFixedIPSerializer.properties.attachments"
    """

    created_at: datetime
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/created_at'
    "$.components.schemas.ReservedFixedIPSerializer.properties.created_at"
    """

    is_external: bool
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/is_external'
    "$.components.schemas.ReservedFixedIPSerializer.properties.is_external"
    """

    is_vip: bool
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/is_vip'
    "$.components.schemas.ReservedFixedIPSerializer.properties.is_vip"
    """

    name: str
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/name'
    "$.components.schemas.ReservedFixedIPSerializer.properties.name"
    """

    network: Network
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/network'
    "$.components.schemas.ReservedFixedIPSerializer.properties.network"
    """

    network_id: str
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/network_id'
    "$.components.schemas.ReservedFixedIPSerializer.properties.network_id"
    """

    port_id: str
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/port_id'
    "$.components.schemas.ReservedFixedIPSerializer.properties.port_id"
    """

    region: str
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/region'
    "$.components.schemas.ReservedFixedIPSerializer.properties.region"
    """

    region_id: int
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/region_id'
    "$.components.schemas.ReservedFixedIPSerializer.properties.region_id"
    """

    reservation: Reservation
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/reservation'
    "$.components.schemas.ReservedFixedIPSerializer.properties.reservation"
    """

    status: str
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/status'
    "$.components.schemas.ReservedFixedIPSerializer.properties.status"
    """

    updated_at: datetime
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/updated_at'
    "$.components.schemas.ReservedFixedIPSerializer.properties.updated_at"
    """

    creator_task_id: Optional[str] = None
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/creator_task_id/anyOf/0'
    "$.components.schemas.ReservedFixedIPSerializer.properties.creator_task_id.anyOf[0]"
    """

    fixed_ip_address: Optional[str] = None
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/fixed_ip_address/anyOf/0'
    "$.components.schemas.ReservedFixedIPSerializer.properties.fixed_ip_address.anyOf[0]"
    """

    fixed_ipv6_address: Optional[str] = None
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/fixed_ipv6_address/anyOf/0'
    "$.components.schemas.ReservedFixedIPSerializer.properties.fixed_ipv6_address.anyOf[0]"
    """

    project_id: Optional[int] = None
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/project_id/anyOf/0'
    "$.components.schemas.ReservedFixedIPSerializer.properties.project_id.anyOf[0]"
    """

    subnet_id: Optional[str] = None
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/subnet_id/anyOf/0'
    "$.components.schemas.ReservedFixedIPSerializer.properties.subnet_id.anyOf[0]"
    """

    subnet_v6_id: Optional[str] = None
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/subnet_v6_id/anyOf/0'
    "$.components.schemas.ReservedFixedIPSerializer.properties.subnet_v6_id.anyOf[0]"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/ReservedFixedIPSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.ReservedFixedIPSerializer.properties.task_id.anyOf[0]"
    """
