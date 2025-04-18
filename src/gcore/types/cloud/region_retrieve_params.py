# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RegionRetrieveParams"]


class RegionRetrieveParams(TypedDict, total=False):
    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fregions%2F%7Bregion_id%7D/get/parameters/0/schema'
    "$.paths['/cloud/v1/regions/{region_id}'].get.parameters[0].schema"
    """

    show_volume_types: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Fregions%2F%7Bregion_id%7D/get/parameters/1'
    "$.paths['/cloud/v1/regions/{region_id}'].get.parameters[1]"
    """
