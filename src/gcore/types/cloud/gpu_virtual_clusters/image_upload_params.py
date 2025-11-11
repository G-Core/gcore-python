# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImageUploadParams"]


class ImageUploadParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    name: Required[str]
    """Image name"""

    url: Required[str]
    """Image URL"""

    architecture: Optional[Literal["aarch64", "x86_64"]]
    """Image architecture type: aarch64, `x86_64`"""

    cow_format: bool
    """
    When True, image cannot be deleted unless all volumes, created from it, are
    deleted.
    """

    hw_firmware_type: Optional[Literal["bios", "uefi"]]
    """Specifies the type of firmware with which to boot the guest."""

    os_distro: Optional[str]
    """OS Distribution, i.e. Debian, CentOS, Ubuntu, CoreOS etc."""

    os_type: Optional[Literal["linux", "windows"]]
    """The operating system installed on the image. Linux by default"""

    os_version: Optional[str]
    """OS version, i.e. 19.04 (for Ubuntu) or 9.4 for Debian"""

    ssh_key: Literal["allow", "deny", "required"]
    """Permission to use a ssh key in instances"""

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """
