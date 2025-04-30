# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..tag_update_list_param import TagUpdateListParam

__all__ = ["ImageUploadParams"]


class ImageUploadParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages/post/parameters/0/schema'
    "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages/post/parameters/1/schema'
    "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images'].post.parameters[1].schema"
    """

    name: Required[str]
    """
    '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/name'
    "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.name"
    """

    url: Required[str]
    """
    '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/url/anyOf/0'
    "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.url.anyOf[0]"
    """

    architecture: Optional[Literal["aarch64", "x86_64"]]
    """
    '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/architecture/anyOf/0'
    "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.architecture.anyOf[0]"
    """

    cow_format: bool
    """
    '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/cow_format'
    "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.cow_format"
    """

    hw_firmware_type: Optional[Literal["bios", "uefi"]]
    """
    '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/hw_firmware_type/anyOf/0'
    "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.hw_firmware_type.anyOf[0]"
    """

    os_distro: Optional[str]
    """
    '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/os_distro/anyOf/0'
    "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.os_distro.anyOf[0]"
    """

    os_type: Optional[Literal["linux", "windows"]]
    """
    '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/os_type/anyOf/0'
    "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.os_type.anyOf[0]"
    """

    os_version: Optional[str]
    """
    '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/os_version/anyOf/0'
    "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.os_version.anyOf[0]"
    """

    ssh_key: Literal["allow", "deny", "required"]
    """
    '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/ssh_key'
    "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.ssh_key"
    """

    tags: TagUpdateListParam
    """
    '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/tags'
    "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.tags"
    """
