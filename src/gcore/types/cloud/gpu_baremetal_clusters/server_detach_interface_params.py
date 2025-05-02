# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ServerDetachInterfaceParams"]


class ServerDetachInterfaceParams(TypedDict, total=False):
    project_id: int

    region_id: int

    ip_address: Required[str]
    """IP address"""

    port_id: Required[str]
    """ID of the port"""
