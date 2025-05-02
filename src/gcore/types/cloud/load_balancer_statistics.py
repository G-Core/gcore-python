# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["LoadBalancerStatistics"]


class LoadBalancerStatistics(BaseModel):
    active_connections: int
    """Currently active connections"""

    bytes_in: int
    """Total bytes received"""

    bytes_out: int
    """Total bytes sent"""

    request_errors: int
    """Total requests that were unable to be fulfilled"""

    total_connections: int
    """Total connections handled"""
