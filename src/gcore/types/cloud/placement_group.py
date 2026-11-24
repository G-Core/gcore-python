# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PlacementGroup", "ManagedBy"]


class ManagedBy(BaseModel):
    """Service that operates this placement group.

    A managed group is read-only and you cannot delete it. Null when you operate the group.
    """

    type: Literal["system"]
    """Type of the managing service."""


class PlacementGroup(BaseModel):
    id: str
    """Placement group ID."""

    created_at: datetime
    """Datetime when the placement group was first seen."""

    managed_by: Optional[ManagedBy] = None
    """Service that operates this placement group.

    A managed group is read-only and you cannot delete it. Null when you operate the
    group.
    """

    member_ids: List[str]
    """
    UUIDs of the instances that are members of this placement group, sorted
    ascending.
    """

    name: str
    """Placement group name."""

    policy: Literal["affinity", "anti-affinity", "soft-affinity", "soft-anti-affinity"]
    """
    Placement policy: affinity, anti-affinity, soft-affinity, or soft-anti-affinity.
    """

    region_id: int
    """Region ID."""

    updated_at: datetime
    """Datetime when the placement group last changed."""
