# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ImageUpdateParams"]


class ImageUpdateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/patch/parameters/0/schema'
    "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}'].patch.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/patch/parameters/1/schema'
    "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}'].patch.parameters[1].schema"
    """

    hw_firmware_type: Literal["bios", "uefi"]
    """
    '#/components/schemas/UpdateImageSchema/properties/hw_firmware_type'
    "$.components.schemas.UpdateImageSchema.properties.hw_firmware_type"
    """

    hw_machine_type: Literal["i440", "q35"]
    """
    '#/components/schemas/UpdateImageSchema/properties/hw_machine_type'
    "$.components.schemas.UpdateImageSchema.properties.hw_machine_type"
    """

    is_baremetal: Optional[bool]
    """
    '#/components/schemas/UpdateImageSchema/properties/is_baremetal'
    "$.components.schemas.UpdateImageSchema.properties.is_baremetal"
    """

    metadata: object
    """
    '#/components/schemas/UpdateImageSchema/properties/metadata'
    "$.components.schemas.UpdateImageSchema.properties.metadata"
    """

    name: str
    """
    '#/components/schemas/UpdateImageSchema/properties/name'
    "$.components.schemas.UpdateImageSchema.properties.name"
    """

    os_type: Literal["linux", "windows"]
    """
    '#/components/schemas/UpdateImageSchema/properties/os_type'
    "$.components.schemas.UpdateImageSchema.properties.os_type"
    """

    ssh_key: Literal["allow", "deny", "required"]
    """
    '#/components/schemas/UpdateImageSchema/properties/ssh_key'
    "$.components.schemas.UpdateImageSchema.properties.ssh_key"
    """
