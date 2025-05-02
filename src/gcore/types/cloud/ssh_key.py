# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SSHKey"]


class SSHKey(BaseModel):
    id: str
    """SSH key ID"""

    created_at: Optional[datetime] = None
    """SSH key creation time"""

    fingerprint: str
    """Fingerprint"""

    name: str
    """SSH key name"""

    project_id: Optional[int] = None
    """Project ID"""

    public_key: str
    """The public part of an SSH key is the shareable portion of an SSH key pair.

    It can be safely sent to servers or services to grant access. It does not
    contain sensitive information.
    """

    shared_in_project: bool
    """SSH key will be visible to all users in the project"""

    state: Literal["ACTIVE", "DELETING"]
    """SSH key state"""
