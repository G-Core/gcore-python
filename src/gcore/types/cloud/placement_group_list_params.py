# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["PlacementGroupListParams", "Name"]


class PlacementGroupListParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    ids: SequenceNotStr[str]
    """Filter by one or more placement group IDs (exact match)."""

    limit: int
    """Maximum number of items to return."""

    managed: bool
    """Filter placement groups that a service operates (true) or not (false)."""

    managed_by: Literal["system"]
    """Filter by the type of the managing service."""

    member_ids: SequenceNotStr[str]
    """Filter to placement groups containing any of these instance UUIDs."""

    name: Name
    """Operator-based name filter, e.g.

    `name[contains]=web`, `name[prefix]=prod-`. Case-insensitive.
    """

    offset: int
    """Number of items to skip from the start of the result."""

    order_by: Literal[
        "created_at.asc",
        "created_at.desc",
        "name.asc",
        "name.desc",
        "region_id.asc",
        "region_id.desc",
        "updated_at.asc",
        "updated_at.desc",
    ]
    """Sort field and direction."""

    policies: List[Literal["affinity", "anti-affinity", "soft-affinity", "soft-anti-affinity"]]
    """Filter by one or more placement policies."""

    region_ids: Iterable[int]
    """Filter by one or more region IDs. Omit to list across all regions."""


class Name(TypedDict, total=False):
    """Operator-based name filter, e.g.

    `name[contains]=web`, `name[prefix]=prod-`. Case-insensitive.
    """

    contains: SequenceNotStr[str]
    """Case-insensitive substring, e.g.

    `[contains]=web`. Repeat the key to match any substring.
    """

    exact: SequenceNotStr[str]
    """Case-insensitive exact match, e.g.

    `[exact]=web-1`. Repeat the key to match any of several.
    """

    prefix: SequenceNotStr[str]
    """Case-insensitive starts-with, e.g.

    `[prefix]=prod-`. Repeat the key to match any prefix.
    """

    suffix: SequenceNotStr[str]
    """Case-insensitive ends-with, e.g.

    `[suffix]=-db`. Repeat the key to match any suffix.
    """
