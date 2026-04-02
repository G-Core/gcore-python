# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["ConfigListParams"]


class ConfigListParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return in the response. Cannot exceed 1000."""

    offset: int
    """Number of items to skip from the beginning of the list."""

    resource_ids: Iterable[int]
    """Filter by ids of CDN resources that are assigned to given config."""

    search: str
    """Search by config name or id."""
