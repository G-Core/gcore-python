# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ZoneListParams"]


class ZoneListParams(TypedDict, total=False):
    id: Iterable[int]
    """to pass several ids `id=1&id=3&id=5...`"""

    case_sensitive: bool

    client_id: Iterable[int]
    """to pass several `client_ids` `client_id=1&client_id=3&client_id=5...`"""

    dynamic: bool
    """Zones with dynamic RRsets"""

    enabled: bool

    exact_match: bool

    healthcheck: bool
    """Zones with RRsets that have healthchecks"""

    iam_reseller_id: Iterable[int]

    limit: int
    """Max number of records in response"""

    name: SequenceNotStr[str]
    """to pass several names `name=first&name=second...`"""

    offset: int
    """Amount of records to skip before beginning to write in response."""

    order_by: str
    """Field name to sort by"""

    order_direction: Literal["asc", "desc"]
    """Ascending or descending order"""

    reseller_id: Iterable[int]

    status: str

    updated_at_from: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    updated_at_to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
