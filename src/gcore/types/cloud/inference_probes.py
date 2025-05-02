# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .container_probe_config import ContainerProbeConfig

__all__ = ["InferenceProbes"]


class InferenceProbes(BaseModel):
    liveness_probe: Optional[ContainerProbeConfig] = None
    """Liveness probe configuration"""

    readiness_probe: Optional[ContainerProbeConfig] = None
    """Readiness probe configuration"""

    startup_probe: Optional[ContainerProbeConfig] = None
    """Startup probe configuration"""
