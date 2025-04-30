# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ImageListParams"]


class ImageListParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fbmimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
    "$.paths['/cloud/v1/bmimages/{project_id}/{region_id}'].get.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fbmimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
    "$.paths['/cloud/v1/bmimages/{project_id}/{region_id}'].get.parameters[1].schema"
    """

    include_prices: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Fbmimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
    "$.paths['/cloud/v1/bmimages/{project_id}/{region_id}'].get.parameters[2]"
    """

    private: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fbmimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
    "$.paths['/cloud/v1/bmimages/{project_id}/{region_id}'].get.parameters[3]"
    """

    tag_key: List[str]
    """
    '#/paths/%2Fcloud%2Fv1%2Fbmimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
    "$.paths['/cloud/v1/bmimages/{project_id}/{region_id}'].get.parameters[4]"
    """

    tag_key_value: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fbmimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
    "$.paths['/cloud/v1/bmimages/{project_id}/{region_id}'].get.parameters[5]"
    """

    visibility: Literal["private", "public", "shared"]
    """
    '#/paths/%2Fcloud%2Fv1%2Fbmimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
    "$.paths['/cloud/v1/bmimages/{project_id}/{region_id}'].get.parameters[6]"
    """
