# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["IPReputationListParams"]


class IPReputationListParams(TypedDict, total=False):
    ip: Required[str]
    """The IP address to check"""

    limit: int
    """Number of items to return"""

    offset: int
    """Number of items to skip"""

    ordering: Literal["date", "-date", "domain_name", "-domain_name"]
    """Sort the response by given field."""
