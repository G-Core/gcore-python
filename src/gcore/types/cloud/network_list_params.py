# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["NetworkListParams"]


class NetworkListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    external: bool
    """Filter by external network status"""

    limit: int
    """Optional. Limit the number of returned items"""

    name: str
    """Filter networks by name"""

    network_type: Literal["vlan", "vxlan"]
    """Filter by network type (vlan or vxlan)"""

    offset: int
    """Optional.

    Offset value is used to exclude the first set of records from the result
    """

    order_by: Literal["created_at.asc", "created_at.desc", "name.asc", "name.desc", "priority.desc"]
    """
    Ordering networks list result by `name`, `created_at` or `priority` fields and
    directions (e.g. `created_at.desc`). Default is `created_at.desc`. Use
    `priority.desc` to sort by shared network priority (relevant when
    `owned_by=any`).
    """

    owned_by: Literal["any", "project"]
    """Controls which networks are returned.

    'project' (default) returns only networks owned by the project. 'any' returns
    all networks that the project can use, including shared networks from other
    projects.
    """

    tag_key: SequenceNotStr[str]
    """Optional. Filter by tag keys. ?`tag_key`=key1&`tag_key`=key2"""

    tag_key_value: str
    """Optional. Filter by tag key-value pairs."""
