# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["TargetListParams"]


class TargetListParams(TypedDict, total=False):
    config_ids: Iterable[int]
    """Filter by ids of related logs uploader configs that use given target."""

    search: str
    """Search by target name or id."""
