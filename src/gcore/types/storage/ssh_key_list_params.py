# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SSHKeyListParams"]


class SSHKeyListParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return"""

    name: str
    """Filter by name (partial match)"""

    offset: int
    """Number of items to skip"""

    order_by: str

    accept_language: Annotated[str, PropertyInfo(alias="Accept-Language")]
