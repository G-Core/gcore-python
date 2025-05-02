# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .container_probe import ContainerProbe

__all__ = ["ContainerProbeConfig"]


class ContainerProbeConfig(BaseModel):
    enabled: bool
    """Whether the probe is enabled or not."""

    probe: Optional[ContainerProbe] = None
    """Probe configuration (exec, http_get or tcp_socket)"""
