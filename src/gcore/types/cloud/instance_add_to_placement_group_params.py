# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InstanceAddToPlacementGroupParams"]


class InstanceAddToPlacementGroupParams(TypedDict, total=False):
    project_id: int

    region_id: int

    servergroup_id: Required[str]
    """Anti-affinity or affinity or soft-anti-affinity server group ID."""
