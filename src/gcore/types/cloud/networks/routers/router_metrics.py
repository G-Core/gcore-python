# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["RouterMetrics", "Metric"]


class Metric(BaseModel):
    network_bps_egress: Optional[float] = None
    """Network out, bits per second. Null when no data point is available."""

    network_bps_ingress: Optional[float] = None
    """Network in, bits per second. Null when no data point is available."""

    network_pps_egress: Optional[float] = None
    """Network out, packets per second. Null when no data point is available."""

    network_pps_ingress: Optional[float] = None
    """Network in, packets per second. Null when no data point is available."""

    time: str
    """Timestamp"""


class RouterMetrics(BaseModel):
    interface_type: Literal["private", "public"]
    """Interface type.

    The public interface includes the router gateway and the floating IPs. A private
    interface connects the router to a subnet.
    """

    ip_addresses: List[str]
    """IP addresses of the port"""

    metrics: List[Metric]
    """Traffic metrics of the interface, in order of time"""

    network_id: str
    """Network ID"""

    port_id: str
    """Port ID"""
