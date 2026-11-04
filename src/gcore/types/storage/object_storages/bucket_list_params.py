# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["BucketListParams"]


class BucketListParams(TypedDict, total=False):
    limit: int
    """Max number of records in response"""

    offset: int
    """Number of records to skip before beginning to return results"""

    accept_language: Annotated[str, PropertyInfo(alias="Accept-Language")]
