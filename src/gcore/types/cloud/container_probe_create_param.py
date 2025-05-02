# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .container_probe_exec_create_param import ContainerProbeExecCreateParam
from .container_probe_http_get_create_param import ContainerProbeHTTPGetCreateParam
from .container_probe_tcp_socket_create_param import ContainerProbeTcpSocketCreateParam

__all__ = ["ContainerProbeCreateParam"]


class ContainerProbeCreateParam(TypedDict, total=False):
    exec: Optional[ContainerProbeExecCreateParam]
    """Exec probe configuration"""

    failure_threshold: int
    """The number of consecutive probe failures that mark the container as unhealthy."""

    http_get: Optional[ContainerProbeHTTPGetCreateParam]
    """HTTP GET probe configuration"""

    initial_delay_seconds: int
    """The initial delay before starting the first probe."""

    period_seconds: int
    """How often (in seconds) to perform the probe."""

    success_threshold: int
    """The number of consecutive successful probes that mark the container as healthy."""

    tcp_socket: Optional[ContainerProbeTcpSocketCreateParam]
    """TCP socket probe configuration"""

    timeout_seconds: int
    """The timeout for each probe."""
