# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FlavorListParams"]


class FlavorListParams(TypedDict, total=False):
    limit: int
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2Fflavors/get/parameters/0'
    "$.paths['/cloud/v3/inference/flavors'].get.parameters[0]"
    """

    offset: int
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2Fflavors/get/parameters/1'
    "$.paths['/cloud/v3/inference/flavors'].get.parameters[1]"
    """
