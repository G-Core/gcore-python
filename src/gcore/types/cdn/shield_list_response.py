# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ShieldListResponse", "PlainList", "PaginatedList", "PaginatedListResult"]


class PlainList(BaseModel):
    id: Optional[int] = None
    """Origin shielding location ID."""

    city: Optional[str] = None
    """City of origin shielding location."""

    country: Optional[str] = None
    """Country of origin shielding location."""

    datacenter: Optional[str] = None
    """Name of origin shielding location datacenter."""


class PaginatedListResult(BaseModel):
    id: Optional[int] = None
    """Origin shielding location ID."""

    city: Optional[str] = None
    """City of origin shielding location."""

    country: Optional[str] = None
    """Country of origin shielding location."""

    datacenter: Optional[str] = None
    """Name of origin shielding location datacenter."""


class PaginatedList(BaseModel):
    count: int
    """Total number of items."""

    next: Optional[str] = None
    """URL to the next page of results. Null if current page is the last one."""

    previous: Optional[str] = None
    """URL to the previous page of results. Null if current page is the first one."""

    results: List[PaginatedListResult]


ShieldListResponse: TypeAlias = Union[List[PlainList], PaginatedList]
