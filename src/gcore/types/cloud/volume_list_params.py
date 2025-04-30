# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["VolumeListParams"]


class VolumeListParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[1].schema"
    """

    bootable: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[2]"
    """

    cluster_id: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[3]"
    """

    has_attachments: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[4]"
    """

    id_part: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[5]"
    """

    instance_id: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[6]"
    """

    limit: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/7'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[7]"
    """

    name_part: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/8'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[8]"
    """

    offset: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/9'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[9]"
    """

    tag_key: List[str]
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/10'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[10]"
    """

    tag_key_value: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/11'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[11]"
    """
