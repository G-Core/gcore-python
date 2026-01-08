# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["LoadBalancerListParams"]


class LoadBalancerListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    assigned_floating: bool
    """With or without assigned floating IP"""

    limit: int
    """Limit of items on a single page"""

    logging_enabled: bool
    """With or without logging enabled"""

    name: str
    """Filter by name"""

    offset: int
    """Offset in results list"""

    order_by: Literal[
        "created_at.asc",
        "created_at.desc",
        "flavor.asc",
        "flavor.desc",
        "name.asc",
        "name.desc",
        "operating_status.asc",
        "operating_status.desc",
        "provisioning_status.asc",
        "provisioning_status.desc",
        "updated_at.asc",
        "updated_at.desc",
        "vip_address.asc",
        "vip_address.desc",
        "vip_ip_family.asc",
        "vip_ip_family.desc",
    ]
    """Order by field and direction."""

    show_stats: bool
    """Show statistics"""

    tag_key: SequenceNotStr[str]
    """Optional. Filter by tag keys. ?`tag_key`=key1&`tag_key`=key2"""

    tag_key_value: str
    """Optional. Filter by tag key-value pairs."""

    with_ddos: bool
    """Show Advanced DDoS protection profile, if exists"""
