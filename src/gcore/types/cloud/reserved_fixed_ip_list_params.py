# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ReservedFixedIPListParams"]


class ReservedFixedIPListParams(TypedDict, total=False):
    project_id: int

    region_id: int

    available_only: bool
    """
    Set to true if the response should only list IP addresses that are not attached
    to any instance
    """

    device_id: str
    """Filter IPs by device ID it is attached to"""

    external_only: bool
    """Set to true if the response should only list public IP addresses"""

    internal_only: bool
    """Set to true if the response should only list private IP addresses"""

    ip_address: str
    """An IPv4 address to filter results by. Regular expression allowed"""

    limit: int
    """Limit the number of returned IPs"""

    offset: int
    """Offset value is used to exclude the first set of records from the result"""

    order_by: str
    """
    Ordering reserved fixed IP list result by name, status, `updated_at`,
    `created_at` or `fixed_ip_address` fields and directions (status.asc), default
    is "`fixed_ip_address`.asc"
    """

    vip_only: bool
    """Set to true if the response should only list VIPs"""
