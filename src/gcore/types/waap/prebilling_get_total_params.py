# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PrebillingGetTotalParams"]


class PrebillingGetTotalParams(TypedDict, total=False):
    from_: Required[Annotated[Union[str, date], PropertyInfo(alias="from", format="iso8601")]]
    """The report start date (inclusive) in ISO 8601 format"""

    to: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The report end date (exclusive) in ISO 8601 format"""

    limit: int
    """Number of items to return"""

    offset: int
    """Number of items to skip"""
