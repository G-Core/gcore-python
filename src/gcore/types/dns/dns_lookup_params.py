# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DNSLookupParams"]


class DNSLookupParams(TypedDict, total=False):
    name: str
    """Domain name"""

    request_server: Literal["authoritative_dns", "google", "cloudflare", "open_dns", "quad9", "gcore"]
    """Server that will be used as resolver"""
