# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RouterDetachSubnetParams"]


class RouterDetachSubnetParams(TypedDict, total=False):
    project_id: int

    region_id: int

    subnet_id: Required[str]
    """Target IP is identified by it's subnet"""
