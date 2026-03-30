# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AccessKeyListParams"]


class AccessKeyListParams(TypedDict, total=False):
    limit: int
    """Max number of records in response"""

    offset: int
    """Number of records to skip before beginning to return results"""

    order_by: str
