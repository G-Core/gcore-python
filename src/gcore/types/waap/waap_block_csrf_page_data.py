# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["WaapBlockCsrfPageData"]


class WaapBlockCsrfPageData(BaseModel):
    enabled: bool
    """Indicates whether the custom custom page is active or inactive"""

    header: Optional[str] = None
    """The text to display in the header of the custom page"""

    logo: Optional[str] = None
    """
    Supported image types are JPEG, PNG and JPG, size is limited to width 450px,
    height 130px. This should be a base 64 encoding of the full HTML img tag
    compatible image, with the header included.
    """

    text: Optional[str] = None
    """The text to display in the body of the custom page"""

    title: Optional[str] = None
    """The text to display in the title of the custom page"""
