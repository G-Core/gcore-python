# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SftpStorage"]


class SftpStorage(BaseModel):
    id: int
    """Unique identifier for the storage instance"""

    address: str
    """Full hostname/address for accessing the storage endpoint"""

    created_at: datetime
    """ISO 8601 timestamp when the storage was created"""

    expires: str
    """Duration when the storage will expire. Null if no expiration is set."""

    full_name: str
    """
    Read-only internal full name of the storage, composed as "{`client_id`}-{name}".
    Used by the SFTP backend as the login username. Clients should use this value
    when connecting but should continue to identify the storage by `name` in their
    own configuration.
    """

    has_custom_config_file: bool
    """Whether this storage uses a custom configuration file"""

    has_password: bool
    """Whether password authentication is configured for this storage"""

    is_http_disabled: bool
    """Whether HTTP access is disabled for this storage (HTTPS only)"""

    location_name: str
    """Geographic location code where the storage is provisioned"""

    name: str
    """User-defined name for the storage instance, as supplied at creation time."""

    provisioning_status: Literal["creating", "active", "updating", "deleting", "deleted"]
    """Lifecycle status of the storage. Use this to check readiness before operations."""

    server_alias: str
    """Custom domain alias for accessing the storage. Null if no alias is configured."""

    ssh_key_ids: List[int]
    """IDs of SSH keys associated with this SFTP storage"""

    password: Optional[str] = None
    """SFTP password.

    Only returned when newly generated or set (create/patch). Omitted in GET/list
    responses.
    """
