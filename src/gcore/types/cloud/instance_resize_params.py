# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InstanceResizeParams"]


class InstanceResizeParams(TypedDict, total=False):
    project_id: int

    region_id: int

    flavor_id: Required[str]
    """Flavor ID"""
