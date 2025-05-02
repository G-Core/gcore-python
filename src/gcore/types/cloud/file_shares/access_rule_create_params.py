# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccessRuleCreateParams"]


class AccessRuleCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    access_mode: Required[Literal["ro", "rw"]]
    """Access mode"""

    ip_address: Required[str]
    """Source IP or network"""
