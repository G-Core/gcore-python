# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ...tag import Tag
from ....._models import BaseModel

__all__ = ["GPUVirtualClusterVolume"]


class GPUVirtualClusterVolume(BaseModel):
    id: str
    """Volume unique identifier"""

    bootable: bool
    """True if this is bootable volume"""

    created_at: datetime
    """Volume creation date and time"""

    name: str
    """User defined name"""

    root_fs: bool
    """True if this volume contains root file system"""

    server_id: str
    """Server UUID"""

    size: int
    """Volume size in GiB"""

    status: Literal[
        "attaching",
        "available",
        "awaiting-transfer",
        "backing-up",
        "creating",
        "deleting",
        "detaching",
        "downloading",
        "error",
        "error_backing-up",
        "error_deleting",
        "error_extending",
        "error_restoring",
        "extending",
        "in-use",
        "maintenance",
        "reserved",
        "restoring-backup",
        "retyping",
        "reverting",
        "uploading",
    ]
    """Current volume status"""

    tags: List[Tag]
    """User defined tags"""

    type: str
    """Volume type"""
