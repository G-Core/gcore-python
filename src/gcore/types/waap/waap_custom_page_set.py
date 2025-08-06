# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["WaapCustomPageSet", "Block", "BlockCsrf", "Captcha", "CookieDisabled", "Handshake", "JavascriptDisabled"]


class Block(BaseModel):
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


class BlockCsrf(BaseModel):
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


class Captcha(BaseModel):
    enabled: bool
    """Indicates whether the custom custom page is active or inactive"""

    error: Optional[str] = None
    """Error message"""

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


class CookieDisabled(BaseModel):
    enabled: bool
    """Indicates whether the custom custom page is active or inactive"""

    header: Optional[str] = None
    """The text to display in the header of the custom page"""

    text: Optional[str] = None
    """The text to display in the body of the custom page"""


class Handshake(BaseModel):
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

    title: Optional[str] = None
    """The text to display in the title of the custom page"""


class JavascriptDisabled(BaseModel):
    enabled: bool
    """Indicates whether the custom custom page is active or inactive"""

    header: Optional[str] = None
    """The text to display in the header of the custom page"""

    text: Optional[str] = None
    """The text to display in the body of the custom page"""


class WaapCustomPageSet(BaseModel):
    id: int
    """The ID of the custom page set"""

    name: str
    """Name of the custom page set"""

    block: Optional[Block] = None

    block_csrf: Optional[BlockCsrf] = None

    captcha: Optional[Captcha] = None

    cookie_disabled: Optional[CookieDisabled] = None

    domains: Optional[List[int]] = None
    """List of domain IDs that are associated with this page set"""

    handshake: Optional[Handshake] = None

    javascript_disabled: Optional[JavascriptDisabled] = None
