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
    """Filter by binary ID (shows apps using this binary)"""

    limit: int
    """Maximum number of results to return"""

    name: str
    """Filter by application name (case-insensitive partial match)"""

    offset: int
    """Number of results to skip for pagination"""

    ordering: Literal[
        "name", "-name", "status", "-status", "id", "-id", "template", "-template", "binary", "-binary", "plan", "-plan"
    ]
    """Sort order. Use - prefix for descending (e.g., -name sorts by name descending)"""

    plan: int
    """Filter by plan ID"""

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
    """Filter by template ID (shows apps created from this template)"""
