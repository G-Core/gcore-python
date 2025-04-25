# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Image"]


class Image(BaseModel):
    name: str
    """
    '#/components/schemas/ImageSchema/properties/name'
    "$.components.schemas.ImageSchema.properties.name"
    """

    id: Optional[str] = None
    """
    '#/components/schemas/ImageSchema/properties/id'
    "$.components.schemas.ImageSchema.properties.id"
    """

    architecture: Optional[Literal["aarch64", "x86_64"]] = None
    """
    '#/components/schemas/ImageSchema/properties/architecture'
    "$.components.schemas.ImageSchema.properties.architecture"
    """

    created_at: Optional[datetime] = None
    """
    '#/components/schemas/ImageSchema/properties/created_at'
    "$.components.schemas.ImageSchema.properties.created_at"
    """

    creator_task_id: Optional[str] = None
    """
    '#/components/schemas/ImageSchema/properties/creator_task_id'
    "$.components.schemas.ImageSchema.properties.creator_task_id"
    """

    currency_code: Optional[str] = None
    """
    '#/components/schemas/ImageSchema/properties/currency_code'
    "$.components.schemas.ImageSchema.properties.currency_code"
    """

    description: Optional[str] = None
    """
    '#/components/schemas/ImageSchema/properties/description'
    "$.components.schemas.ImageSchema.properties.description"
    """

    disk_format: Optional[str] = None
    """
    '#/components/schemas/ImageSchema/properties/disk_format'
    "$.components.schemas.ImageSchema.properties.disk_format"
    """

    display_order: Optional[int] = None
    """
    '#/components/schemas/ImageSchema/properties/display_order'
    "$.components.schemas.ImageSchema.properties.display_order"
    """

    hw_firmware_type: Optional[Literal["bios", "uefi"]] = None
    """
    '#/components/schemas/ImageSchema/properties/hw_firmware_type'
    "$.components.schemas.ImageSchema.properties.hw_firmware_type"
    """

    hw_machine_type: Optional[Literal["i440", "q35"]] = None
    """
    '#/components/schemas/ImageSchema/properties/hw_machine_type'
    "$.components.schemas.ImageSchema.properties.hw_machine_type"
    """

    internally_shared: Optional[bool] = None
    """
    '#/components/schemas/ImageSchema/properties/internally_shared'
    "$.components.schemas.ImageSchema.properties.internally_shared"
    """

    is_baremetal: Optional[bool] = None
    """
    '#/components/schemas/ImageSchema/properties/is_baremetal'
    "$.components.schemas.ImageSchema.properties.is_baremetal"
    """

    metadata: Optional[object] = None
    """
    '#/components/schemas/ImageSchema/properties/metadata'
    "$.components.schemas.ImageSchema.properties.metadata"
    """

    metadata_detailed: Optional[object] = None
    """
    '#/components/schemas/ImageSchema/properties/metadata_detailed'
    "$.components.schemas.ImageSchema.properties.metadata_detailed"
    """

    min_disk: Optional[int] = None
    """
    '#/components/schemas/ImageSchema/properties/min_disk'
    "$.components.schemas.ImageSchema.properties.min_disk"
    """

    min_ram: Optional[int] = None
    """
    '#/components/schemas/ImageSchema/properties/min_ram'
    "$.components.schemas.ImageSchema.properties.min_ram"
    """

    os_distro: Optional[str] = None
    """
    '#/components/schemas/ImageSchema/properties/os_distro'
    "$.components.schemas.ImageSchema.properties.os_distro"
    """

    os_type: Optional[Literal["linux", "windows"]] = None
    """
    '#/components/schemas/ImageSchema/properties/os_type'
    "$.components.schemas.ImageSchema.properties.os_type"
    """

    os_version: Optional[str] = None
    """
    '#/components/schemas/ImageSchema/properties/os_version'
    "$.components.schemas.ImageSchema.properties.os_version"
    """

    price_per_hour: Optional[float] = None
    """
    '#/components/schemas/ImageSchema/properties/price_per_hour'
    "$.components.schemas.ImageSchema.properties.price_per_hour"
    """

    price_per_month: Optional[float] = None
    """
    '#/components/schemas/ImageSchema/properties/price_per_month'
    "$.components.schemas.ImageSchema.properties.price_per_month"
    """

    price_status: Optional[Literal["error", "hide", "show"]] = None
    """
    '#/components/schemas/ImageSchema/properties/price_status'
    "$.components.schemas.ImageSchema.properties.price_status"
    """

    project_id: Optional[int] = None
    """
    '#/components/schemas/ImageSchema/properties/project_id'
    "$.components.schemas.ImageSchema.properties.project_id"
    """

    region: Optional[str] = None
    """
    '#/components/schemas/ImageSchema/properties/region'
    "$.components.schemas.ImageSchema.properties.region"
    """

    region_id: Optional[int] = None
    """
    '#/components/schemas/ImageSchema/properties/region_id'
    "$.components.schemas.ImageSchema.properties.region_id"
    """

    size: Optional[int] = None
    """
    '#/components/schemas/ImageSchema/properties/size'
    "$.components.schemas.ImageSchema.properties.size"
    """

    ssh_key: Optional[Literal["allow", "deny", "required"]] = None
    """
    '#/components/schemas/ImageSchema/properties/ssh_key'
    "$.components.schemas.ImageSchema.properties.ssh_key"
    """

    status: Optional[str] = None
    """
    '#/components/schemas/ImageSchema/properties/status'
    "$.components.schemas.ImageSchema.properties.status"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/ImageSchema/properties/task_id'
    "$.components.schemas.ImageSchema.properties.task_id"
    """

    updated_at: Optional[datetime] = None
    """
    '#/components/schemas/ImageSchema/properties/updated_at'
    "$.components.schemas.ImageSchema.properties.updated_at"
    """

    visibility: Optional[str] = None
    """
    '#/components/schemas/ImageSchema/properties/visibility'
    "$.components.schemas.ImageSchema.properties.visibility"
    """
