# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .probe_exec import ProbeExec
from .probe_http_get import ProbeHTTPGet
from .probe_tcp_socket import ProbeTcpSocket

__all__ = ["Probe"]


class Probe(BaseModel):
    exec: Optional[ProbeExec] = None
    """Exec probe configuration"""

    failure_threshold: int
    """The number of consecutive probe failures that mark the container as unhealthy."""

    http_get: Optional[ProbeHTTPGet] = None
    """HTTP GET probe configuration"""

    initial_delay_seconds: int
    """The initial delay before starting the first probe."""

    period_seconds: int
    """How often (in seconds) to perform the probe."""

    success_threshold: int
    """The number of consecutive successful probes that mark the container as healthy."""

    tcp_socket: Optional[ProbeTcpSocket] = None
    """TCP socket probe configuration"""

    timeout_seconds: int
    """The timeout for each probe."""
