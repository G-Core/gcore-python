# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .tag import Tag
from ..._models import BaseModel

__all__ = ["Network"]


class Network(BaseModel):
    id: str
    """
    '#/components/schemas/NetworkSerializer/properties/id'
    "$.components.schemas.NetworkSerializer.properties.id"
    """

    created_at: datetime
    """
    '#/components/schemas/NetworkSerializer/properties/created_at'
    "$.components.schemas.NetworkSerializer.properties.created_at"
    """

    external: bool
    """
    '#/components/schemas/NetworkSerializer/properties/external'
    "$.components.schemas.NetworkSerializer.properties.external"
    """

    metadata: List[Tag]
    """
    '#/components/schemas/NetworkSerializer/properties/metadata'
    "$.components.schemas.NetworkSerializer.properties.metadata"
    """

    name: str
    """
    '#/components/schemas/NetworkSerializer/properties/name'
    "$.components.schemas.NetworkSerializer.properties.name"
    """

    port_security_enabled: bool
    """
    '#/components/schemas/NetworkSerializer/properties/port_security_enabled'
    "$.components.schemas.NetworkSerializer.properties.port_security_enabled"
    """

    region: str
    """
    '#/components/schemas/NetworkSerializer/properties/region'
    "$.components.schemas.NetworkSerializer.properties.region"
    """

    region_id: int
    """
    '#/components/schemas/NetworkSerializer/properties/region_id'
    "$.components.schemas.NetworkSerializer.properties.region_id"
    """

    shared: bool
    """
    '#/components/schemas/NetworkSerializer/properties/shared'
    "$.components.schemas.NetworkSerializer.properties.shared"
    """

    subnets: List[str]
    """
    '#/components/schemas/NetworkSerializer/properties/subnets'
    "$.components.schemas.NetworkSerializer.properties.subnets"
    """

    tags: List[Tag]
    """
    '#/components/schemas/NetworkSerializer/properties/tags'
    "$.components.schemas.NetworkSerializer.properties.tags"
    """

    type: str
    """
    '#/components/schemas/NetworkSerializer/properties/type'
    "$.components.schemas.NetworkSerializer.properties.type"
    """

    updated_at: datetime
    """
    '#/components/schemas/NetworkSerializer/properties/updated_at'
    "$.components.schemas.NetworkSerializer.properties.updated_at"
    """

    creator_task_id: Optional[str] = None
    """
    '#/components/schemas/NetworkSerializer/properties/creator_task_id/anyOf/0'
    "$.components.schemas.NetworkSerializer.properties.creator_task_id.anyOf[0]"
    """

    default: Optional[bool] = None
    """
    '#/components/schemas/NetworkSerializer/properties/default/anyOf/0'
    "$.components.schemas.NetworkSerializer.properties['default'].anyOf[0]"
    """

    mtu: Optional[int] = None
    """
    '#/components/schemas/NetworkSerializer/properties/mtu'
    "$.components.schemas.NetworkSerializer.properties.mtu"
    """

    project_id: Optional[int] = None
    """
    '#/components/schemas/NetworkSerializer/properties/project_id/anyOf/0'
    "$.components.schemas.NetworkSerializer.properties.project_id.anyOf[0]"
    """

    segmentation_id: Optional[int] = None
    """
    '#/components/schemas/NetworkSerializer/properties/segmentation_id/anyOf/0'
    "$.components.schemas.NetworkSerializer.properties.segmentation_id.anyOf[0]"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/NetworkSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.NetworkSerializer.properties.task_id.anyOf[0]"
    """
