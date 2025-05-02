# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VipToggleParams"]


class VipToggleParams(TypedDict, total=False):
    project_id: int

    region_id: int

    is_vip: Required[bool]
    """If reserved fixed IP should be a VIP"""
