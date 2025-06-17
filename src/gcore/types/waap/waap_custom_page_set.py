# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .waap_block_page_data import WaapBlockPageData
from .waap_captcha_page_data import WaapCaptchaPageData
from .waap_handshake_page_data import WaapHandshakePageData
from .waap_block_csrf_page_data import WaapBlockCsrfPageData
from .waap_cookie_disabled_page_data import WaapCookieDisabledPageData
from .waap_javascript_disabled_page_data import WaapJavascriptDisabledPageData

__all__ = ["WaapCustomPageSet"]


class WaapCustomPageSet(BaseModel):
    id: int
    """The ID of the custom page set"""

    name: str
    """Name of the custom page set"""

    block: Optional[WaapBlockPageData] = None

    block_csrf: Optional[WaapBlockCsrfPageData] = None

    captcha: Optional[WaapCaptchaPageData] = None

    cookie_disabled: Optional[WaapCookieDisabledPageData] = None

    domains: Optional[List[int]] = None
    """List of domain IDs that are associated with this page set"""

    handshake: Optional[WaapHandshakePageData] = None

    javascript_disabled: Optional[WaapJavascriptDisabledPageData] = None
