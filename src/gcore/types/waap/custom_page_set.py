# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .block_page_data import BlockPageData
from .captcha_page_data import CaptchaPageData
from .handshake_page_data import HandshakePageData
from .block_csrf_page_data import BlockCsrfPageData
from .cookie_disabled_page_data import CookieDisabledPageData
from .javascript_disabled_page_data import JavascriptDisabledPageData

__all__ = ["CustomPageSet"]


class CustomPageSet(BaseModel):
    id: int
    """The ID of the custom page set"""

    name: str
    """Name of the custom page set"""

    block: Optional[BlockPageData] = None

    block_csrf: Optional[BlockCsrfPageData] = None

    captcha: Optional[CaptchaPageData] = None

    cookie_disabled: Optional[CookieDisabledPageData] = None

    domains: Optional[List[int]] = None
    """List of domain IDs that are associated with this page set"""

    handshake: Optional[HandshakePageData] = None

    javascript_disabled: Optional[JavascriptDisabledPageData] = None
