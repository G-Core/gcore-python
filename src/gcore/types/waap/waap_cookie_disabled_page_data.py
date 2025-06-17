# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["WaapCookieDisabledPageData"]


class WaapCookieDisabledPageData(BaseModel):
    enabled: bool
    """Indicates whether the custom custom page is active or inactive"""

    header: Optional[str] = None
    """The text to display in the header of the custom page"""

    text: Optional[str] = None
    """The text to display in the body of the custom page"""
