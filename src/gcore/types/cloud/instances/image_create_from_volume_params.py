# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImageCreateFromVolumeParams"]


class ImageCreateFromVolumeParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/images/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/images/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    name: Required[str]
    """
    '#/components/schemas/ImageCreateSchema/properties/name'
    "$.components.schemas.ImageCreateSchema.properties.name"
    """

    volume_id: Required[str]
    """
    '#/components/schemas/ImageCreateSchema/properties/volume_id'
    "$.components.schemas.ImageCreateSchema.properties.volume_id"
    """

    architecture: Literal["aarch64", "x86_64"]
    """
    '#/components/schemas/ImageCreateSchema/properties/architecture'
    "$.components.schemas.ImageCreateSchema.properties.architecture"
    """

    hw_firmware_type: Literal["bios", "uefi"]
    """
    '#/components/schemas/ImageCreateSchema/properties/hw_firmware_type'
    "$.components.schemas.ImageCreateSchema.properties.hw_firmware_type"
    """

    hw_machine_type: Literal["i440", "q35"]
    """
    '#/components/schemas/ImageCreateSchema/properties/hw_machine_type'
    "$.components.schemas.ImageCreateSchema.properties.hw_machine_type"
    """

    is_baremetal: Optional[bool]
    """
    '#/components/schemas/ImageCreateSchema/properties/is_baremetal'
    "$.components.schemas.ImageCreateSchema.properties.is_baremetal"
    """

    metadata: object
    """
    '#/components/schemas/ImageCreateSchema/properties/metadata'
    "$.components.schemas.ImageCreateSchema.properties.metadata"
    """

    os_type: Literal["linux", "windows"]
    """
    '#/components/schemas/ImageCreateSchema/properties/os_type'
    "$.components.schemas.ImageCreateSchema.properties.os_type"
    """

    source: str
    """
    '#/components/schemas/ImageCreateSchema/properties/source'
    "$.components.schemas.ImageCreateSchema.properties.source"
    """

    ssh_key: Literal["allow", "deny", "required"]
    """
    '#/components/schemas/ImageCreateSchema/properties/ssh_key'
    "$.components.schemas.ImageCreateSchema.properties.ssh_key"
    """
