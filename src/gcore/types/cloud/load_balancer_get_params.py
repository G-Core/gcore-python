# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LoadBalancerGetParams"]


class LoadBalancerGetParams(TypedDict, total=False):
    project_id: int

    region_id: int

    show_stats: bool
    """Show statistics"""

    with_ddos: bool
    """Show DDoS profile"""
