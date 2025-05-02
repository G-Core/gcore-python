# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RegistryResizeParams"]


class RegistryResizeParams(TypedDict, total=False):
    project_id: int

    region_id: int

    storage_limit: int
    """Registry storage limit, GiB"""
