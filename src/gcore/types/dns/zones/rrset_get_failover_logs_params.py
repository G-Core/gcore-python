# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RrsetGetFailoverLogsParams"]


class RrsetGetFailoverLogsParams(TypedDict, total=False):
    zone_name: Required[Annotated[str, PropertyInfo(alias="zoneName")]]

    rrset_name: Required[Annotated[str, PropertyInfo(alias="rrsetName")]]

    limit: int
    """Max number of records in response"""

    offset: int
    """Amount of records to skip before beginning to write in response."""
