# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..tag import Tag
from ...._models import BaseModel

__all__ = ["BaremetalImage"]


class BaremetalImage(BaseModel):
    id: str
    """Image ID"""

    architecture: Literal["aarch64", "x86_64"]
    """An image architecture type: aarch64, `x86_64`."""

    created_at: datetime
    """Datetime when the image was created"""

    creator_task_id: Optional[str] = None
    """Task that created this entity"""

    currency_code: Optional[str] = None
    """Currency code. Shown if the `include_prices` query parameter if set to true"""

    description: Optional[str] = None
    """Image description"""

    disk_format: str
    """Disk format"""

    display_order: Optional[int] = None

    gpu_driver: Optional[str] = None
    """Name of the GPU driver vendor"""

    gpu_driver_type: Optional[str] = None
    """Type of the GPU driver"""

    gpu_driver_version: Optional[str] = None
    """Version of the installed GPU driver"""

    hw_firmware_type: Optional[Literal["bios", "uefi"]] = None
    """Specifies the type of firmware with which to boot the guest."""

    hw_machine_type: Optional[Literal["pc", "q35"]] = None
    """A virtual chipset type."""

    is_baremetal: Optional[bool] = None
    """For bare metal servers this value is always set to true"""

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
    """Price per hour. Shown if the `include_prices` query parameter if set to true"""

    price_per_month: Optional[float] = None
    """Price per month. Shown if the `include_prices` query parameter if set to true"""

    price_status: Optional[Literal["error", "hide", "show"]] = None
    """Price status for the UI"""

    project_id: int
    """Project ID"""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    size: Optional[int] = None
    """Image size in bytes"""

    ssh_key: Optional[Literal["allow", "deny", "required"]] = None
    """Whether the image supports SSH key or not"""

    status: str
    """Image status, i.e. active"""

    tags: List[Tag]
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
