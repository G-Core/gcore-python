# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .probe import Probe
from ...._models import BaseModel

__all__ = ["ProbeConfig"]


class ProbeConfig(BaseModel):
    enabled: bool
    """Whether the probe is enabled or not."""

    probe: Optional[Probe] = None
    """Probe configuration (exec, `http_get` or `tcp_socket`)"""
