# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AppListParams"]


class AppListParams(TypedDict, total=False):
    api_type: Literal["wasi-http", "proxy-wasm"]
    """
    API type:
    wasi-http - WASI with HTTP entry point
    proxy-wasm - Proxy-Wasm app, callable from CDN
    """

    binary: int
    """Binary ID"""

    limit: int
    """Limit for pagination"""

    name: str
    """Name of the app"""

    offset: int
    """Offset for pagination"""

    ordering: Literal[
        "name", "-name", "status", "-status", "id", "-id", "template", "-template", "binary", "-binary", "plan", "-plan"
    ]
    """Ordering"""

    plan: int
    """Plan ID"""

    status: int
    """
    Status code:
    0 - draft (inactive)
    1 - enabled
    2 - disabled
    3 - hourly call limit exceeded
    4 - daily call limit exceeded
    5 - suspended
    """

    template: int
    """Template ID"""
