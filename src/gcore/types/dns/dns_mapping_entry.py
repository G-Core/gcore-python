# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["DNSMappingEntry"]


class DNSMappingEntry(BaseModel):
    cidr4: Optional[List[str]] = None

    cidr6: Optional[List[str]] = None

    tags: Optional[List[str]] = None
