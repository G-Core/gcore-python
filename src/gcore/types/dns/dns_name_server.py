# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DNSNameServer"]


class DNSNameServer(BaseModel):
    """NameServer"""

    ipv4_addresses: Optional[List[str]] = FieldInfo(alias="ipv4Addresses", default=None)

    ipv6_addresses: Optional[List[str]] = FieldInfo(alias="ipv6Addresses", default=None)

    name: Optional[str] = None
