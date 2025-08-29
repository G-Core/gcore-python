# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["K8sClusterVersion"]


class K8sClusterVersion(BaseModel):
    version: str
    """List of supported Kubernetes cluster versions"""
