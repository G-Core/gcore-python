# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["K8SClusterKubeconfig"]


class K8SClusterKubeconfig(BaseModel):
    client_certificate: str
    """String in base64 format. Cluster client certificate"""

    client_key: str
    """String in base64 format. Cluster client key"""

    cluster_ca_certificate: str
    """String in base64 format. Cluster ca certificate"""

    config: str
    """Cluster kubeconfig"""

    created_at: datetime
    """Kubeconfig creation date"""

    expires_at: datetime
    """Kubeconfig expiration date"""

    host: str
    """Cluster host"""
