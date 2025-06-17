# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["WaapPageType"]

WaapPageType: TypeAlias = Literal[
    "block.html", "block_csrf.html", "captcha.html", "cookieDisabled.html", "handshake.html", "javascriptDisabled.html"
]
