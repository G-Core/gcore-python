# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IPInfoGetAccountAttackTimeSeriesParams"]


class IPInfoGetAccountAttackTimeSeriesParams(TypedDict, total=False):
    ip: Required[str]
    """The IP address to check"""

    days: int
    """Number of days to look back for attack data"""
