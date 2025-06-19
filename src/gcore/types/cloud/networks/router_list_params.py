# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RouterListParams"]


class RouterListParams(TypedDict, total=False):
    project_id: int

    region_id: int

    limit: int
    """Limit the number of returned routers"""

    offset: int
    """Offset value is used to exclude the first set of records from the result"""
