# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SSHKeyListParams"]


class SSHKeyListParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return"""

    name: str
    """Filter by name (partial match)"""

    offset: int
    """Number of items to skip"""

    order_by: str
