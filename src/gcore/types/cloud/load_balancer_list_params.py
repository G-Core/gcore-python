# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["LoadBalancerListParams"]


class LoadBalancerListParams(TypedDict, total=False):
    project_id: int

    region_id: int

    assigned_floating: bool
    """With or without assigned floating IP"""

    limit: int
    """Limit the number of returned limit request entities."""

    logging_enabled: bool
    """With or without logging"""

    name: str
    """Filter by name"""

    offset: int
    """Offset value is used to exclude the first set of records from the result."""

    order_by: str
    """
    Ordering Load Balancer list result by name, `created_at`, `updated_at`,
    `operating_status`, `provisioning_status`, `vip_address`, `vip_ip_family` and
    flavor fields of the load balancer and directions (name.asc), default is
    "`created_at`.asc"
    """

    show_stats: bool
    """Show statistics"""

    tag_key: List[str]
    """Filter by tag keys."""

    tag_key_value: str
    """Filter by tag key-value pairs. Must be a valid JSON string."""

    with_ddos: bool
    """Show Advanced DDoS protection profile, if exists"""
