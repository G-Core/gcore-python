# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Location"]


class Location(BaseModel):
    address: str
    """Full hostname/address for accessing the storage endpoint."""

    name: str
    """Human-readable display name for the location."""

    technical_name: str
    """Internal technical identifier for the location"""

    title: str
    """Display title for the location (English). Null if no title is set."""

    type: Literal["s3_compatible", "sftp"]
    """Storage type supported by this location"""
