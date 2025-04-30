# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["FloatingIPListParams"]


class FloatingIPListParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Ffloatingips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
    "$.paths['/cloud/v1/floatingips/{project_id}/{region_id}'].get.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Ffloatingips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
    "$.paths['/cloud/v1/floatingips/{project_id}/{region_id}'].get.parameters[1].schema"
    """

    limit: int
    """
    '#/paths/%2Fcloud%2Fv1%2Ffloatingips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
    "$.paths['/cloud/v1/floatingips/{project_id}/{region_id}'].get.parameters[2]"
    """

    offset: int
    """
    '#/paths/%2Fcloud%2Fv1%2Ffloatingips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
    "$.paths['/cloud/v1/floatingips/{project_id}/{region_id}'].get.parameters[3]"
    """

    tag_key: List[str]
    """
    '#/paths/%2Fcloud%2Fv1%2Ffloatingips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
    "$.paths['/cloud/v1/floatingips/{project_id}/{region_id}'].get.parameters[4]"
    """

    tag_key_value: str
    """
    '#/paths/%2Fcloud%2Fv1%2Ffloatingips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
    "$.paths['/cloud/v1/floatingips/{project_id}/{region_id}'].get.parameters[5]"
    """
