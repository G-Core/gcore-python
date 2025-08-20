# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["DNSLookupResponse", "DNSLookupResponseItem"]


class DNSLookupResponseItem(BaseModel):
    content: Optional[List[str]] = None

    name: Optional[str] = None

    ttl: Optional[int] = None

    type: Optional[str] = None


DNSLookupResponse: TypeAlias = List[DNSLookupResponseItem]
