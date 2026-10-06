# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PolicyOverrideListOwaspTopThreatsTargetsParams"]


class PolicyOverrideListOwaspTopThreatsTargetsParams(TypedDict, total=False):
    limit: int
    """Number of items to return"""

    offset: int
    """Number of items to skip"""
