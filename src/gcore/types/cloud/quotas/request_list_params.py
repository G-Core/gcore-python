# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RequestListParams"]


class RequestListParams(TypedDict, total=False):
    created_from: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter limit requests created at or after this datetime (inclusive)"""

    created_to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter limit requests created at or before this datetime (inclusive)"""

    limit: int
    """Optional. Limit the number of returned items"""

    offset: int
    """Optional.

    Offset value is used to exclude the first set of records from the result
    """

    request_ids: Iterable[int]
    """List of limit request IDs for filtering"""

    status: List[Literal["done", "in progress", "rejected"]]
    """List of limit requests statuses for filtering"""
