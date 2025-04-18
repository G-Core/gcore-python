# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RegionListParams"]


class RegionListParams(TypedDict, total=False):
    limit: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fregions/get/parameters/0'
    "$.paths['/cloud/v1/regions'].get.parameters[0]"
    """

    offset: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fregions/get/parameters/1'
    "$.paths['/cloud/v1/regions'].get.parameters[1]"
    """

    order_by: Literal["created_at.asc", "created_at.desc", "display_name.asc", "display_name.desc"]
    """
    '#/paths/%2Fcloud%2Fv1%2Fregions/get/parameters/2'
    "$.paths['/cloud/v1/regions'].get.parameters[2]"
    """

    product: Literal["containers", "inference"]
    """
    '#/paths/%2Fcloud%2Fv1%2Fregions/get/parameters/3'
    "$.paths['/cloud/v1/regions'].get.parameters[3]"
    """

    show_volume_types: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Fregions/get/parameters/4'
    "$.paths['/cloud/v1/regions'].get.parameters[4]"
    """
