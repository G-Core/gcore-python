# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LoadBalancerFailoverParams"]


class LoadBalancerFailoverParams(TypedDict, total=False):
    project_id: int

    region_id: int

    force: bool
    """Validate current load balancer status before failover or not."""
