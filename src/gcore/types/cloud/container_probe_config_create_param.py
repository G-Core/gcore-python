# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .container_probe_create_param import ContainerProbeCreateParam

__all__ = ["ContainerProbeConfigCreateParam"]


class ContainerProbeConfigCreateParam(TypedDict, total=False):
    enabled: Required[bool]
    """Whether the probe is enabled or not."""

    probe: Optional[ContainerProbeCreateParam]
    """Probe configuration (exec, http_get or tcp_socket)"""
