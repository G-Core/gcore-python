# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .logs_uploader_target import LogsUploaderTarget

__all__ = ["LogsUploaderTargetList"]


class LogsUploaderTargetList(BaseModel):
    count: int
    """Total number of items."""

    next: Optional[str] = None
    """URL to the next page of results. Null if current page is the last one."""

    previous: Optional[str] = None
    """URL to the previous page of results. Null if current page is the first one."""

    results: List[LogsUploaderTarget]
