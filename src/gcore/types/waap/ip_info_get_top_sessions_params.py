# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IPInfoGetTopSessionsParams"]


class IPInfoGetTopSessionsParams(TypedDict, total=False):
    domain_id: Required[int]
    """The domain ID"""

    ip: Required[str]
    """The IP address to check"""
