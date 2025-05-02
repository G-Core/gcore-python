# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["InferenceFlavor"]


class InferenceFlavor(BaseModel):
    cpu: float
    """Inference flavor cpu count."""

    description: str
    """Inference flavor description."""

    gpu: int
    """Inference flavor gpu count."""

    gpu_compute_capability: str
    """Inference flavor gpu compute capability."""

    gpu_memory: float
    """Inference flavor gpu memory in Gi."""

    gpu_model: str
    """Inference flavor gpu model."""

    is_gpu_shared: bool
    """Inference flavor is gpu shared."""

    memory: float
    """Inference flavor memory in Gi."""

    name: str
    """Inference flavor name."""
