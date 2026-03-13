# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ServerDeleteParams"]


class ServerDeleteParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    all_floating_ips: bool
    """True if it is required to delete floating IPs assigned to the instance.

    Can't be used with `floating_ip_ids`.
    """

    floating_ip_ids: str
    """Comma separated list of floating ids that should be deleted.

    Can't be used with `all_floating_ips`.
    """

    reserved_fixed_ip_ids: str
    """Comma separated list of port IDs to be deleted with the instance"""
