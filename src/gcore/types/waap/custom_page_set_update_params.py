# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .waap_block_page_data_param import WaapBlockPageDataParam
from .waap_captcha_page_data_param import WaapCaptchaPageDataParam
from .waap_handshake_page_data_param import WaapHandshakePageDataParam
from .waap_block_csrf_page_data_param import WaapBlockCsrfPageDataParam
from .waap_cookie_disabled_page_data_param import WaapCookieDisabledPageDataParam
from .waap_javascript_disabled_page_data_param import WaapJavascriptDisabledPageDataParam

__all__ = ["CustomPageSetUpdateParams"]


class CustomPageSetUpdateParams(TypedDict, total=False):
    block: Optional[WaapBlockPageDataParam]

    block_csrf: Optional[WaapBlockCsrfPageDataParam]

    captcha: Optional[WaapCaptchaPageDataParam]

    cookie_disabled: Optional[WaapCookieDisabledPageDataParam]

    domains: Optional[Iterable[int]]
    """List of domain IDs that are associated with this page set"""

    handshake: Optional[WaapHandshakePageDataParam]

    javascript_disabled: Optional[WaapJavascriptDisabledPageDataParam]

    name: Optional[str]
    """Name of the custom page set"""
