# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["K8SClusterVersion"]


class K8SClusterVersion(BaseModel):
    version: str
    """List of supported Kubernetes cluster versions"""
