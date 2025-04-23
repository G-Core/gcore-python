# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VolumeChangeTypeParams"]


class VolumeChangeTypeParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fretype/post/parameters/0/schema'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/retype'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fretype/post/parameters/1/schema'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/retype'].post.parameters[1].schema"
    """

    volume_type: Required[Literal["ssd_hiiops", "standard"]]
    """
    '#/components/schemas/VolumeRetypeSerializer/properties/volume_type'
    "$.components.schemas.VolumeRetypeSerializer.properties.volume_type"
    """
