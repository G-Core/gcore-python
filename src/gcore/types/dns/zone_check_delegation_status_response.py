# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .dns_name_server import DNSNameServer

__all__ = ["ZoneCheckDelegationStatusResponse"]


class ZoneCheckDelegationStatusResponse(BaseModel):
    authoritative_name_servers: Optional[List[DNSNameServer]] = None

    gcore_authorized_count: Optional[int] = None

    is_whitelabel_delegation: Optional[bool] = None

    non_gcore_authorized_count: Optional[int] = None

    zone_exists: Optional[bool] = None
