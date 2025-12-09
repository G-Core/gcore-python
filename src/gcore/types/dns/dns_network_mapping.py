# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .dns_mapping_entry import DNSMappingEntry

__all__ = ["DNSNetworkMapping"]


class DNSNetworkMapping(BaseModel):
    id: Optional[int] = None

    mapping: Optional[List[DNSMappingEntry]] = None

    name: Optional[str] = None
