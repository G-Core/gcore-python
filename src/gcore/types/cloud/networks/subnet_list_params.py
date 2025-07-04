# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["SubnetListParams"]


class SubnetListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    limit: int
    """Optional. Limit the number of returned items"""

    network_id: str
    """Only list subnets of this network"""

    offset: int
    """Optional.

    Offset value is used to exclude the first set of records from the result
    """

    order_by: Literal[
        "available_ips.asc",
        "available_ips.desc",
        "cidr.asc",
        "cidr.desc",
        "created_at.asc",
        "created_at.desc",
        "name.asc",
        "name.desc",
        "total_ips.asc",
        "total_ips.desc",
        "updated_at.asc",
        "updated_at.desc",
    ]
    """
    Ordering subnets list result by `name`, `created_at`, `updated_at`,
    `available_ips`, `total_ips`, and `cidr` (default) fields of the subnet and
    directions (`name.asc`).
    """

    tag_key: List[str]
    """Optional. Filter by tag keys. ?`tag_key`=key1&`tag_key`=key2"""

    tag_key_value: str
    """Optional. Filter by tag key-value pairs."""
