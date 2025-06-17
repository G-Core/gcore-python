# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WaapJavascriptDisabledPageDataParam"]


class WaapJavascriptDisabledPageDataParam(TypedDict, total=False):
    enabled: Required[bool]
    """Indicates whether the custom custom page is active or inactive"""

    header: str
    """The text to display in the header of the custom page"""

    text: str
    """The text to display in the body of the custom page"""
