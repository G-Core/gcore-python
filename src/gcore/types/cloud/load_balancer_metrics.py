# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LoadBalancerMetrics"]


class LoadBalancerMetrics(BaseModel):
    cpu_util: Optional[float] = None
    """CPU utilization, % (max 100% for multi-core).

    Null when no data point is available.
    """

    memory_util: Optional[float] = None
    """RAM utilization, %. Null when no data point is available."""

    network_bps_egress: Optional[float] = FieldInfo(alias="network_Bps_egress", default=None)
    """Network out, bytes per second. Null when no data point is available."""

    network_bps_ingress: Optional[float] = FieldInfo(alias="network_Bps_ingress", default=None)
    """Network in, bytes per second. Null when no data point is available."""

    network_pps_egress: Optional[float] = None
    """Network out, packets per second. Null when no data point is available."""

    network_pps_ingress: Optional[float] = None
    """Network in, packets per second. Null when no data point is available."""

    time: Optional[str] = None
    """Timestamp. Null when no data point is available."""
