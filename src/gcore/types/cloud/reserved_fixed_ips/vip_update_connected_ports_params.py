# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["VipUpdateConnectedPortsParams"]


class VipUpdateConnectedPortsParams(TypedDict, total=False):
    project_id: int

    region_id: int

    port_ids: List[str]
    """List of port IDs that will share one VIP"""
