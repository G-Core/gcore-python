# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["K8sClusterCertificate"]


class K8sClusterCertificate(BaseModel):
    certificate: str
    """Cluster CA certificate"""

    key: str
    """Cluster CA private key"""
