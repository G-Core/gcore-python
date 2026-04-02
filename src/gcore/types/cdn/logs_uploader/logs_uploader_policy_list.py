# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel
from .logs_uploader_policy import LogsUploaderPolicy

__all__ = ["LogsUploaderPolicyList", "PaginatedList"]


class PaginatedList(BaseModel):
    count: int
    """Total number of items."""

    next: Optional[str] = None
    """URL to the next page of results. Null if current page is the last one."""

    previous: Optional[str] = None
    """URL to the previous page of results. Null if current page is the first one."""

    results: List[LogsUploaderPolicy]


LogsUploaderPolicyList: TypeAlias = Union[List[LogsUploaderPolicy], PaginatedList]
