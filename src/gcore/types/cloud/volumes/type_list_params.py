# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TypeListParams"]


class TypeListParams(TypedDict, total=False):
    region_id: int
    """Region ID.

    If you set it, the list shows only the types that the region supports. The
    capabilities then also include the limits of that region.
    """
