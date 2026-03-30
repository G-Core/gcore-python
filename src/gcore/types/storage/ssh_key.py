# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["SSHKey"]


class SSHKey(BaseModel):
    id: int
    """Unique identifier for the SSH key"""

    created_at: datetime
    """ISO 8601 timestamp when the SSH key was created"""

    name: str
    """User-defined name for the SSH key"""

    public_key: str
    """The SSH public key content"""
