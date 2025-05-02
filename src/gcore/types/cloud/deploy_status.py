# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["DeployStatus"]


class DeployStatus(BaseModel):
    ready: int
    """Number of ready instances"""

    total: int
    """Total number of instances"""
