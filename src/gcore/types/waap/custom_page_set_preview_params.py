# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .waap_page_type import WaapPageType

__all__ = ["CustomPageSetPreviewParams"]


class CustomPageSetPreviewParams(TypedDict, total=False):
    page_type: Required[WaapPageType]
    """The type of the custom page"""

    error: Optional[str]
    """Error message"""

    header: Optional[str]
    """The text to display in the header of the custom page"""

    logo: Optional[str]
    """
    Supported image types are JPEG, PNG and JPG, size is limited to width 450px,
    height 130px. This should be a base 64 encoding of the full HTML img tag
    compatible image, with the header included.
    """

    text: Optional[str]
    """The text to display in the body of the custom page"""

    title: Optional[str]
    """The text to display in the title of the custom page"""
