# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TemplateListParams"]


class TemplateListParams(TypedDict, total=False):
    api_type: Literal["wasi-http", "proxy-wasm"]
    """
    API type:
    wasi-http - WASI with HTTP entry point
    proxy-wasm - Proxy-Wasm app, callable from CDN
    """

    limit: int
    """Maximum number of results to return"""

    offset: int
    """Number of results to skip for pagination"""

    only_mine: bool
    """When true, returns only templates created by the client.

    When false, includes shared templates.
    """
