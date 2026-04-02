# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .origin_groups import OriginGroups

__all__ = ["OriginGroupsList", "PaginatedList"]


class PaginatedList(BaseModel):
    count: int
    """Total number of items."""

    next: Optional[str] = None
    """URL to the next page of results. Null if current page is the last one."""

    previous: Optional[str] = None
    """URL to the previous page of results. Null if current page is the first one."""

    results: List[OriginGroups]


OriginGroupsList: TypeAlias = Union[List[OriginGroups], PaginatedList]
