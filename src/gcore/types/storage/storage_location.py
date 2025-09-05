# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["StorageLocation"]


class StorageLocation(BaseModel):
    id: Optional[int] = None

    address: Optional[str] = None

    allow_for_new_storage: Optional[Literal["deny", "allow"]] = None
    """
    Indicates whether new storage can be created in this location: `allow` enables
    storage creation, `deny` prevents it
    """

    name: Optional[Literal["s-ed1", "s-drc2", "s-sgc1", "s-nhn2", "s-darz", "s-ws1", "ams", "sin", "fra", "mia"]] = None

    type: Optional[Literal["s3", "sftp"]] = None
