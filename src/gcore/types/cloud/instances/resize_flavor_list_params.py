# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ResizeFlavorListParams"]


class ResizeFlavorListParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    limit: int
    """Max items to return."""

    offset: int
    """Items to skip."""

    order_by: Literal["name.asc", "name.desc", "ram_mib.asc", "ram_mib.desc", "vcpus.asc", "vcpus.desc"]
    """Sort field and direction."""
