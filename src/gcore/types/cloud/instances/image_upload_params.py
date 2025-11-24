# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImageUploadParams"]


class ImageUploadParams(TypedDict, total=False):
    project_id: int

    region_id: int

    name: Required[str]
    """Image name"""

    url: Required[str]
    """URL"""

    architecture: Literal["aarch64", "x86_64"]
    """Image CPU architecture type: `aarch64`, `x86_64`"""

    cow_format: bool
    """
    When True, image cannot be deleted unless all volumes, created from it, are
    deleted.
    """

    hw_firmware_type: Optional[Literal["bios", "uefi"]]
    """Specifies the type of firmware with which to boot the guest."""

    hw_machine_type: Optional[Literal["pc", "q35"]]
    """A virtual chipset type."""

    is_baremetal: bool
    """Set to true if the image will be used by bare metal servers. Defaults to false."""

    os_distro: Optional[str]
    """OS Distribution, i.e. Debian, CentOS, Ubuntu, CoreOS etc."""

    os_type: Literal["linux", "windows"]
    """The operating system installed on the image."""

    os_version: Optional[str]
    """OS version, i.e. 22.04 (for Ubuntu) or 9.4 for Debian"""

    ssh_key: Literal["allow", "deny", "required"]
    """Whether the image supports SSH key or not"""

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Both
    tag keys and values have a maximum length of 255 characters. Some tags are
    read-only and cannot be modified by the user. Tags are also integrated with cost
    reports, allowing cost data to be filtered based on tag keys or values.
    """
