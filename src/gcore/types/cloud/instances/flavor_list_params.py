# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FlavorListParams"]


class FlavorListParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fflavors%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
    "$.paths['/cloud/v1/flavors/{project_id}/{region_id}'].get.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fflavors%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
    "$.paths['/cloud/v1/flavors/{project_id}/{region_id}'].get.parameters[1].schema"
    """

    disabled: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Fflavors%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
    "$.paths['/cloud/v1/flavors/{project_id}/{region_id}'].get.parameters[2]"
    """

    exclude_linux: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Fflavors%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
    "$.paths['/cloud/v1/flavors/{project_id}/{region_id}'].get.parameters[3]"
    """

    exclude_windows: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Fflavors%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
    "$.paths['/cloud/v1/flavors/{project_id}/{region_id}'].get.parameters[4]"
    """

    include_prices: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Fflavors%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
    "$.paths['/cloud/v1/flavors/{project_id}/{region_id}'].get.parameters[5]"
    """
