# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..tag import Tag
from ...._models import BaseModel

__all__ = ["Image"]


class Image(BaseModel):
    id: str
    """Image ID"""

    architecture: Literal["aarch64", "x86_64"]
    """An image architecture type: aarch64, `x86_64`."""

    created_at: datetime
    """Datetime when the image was created"""

    creator_task_id: Optional[str] = None
    """Task that created this entity. The value is null if no task created the image."""

    currency_code: Optional[str] = None
    """Currency code. The value is null if the price is not available."""

    description: Optional[str] = None
    """Image description. The value is null if the image has no description."""

    disk_format: str
    """Disk format"""

    display_order: Optional[int] = None
    """The display order of the image.

    The value is null if the image has no display order.
    """

    gpu_driver: Optional[str] = None
    """Name of the GPU driver vendor.

    The value is null if the image has no GPU driver.
    """

    gpu_driver_type: Optional[str] = None
    """Type of the GPU driver. The value is null if the image has no GPU driver."""

    gpu_driver_version: Optional[str] = None
    """Version of the installed GPU driver.

    The value is null if the image has no GPU driver.
    """

    hw_firmware_type: Optional[Literal["bios", "uefi"]] = None
    """Specifies the type of firmware with which to boot the guest.

    The value is null if the image sets no firmware type.
    """

    hw_machine_type: Optional[Literal["i440", "q35"]] = None
    """A virtual chipset type. The value is null if the image sets no machine type."""

    is_baremetal: bool
    """Set to true if the image will be used by bare metal servers."""

    min_disk: int
    """Minimal boot volume required"""

    min_ram: int
    """Minimal VM RAM required"""

    name: str
    """Image display name"""

    os_distro: str
    """OS Distribution, i.e. Debian, CentOS, Ubuntu, CoreOS etc."""

    os_type: Literal["linux", "windows"]
    """The operating system installed on the image."""

    os_version: str
    """OS version, i.e. 19.04 (for Ubuntu) or 9.4 for Debian"""

    price_per_hour: Optional[float] = None
    """Price per hour. The value is null if the price is not available."""

    price_per_month: Optional[float] = None
    """Price per month. The value is null if the price is not available."""

    price_status: Optional[Literal["error", "hide", "show"]] = None
    """Price status for the UI. The value is null if the price is not available."""

    project_id: int
    """Project ID"""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    size: Optional[int] = None
    """Image size in bytes. The value is null if the size is not known."""

    ssh_key: Optional[Literal["allow", "deny", "required"]] = None
    """Whether the image supports SSH key or not.

    The value is null if the image has no SSH key setting.
    """

    status: str
    """Image status, i.e. active"""

    tags_v2: List[Tag]
    """List of key-value tags associated with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """

    updated_at: datetime
    """Datetime when the image was updated"""

    visibility: str
    """Image visibility. Globally visible images are public"""
