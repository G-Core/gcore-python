# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ProbeTcpSocket"]


class ProbeTcpSocket(BaseModel):
    port: int
    """Port number to check if it's open."""
