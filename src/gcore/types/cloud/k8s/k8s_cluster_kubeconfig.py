# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["K8sClusterKubeconfig"]


class K8sClusterKubeconfig(BaseModel):
    config: str
    """Cluster kubeconfig"""

    created_at: Optional[datetime] = None
    """Kubeconfig creation date"""

    expires_at: Optional[datetime] = None
    """Kubeconfig expiration date"""
