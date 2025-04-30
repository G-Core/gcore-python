# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .tag import Tag
from ..._models import BaseModel

__all__ = ["Image"]


class Image(BaseModel):
    id: str
    """
    '#/components/schemas/ImageSerializer/properties/id'
    "$.components.schemas.ImageSerializer.properties.id"
    """

    created_at: datetime
    """
    '#/components/schemas/ImageSerializer/properties/created_at'
    "$.components.schemas.ImageSerializer.properties.created_at"
    """

    disk_format: str
    """
    '#/components/schemas/ImageSerializer/properties/disk_format'
    "$.components.schemas.ImageSerializer.properties.disk_format"
    """

    min_disk: int
    """
    '#/components/schemas/ImageSerializer/properties/min_disk'
    "$.components.schemas.ImageSerializer.properties.min_disk"
    """

    min_ram: int
    """
    '#/components/schemas/ImageSerializer/properties/min_ram'
    "$.components.schemas.ImageSerializer.properties.min_ram"
    """

    name: str
    """
    '#/components/schemas/ImageSerializer/properties/name'
    "$.components.schemas.ImageSerializer.properties.name"
    """

    os_distro: str
    """
    '#/components/schemas/ImageSerializer/properties/os_distro'
    "$.components.schemas.ImageSerializer.properties.os_distro"
    """

    os_type: Literal["linux", "windows"]
    """
    '#/components/schemas/ImageSerializer/properties/os_type'
    "$.components.schemas.ImageSerializer.properties.os_type"
    """

    os_version: str
    """
    '#/components/schemas/ImageSerializer/properties/os_version'
    "$.components.schemas.ImageSerializer.properties.os_version"
    """

    project_id: int
    """
    '#/components/schemas/ImageSerializer/properties/project_id'
    "$.components.schemas.ImageSerializer.properties.project_id"
    """

    region: str
    """
    '#/components/schemas/ImageSerializer/properties/region'
    "$.components.schemas.ImageSerializer.properties.region"
    """

    region_id: int
    """
    '#/components/schemas/ImageSerializer/properties/region_id'
    "$.components.schemas.ImageSerializer.properties.region_id"
    """

    size: int
    """
    '#/components/schemas/ImageSerializer/properties/size'
    "$.components.schemas.ImageSerializer.properties.size"
    """

    status: str
    """
    '#/components/schemas/ImageSerializer/properties/status'
    "$.components.schemas.ImageSerializer.properties.status"
    """

    tags: List[Tag]
    """
    '#/components/schemas/ImageSerializer/properties/tags'
    "$.components.schemas.ImageSerializer.properties.tags"
    """

    updated_at: datetime
    """
    '#/components/schemas/ImageSerializer/properties/updated_at'
    "$.components.schemas.ImageSerializer.properties.updated_at"
    """

    visibility: str
    """
    '#/components/schemas/ImageSerializer/properties/visibility'
    "$.components.schemas.ImageSerializer.properties.visibility"
    """

    architecture: Optional[Literal["aarch64", "x86_64"]] = None
    """
    '#/components/schemas/ImageSerializer/properties/architecture'
    "$.components.schemas.ImageSerializer.properties.architecture"
    """

    creator_task_id: Optional[str] = None
    """
    '#/components/schemas/ImageSerializer/properties/creator_task_id/anyOf/0'
    "$.components.schemas.ImageSerializer.properties.creator_task_id.anyOf[0]"
    """

    description: Optional[str] = None
    """
    '#/components/schemas/ImageSerializer/properties/description/anyOf/0'
    "$.components.schemas.ImageSerializer.properties.description.anyOf[0]"
    """

    display_order: Optional[int] = None
    """
    '#/components/schemas/ImageSerializer/properties/display_order/anyOf/0'
    "$.components.schemas.ImageSerializer.properties.display_order.anyOf[0]"
    """

    hw_firmware_type: Optional[Literal["bios", "uefi"]] = None
    """
    '#/components/schemas/ImageSerializer/properties/hw_firmware_type/anyOf/0'
    "$.components.schemas.ImageSerializer.properties.hw_firmware_type.anyOf[0]"
    """

    hw_machine_type: Optional[Literal["pc", "q35"]] = None
    """
    '#/components/schemas/ImageSerializer/properties/hw_machine_type/anyOf/0'
    "$.components.schemas.ImageSerializer.properties.hw_machine_type.anyOf[0]"
    """

    is_baremetal: Optional[bool] = None
    """
    '#/components/schemas/ImageSerializer/properties/is_baremetal/anyOf/0'
    "$.components.schemas.ImageSerializer.properties.is_baremetal.anyOf[0]"
    """

    ssh_key: Optional[Literal["allow", "deny", "required"]] = None
    """
    '#/components/schemas/ImageSerializer/properties/ssh_key/anyOf/0'
    "$.components.schemas.ImageSerializer.properties.ssh_key.anyOf[0]"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/ImageSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.ImageSerializer.properties.task_id.anyOf[0]"
    """
