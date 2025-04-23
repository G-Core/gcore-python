# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VolumeUpdateParams"]


class VolumeUpdateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/patch/parameters/0/schema'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}'].patch.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/patch/parameters/1/schema'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}'].patch.parameters[1].schema"
    """

    name: Required[str]
    """
    '#/components/schemas/NameSerializer/properties/name'
    "$.components.schemas.NameSerializer.properties.name"
    """
