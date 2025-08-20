# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .dns_output_rrset import DNSOutputRrset

__all__ = ["RrsetListResponse"]


class RrsetListResponse(BaseModel):
    rrsets: Optional[List[DNSOutputRrset]] = None

    total_amount: Optional[int] = None
