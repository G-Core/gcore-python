# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["StorageLocation"]


class StorageLocation(BaseModel):
    id: int

    address: str
    """Full hostname/address for accessing the storage endpoint"""

    allow_for_new_storage: Literal["deny", "allow"]
    """
    Indicates whether new storage can be created in this location: `allow` enables
    storage creation, `deny` prevents it
    """

    name: Literal["s-ed1", "s-drc2", "s-sgc1", "s-nhn2", "s-darz", "s-ws1", "ams", "sin", "fra", "mia"]

    type: Literal["s3", "sftp"]
