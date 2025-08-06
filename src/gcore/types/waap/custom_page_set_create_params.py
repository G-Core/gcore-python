# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = [
    "CustomPageSetCreateParams",
    "Block",
    "BlockCsrf",
    "Captcha",
    "CookieDisabled",
    "Handshake",
    "JavascriptDisabled",
]


class CustomPageSetCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the custom page set"""

    block: Optional[Block]

    block_csrf: Optional[BlockCsrf]

    captcha: Optional[Captcha]

    cookie_disabled: Optional[CookieDisabled]

    domains: Optional[Iterable[int]]
    """List of domain IDs that are associated with this page set"""

    handshake: Optional[Handshake]

    javascript_disabled: Optional[JavascriptDisabled]


class Block(TypedDict, total=False):
    enabled: Required[bool]
    """Indicates whether the custom custom page is active or inactive"""

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


class BlockCsrf(TypedDict, total=False):
    enabled: Required[bool]
    """Indicates whether the custom custom page is active or inactive"""

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


class Captcha(TypedDict, total=False):
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


class CookieDisabled(TypedDict, total=False):
    enabled: Required[bool]
    """Indicates whether the custom custom page is active or inactive"""

    header: str
    """The text to display in the header of the custom page"""

    text: str
    """The text to display in the body of the custom page"""


class Handshake(TypedDict, total=False):
    enabled: Required[bool]
    """Indicates whether the custom custom page is active or inactive"""

    header: str
    """The text to display in the header of the custom page"""

    logo: str
    """
    Supported image types are JPEG, PNG and JPG, size is limited to width 450px,
    height 130px. This should be a base 64 encoding of the full HTML img tag
    compatible image, with the header included.
    """

    title: str
    """The text to display in the title of the custom page"""


class JavascriptDisabled(TypedDict, total=False):
    enabled: Required[bool]
    """Indicates whether the custom custom page is active or inactive"""

    header: str
    """The text to display in the header of the custom page"""

    text: str
    """The text to display in the body of the custom page"""
