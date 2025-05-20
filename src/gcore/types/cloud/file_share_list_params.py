# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FileShareListParams"]


class FileShareListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    limit: int
    """Optional. Limit the number of returned items"""

    name: str
    """File share name. Uses partial match."""

    offset: int
    """Optional.

    Offset value is used to exclude the first set of records from the result
    """

    type_name: Literal["standard", "vast"]
    """File share type name"""
