# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["WaapDomainDDOSSettings"]


class WaapDomainDDOSSettings(BaseModel):
    """DDoS settings for a domain."""

    burst_threshold: Optional[int] = None
    """The burst threshold detects sudden rises in traffic.

    If it is met and the number of requests is at least five times the last 2-second
    interval, DDoS protection will activate. Default is 1000.
    """

    global_threshold: Optional[int] = None
    """
    The global threshold is responsible for identifying DDoS attacks with a slow
    rise in traffic. If the threshold is met and the current number of requests is
    at least double that of the previous 10-second window, DDoS protection will
    activate. Default is 5000.
    """

    sub_second_threshold: Optional[int] = None
    """
    The sub-second threshold protects WAAP servers against attacks from traffic
    bursts. When this threshold is reached, the DDoS mode will activate on the
    affected WAAP server, not the whole WAAP cluster. Default is 50.
    """
