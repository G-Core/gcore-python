# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["PostgresClusterShort"]


class PostgresClusterShort(BaseModel):
    cluster_name: str
    """PostgreSQL cluster name"""

    created_at: datetime
    """Creation timestamp"""

    status: Literal["DELETING", "FAILED", "PREPARING", "READY", "UNHEALTHY", "UNKNOWN", "UPDATING"]
    """Current cluster status"""

    version: str
    """Cluster version"""
