# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["RequestListParams"]


class RequestListParams(TypedDict, total=False):
    limit: int
    """
    '#/paths/%2Fcloud%2Fv2%2Flimits_request/get/parameters/0'
    "$.paths['/cloud/v2/limits_request'].get.parameters[0]"
    """

    offset: int
    """
    '#/paths/%2Fcloud%2Fv2%2Flimits_request/get/parameters/1'
    "$.paths['/cloud/v2/limits_request'].get.parameters[1]"
    """

    status: Optional[List[Literal["done", "in progress", "rejected"]]]
    """
    '#/paths/%2Fcloud%2Fv2%2Flimits_request/get/parameters/2/schema/anyOf/0'
    "$.paths['/cloud/v2/limits_request'].get.parameters[2].schema.anyOf[0]"
    """
