# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InsightReplaceParams"]


class InsightReplaceParams(TypedDict, total=False):
    domain_id: Required[int]
    """The domain ID"""

    status: Required[Literal["OPEN", "ACKED", "CLOSED"]]
    """The status of the insight"""
