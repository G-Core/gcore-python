# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
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
    '#/components/schemas/ImageCreateFromVolumeSerializer/properties/name'
    "$.components.schemas.ImageCreateFromVolumeSerializer.properties.name"
    """

    volume_id: Required[str]
    """
    '#/components/schemas/ImageCreateFromVolumeSerializer/properties/volume_id'
    "$.components.schemas.ImageCreateFromVolumeSerializer.properties.volume_id"
    """

    architecture: Literal["aarch64", "x86_64"]
    """
    '#/components/schemas/ImageCreateFromVolumeSerializer/properties/architecture'
    "$.components.schemas.ImageCreateFromVolumeSerializer.properties.architecture"
    """

    hw_firmware_type: Optional[Literal["bios", "uefi"]]
    """
    '#/components/schemas/ImageCreateFromVolumeSerializer/properties/hw_firmware_type/anyOf/0'
    "$.components.schemas.ImageCreateFromVolumeSerializer.properties.hw_firmware_type.anyOf[0]"
    """

    hw_machine_type: Optional[Literal["pc", "q35"]]
    """
    '#/components/schemas/ImageCreateFromVolumeSerializer/properties/hw_machine_type/anyOf/0'
    "$.components.schemas.ImageCreateFromVolumeSerializer.properties.hw_machine_type.anyOf[0]"
    """

    is_baremetal: bool
    """
    '#/components/schemas/ImageCreateFromVolumeSerializer/properties/is_baremetal'
    "$.components.schemas.ImageCreateFromVolumeSerializer.properties.is_baremetal"
    """

    os_type: Literal["linux", "windows"]
    """
    '#/components/schemas/ImageCreateFromVolumeSerializer/properties/os_type'
    "$.components.schemas.ImageCreateFromVolumeSerializer.properties.os_type"
    """

    source: Literal["volume"]
    """
    '#/components/schemas/ImageCreateFromVolumeSerializer/properties/source'
    "$.components.schemas.ImageCreateFromVolumeSerializer.properties.source"
    """

    ssh_key: Literal["allow", "deny", "required"]
    """
    '#/components/schemas/ImageCreateFromVolumeSerializer/properties/ssh_key'
    "$.components.schemas.ImageCreateFromVolumeSerializer.properties.ssh_key"
    """

    tags: Dict[str, str]
    """
    '#/components/schemas/ImageCreateFromVolumeSerializer/properties/tags'
    "$.components.schemas.ImageCreateFromVolumeSerializer.properties.tags"
    """
