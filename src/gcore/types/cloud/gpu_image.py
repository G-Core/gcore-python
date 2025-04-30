# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .tag import Tag
from ..._models import BaseModel

__all__ = ["GPUImage"]


class GPUImage(BaseModel):
    id: str
    """
    '#/components/schemas/GpuImageSerializer/properties/id'
    "$.components.schemas.GpuImageSerializer.properties.id"
    """

    created_at: datetime
    """
    '#/components/schemas/GpuImageSerializer/properties/created_at'
    "$.components.schemas.GpuImageSerializer.properties.created_at"
    """

    min_disk: int
    """
    '#/components/schemas/GpuImageSerializer/properties/min_disk'
    "$.components.schemas.GpuImageSerializer.properties.min_disk"
    """

    min_ram: int
    """
    '#/components/schemas/GpuImageSerializer/properties/min_ram'
    "$.components.schemas.GpuImageSerializer.properties.min_ram"
    """

    name: str
    """
    '#/components/schemas/GpuImageSerializer/properties/name'
    "$.components.schemas.GpuImageSerializer.properties.name"
    """

    status: str
    """
    '#/components/schemas/GpuImageSerializer/properties/status'
    "$.components.schemas.GpuImageSerializer.properties.status"
    """

    tags: List[Tag]
    """
    '#/components/schemas/GpuImageSerializer/properties/tags'
    "$.components.schemas.GpuImageSerializer.properties.tags"
    """

    updated_at: datetime
    """
    '#/components/schemas/GpuImageSerializer/properties/updated_at'
    "$.components.schemas.GpuImageSerializer.properties.updated_at"
    """

    visibility: str
    """
    '#/components/schemas/GpuImageSerializer/properties/visibility'
    "$.components.schemas.GpuImageSerializer.properties.visibility"
    """

    architecture: Optional[str] = None
    """
    '#/components/schemas/GpuImageSerializer/properties/architecture/anyOf/0'
    "$.components.schemas.GpuImageSerializer.properties.architecture.anyOf[0]"
    """

    os_distro: Optional[str] = None
    """
    '#/components/schemas/GpuImageSerializer/properties/os_distro/anyOf/0'
    "$.components.schemas.GpuImageSerializer.properties.os_distro.anyOf[0]"
    """

    os_type: Optional[str] = None
    """
    '#/components/schemas/GpuImageSerializer/properties/os_type/anyOf/0'
    "$.components.schemas.GpuImageSerializer.properties.os_type.anyOf[0]"
    """

    os_version: Optional[str] = None
    """
    '#/components/schemas/GpuImageSerializer/properties/os_version/anyOf/0'
    "$.components.schemas.GpuImageSerializer.properties.os_version.anyOf[0]"
    """

    size: Optional[int] = None
    """
    '#/components/schemas/GpuImageSerializer/properties/size'
    "$.components.schemas.GpuImageSerializer.properties.size"
    """

    ssh_key: Optional[str] = None
    """
    '#/components/schemas/GpuImageSerializer/properties/ssh_key/anyOf/0'
    "$.components.schemas.GpuImageSerializer.properties.ssh_key.anyOf[0]"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/GpuImageSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.GpuImageSerializer.properties.task_id.anyOf[0]"
    """
