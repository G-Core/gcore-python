# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ReservedFixedIPListParams"]


class ReservedFixedIPListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    available_only: bool
    """
    Set True if response should only list IP addresses that are not attached to any
    instance
    """

    device_id: str
    """Filter IPs by device ID it is attached to"""

    external_only: bool
    """Set to true if the response should only list public IP addresses"""

    internal_only: bool
    """Set to true if the response should only list private IP addresses"""

    ip_address: str
    """Optional. An IPv4 address to filter results by. Regular expression allowed"""

    limit: int
    """Optional. Limit the number of returned items"""

    offset: int
    """Optional.

    Offset value is used to exclude the first set of records from the result
    """

    order_by: Literal[
        "created_at.asc",
        "created_at.desc",
        "fixed_ip_address.asc",
        "fixed_ip_address.desc",
        "name.asc",
        "name.desc",
        "status.asc",
        "status.desc",
        "updated_at.asc",
        "updated_at.desc",
    ]
    """Optional.

    Ordering reserved fixed IP list result by name, status, `updated_at`,
    `fixed_ip_address` or `created_at` fields of the reserved fixed IP and
    directions (status.asc).
    """

    vip_only: bool
    """Set to true if the response should only list VIPs"""
