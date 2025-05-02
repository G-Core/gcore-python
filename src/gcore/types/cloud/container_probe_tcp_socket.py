# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ContainerProbeTcpSocket"]


class ContainerProbeTcpSocket(BaseModel):
    port: int
    """Port number to check if it's open."""
