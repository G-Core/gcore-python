# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FlavorListSuitableParams", "Volume"]


class FlavorListSuitableParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Favailable_flavors/post/parameters/0/schema'
    "$.paths['/cloud/v1/instances/{project_id}/{region_id}/available_flavors'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Favailable_flavors/post/parameters/1/schema'
    "$.paths['/cloud/v1/instances/{project_id}/{region_id}/available_flavors'].post.parameters[1].schema"
    """

    volumes: Required[Iterable[Volume]]
    """
    '#/components/schemas/CreateInstanceVolumeListSchema/properties/volumes'
    "$.components.schemas.CreateInstanceVolumeListSchema.properties.volumes"
    """

    include_prices: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Favailable_flavors/post/parameters/2'
    "$.paths['/cloud/v1/instances/{project_id}/{region_id}/available_flavors'].post.parameters[2]"
    """


class Volume(TypedDict, total=False):
    source: Required[Literal["apptemplate", "existing-volume", "image", "new-volume", "snapshot"]]
    """
    '#/components/schemas/CheckFlavorVolumeSchema/properties/source'
    "$.components.schemas.CheckFlavorVolumeSchema.properties.source"
    """

    apptemplate_id: str
    """
    '#/components/schemas/CheckFlavorVolumeSchema/properties/apptemplate_id'
    "$.components.schemas.CheckFlavorVolumeSchema.properties.apptemplate_id"
    """

    boot_index: int
    """
    '#/components/schemas/CheckFlavorVolumeSchema/properties/boot_index'
    "$.components.schemas.CheckFlavorVolumeSchema.properties.boot_index"
    """

    image_id: str
    """
    '#/components/schemas/CheckFlavorVolumeSchema/properties/image_id'
    "$.components.schemas.CheckFlavorVolumeSchema.properties.image_id"
    """

    name: Optional[str]
    """
    '#/components/schemas/CheckFlavorVolumeSchema/properties/name'
    "$.components.schemas.CheckFlavorVolumeSchema.properties.name"
    """

    size: int
    """
    '#/components/schemas/CheckFlavorVolumeSchema/properties/size'
    "$.components.schemas.CheckFlavorVolumeSchema.properties.size"
    """

    snapshot_id: str
    """
    '#/components/schemas/CheckFlavorVolumeSchema/properties/snapshot_id'
    "$.components.schemas.CheckFlavorVolumeSchema.properties.snapshot_id"
    """

    type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
    """
    '#/components/schemas/CheckFlavorVolumeSchema/properties/type_name'
    "$.components.schemas.CheckFlavorVolumeSchema.properties.type_name"
    """

    volume_id: str
    """
    '#/components/schemas/CheckFlavorVolumeSchema/properties/volume_id'
    "$.components.schemas.CheckFlavorVolumeSchema.properties.volume_id"
    """
