# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .block_page_data_param import BlockPageDataParam
from .captcha_page_data_param import CaptchaPageDataParam
from .handshake_page_data_param import HandshakePageDataParam
from .block_csrf_page_data_param import BlockCsrfPageDataParam
from .cookie_disabled_page_data_param import CookieDisabledPageDataParam
from .javascript_disabled_page_data_param import JavascriptDisabledPageDataParam

__all__ = ["CustomPageSetCreateParams"]


class CustomPageSetCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the custom page set"""

    block: Optional[BlockPageDataParam]

    block_csrf: Optional[BlockCsrfPageDataParam]

    captcha: Optional[CaptchaPageDataParam]

    cookie_disabled: Optional[CookieDisabledPageDataParam]

    domains: Optional[Iterable[int]]
    """List of domain IDs that are associated with this page set"""

    handshake: Optional[HandshakePageDataParam]

    javascript_disabled: Optional[JavascriptDisabledPageDataParam]
