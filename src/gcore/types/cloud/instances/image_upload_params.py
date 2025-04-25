# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
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
    '#/components/schemas/ImageDownloadSchema/properties/name'
    "$.components.schemas.ImageDownloadSchema.properties.name"
    """

    url: Required[str]
    """
    '#/components/schemas/ImageDownloadSchema/properties/url'
    "$.components.schemas.ImageDownloadSchema.properties.url"
    """

    architecture: Literal["aarch64", "x86_64"]
    """
    '#/components/schemas/ImageDownloadSchema/properties/architecture'
    "$.components.schemas.ImageDownloadSchema.properties.architecture"
    """

    cow_format: bool
    """
    '#/components/schemas/ImageDownloadSchema/properties/cow_format'
    "$.components.schemas.ImageDownloadSchema.properties.cow_format"
    """

    hw_firmware_type: Literal["bios", "uefi"]
    """
    '#/components/schemas/ImageDownloadSchema/properties/hw_firmware_type'
    "$.components.schemas.ImageDownloadSchema.properties.hw_firmware_type"
    """

    hw_machine_type: Literal["i440", "q35"]
    """
    '#/components/schemas/ImageDownloadSchema/properties/hw_machine_type'
    "$.components.schemas.ImageDownloadSchema.properties.hw_machine_type"
    """

    is_baremetal: Optional[bool]
    """
    '#/components/schemas/ImageDownloadSchema/properties/is_baremetal'
    "$.components.schemas.ImageDownloadSchema.properties.is_baremetal"
    """

    metadata: object
    """
    '#/components/schemas/ImageDownloadSchema/properties/metadata'
    "$.components.schemas.ImageDownloadSchema.properties.metadata"
    """

    os_distro: str
    """
    '#/components/schemas/ImageDownloadSchema/properties/os_distro'
    "$.components.schemas.ImageDownloadSchema.properties.os_distro"
    """

    os_type: Literal["linux", "windows"]
    """
    '#/components/schemas/ImageDownloadSchema/properties/os_type'
    "$.components.schemas.ImageDownloadSchema.properties.os_type"
    """

    os_version: str
    """
    '#/components/schemas/ImageDownloadSchema/properties/os_version'
    "$.components.schemas.ImageDownloadSchema.properties.os_version"
    """

    ssh_key: Literal["allow", "deny", "required"]
    """
    '#/components/schemas/ImageDownloadSchema/properties/ssh_key'
    "$.components.schemas.ImageDownloadSchema.properties.ssh_key"
    """
