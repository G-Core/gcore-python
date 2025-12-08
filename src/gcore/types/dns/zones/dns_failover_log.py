# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["DNSFailoverLog", "DNSFailoverLogItem"]


class DNSFailoverLogItem(BaseModel):
    """FailoverLogEntry"""

    action: Optional[str] = None

    address: Optional[str] = None

    time: Optional[int] = None


DNSFailoverLog: TypeAlias = List[DNSFailoverLogItem]
