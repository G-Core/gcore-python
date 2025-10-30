# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["IPRangeListIPsParams"]


class IPRangeListIPsParams(TypedDict, total=False):
    format: Literal["json", "plain"]
    """
    Optional format override. When set, this takes precedence over the `Accept`
    header.
    """

    accept: Annotated[Literal["application/json", "text/plain"], PropertyInfo(alias="Accept")]
