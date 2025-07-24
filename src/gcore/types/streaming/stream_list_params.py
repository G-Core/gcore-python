# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["StreamListParams"]


class StreamListParams(TypedDict, total=False):
    page: int
    """Query parameter. Use it to list the paginated content"""

    with_broadcasts: int
    """Query parameter.

    Set to 1 to get details of the broadcasts associated with the stream
    """
