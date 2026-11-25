# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

from ....._types import SequenceNotStr

__all__ = ["FlavorListParams"]


class FlavorListParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    flavor_names: SequenceNotStr[str]
    """Filter by exact flavor names."""

    limit: int
    """Max items to return."""

    offset: int
    """Items to skip."""

    order_by: Literal["flavor_name.asc", "flavor_name.desc", "region_id.asc", "region_id.desc"]
    """Sort field and direction."""

    region_ids: Iterable[int]
    """Filter by region IDs. Omit to get all regions that the client can see."""
