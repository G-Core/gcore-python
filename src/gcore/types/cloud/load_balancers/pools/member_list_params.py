# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MemberListParams"]


class MemberListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    limit: int
    """Optional. Limit the number of returned items"""

    offset: int
    """Optional.

    Offset value is used to exclude the first set of records from the result
    """

    order_by: Literal["address.asc", "address.desc", "created_at.asc", "created_at.desc"]
    """
    Ordering pool members list result by `address` or `created_at` fields and
    directions (e.g. `address.desc`). Default is `address.asc`.
    """
