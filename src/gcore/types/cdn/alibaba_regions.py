# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["AlibabaRegions", "PlainList", "PaginatedList", "PaginatedListResult"]


class PlainList(BaseModel):
    id: Optional[int] = None
    """Region ID."""

    code: Optional[str] = None
    """Region code."""

    name: Optional[str] = None
    """Region name."""


class PaginatedListResult(BaseModel):
    id: Optional[int] = None
    """Region ID."""

    code: Optional[str] = None
    """Region code."""

    name: Optional[str] = None
    """Region name."""


class PaginatedList(BaseModel):
    count: int
    """Total number of items."""

    next: Optional[str] = None
    """URL to the next page of results. Null if current page is the last one."""

    previous: Optional[str] = None
    """URL to the previous page of results. Null if current page is the first one."""

    results: List[PaginatedListResult]


AlibabaRegions: TypeAlias = Union[List[PlainList], PaginatedList]
