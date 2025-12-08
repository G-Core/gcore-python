# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Location"]


class Location(BaseModel):
    """LocationV2 represents location data for v2 API where title is a string"""

    address: str
    """Full hostname/address for accessing the storage endpoint in this location"""

    allow_for_new_storage: Literal["deny", "allow"]
    """Indicates whether new storage can be created in this location"""

    name: str
    """Location code (region identifier)"""

    title: str
    """Human-readable title for the location"""

    type: Literal["s3", "sftp"]
    """Storage protocol type supported in this location"""
