# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WaapCaptchaPageDataParam"]


class WaapCaptchaPageDataParam(TypedDict, total=False):
    enabled: Required[bool]
    """Indicates whether the custom custom page is active or inactive"""

    error: str
    """Error message"""

    header: str
    """The text to display in the header of the custom page"""

    logo: str
    """
    Supported image types are JPEG, PNG and JPG, size is limited to width 450px,
    height 130px. This should be a base 64 encoding of the full HTML img tag
    compatible image, with the header included.
    """

    text: str
    """The text to display in the body of the custom page"""

    title: str
    """The text to display in the title of the custom page"""
