# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ..tag_update_list_param import TagUpdateListParam

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
    '#/components/schemas/UpdateImageSerializer/properties/hw_firmware_type'
    "$.components.schemas.UpdateImageSerializer.properties.hw_firmware_type"
    """

    hw_machine_type: Literal["pc", "q35"]
    """
    '#/components/schemas/UpdateImageSerializer/properties/hw_machine_type'
    "$.components.schemas.UpdateImageSerializer.properties.hw_machine_type"
    """

    is_baremetal: bool
    """
    '#/components/schemas/UpdateImageSerializer/properties/is_baremetal'
    "$.components.schemas.UpdateImageSerializer.properties.is_baremetal"
    """

    name: str
    """
    '#/components/schemas/UpdateImageSerializer/properties/name'
    "$.components.schemas.UpdateImageSerializer.properties.name"
    """

    os_type: Literal["linux", "windows"]
    """
    '#/components/schemas/UpdateImageSerializer/properties/os_type'
    "$.components.schemas.UpdateImageSerializer.properties.os_type"
    """

    ssh_key: Literal["allow", "deny", "required"]
    """
    '#/components/schemas/UpdateImageSerializer/properties/ssh_key'
    "$.components.schemas.UpdateImageSerializer.properties.ssh_key"
    """

    tags: TagUpdateListParam
    """
    '#/components/schemas/UpdateImageSerializer/properties/tags'
    "$.components.schemas.UpdateImageSerializer.properties.tags"
    """
