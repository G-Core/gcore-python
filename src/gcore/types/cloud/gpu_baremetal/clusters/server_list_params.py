# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["ServerListParams"]


class ServerListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    changed_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Filters the results to include only servers whose last change timestamp is less
    than the specified datetime. Format: ISO 8601.
    """

    changed_since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Filters the results to include only servers whose last change timestamp is
    greater than or equal to the specified datetime. Format: ISO 8601.
    """

    ip_address: str
    """Filter servers by ip address."""

    limit: int
    """Limit of items on a single page"""

    name: str
    """Filter servers by name.

    You can provide a full or partial name, servers with matching names will be
    returned. For example, entering 'test' will return all servers that contain
    'test' in their name.
    """

    offset: int
    """Offset in results list"""

    order_by: Literal["created_at.asc", "created_at.desc", "status.asc", "status.desc"]
    """Order field"""

    status: Literal[
        "ACTIVE",
        "BUILD",
        "ERROR",
        "HARD_REBOOT",
        "MIGRATING",
        "PAUSED",
        "REBOOT",
        "REBUILD",
        "RESIZE",
        "REVERT_RESIZE",
        "SHELVED",
        "SHELVED_OFFLOADED",
        "SHUTOFF",
        "SOFT_DELETED",
        "SUSPENDED",
        "VERIFY_RESIZE",
    ]
    """Filters servers by status."""

    uuids: SequenceNotStr[str]
    """Filter servers by uuid."""
