# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .dns_network_mapping import DNSNetworkMapping

__all__ = ["NetworkMappingListResponse"]


class NetworkMappingListResponse(BaseModel):
    network_mappings: Optional[List[DNSNetworkMapping]] = None

    total_amount: Optional[int] = None
