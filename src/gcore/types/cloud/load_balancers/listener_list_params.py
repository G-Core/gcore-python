# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ListenerListParams"]


class ListenerListParams(TypedDict, total=False):
    project_id: int

    region_id: int

    loadbalancer_id: str
    """Load balancer ID"""

    show_stats: bool
    """Show statistics"""
