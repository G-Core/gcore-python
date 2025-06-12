# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SSHKeyCreated"]


class SSHKeyCreated(BaseModel):
    id: str
    """SSH key ID"""

    created_at: datetime
    """SSH key creation time"""

    fingerprint: str
    """Fingerprint"""

    name: str
    """SSH key name"""

    private_key: Optional[str] = None
    """The private part of an SSH key is the confidential portion of the key pair.

    It should never be shared or exposed. This key is used to prove your identity
    when connecting to a server. If you omit the `public_key`, the platform will
    generate a key for you. The `private_key` will be returned **once** in the API
    response. Be sure to save it securely, as it cannot be retrieved again later.
    Best practice: Save the private key to a secure location on your machine (e.g.,
    `~/.ssh/id_ed25519`) and set the file permissions to be readable only by you.
    """

    project_id: int
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
