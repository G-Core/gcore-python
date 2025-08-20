# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .dns_failover_log import DNSFailoverLog

__all__ = ["RrsetGetFailoverLogsResponse"]


class RrsetGetFailoverLogsResponse(BaseModel):
    log: Optional[DNSFailoverLog] = None
    """FailoverLog"""

    total_amount: Optional[int] = None
