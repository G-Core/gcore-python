# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VolumeDeleteParams"]


class VolumeDeleteParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/delete/parameters/0/schema'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}']['delete'].parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/delete/parameters/1/schema'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}']['delete'].parameters[1].schema"
    """

    snapshots: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/delete/parameters/3'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}']['delete'].parameters[3]"
    """
