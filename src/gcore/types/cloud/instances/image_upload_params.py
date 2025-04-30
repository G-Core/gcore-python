# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImageUploadParams"]


class ImageUploadParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fdownloadimage%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/downloadimage/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fdownloadimage%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/downloadimage/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    name: Required[str]
    """
    '#/components/schemas/ImageDownloadSerializer/properties/name'
    "$.components.schemas.ImageDownloadSerializer.properties.name"
    """

    url: Required[str]
    """
    '#/components/schemas/ImageDownloadSerializer/properties/url'
    "$.components.schemas.ImageDownloadSerializer.properties.url"
    """

    architecture: Literal["aarch64", "x86_64"]
    """
    '#/components/schemas/ImageDownloadSerializer/properties/architecture'
    "$.components.schemas.ImageDownloadSerializer.properties.architecture"
    """

    cow_format: bool
    """
    '#/components/schemas/ImageDownloadSerializer/properties/cow_format'
    "$.components.schemas.ImageDownloadSerializer.properties.cow_format"
    """

    hw_firmware_type: Optional[Literal["bios", "uefi"]]
    """
    '#/components/schemas/ImageDownloadSerializer/properties/hw_firmware_type/anyOf/0'
    "$.components.schemas.ImageDownloadSerializer.properties.hw_firmware_type.anyOf[0]"
    """

    hw_machine_type: Optional[Literal["pc", "q35"]]
    """
    '#/components/schemas/ImageDownloadSerializer/properties/hw_machine_type/anyOf/0'
    "$.components.schemas.ImageDownloadSerializer.properties.hw_machine_type.anyOf[0]"
    """

    is_baremetal: bool
    """
    '#/components/schemas/ImageDownloadSerializer/properties/is_baremetal'
    "$.components.schemas.ImageDownloadSerializer.properties.is_baremetal"
    """

    os_distro: Optional[str]
    """
    '#/components/schemas/ImageDownloadSerializer/properties/os_distro/anyOf/0'
    "$.components.schemas.ImageDownloadSerializer.properties.os_distro.anyOf[0]"
    """

    os_type: Literal["linux", "windows"]
    """
    '#/components/schemas/ImageDownloadSerializer/properties/os_type'
    "$.components.schemas.ImageDownloadSerializer.properties.os_type"
    """

    os_version: Optional[str]
    """
    '#/components/schemas/ImageDownloadSerializer/properties/os_version/anyOf/0'
    "$.components.schemas.ImageDownloadSerializer.properties.os_version.anyOf[0]"
    """

    ssh_key: Literal["allow", "deny", "required"]
    """
    '#/components/schemas/ImageDownloadSerializer/properties/ssh_key'
    "$.components.schemas.ImageDownloadSerializer.properties.ssh_key"
    """

    tags: Dict[str, str]
    """
    '#/components/schemas/ImageDownloadSerializer/properties/tags'
    "$.components.schemas.ImageDownloadSerializer.properties.tags"
    """
