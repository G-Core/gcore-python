# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FlavorListForResizeParams"]


class FlavorListForResizeParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Favailable_flavors/get/parameters/0/schema'
    "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/available_flavors'].get.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Favailable_flavors/get/parameters/1/schema'
    "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/available_flavors'].get.parameters[1].schema"
    """

    include_prices: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Favailable_flavors/get/parameters/3'
    "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/available_flavors'].get.parameters[3]"
    """
